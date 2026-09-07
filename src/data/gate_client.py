"""Read-only client for Gate.io API v4 public endpoints (USDT perpetuals + spot tickers).

Safety design:
* GET only.
* An explicit allow-list of public endpoint paths; anything else raises before a request.
* No API key, signature or private header is ever attached.

Gate specifics handled here:
* symbols are ``BTC_USDT`` (perp contract and spot pair share the name) -> canonical ``BTCUSDT``;
* ``funding_rate`` history accepts ``from``/``to`` (seconds) but only ~30 days per call and
  at most 180 days back, so we page in 30-day windows;
* funding interval is 8h for most contracts (``funding_interval`` seconds is exposed).
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any

import pandas as pd
import requests

from src.data.exchange import Ticker, canonical
from src.data.storage import FUNDING_COLUMNS, KLINE_COLUMNS, merge_funding

log = logging.getLogger(__name__)

BASE_URL = "https://api.gateio.ws"

FUT_CONTRACTS = "/api/v4/futures/usdt/contracts"
FUT_TICKERS = "/api/v4/futures/usdt/tickers"
FUT_FUNDING = "/api/v4/futures/usdt/funding_rate"
FUT_CANDLES = "/api/v4/futures/usdt/candlesticks"
SPOT_TICKERS = "/api/v4/spot/tickers"

ALLOWED_PATHS = frozenset({FUT_CONTRACTS, FUT_TICKERS, FUT_FUNDING, FUT_CANDLES, SPOT_TICKERS})

DAY_S = 86_400
WINDOW_S = 29 * DAY_S          # one funding_rate page (~87 settlements at 8h)
MAX_HISTORY_DAYS = 180


class GateError(RuntimeError):
    """Non-2xx / malformed answer after retries."""


class ForbiddenEndpoint(ValueError):
    """Attempt to reach anything outside the public allow-list."""


def to_gate(symbol: str) -> str:
    """``BTCUSDT`` -> ``BTC_USDT`` (quote is always USDT in this project)."""
    s = canonical(symbol)
    return s[:-4] + "_USDT" if s.endswith("USDT") and "_" not in symbol else symbol


@dataclass
class GatePublicClient:
    base_url: str = BASE_URL
    timeout: float = 15.0
    max_retries: int = 4
    backoff: float = 1.5
    session: requests.Session = field(default_factory=requests.Session)
    name: str = "gate"
    max_history_days: int = MAX_HISTORY_DAYS

    # ----- transport -----------------------------------------------------

    def get(self, path: str, params: dict[str, Any] | None = None) -> Any:
        if path not in ALLOWED_PATHS:
            raise ForbiddenEndpoint(f"{path!r} is not a public market-data endpoint")
        url = self.base_url.rstrip("/") + path
        last_err: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout, headers={"Accept": "application/json"})
                if resp.status_code == 429 or resp.status_code >= 500:
                    raise GateError(f"HTTP {resp.status_code}")
                resp.raise_for_status()
                body = resp.json()
                if isinstance(body, dict) and "label" in body:
                    raise GateError(f"{body.get('label')}: {body.get('message')}")
                return body
            except (requests.RequestException, GateError, ValueError) as exc:
                last_err = exc
                if attempt == self.max_retries:
                    break
                sleep = self.backoff ** attempt
                log.warning("GET %s failed (%s), retry %d/%d in %.1fs", path, exc, attempt, self.max_retries, sleep)
                time.sleep(sleep)
        raise GateError(f"GET {path} failed after {self.max_retries} attempts: {last_err}")

    # ----- MarketDataSource ----------------------------------------------

    @staticmethod
    def _ticker(row: dict[str, Any]) -> Ticker:
        return Ticker(
            symbol=canonical(row["contract"]),
            last_price=float(row["last"]),
            mark_price=float(row.get("mark_price") or row["last"]),
            turnover_24h=float(row.get("volume_24h_settle") or row.get("volume_24h_quote") or 0),
            funding_rate=float(row["funding_rate"]) if row.get("funding_rate") not in (None, "") else None,
        )

    def perp_tickers(self) -> list[Ticker]:
        rows = self.get(FUT_TICKERS)
        return [self._ticker(r) for r in rows if str(r.get("contract", "")).endswith("_USDT")]

    def perp_ticker(self, symbol: str) -> Ticker:
        rows = self.get(FUT_TICKERS, {"contract": to_gate(symbol)})
        if not rows:
            raise GateError(f"no perp ticker for {symbol}")
        return self._ticker(rows[0])

    def spot_price(self, symbol: str) -> float:
        rows = self.get(SPOT_TICKERS, {"currency_pair": to_gate(symbol)})
        if not rows:
            raise GateError(f"no spot ticker for {symbol}")
        return float(rows[0]["last"])

    @staticmethod
    def parse_funding_rows(symbol: str, rows: list[dict[str, Any]]) -> pd.DataFrame:
        if not rows:
            return pd.DataFrame(columns=FUNDING_COLUMNS)
        df = pd.DataFrame(
            {
                "symbol": canonical(symbol),
                "ts": pd.to_datetime([int(r["t"]) for r in rows], unit="s", utc=True),
                "funding_rate": [float(r["r"]) for r in rows],
            }
        )
        return df.drop_duplicates("ts").sort_values("ts").reset_index(drop=True)

    def funding_history(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        start_s = max(start_ms // 1000, int(time.time()) - self.max_history_days * DAY_S + 60)
        end_s = end_ms // 1000
        frames: list[pd.DataFrame] = []
        cursor = start_s
        while cursor < end_s:
            window_end = min(cursor + WINDOW_S, end_s)
            rows = self.get(FUT_FUNDING, {"contract": to_gate(symbol), "limit": 1000, "from": cursor, "to": window_end})
            frames.append(self.parse_funding_rows(symbol, rows))
            cursor = window_end + 1
            time.sleep(0.1)
        if not frames:
            return pd.DataFrame(columns=FUNDING_COLUMNS)
        return merge_funding(None, pd.concat(frames, ignore_index=True))

    def recent_funding(self, symbol: str, n: int) -> list[tuple[datetime, float]]:
        rows = self.get(FUT_FUNDING, {"contract": to_gate(symbol), "limit": max(n, 1)})
        pairs = [(datetime.fromtimestamp(int(r["t"]), tz=timezone.utc), float(r["r"])) for r in rows]
        return sorted(pairs)[-n:]

    def daily_klines(self, symbol: str, start_ms: int, end_ms: int) -> pd.DataFrame:
        rows = self.get(
            FUT_CANDLES,
            {"contract": to_gate(symbol), "interval": "1d", "from": start_ms // 1000, "to": end_ms // 1000},
        )
        if not rows:
            return pd.DataFrame(columns=KLINE_COLUMNS)
        df = pd.DataFrame(
            {
                "symbol": canonical(symbol),
                "ts": pd.to_datetime([int(r["t"]) for r in rows], unit="s", utc=True),
                "open": [float(r["o"]) for r in rows],
                "high": [float(r["h"]) for r in rows],
                "low": [float(r["l"]) for r in rows],
                "close": [float(r["c"]) for r in rows],
                "volume": [float(r["v"]) for r in rows],
                "turnover": [float(r.get("sum") or 0) for r in rows],
            }
        )
        return df.drop_duplicates("ts").sort_values("ts").reset_index(drop=True)
