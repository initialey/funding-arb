"""Markdown + PNG output for backtest and walk-forward results."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402

from src.backtest.engine import BacktestResult  # noqa: E402
from src.backtest.metrics import Summary, per_symbol_table  # noqa: E402
from src.backtest.walkforward import WalkForwardResult  # noqa: E402
from src.config import Config  # noqa: E402


def pct(x: float, digits: int = 2) -> str:
    return f"{x * 100:.{digits}f}%"


def summary_table(summaries: list[Summary]) -> str:
    lines = [
        "| threshold / interval | APR | max DD | exposure days | slot util. | trades | funding PnL | costs | net PnL |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for s in summaries:
        lines.append(
            f"| {pct(s.threshold, 3)} | **{pct(s.apr)}** | {pct(s.max_drawdown)} | {pct(s.exposure_days_ratio, 1)} | "
            f"{pct(s.avg_slot_utilisation, 1)} | {s.trades} | {s.funding_pnl:,.2f} | {s.costs:,.2f} | {s.net_pnl:,.2f} |"
        )
    return "\n".join(lines)


def symbol_table(result: BacktestResult, cfg: Config) -> str:
    df = per_symbol_table(result, cfg.slot_usdt)
    lines = [
        "| symbol | events | trades | held ratio | mean rate | funding PnL | costs | net PnL | APR on slot |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for _, r in df.iterrows():
        lines.append(
            f"| {r.symbol} | {int(r.events)} | {int(r.trades)} | {pct(r.held_ratio, 1)} | {pct(r.mean_rate, 4)} | "
            f"{r.funding_pnl:,.2f} | {r.costs:,.2f} | {r.net_pnl:,.2f} | {pct(r.apr_on_slot)} |"
        )
    return "\n".join(lines)


def walkforward_table(wf: WalkForwardResult) -> str:
    lines = [
        "| train start | train end | test end | chosen threshold | train APR | test APR | test max DD | test trades |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for w in wf.windows:
        lines.append(
            f"| {w.train_start:%Y-%m-%d} | {w.train_end:%Y-%m-%d} | {w.test_end:%Y-%m-%d} | {pct(w.chosen_threshold, 3)} | "
            f"{pct(w.train_apr)} | {pct(w.test_summary.apr)} | {pct(w.test_summary.max_drawdown)} | {w.test_summary.trades} |"
        )
    return "\n".join(lines)


def plot_equity_curves(results: dict[float, BacktestResult], wf: WalkForwardResult | None, path: Path) -> Path:
    fig, ax = plt.subplots(figsize=(10, 5))
    for thr, res in results.items():
        if not res.equity.empty:
            ax.plot(res.equity["ts"], res.equity["equity"], label=f"threshold {thr * 100:.3f}%")
    if wf is not None and not wf.oos_equity.empty:
        ax.plot(wf.oos_equity["ts"], wf.oos_equity["equity"], "k--", label="walk-forward OOS")
    ax.set_title("Funding carry: equity (USDT)")
    ax.set_ylabel("equity")
    ax.grid(alpha=0.3)
    ax.legend()
    fig.autofmt_xdate()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.tight_layout()
    fig.savefig(path, dpi=120)
    plt.close(fig)
    return path


def write_backtest_report(
    results: dict[float, BacktestResult],
    summaries: list[Summary],
    wf: WalkForwardResult | None,
    cfg: Config,
    funding: pd.DataFrame,
    out_dir: Path,
) -> Path:
    out_dir.mkdir(parents=True, exist_ok=True)
    png = plot_equity_curves(results, wf, out_dir / "backtest_equity.png")
    best = max(summaries, key=lambda s: s.apr)
    best_res = results[best.threshold]
    now = datetime.now(tz=timezone.utc)
    md = [
        "# Funding carry backtest",
        "",
        f"Generated {now:%Y-%m-%d %H:%M UTC}. Data: {funding['symbol'].nunique()} symbols, "
        f"{len(funding):,} funding events, {funding['ts'].min():%Y-%m-%d} → {funding['ts'].max():%Y-%m-%d}.",
        "",
        f"Capital {cfg.capital.total_usdt:,.0f} USDT, {cfg.universe.size} slots × {cfg.slot_usdt:,.0f} USDT, "
        f"leg notional {cfg.leg_notional:,.0f} USDT, leverage {cfg.capital.leverage:.0f}x. "
        f"Cost per fill {pct(cfg.costs.per_fill, 3)} (taker {pct(cfg.costs.taker_fee, 3)} + spread {pct(cfg.costs.spread, 3)}), "
        f"round trip {pct(cfg.costs.round_trip, 2)} of leg notional. Signal: mean of last {cfg.strategy.lookback} settled rates.",
        "",
        "## Threshold comparison (full sample, in-sample)",
        "",
        summary_table(summaries),
        "",
        f"![equity]({png.name})",
        "",
        f"## Per-symbol breakdown (threshold {pct(best.threshold, 3)})",
        "",
        symbol_table(best_res, cfg),
    ]
    if wf is not None:
        md += [
            "",
            "## Walk-forward (out-of-sample)",
            "",
            f"Train {cfg.walkforward.train_days}d → test {cfg.walkforward.test_days}d, step {cfg.walkforward.step_days}d. "
            f"Stitched OOS: **APR {pct(wf.oos_summary.apr)}**, max DD {pct(wf.oos_summary.max_drawdown)}, "
            f"exposure days {pct(wf.oos_summary.exposure_days_ratio, 1)}, trades {wf.oos_summary.trades}, "
            f"net PnL {wf.oos_summary.net_pnl:,.2f} USDT over {wf.oos_summary.days:.0f} days.",
            "",
            walkforward_table(wf),
        ]
    md += [
        "",
        "## Assumptions",
        "",
        "- Spot long and perp short are equal notional; basis / mark-to-market between legs is assumed to net to zero.",
        "- Funding PnL = leg notional × funding rate for every settlement while in position (short receives positive rates).",
        "- Notional is fixed per slot (no compounding); APR = net PnL / capital × 365 / days.",
        "- Signal uses only settled rates (no look-ahead). A position open at the end of the sample is closed and charged exit costs.",
    ]
    path = out_dir / "backtest_report.md"
    path.write_text("\n".join(md) + "\n")
    return path
