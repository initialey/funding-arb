"""Download funding history and daily klines for the universe into Parquet.

Works against any :class:`MarketDataSource`. Failures are retried inside the
client; a symbol that still fails is skipped and recorded in
``FetchResult.skipped`` so the caller can log it.
"""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime, timezone

import pandas as pd

from src.config import Config
from src.data.exchange import MarketDataSource
from src.data.storage import (
    FUNDING_COLUMNS,
    KLINE_COLUMNS,
    funding_path,
    kline_path,
    load_parquet,
    merge_funding,
    save_parquet,
)

log = logging.getLogger(__name__)

DAY_MS = 86_400_000


@dataclass
class FetchResult:
    funding: pd.DataFrame
    klines: pd.DataFrame
    skipped: dict[str, str] = field(default_factory=dict)


def _now_ms() -> int:
    return int(datetime.now(tz=timezone.utc).timestamp() * 1000)


def fetch_all(source: MarketDataSource, symbols: list[str], cfg: Config, end_ms: int | None = None) -> FetchResult:
    end_ms = end_ms or _now_ms()
    days = min(cfg.universe.history_days, source.max_history_days)
    start_ms = end_ms - days * DAY_MS
    funding_frames, kline_frames, skipped = [], [], {}
    for sym in symbols:
        try:
            funding_frames.append(source.funding_history(sym, start_ms, end_ms))
            kline_frames.append(source.daily_klines(sym, start_ms, end_ms))
            log.info("fetched %s", sym)
        except Exception as exc:  # adapter-specific error types; skip and record
            skipped[sym] = str(exc)
            log.error("skipping %s: %s", sym, exc)
    funding = merge_funding(None, pd.concat(funding_frames, ignore_index=True)) if funding_frames else pd.DataFrame(columns=FUNDING_COLUMNS)
    klines = pd.concat(kline_frames, ignore_index=True) if kline_frames else pd.DataFrame(columns=KLINE_COLUMNS)
    return FetchResult(funding=funding, klines=klines, skipped=skipped)


def update_parquet(result: FetchResult, cfg: Config) -> None:
    """Merge freshly fetched rows into the on-disk Parquet files (incremental-safe)."""
    fp, kp = funding_path(cfg.data_dir), kline_path(cfg.data_dir)
    old_f = load_parquet(fp) if fp.exists() else None
    save_parquet(merge_funding(old_f, result.funding), fp)
    old_k = load_parquet(kp) if kp.exists() else None
    frames = [f for f in (old_k, result.klines) if f is not None and not f.empty]
    klines = (
        pd.concat(frames, ignore_index=True).drop_duplicates(["symbol", "ts"], keep="last").sort_values(["symbol", "ts"])
        if frames
        else pd.DataFrame(columns=KLINE_COLUMNS)
    )
    save_parquet(klines.reset_index(drop=True), kp)
