"""Select the trading universe: core symbols plus top USDT linear perps by 24h turnover."""
from __future__ import annotations

from typing import Any

from src.config import UniverseConfig
from src.data.bybit_client import BybitPublicClient


def rank_by_turnover(tickers: list[dict[str, Any]], quote: str) -> list[str]:
    """Return USDT-margined perp symbols sorted by 24h turnover, highest first."""
    rows = []
    for t in tickers:
        sym = t.get("symbol", "")
        if not sym.endswith(quote):
            continue
        # skip dated futures like BTCUSDT-27DEC24 and pre-market tickers
        if "-" in sym:
            continue
        try:
            turnover = float(t.get("turnover24h") or 0)
        except ValueError:
            continue
        rows.append((turnover, sym))
    rows.sort(reverse=True)
    return [s for _, s in rows]


def select_universe(tickers: list[dict[str, Any]], cfg: UniverseConfig) -> list[str]:
    ranked = rank_by_turnover(tickers, cfg.quote)
    chosen = [s for s in cfg.core if s in ranked or not ranked]
    for sym in ranked:
        if len(chosen) >= cfg.size:
            break
        if sym not in chosen:
            chosen.append(sym)
    return chosen[: cfg.size]


def fetch_universe(client: BybitPublicClient, cfg: UniverseConfig) -> list[str]:
    return select_universe(client.tickers("linear"), cfg)
