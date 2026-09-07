"""Markdown / PNG report and Telegram text for one paper-trading step."""
from __future__ import annotations

import json
import sqlite3
from datetime import datetime
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from src.config import Config  # noqa: E402
from src.paper import db as pdb  # noqa: E402
from src.paper.runner import RunSummary  # noqa: E402


def _pct(x: float | None, d: int = 2) -> str:
    return "-" if x is None else f"{x * 100:.{d}f}%"


def _num(x: float | None, d: int = 2) -> str:
    return "-" if x is None else f"{x:,.{d}f}"


def plot_equity(conn: sqlite3.Connection, path: Path) -> Path | None:
    rows = pdb.equity_history(conn)
    if len(rows) < 2:
        return None
    ts = [datetime.strptime(r["ts"], "%Y-%m-%dT%H:%M:%SZ") for r in rows]
    eq = [r["equity"] for r in rows]
    n_open = [r["n_open"] for r in rows]
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(ts, eq, label="equity (USDT)")
    ax.set_ylabel("equity")
    ax.grid(alpha=0.3)
    ax2 = ax.twinx()
    ax2.step(ts, n_open, where="post", color="grey", alpha=0.5, label="open pairs")
    ax2.set_ylabel("open pairs")
    ax.set_title("Paper trading equity")
    fig.autofmt_xdate()
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def write_paper_report(summary: RunSummary, conn: sqlite3.Connection, cfg: Config, out_dir: Path) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    png = plot_equity(conn, out_dir / "paper_equity.png")
    first = conn.execute("SELECT ts FROM runs ORDER BY run_id LIMIT 1").fetchone()
    start = datetime.strptime(first["ts"], "%Y-%m-%dT%H:%M:%SZ") if first else summary.ts.replace(tzinfo=None)
    days = max((summary.ts.replace(tzinfo=None) - start).total_seconds() / 86_400, 1e-9)
    ret = summary.equity / cfg.capital.total_usdt - 1
    apr = ret * 365 / days if days >= 1 else None

    md = [
        "# Paper trading status",
        "",
        f"Run #{summary.run_id} at {summary.ts:%Y-%m-%d %H:%M UTC}. Threshold {_pct(summary.threshold, 3)} per funding interval, "
        f"signal = mean of last {cfg.strategy.lookback} settled rates. Universe: {', '.join(summary.universe)}.",
        "",
        "| metric | value |",
        "|---|---|",
        f"| equity | {_num(summary.equity)} USDT |",
        f"| return since start | {_pct(ret)} ({days:.1f} days) |",
        f"| annualised | {_pct(apr) if apr is not None else 'n/a (<1 day)'} |",
        f"| realized (closed pairs) | {_num(summary.realized_total)} USDT |",
        f"| funding received this run | {_num(summary.funding_received, 4)} USDT |",
        f"| open pairs | {summary.n_open} / {cfg.universe.size} |",
        f"| free cash | {_num(summary.cash)} USDT |",
        f"| skipped symbols | {len(summary.skipped)} |",
        "",
        "## Positions & risk",
        "",
        "| symbol | held | action | signal | mark | spot | funding accrued | basis MTM | margin ratio | liq. price | liq. distance |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
    ]
    for s in sorted(summary.states, key=lambda x: (not x.held, x.symbol)):
        md.append(
            f"| {s.symbol} | {'yes' if s.held else 'no'} | {s.action or ''} | {_pct(s.signal, 4)} | {_num(s.mark_price, 4)} | "
            f"{_num(s.spot_price, 4)} | {_num(s.funding_accrued, 4) if s.held else '-'} | {_num(s.unrealized, 4)} | "
            f"{_pct(s.margin_ratio)} | {_num(s.liq_price, 4)} | {_pct(s.liq_distance, 1)} |"
        )
    if summary.skipped:
        md += ["", "## Skipped this run", ""] + [f"- `{k}`: {v}" for k, v in summary.skipped.items()]
    if png is not None:
        md += ["", f"![equity]({png.name})"]
    md += [
        "",
        "_Margin ratio = maintenance margin / (margin + unrealized) on the isolated perp short; ≥100% means liquidation. "
        "Liq. distance = how far mark must rise before liquidation._",
    ]
    path = out_dir / "paper_latest.md"
    path.write_text("\n".join(md) + "\n")
    return path


def write_paper_json(summary: RunSummary, conn: sqlite3.Connection, cfg: Config, path: Path) -> Path:
    """Dashboard payload: latest run, per-symbol states, equity history, recent trades."""
    runs = pdb.equity_history(conn)
    first_ts = datetime.strptime(runs[0]["ts"], "%Y-%m-%dT%H:%M:%SZ") if runs else summary.ts.replace(tzinfo=None)
    days = max((summary.ts.replace(tzinfo=None) - first_ts).total_seconds() / 86_400, 0.0)
    ret = summary.equity / cfg.capital.total_usdt - 1
    trades = conn.execute(
        "SELECT ts, symbol, side, spot_price, perp_price, notional, fees, realized, signal FROM trades ORDER BY trade_id DESC LIMIT 50"
    ).fetchall()
    funding_total = conn.execute("SELECT COALESCE(SUM(amount), 0) FROM funding_events").fetchone()[0]
    payload = {
        "generated_at": summary.ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "run_id": summary.run_id,
        "threshold": summary.threshold,
        "lookback": cfg.strategy.lookback,
        "capital": cfg.capital.total_usdt,
        "slots": cfg.universe.size,
        "universe": summary.universe,
        "equity": summary.equity,
        "cash": summary.cash,
        "return": ret,
        "days": days,
        "apr": (ret * 365 / days) if days >= 1 else None,
        "realized_total": summary.realized_total,
        "funding_total": float(funding_total),
        "funding_this_run": summary.funding_received,
        "n_open": summary.n_open,
        "skipped": summary.skipped,
        "states": [
            {
                "symbol": s.symbol,
                "held": s.held,
                "action": s.action,
                "signal": s.signal,
                "mark_price": s.mark_price,
                "spot_price": s.spot_price,
                "funding_accrued": s.funding_accrued if s.held else None,
                "unrealized": s.unrealized,
                "margin_ratio": s.margin_ratio,
                "liq_price": s.liq_price,
                "liq_distance": s.liq_distance,
            }
            for s in summary.states
        ],
        "equity_history": [{"t": r["ts"], "equity": r["equity"], "n_open": r["n_open"]} for r in runs],
        "recent_trades": [dict(t) for t in trades],
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=1, default=str))
    return path


def telegram_text(summary: RunSummary, cfg: Config) -> str:
    ret = summary.equity / cfg.capital.total_usdt - 1
    lines = [
        f"*Funding carry paper #{summary.run_id}* {summary.ts:%m-%d %H:%M}Z",
        f"Equity {summary.equity:,.2f} USDT ({ret * 100:+.2f}%), open {summary.n_open}/{cfg.universe.size}",
        f"Funding this run {summary.funding_received:+.4f} USDT",
    ]
    actions = [f"{s.action} {s.symbol}" for s in summary.states if s.action in ("OPEN", "CLOSE")]
    if actions:
        lines.append("Actions: " + ", ".join(actions))
    held = [s for s in summary.states if s.held and s.liq_distance is not None]
    if held:
        worst = min(held, key=lambda s: s.liq_distance)
        lines.append(f"Tightest liq: {worst.symbol} {worst.liq_distance * 100:.1f}% away, margin ratio {worst.margin_ratio * 100:.2f}%")
    if summary.skipped:
        lines.append(f"Skipped: {', '.join(k for k in summary.skipped)}")
    return "\n".join(lines)
