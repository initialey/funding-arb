"""Shared fixtures: an in-memory MarketDataSource and synthetic funding data."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from src.config import Config, load_config
from src.data.exchange import Ticker
from src.data.storage import FUNDING_COLUMNS, KLINE_COLUMNS

ROOT = Path(__file__).resolve().parent.parent
T0 = datetime(2025, 1, 1, tzinfo=timezone.utc)


@pytest.fixture
def cfg() -> Config:
    return load_config(ROOT / "config.toml")


def synthetic_funding(symbols: list[str], n_events: int = 3 * 365, seed: int = 7, start: datetime = T0) -> pd.DataFrame:
    """8-hourly funding with symbol-specific mean, mild autocorrelation, positive drift for majors."""
    rng = np.random.default_rng(seed)
    frames = []
    ts = pd.date_range(start, periods=n_events, freq="8h", tz="UTC")
    for i, sym in enumerate(symbols):
        mean = 0.0001 * (1 + 0.5 * i / max(len(symbols) - 1, 1))
        noise = rng.normal(0, 0.00012, n_events)
        rates = np.empty(n_events)
        rates[0] = mean
        for k in range(1, n_events):
            rates[k] = 0.7 * rates[k - 1] + 0.3 * mean + noise[k]
        frames.append(pd.DataFrame({"symbol": sym, "ts": ts, "funding_rate": rates}))
    return pd.concat(frames, ignore_index=True)


@pytest.fixture
def funding_df() -> pd.DataFrame:
    return synthetic_funding(["BTCUSDT", "ETHUSDT", "SOLUSDT", "XRPUSDT"])


class SourceOutage(RuntimeError):
    pass


class FakeSource:
    """In-memory MarketDataSource: 8h settlements ending at ``now``, small positive perp basis."""

    name = "fake"
    max_history_days = 365

    def __init__(self, now: datetime, rates: dict[str, list[float]], prices: dict[str, float], fail: set[str] | None = None):
        self.now = now
        self.rates = rates
        self.prices = prices
        self.fail = fail or set()
        self.calls: list[tuple[str, str | None]] = []

    def _check(self, symbol: str | None, what: str):
        self.calls.append((what, symbol))
        if symbol in self.fail:
            raise SourceOutage(f"simulated outage for {symbol}")

    def _ticker(self, s: str, i: int) -> Ticker:
        p = self.prices[s] * 1.0005
        return Ticker(symbol=s, last_price=p, mark_price=p, turnover_24h=1e9 / (i + 1), funding_rate=self.rates[s][-1],
                      next_funding_time=self.now + timedelta(hours=8))

    def perp_tickers(self) -> list[Ticker]:
        self._check(None, "perp_tickers")
        return [self._ticker(s, i) for i, s in enumerate(self.prices)]

    def perp_ticker(self, symbol: str) -> Ticker:
        self._check(symbol, "perp_ticker")
        return self._ticker(symbol, list(self.prices).index(symbol))

    def spot_price(self, symbol: str) -> float:
        self._check(symbol, "spot_price")
        return self.prices[symbol]

    def recent_funding(self, symbol: str, n: int) -> list[tuple[datetime, float]]:
        self._check(symbol, "recent_funding")
        rates = self.rates[symbol][-n:]
        return [(self.now - timedelta(hours=8 * (len(rates) - 1 - k)), r) for k, r in enumerate(rates)]

    def funding_history(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        self._check(symbol, "funding_history")
        pairs = self.recent_funding(symbol, len(self.rates[symbol]))
        return pd.DataFrame({"symbol": symbol, "ts": [t for t, _ in pairs], "funding_rate": [r for _, r in pairs]}, columns=FUNDING_COLUMNS)

    def daily_klines(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        self._check(symbol, "daily_klines")
        p = self.prices[symbol]
        rows = [{"symbol": symbol, "ts": self.now - timedelta(days=k), "open": p, "high": p * 1.01, "low": p * 0.99, "close": p,
                 "volume": 100.0, "turnover": 100.0 * p} for k in range(5)]
        return pd.DataFrame(rows, columns=KLINE_COLUMNS)
