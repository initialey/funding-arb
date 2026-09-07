"""Rolling walk-forward validation.

For each window: pick the threshold with the highest in-sample APR on the train
segment, apply it to the following out-of-sample test segment, and stitch the
test segments into one out-of-sample equity curve.
"""
from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from src.backtest.engine import BacktestResult, run_backtest
from src.backtest.metrics import Summary, summarise
from src.config import Config


@dataclass
class WalkForwardWindow:
    train_start: pd.Timestamp
    train_end: pd.Timestamp
    test_end: pd.Timestamp
    chosen_threshold: float
    train_apr: float
    test_summary: Summary


@dataclass
class WalkForwardResult:
    windows: list[WalkForwardWindow]
    oos_equity: pd.DataFrame
    oos_summary: Summary


def _slice(funding: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp) -> pd.DataFrame:
    return funding[(funding["ts"] >= start) & (funding["ts"] < end)]


def _with_warmup(funding: pd.DataFrame, start: pd.Timestamp, end: pd.Timestamp, lookback: int) -> pd.DataFrame:
    """Test slice plus ``lookback`` prior rows per symbol so the signal has no cold start."""
    parts = []
    for sym, g in funding.groupby("symbol"):
        g = g.sort_values("ts")
        before = g[g["ts"] < start].tail(lookback)
        inside = g[(g["ts"] >= start) & (g["ts"] < end)]
        parts.append(pd.concat([before, inside]))
    return pd.concat(parts, ignore_index=True) if parts else funding.iloc[0:0]


def _trim(result: BacktestResult, start: pd.Timestamp) -> BacktestResult:
    """Drop warm-up rows so metrics only count the test period."""
    for r in result.per_symbol.values():
        r.events = r.events[r.events["ts"] >= start].reset_index(drop=True)
        r.trades = int((r.events["held"] & ~r.events["held"].shift(1, fill_value=False)).sum())
        r.funding_pnl = float(r.events["funding_pnl"].sum())
        r.costs = float(r.events["cost"].sum())
    result.equity = result.equity[result.equity["ts"] >= start].reset_index(drop=True)
    return result


def run_walkforward(funding: pd.DataFrame, cfg: Config, thresholds: list[float] | None = None) -> WalkForwardResult:
    thresholds = thresholds or cfg.strategy.thresholds
    wf = cfg.walkforward
    capital = cfg.capital.total_usdt
    n_sym = funding["symbol"].nunique()
    t0, t_last = funding["ts"].min(), funding["ts"].max()

    windows: list[WalkForwardWindow] = []
    oos_frames: list[pd.DataFrame] = []
    train_start = t0
    while True:
        train_end = train_start + pd.Timedelta(days=wf.train_days)
        test_end = train_end + pd.Timedelta(days=wf.test_days)
        if train_end >= t_last:
            break
        train = _slice(funding, train_start, train_end)
        best_thr, best_apr = thresholds[0], float("-inf")
        for thr in thresholds:
            s = summarise(run_backtest(train, thr, cfg), capital, n_sym)
            if s.apr > best_apr:
                best_thr, best_apr = thr, s.apr
        test = _with_warmup(funding, train_end, test_end, cfg.strategy.lookback)
        test_res = _trim(run_backtest(test, best_thr, cfg), train_end)
        test_sum = summarise(test_res, capital, n_sym)
        windows.append(WalkForwardWindow(train_start, train_end, min(test_end, t_last), best_thr, best_apr, test_sum))
        oos_frames.append(test_res.equity[["ts", "pnl", "n_open"]])
        train_start = train_start + pd.Timedelta(days=wf.step_days)

    if oos_frames:
        oos = pd.concat(oos_frames, ignore_index=True).sort_values("ts").reset_index(drop=True)
        oos["cum_pnl"] = oos["pnl"].cumsum()
        oos["equity"] = capital + oos["cum_pnl"]
    else:
        oos = pd.DataFrame(columns=["ts", "pnl", "n_open", "cum_pnl", "equity"])

    # Build a lightweight BacktestResult-like summary for the stitched OOS curve.
    stitched = BacktestResult(threshold=float("nan"), per_symbol={}, equity=oos)
    oos_summary = summarise(stitched, capital, n_sym)
    oos_summary.net_pnl = float(oos["pnl"].sum()) if not oos.empty else 0.0
    oos_summary.apr = (oos_summary.net_pnl / capital) * (365.0 / oos_summary.days) if oos_summary.days > 0 else 0.0
    oos_summary.trades = sum(w.test_summary.trades for w in windows)
    oos_summary.funding_pnl = sum(w.test_summary.funding_pnl for w in windows)
    oos_summary.costs = sum(w.test_summary.costs for w in windows)
    return WalkForwardResult(windows=windows, oos_equity=oos, oos_summary=oos_summary)
