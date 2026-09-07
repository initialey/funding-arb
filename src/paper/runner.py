"""One paper-trading step (intended to run every 8 hours, just after funding settles).

Steps
-----
1. Refresh the universe (top turnover) – fall back to the previous universe on failure.
2. Per symbol: fetch recent funding history + linear/spot tickers (skip & record on failure).
3. Accrue funding for settlements that happened since the last step on open positions.
4. Apply the entry/exit rule (mean of last N settled rates vs threshold).
5. Snapshot margin ratio / liquidation distance for every position, persist a run row.

No order endpoint is ever touched: positions are rows in SQLite.
"""
from __future__ import annotations

import logging
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timezone

from src.config import Config
from src.data.exchange import MarketDataSource
from src.data.universe import select_universe
from src.paper import db as pdb
from src.paper.portfolio import (
    basis_pnl,
    funding_amount,
    liquidation_distance,
    short_liquidation_price,
    short_margin_ratio,
    size_pair,
)

log = logging.getLogger(__name__)


def _iso(dt: datetime) -> str:
    return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _parse_iso(s: str) -> datetime:
    return datetime.strptime(s, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


@dataclass
class MarketSnapshot:
    symbol: str
    mark_price: float
    perp_last: float
    spot_price: float
    settled: list[tuple[datetime, float]]  # (ts, rate) ascending
    next_funding_ts: datetime | None = None
    current_rate: float | None = None

    def signal(self, lookback: int) -> float | None:
        if len(self.settled) < lookback:
            return None
        return sum(r for _, r in self.settled[-lookback:]) / lookback


@dataclass
class SymbolState:
    symbol: str
    held: bool
    signal: float | None
    mark_price: float | None
    spot_price: float | None
    unrealized: float | None = None
    margin_ratio: float | None = None
    liq_price: float | None = None
    liq_distance: float | None = None
    funding_accrued: float = 0.0
    action: str | None = None  # OPEN / CLOSE / None


@dataclass
class RunSummary:
    run_id: int
    ts: datetime
    equity: float
    cash: float
    realized_total: float
    n_open: int
    states: list[SymbolState]
    skipped: dict[str, str] = field(default_factory=dict)
    funding_received: float = 0.0
    threshold: float = 0.0
    universe: list[str] = field(default_factory=list)


def fetch_snapshot(source: MarketDataSource, symbol: str, lookback: int) -> MarketSnapshot:
    settled = source.recent_funding(symbol, max(lookback + 5, 8))
    t = source.perp_ticker(symbol)
    try:
        spot_price = source.spot_price(symbol)
    except Exception as exc:  # spot pair missing on this venue -> fall back to perp last
        log.warning("spot ticker for %s unavailable (%s); using perp last", symbol, exc)
        spot_price = t.last_price
    return MarketSnapshot(
        symbol=symbol,
        mark_price=t.mark_price,
        perp_last=t.last_price,
        spot_price=spot_price,
        settled=settled,
        next_funding_ts=t.next_funding_time,
        current_rate=t.funding_rate,
    )


def run_step(
    source: MarketDataSource,
    conn: sqlite3.Connection,
    cfg: Config,
    now: datetime | None = None,
    threshold: float | None = None,
) -> RunSummary:
    now = now or datetime.now(tz=timezone.utc)
    threshold = cfg.strategy.default_threshold if threshold is None else threshold
    lookback = cfg.strategy.lookback
    per_fill = cfg.costs.per_fill
    mmr = cfg.paper.maintenance_margin_rate
    skipped: dict[str, str] = {}

    positions = pdb.open_positions(conn)

    # 1. universe
    try:
        universe = select_universe(source.perp_tickers(), cfg.universe)
    except Exception as exc:  # network / venue error: keep going with the core list
        universe = list(cfg.universe.core)
        skipped["__universe__"] = f"tickers failed, using core only: {exc}"
    symbols = list(dict.fromkeys(universe + list(positions)))

    # reserve run_id first so child rows can reference it
    with pdb.transaction(conn):
        cur = conn.execute("INSERT INTO runs (ts, equity, cash, n_open, note) VALUES (?, 0, 0, 0, 'pending')", (_iso(now),))
        run_id = int(cur.lastrowid)

    states: list[SymbolState] = []
    funding_received = 0.0
    open_mtm_total = 0.0
    committed = 0.0

    for sym in symbols:
        pos = positions.get(sym)
        try:
            snap = fetch_snapshot(source, sym, lookback)
        except Exception as exc:  # any fetch/parse failure: skip this symbol this run
            skipped[sym] = str(exc)
            conn.execute("INSERT INTO skips (run_id, ts, symbol, reason) VALUES (?, ?, ?, ?)", (run_id, _iso(now), sym, str(exc)))
            if pos is not None:  # keep the position, count its committed capital, no state change
                committed += 2 * pos["perp_qty"] * pos["perp_entry"]
                states.append(SymbolState(sym, True, None, None, None, funding_accrued=pos["funding_accrued"], action="SKIP"))
            else:
                states.append(SymbolState(sym, False, None, None, None, action="SKIP"))
            continue

        signal = snap.signal(lookback)
        state = SymbolState(sym, pos is not None, signal, snap.mark_price, snap.spot_price)

        with pdb.transaction(conn):
            # 3. accrue funding on an existing position
            if pos is not None:
                last_ts = _parse_iso(pos["last_funding_ts"])
                accrued = pos["funding_accrued"]
                for ts, rate in snap.settled:
                    if ts <= last_ts or ts > now:
                        continue
                    amt = funding_amount(pos["perp_qty"], snap.mark_price, rate)
                    conn.execute(
                        "INSERT OR IGNORE INTO funding_events (symbol, ts, funding_rate, notional, amount, run_id) VALUES (?, ?, ?, ?, ?, ?)",
                        (sym, _iso(ts), rate, pos["perp_qty"] * snap.mark_price, amt, run_id),
                    )
                    accrued += amt
                    funding_received += amt
                    last_ts = ts
                conn.execute(
                    "UPDATE positions SET funding_accrued=?, last_funding_ts=? WHERE symbol=?", (accrued, _iso(last_ts), sym)
                )
                pos = dict(pos) | {"funding_accrued": accrued, "last_funding_ts": _iso(last_ts)}

            # 4. entry / exit
            if pos is not None and signal is not None and signal < threshold:
                notional = pos["perp_qty"] * snap.mark_price
                close_fees = 2 * per_fill * notional
                mtm = basis_pnl(pos["spot_qty"], pos["spot_entry"], snap.spot_price, pos["perp_qty"], pos["perp_entry"], snap.mark_price)
                realized = pos["funding_accrued"] - pos["fees_paid"] - close_fees + mtm
                conn.execute(
                    "INSERT INTO trades (run_id, ts, symbol, side, spot_price, perp_price, notional, fees, realized, signal) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (run_id, _iso(now), sym, "CLOSE", snap.spot_price, snap.mark_price, notional, close_fees, realized, signal),
                )
                conn.execute("DELETE FROM positions WHERE symbol=?", (sym,))
                state.held, state.action, state.funding_accrued = False, "CLOSE", pos["funding_accrued"]
                pos = None
            elif pos is None and sym in universe and signal is not None and signal >= threshold:
                sizing = size_pair(cfg.leg_notional, snap.spot_price, snap.mark_price, cfg.capital.leverage, per_fill)
                conn.execute(
                    "INSERT INTO positions (symbol, opened_ts, spot_qty, spot_entry, perp_qty, perp_entry, perp_margin, leverage, last_funding_ts, funding_accrued, fees_paid) VALUES (?,?,?,?,?,?,?,?,?,0,?)",
                    (sym, _iso(now), sizing.spot_qty, snap.spot_price, sizing.perp_qty, snap.mark_price, sizing.perp_margin, cfg.capital.leverage, _iso(now), sizing.open_fees),
                )
                conn.execute(
                    "INSERT INTO trades (run_id, ts, symbol, side, spot_price, perp_price, notional, fees, realized, signal) VALUES (?,?,?,?,?,?,?,?,NULL,?)",
                    (run_id, _iso(now), sym, "OPEN", snap.spot_price, snap.mark_price, sizing.notional, sizing.open_fees, signal),
                )
                pos = {
                    "symbol": sym, "spot_qty": sizing.spot_qty, "spot_entry": snap.spot_price, "perp_qty": sizing.perp_qty,
                    "perp_entry": snap.mark_price, "perp_margin": sizing.perp_margin, "leverage": cfg.capital.leverage,
                    "funding_accrued": 0.0, "fees_paid": sizing.open_fees,
                }
                state.held, state.action = True, "OPEN"

            # 5. risk snapshot
            if pos is not None:
                state.funding_accrued = pos["funding_accrued"]
                state.unrealized = basis_pnl(pos["spot_qty"], pos["spot_entry"], snap.spot_price, pos["perp_qty"], pos["perp_entry"], snap.mark_price)
                state.margin_ratio = short_margin_ratio(pos["perp_qty"], pos["perp_entry"], snap.mark_price, pos["perp_margin"], mmr)
                state.liq_price = short_liquidation_price(pos["perp_entry"], pos["leverage"], mmr)
                state.liq_distance = liquidation_distance(state.liq_price, snap.mark_price)
                open_mtm_total += pos["funding_accrued"] - pos["fees_paid"] + state.unrealized
                committed += pos["spot_qty"] * pos["spot_entry"] + pos["perp_margin"]
            conn.execute(
                "INSERT OR REPLACE INTO snapshots (run_id, symbol, mark_price, spot_price, signal, held, unrealized, margin_ratio, liq_price, liq_distance) VALUES (?,?,?,?,?,?,?,?,?,?)",
                (run_id, sym, snap.mark_price, snap.spot_price, signal, int(state.held), state.unrealized, state.margin_ratio, state.liq_price, state.liq_distance),
            )
        states.append(state)

    realized_total = pdb.realized_total(conn)
    equity = cfg.capital.total_usdt + realized_total + open_mtm_total
    cash = cfg.capital.total_usdt + realized_total - committed
    n_open = sum(1 for s in states if s.held)
    with pdb.transaction(conn):
        conn.execute(
            "UPDATE runs SET equity=?, cash=?, n_open=?, note=? WHERE run_id=?",
            (equity, cash, n_open, f"skipped={len(skipped)}", run_id),
        )
    return RunSummary(
        run_id=run_id, ts=now, equity=equity, cash=cash, realized_total=realized_total, n_open=n_open,
        states=states, skipped=skipped, funding_received=funding_received, threshold=threshold, universe=universe,
    )
