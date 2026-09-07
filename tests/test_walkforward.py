from __future__ import annotations

import pandas as pd

from src.backtest.walkforward import run_walkforward


def test_walkforward_windows_and_oos_curve(funding_df, cfg):
    wf = run_walkforward(funding_df, cfg)
    # 365 days, train 90 / test 30 / step 30 -> windows while train_end < last ts
    assert len(wf.windows) >= 8
    for w in wf.windows:
        assert w.chosen_threshold in cfg.strategy.thresholds
        assert (w.train_end - w.train_start) == pd.Timedelta(days=cfg.walkforward.train_days)
        assert w.test_end > w.train_end
    oos = wf.oos_equity
    assert not oos.empty
    assert oos["ts"].is_monotonic_increasing
    assert oos["ts"].min() >= wf.windows[0].train_end  # OOS never overlaps the first train set
    assert wf.oos_summary.net_pnl == oos["pnl"].sum()
    assert wf.oos_summary.trades == sum(w.test_summary.trades for w in wf.windows)


def test_walkforward_no_lookahead_in_test_slices(funding_df, cfg):
    """OOS PnL for a window must depend only on data up to its test_end."""
    wf_full = run_walkforward(funding_df, cfg)
    first = wf_full.windows[0]
    truncated = funding_df[funding_df["ts"] < first.test_end]
    wf_trunc = run_walkforward(truncated, cfg)
    assert wf_trunc.windows[0].chosen_threshold == first.chosen_threshold
    assert wf_trunc.windows[0].test_summary.net_pnl == first.test_summary.net_pnl
