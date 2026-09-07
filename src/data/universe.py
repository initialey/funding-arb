"""Select the trading universe: core symbols plus top USDT perps by 24h turnover."""
from __future__ import annotations

from src.config import UniverseConfig
from src.data.exchange import MarketDataSource, Ticker


def rank_by_turnover(tickers: list[Ticker], quote: str) -> list[str]:
    """Canonical perp symbols quoted in ``quote``, sorted by 24h turnover, highest first."""
    rows = [(t.turnover_24h, t.symbol) for t in tickers if t.symbol.endswith(quote)]
    rows.sort(reverse=True)
    return [s for _, s in rows]


def eligible(t: Ticker, cfg: UniverseConfig) -> bool:
    """Crypto USDT perps only: not on the exclude list, standard funding interval when known."""
    if t.symbol in cfg.exclude:
        return False
    if cfg.funding_interval_s and t.funding_interval_s and t.funding_interval_s != cfg.funding_interval_s:
        return False
    return True


def select_universe(tickers: list[Ticker], cfg: UniverseConfig) -> list[str]:
    ranked = rank_by_turnover([t for t in tickers if eligible(t, cfg)], cfg.quote)
    chosen = [s for s in cfg.core if s in ranked or not ranked]
    for sym in ranked:
        if len(chosen) >= cfg.size:
            break
        if sym not in chosen:
            chosen.append(sym)
    return chosen[: cfg.size]


def fetch_universe(source: MarketDataSource, cfg: UniverseConfig) -> list[str]:
    return select_universe(source.perp_tickers(), cfg)
