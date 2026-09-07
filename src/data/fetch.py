"""Download one year of funding history and daily klines for the universe into Parquet.

Failures are retried inside the client; a symbol that still fails is skipped and
recorded in the returned ``FetchResult.skipped`` so the caller can log it.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

import pandas as pd

from src.config import Config
from src.data.bybit_client import BybitError, BybitPublicClient
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


def parse_funding_rows(symbol: str, rows: list[dict]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=FUNDING_COLUMNS)
    df = pd.DataFrame(
        {
            "symbol": symbol,
            "ts": pd.to_datetime([int(r["fundingRateTimestamp"]) for r in rows], unit="ms", utc=True),
            "funding_rate": [float(r["fundingRate"]) for r in rows],
        }
    )
    return df.drop_duplicates("ts").sort_values("ts").reset_index(drop=True)


def parse_kline_rows(symbol: str, rows: list[list[str]]) -> pd.DataFrame:
    if not rows:
        return pd.DataFrame(columns=KLINE_COLUMNS)
    df = pd.DataFrame(rows, columns=["ts", "open", "high", "low", "close", "volume", "turnover"])
    df["ts"] = pd.to_datetime(df["ts"].astype("int64"), unit="ms", utc=True)
    for c in ["open", "high", "low", "close", "volume", "turnover"]:
        df[c] = df[c].astype(float)
    df.insert(0, "symbol", symbol)
    return df.drop_duplicates("ts").sort_values("ts").reset_index(drop=True)


def fetch_funding_history(client: BybitPublicClient, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
    """Page backwards through /v5/market/funding/history (200 rows per call)."""
    frames: list[pd.DataFrame] = []
    cursor_end = end_ms
    while cursor_end > start_ms:
        rows = client.funding_history(symbol, start_ms=start_ms, end_ms=cursor_end, limit=200)
        if not rows:
            break
        df = parse_funding_rows(symbol, rows)
        frames.append(df)
        oldest = int(df["ts"].min().timestamp() * 1000)
        if oldest <= start_ms or len(rows) < 200:
            break
        cursor_end = oldest - 1
        time.sleep(0.1)  # stay far below public rate limits
    if not frames:
        return pd.DataFrame(columns=FUNDING_COLUMNS)
    return merge_funding(None, pd.concat(frames, ignore_index=True))


def fetch_daily_klines(client: BybitPublicClient, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    cursor_end = end_ms
    while cursor_end > start_ms:
        rows = client.kline(symbol, interval="D", start_ms=start_ms, end_ms=cursor_end, limit=1000)
        if not rows:
            break
        df = parse_kline_rows(symbol, rows)
        frames.append(df)
        oldest = int(df["ts"].min().timestamp() * 1000)
        if oldest <= start_ms or len(rows) < 1000:
            break
        cursor_end = oldest - 1
        time.sleep(0.1)
    if not frames:
        return pd.DataFrame(columns=KLINE_COLUMNS)
    return pd.concat(frames, ignore_index=True).drop_duplicates(["symbol", "ts"]).sort_values("ts")


def fetch_all(client: BybitPublicClient, symbols: list[str], cfg: Config, end_ms: int | None = None) -> FetchResult:
    end_ms = end_ms or _now_ms()
    start_ms = end_ms - cfg.universe.history_days * DAY_MS
    funding_frames, kline_frames, skipped = [], [], {}
    for sym in symbols:
        try:
            funding_frames.append(fetch_funding_history(client, sym, start_ms, end_ms))
            kline_frames.append(fetch_daily_klines(client, sym, start_ms, end_ms))
            log.info("fetched %s", sym)
        except BybitError as exc:
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


def default_window(days: int) -> tuple[int, int]:
    end = datetime.now(tz=timezone.utc)
    start = end - timedelta(days=days)
    return int(start.timestamp() * 1000), int(end.timestamp() * 1000)
