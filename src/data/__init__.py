"""Read-only public market-data access (Gate.io / Bybit) and Parquet storage."""
from __future__ import annotations

from src.config import Config
from src.data.exchange import MarketDataSource


def make_source(cfg: Config) -> MarketDataSource:
    """Build the configured exchange adapter. Both adapters are GET-only public clients."""
    name = cfg.exchange.name.lower()
    if name == "gate":
        from src.data.gate_client import GatePublicClient

        return GatePublicClient()
    if name == "bybit":
        from src.data.bybit_source import BybitMarketData

        return BybitMarketData()
    raise ValueError(f"unknown exchange {cfg.exchange.name!r}; expected 'gate' or 'bybit'")
