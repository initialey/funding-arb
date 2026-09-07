"""Entry/exit signal: trailing mean of the last N *settled* funding rates.

At funding event ``t`` the decision uses rates ``t-N .. t-1`` only, so a position
opened on the signal is held through settlement ``t`` and earns ``rate_t``.
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def trailing_signal(rates: pd.Series, lookback: int) -> pd.Series:
    """Mean of the previous ``lookback`` rates, shifted so row t excludes rate_t."""
    return rates.shift(1).rolling(lookback, min_periods=lookback).mean()


def desired_positions(signal: pd.Series, threshold: float, exit_threshold: float | None = None) -> pd.Series:
    """Boolean series: True where a spot-long/perp-short pair should be held at that settlement.

    Enter when signal >= threshold, exit when signal < exit_threshold (defaults to threshold).
    Positions carry over between events (hysteresis is possible by giving a lower exit level).
    """
    exit_threshold = threshold if exit_threshold is None else exit_threshold
    sig = signal.to_numpy(dtype=float)
    held = np.zeros(len(sig), dtype=bool)
    state = False
    for i, s in enumerate(sig):
        if np.isnan(s):
            state = False
        elif state:
            state = s >= exit_threshold
        else:
            state = s >= threshold
        held[i] = state
    return pd.Series(held, index=signal.index)
