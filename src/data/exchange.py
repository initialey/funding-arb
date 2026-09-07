"""Exchange-agnostic read-only market-data interface.

Every adapter speaks in *canonical* symbols (``BTCUSDT``) and returns the same
shapes, so the backtest and paper trader never know which venue is behind them.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol

import pandas as pd


@dataclass(frozen=True)
class Ticker:
    symbol: str                # canonical, e.g. BTCUSDT
    last_price: float
    mark_price: float
    turnover_24h: float        # quote-currency (USDT) volume over 24h
    funding_rate: float | None = None
    next_funding_time: datetime | None = None


class MarketDataSource(Protocol):
    """Read-only public market data. Implementations must issue GET requests only."""

    name: str
    max_history_days: int      # how far back funding history can be fetched

    def perp_tickers(self) -> list[Ticker]: ...

    def perp_ticker(self, symbol: str) -> Ticker: ...

    def spot_price(self, symbol: str) -> float: ...

    def funding_history(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        """Columns: symbol, ts (UTC), funding_rate. Sorted ascending, de-duplicated."""
        ...

    def recent_funding(self, symbol: str, n: int) -> list[tuple[datetime, float]]:
        """Last ``n`` settled (ts, rate) pairs, ascending."""
        ...

    def daily_klines(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        """Columns: symbol, ts, open, high, low, close, volume, turnover."""
        ...


def canonical(symbol: str) -> str:
    """Normalise venue symbols (``BTC_USDT``, ``BTC-USDT-SWAP``) to ``BTCUSDT``."""
    return symbol.replace("_", "").replace("-SWAP", "").replace("-", "").upper()
