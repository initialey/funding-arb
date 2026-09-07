"""MarketDataSource adapter over the Bybit v5 public client.

Note: api.bybit.com refuses requests from US IP ranges (HTTP 403), which includes
GitHub-hosted Actions runners. Use this adapter from a non-US machine, or pick the
Gate adapter for cloud runs.
"""
from __future__ import annotations

import time
from dataclasses import dataclass, field
from datetime import datetime, timezone

import pandas as pd

from src.data.bybit_client import BybitError, BybitPublicClient
from src.data.exchange import Ticker
from src.data.storage import FUNDING_COLUMNS, KLINE_COLUMNS, merge_funding


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


@dataclass
class BybitMarketData:
    client: BybitPublicClient = field(default_factory=BybitPublicClient)
    name: str = "bybit"
    max_history_days: int = 365

    @staticmethod
    def _ticker(t: dict) -> Ticker:
        nft = t.get("nextFundingTime")
        return Ticker(
            symbol=t["symbol"],
            last_price=float(t["lastPrice"]),
            mark_price=float(t.get("markPrice") or t["lastPrice"]),
            turnover_24h=float(t.get("turnover24h") or 0),
            funding_rate=float(t["fundingRate"]) if t.get("fundingRate") not in (None, "") else None,
            next_funding_time=datetime.fromtimestamp(int(nft) / 1000, tz=timezone.utc) if nft else None,
        )

    def perp_tickers(self) -> list[Ticker]:
        out = []
        for t in self.client.tickers("linear"):
            sym = t.get("symbol", "")
            if sym.endswith("USDT") and "-" not in sym:  # skip dated futures like BTCUSDT-27DEC24
                out.append(self._ticker(t))
        return out

    def perp_ticker(self, symbol: str) -> Ticker:
        rows = self.client.tickers("linear", symbol)
        if not rows:
            raise BybitError(f"no linear ticker for {symbol}")
        return self._ticker(rows[0])

    def spot_price(self, symbol: str) -> float:
        rows = self.client.tickers("spot", symbol)
        if not rows:
            raise BybitError(f"no spot ticker for {symbol}")
        return float(rows[0]["lastPrice"])

    def funding_history(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        """Page backwards through /v5/market/funding/history (200 rows per call)."""
        frames: list[pd.DataFrame] = []
        cursor_end = end_ms
        while cursor_end > start_ms:
            rows = self.client.funding_history(symbol, start_ms=start_ms, end_ms=cursor_end, limit=200)
            if not rows:
                break
            df = parse_funding_rows(symbol, rows)
            frames.append(df)
            oldest = int(df["ts"].min().timestamp() * 1000)
            if oldest <= start_ms or len(rows) < 200:
                break
            cursor_end = oldest - 1
            time.sleep(0.1)
        if not frames:
            return pd.DataFrame(columns=FUNDING_COLUMNS)
        return merge_funding(None, pd.concat(frames, ignore_index=True))

    def recent_funding(self, symbol: str, n: int) -> list[tuple[datetime, float]]:
        rows = self.client.funding_history(symbol, limit=max(n, 1))
        pairs = [(datetime.fromtimestamp(int(r["fundingRateTimestamp"]) / 1000, tz=timezone.utc), float(r["fundingRate"])) for r in rows]
        return sorted(pairs)[-n:]

    def daily_klines(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        frames: list[pd.DataFrame] = []
        cursor_end = end_ms
        while cursor_end > start_ms:
            rows = self.client.kline(symbol, interval="D", start_ms=start_ms, end_ms=cursor_end, limit=1000)
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
        return pd.concat(frames, ignore_index=True).drop_duplicates(["symbol", "ts"]).sort_values("ts").reset_index(drop=True)
