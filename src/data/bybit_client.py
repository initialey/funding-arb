"""Minimal read-only client for the Bybit v5 *public* market endpoints.

Safety design:
* Only HTTP GET is ever issued.
* Only paths under ``/v5/market/`` are accepted; anything else raises before a request is made.
* No API key, signature or private header is ever attached.
"""
from __future__ import annotations

import logging
import time
from dataclasses import dataclass, field
from typing import Any

import requests

log = logging.getLogger(__name__)

BASE_URL = "https://api.bybit.com"
ALLOWED_PREFIX = "/v5/market/"

FUNDING_HISTORY = "/v5/market/funding/history"
TICKERS = "/v5/market/tickers"
KLINE = "/v5/market/kline"
SERVER_TIME = "/v5/market/time"


class BybitError(RuntimeError):
    """Raised when the API answers with a non-zero retCode or after retries are exhausted."""


class ForbiddenEndpoint(ValueError):
    """Raised when code tries to reach anything outside the public market namespace."""


@dataclass
class BybitPublicClient:
    base_url: str = BASE_URL
    timeout: float = 15.0
    max_retries: int = 4
    backoff: float = 1.5
    session: requests.Session = field(default_factory=requests.Session)

    def get(self, path: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
        if not path.startswith(ALLOWED_PREFIX):
            raise ForbiddenEndpoint(f"only {ALLOWED_PREFIX}* is allowed, got {path!r}")
        url = self.base_url.rstrip("/") + path
        last_err: Exception | None = None
        for attempt in range(1, self.max_retries + 1):
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout)
                if resp.status_code == 429 or resp.status_code >= 500:
                    raise BybitError(f"HTTP {resp.status_code}")
                resp.raise_for_status()
                body = resp.json()
                if body.get("retCode") != 0:
                    raise BybitError(f"retCode={body.get('retCode')} retMsg={body.get('retMsg')}")
                return body["result"]
            except (requests.RequestException, BybitError, ValueError, KeyError) as exc:
                last_err = exc
                if attempt == self.max_retries:
                    break
                sleep = self.backoff ** attempt
                log.warning("GET %s failed (%s), retry %d/%d in %.1fs", path, exc, attempt, self.max_retries, sleep)
                time.sleep(sleep)
        raise BybitError(f"GET {path} failed after {self.max_retries} attempts: {last_err}")

    # ----- typed helpers -------------------------------------------------

    def server_time_ms(self) -> int:
        return int(self.get(SERVER_TIME)["timeNano"]) // 1_000_000

    def tickers(self, category: str = "linear", symbol: str | None = None) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"category": category}
        if symbol:
            params["symbol"] = symbol
        return self.get(TICKERS, params)["list"]

    def funding_history(
        self,
        symbol: str,
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int = 200,
        category: str = "linear",
    ) -> list[dict[str, Any]]:
        params: dict[str, Any] = {"category": category, "symbol": symbol, "limit": min(limit, 200)}
        if start_ms is not None:
            params["startTime"] = start_ms
        if end_ms is not None:
            params["endTime"] = end_ms
        return self.get(FUNDING_HISTORY, params)["list"]

    def kline(
        self,
        symbol: str,
        interval: str = "D",
        start_ms: int | None = None,
        end_ms: int | None = None,
        limit: int = 1000,
        category: str = "linear",
    ) -> list[list[str]]:
        params: dict[str, Any] = {"category": category, "symbol": symbol, "interval": interval, "limit": min(limit, 1000)}
        if start_ms is not None:
            params["start"] = start_ms
        if end_ms is not None:
            params["end"] = end_ms
        return self.get(KLINE, params)["list"]
