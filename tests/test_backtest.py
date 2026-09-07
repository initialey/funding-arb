"""Strategy signal, engine accounting and metrics on hand-built and synthetic data."""
from __future__ import annotations

import numpy as np
import pandas as pd
import pytest

from src.backtest.engine import run_backtest, simulate_symbol
from src.backtest.metrics import max_drawdown, per_symbol_table, summarise
from src.backtest.strategy import desired_positions, trailing_signal


def _df(rates: list[float], symbol="BTCUSDT") -> pd.DataFrame:
    ts = pd.date_range("2025-01-01", periods=len(rates), freq="8h", tz="UTC")
    return pd.DataFrame({"symbol": symbol, "ts": ts, "funding_rate": rates})


def test_signal_excludes_current_rate():
    s = pd.Series([0.0001, 0.0002, 0.0003, 0.0004, 0.0005])
    sig = trailing_signal(s, 3)
    assert np.isnan(sig.iloc[2])
    assert sig.iloc[3] == pytest.approx(0.0002)  # mean of first three
    assert sig.iloc[4] == pytest.approx(0.0003)


def test_desired_positions_enter_exit():
    sig = pd.Series([np.nan, 0.0002, 0.0002, 0.00005, 0.0003])
    held = desired_positions(sig, 0.0001)
    assert list(held) == [False, True, True, False, True]


def test_engine_accounting_exact(cfg):
    # 3 warm-up rates, then 4 high rates -> enter at index 3, held through end -> closed at end.
    rates = [0.0001, 0.0001, 0.0001, 0.0003, 0.0003, 0.0003, 0.0003]
    r = simulate_symbol(_df(rates), "BTCUSDT", threshold=0.00005, cfg=cfg)
    notional = cfg.leg_notional
    assert r.trades == 1
    assert r.funding_pnl == pytest.approx(notional * 0.0003 * 4)
    assert r.costs == pytest.approx(cfg.costs.round_trip * notional)
    assert r.events["held"].tolist() == [False, False, False, True, True, True, True]


def test_negative_funding_is_paid_and_exit_triggers(cfg):
    rates = [0.0002, 0.0002, 0.0002, -0.0005, -0.0005, -0.0005, -0.0005, -0.0005]
    r = simulate_symbol(_df(rates), "BTCUSDT", threshold=0.0001, cfg=cfg)
    # enter at idx3 (signal 0.0002), receive -0.0005 there; signal at idx4 = mean(0.0002,0.0002,-0.0005) < thr -> exit.
    assert r.events["held"].tolist()[:5] == [False, False, False, True, False]
    assert r.funding_pnl == pytest.approx(cfg.leg_notional * -0.0005)
    assert r.trades == 1


def test_higher_threshold_trades_less(funding_df, cfg):
    low = run_backtest(funding_df, 0.00005, cfg)
    high = run_backtest(funding_df, 0.0002, cfg)
    # with equal entry/exit levels, "held" is exactly signal >= threshold, so exposure is monotonic
    assert low.equity["n_open"].sum() >= high.equity["n_open"].sum()
    n = funding_df["symbol"].nunique()
    s_low, s_high = summarise(low, cfg.capital.total_usdt, n), summarise(high, cfg.capital.total_usdt, n)
    assert s_low.exposure_days_ratio >= s_high.exposure_days_ratio
    assert -1 <= s_low.max_drawdown <= 0
    assert 0 <= s_low.avg_slot_utilisation <= 1
    assert s_low.days == pytest.approx(365 - 8 / 24, abs=0.5)


def test_summary_apr_matches_pnl(funding_df, cfg):
    res = run_backtest(funding_df, 0.0001, cfg)
    s = summarise(res, cfg.capital.total_usdt, funding_df["symbol"].nunique())
    assert s.net_pnl == pytest.approx(res.totals()["net_pnl"])
    assert s.apr == pytest.approx(s.net_pnl / cfg.capital.total_usdt * 365 / s.days)
    tbl = per_symbol_table(res, cfg.slot_usdt)
    assert set(tbl["symbol"]) == set(funding_df["symbol"].unique())
    assert tbl["net_pnl"].sum() == pytest.approx(s.net_pnl)


def test_max_drawdown():
    eq = pd.Series([10000, 10100, 9900, 10200, 9800.0])
    assert max_drawdown(eq, 10000) == pytest.approx(-0.04)
