"""Shared fixtures: a fake Bybit client that serves canned v5-shaped responses, synthetic funding data."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from src.config import Config, load_config
from src.data.bybit_client import ALLOWED_PREFIX, ForbiddenEndpoint

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


class FakeBybitClient:
    """Serves the same shapes as Bybit v5 so parsing code is exercised end to end."""

    def __init__(self, now: datetime, rates: dict[str, list[float]], prices: dict[str, float], fail: set[str] | None = None):
        self.now = now
        self.rates = rates
        self.prices = prices
        self.fail = fail or set()
        self.calls: list[tuple[str, dict]] = []

    def get(self, path: str, params=None):
        if not path.startswith(ALLOWED_PREFIX):
            raise ForbiddenEndpoint(path)
        self.calls.append((path, params or {}))
        raise NotImplementedError("tests use typed helpers")

    def _check(self, symbol: str | None):
        from src.data.bybit_client import BybitError

        if symbol in self.fail:
            raise BybitError(f"simulated outage for {symbol}")

    def tickers(self, category="linear", symbol=None):
        self._check(symbol)
        self.calls.append(("tickers", {"category": category, "symbol": symbol}))
        syms = [symbol] if symbol else list(self.prices)
        out = []
        for i, s in enumerate(syms):
            p = self.prices[s] * (1.0005 if category == "linear" else 1.0)  # small positive basis
            out.append(
                {
                    "symbol": s,
                    "lastPrice": f"{p:.4f}",
                    "markPrice": f"{p:.4f}",
                    "turnover24h": str(1e9 / (i + 1)),
                    "fundingRate": f"{self.rates[s][-1]:.6f}",
                    "nextFundingTime": str(int((self.now + timedelta(hours=8)).timestamp() * 1000)),
                }
            )
        return out

    def funding_history(self, symbol, start_ms=None, end_ms=None, limit=200, category="linear"):
        self._check(symbol)
        self.calls.append(("funding_history", {"symbol": symbol, "limit": limit}))
        rates = self.rates[symbol]
        rows = []
        for k, r in enumerate(reversed(rates[-limit:])):
            ts = self.now - timedelta(hours=8 * k)
            rows.append({"symbol": symbol, "fundingRate": f"{r:.8f}", "fundingRateTimestamp": str(int(ts.timestamp() * 1000))})
        return rows  # newest first, like the real API

    def kline(self, symbol, interval="D", start_ms=None, end_ms=None, limit=1000, category="linear"):
        self._check(symbol)
        rows = []
        for k in range(min(limit, 5)):
            ts = self.now - timedelta(days=k)
            p = self.prices[symbol]
            rows.append([str(int(ts.timestamp() * 1000)), str(p), str(p * 1.01), str(p * 0.99), str(p), "100", str(100 * p)])
        return rows
