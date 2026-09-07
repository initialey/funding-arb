"""Event-driven simulation of the carry trade on historical funding data.

Model
-----
* Each symbol owns a fixed capital slot; ``leg_notional`` USDT is long spot and the
  same notional is short perp (1x). Notional is not compounded.
* PnL per funding event while in position = ``leg_notional * funding_rate``
  (a short receives positive funding and pays negative funding).
* Costs: ``per_fill`` fraction of leg notional on each of the 4 fills of a round
  trip (2 at open, 2 at close). Basis / mark-to-market between legs is assumed to
  net to zero and is ignored; this is documented in the README.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from src.backtest.strategy import desired_positions, trailing_signal
from src.config import Config


@dataclass
class SymbolResult:
    symbol: str
    events: pd.DataFrame  # ts, funding_rate, signal, held, funding_pnl, cost, pnl, cum_pnl
    trades: int
    funding_pnl: float
    costs: float

    @property
    def net_pnl(self) -> float:
        return self.funding_pnl - self.costs


@dataclass
class BacktestResult:
    threshold: float
    per_symbol: dict[str, SymbolResult]
    equity: pd.DataFrame  # ts, pnl, cum_pnl, equity, n_open

    def totals(self) -> dict[str, float]:
        return {
            "funding_pnl": sum(r.funding_pnl for r in self.per_symbol.values()),
            "costs": sum(r.costs for r in self.per_symbol.values()),
            "net_pnl": sum(r.net_pnl for r in self.per_symbol.values()),
            "trades": sum(r.trades for r in self.per_symbol.values()),
        }


def simulate_symbol(df: pd.DataFrame, symbol: str, threshold: float, cfg: Config) -> SymbolResult:
    d = df[df["symbol"] == symbol].sort_values("ts").reset_index(drop=True)[["ts", "funding_rate"]].copy()
    notional = cfg.leg_notional
    open_cost = 2 * cfg.costs.per_fill * notional  # two fills to open
    close_cost = open_cost

    d["signal"] = trailing_signal(d["funding_rate"], cfg.strategy.lookback)
    d["held"] = desired_positions(d["signal"], threshold)
    prev_held = d["held"].shift(1, fill_value=False)
    entered = d["held"] & ~prev_held
    exited = ~d["held"] & prev_held

    d["funding_pnl"] = d["funding_rate"].where(d["held"], 0.0) * notional
    d["cost"] = entered.astype(float) * open_cost + exited.astype(float) * close_cost
    # A position still open at the end of the sample is closed at the last event.
    if len(d) and bool(d["held"].iloc[-1]):
        d.loc[d.index[-1], "cost"] += close_cost
    d["pnl"] = d["funding_pnl"] - d["cost"]
    d["cum_pnl"] = d["pnl"].cumsum()

    return SymbolResult(
        symbol=symbol,
        events=d,
        trades=int(entered.sum()),
        funding_pnl=float(d["funding_pnl"].sum()),
        costs=float(d["cost"].sum()),
    )


def run_backtest(funding: pd.DataFrame, threshold: float, cfg: Config, symbols: list[str] | None = None) -> BacktestResult:
    symbols = symbols or sorted(funding["symbol"].unique())
    per_symbol = {s: simulate_symbol(funding, s, threshold, cfg) for s in symbols}
    frames = []
    for r in per_symbol.values():
        e = r.events[["ts", "pnl", "held"]].copy()
        frames.append(e)
    if frames:
        all_ev = pd.concat(frames, ignore_index=True)
        equity = (
            all_ev.groupby("ts", as_index=False)
            .agg(pnl=("pnl", "sum"), n_open=("held", "sum"))
            .sort_values("ts")
            .reset_index(drop=True)
        )
    else:
        equity = pd.DataFrame(columns=["ts", "pnl", "n_open"])
    equity["cum_pnl"] = equity["pnl"].cumsum()
    equity["equity"] = cfg.capital.total_usdt + equity["cum_pnl"]
    return BacktestResult(threshold=threshold, per_symbol=per_symbol, equity=equity)
