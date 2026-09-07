"""Client behaviour: endpoint allow-lists, retries, response parsing, universe ranking."""
from __future__ import annotations

from unittest.mock import MagicMock

import pandas as pd
import pytest
import requests

from src.config import UniverseConfig
from src.data.bybit_client import BybitError, BybitPublicClient, ForbiddenEndpoint
from src.data.bybit_source import parse_funding_rows, parse_kline_rows
from src.data.exchange import Ticker, canonical
from src.data.gate_client import ForbiddenEndpoint as GateForbidden
from src.data.gate_client import GateError, GatePublicClient, to_gate
from src.data.universe import select_universe


def _resp(status=200, body=None):
    r = MagicMock()
    r.status_code = status
    r.json.return_value = body if body is not None else {"retCode": 0, "retMsg": "OK", "result": {"list": []}}
    r.raise_for_status = MagicMock()
    return r


# ---------------------------------------------------------------- Bybit

def test_bybit_forbidden_endpoint_never_hits_network():
    sess = MagicMock()
    c = BybitPublicClient(session=sess)
    for path in ["/v5/order/create", "/v5/position/list", "/v5/account/wallet-balance", "/v5/order/cancel"]:
        with pytest.raises(ForbiddenEndpoint):
            c.get(path)
    sess.get.assert_not_called()


def test_bybit_retry_then_success(monkeypatch):
    monkeypatch.setattr("src.data.bybit_client.time.sleep", lambda s: None)
    sess = MagicMock()
    sess.get.side_effect = [requests.ConnectionError("boom"), _resp(500), _resp(200, {"retCode": 0, "result": {"list": [1]}})]
    c = BybitPublicClient(session=sess, max_retries=4)
    assert c.get("/v5/market/tickers", {"category": "linear"}) == {"list": [1]}
    assert sess.get.call_count == 3


def test_bybit_retry_exhausted_raises(monkeypatch):
    monkeypatch.setattr("src.data.bybit_client.time.sleep", lambda s: None)
    sess = MagicMock()
    sess.get.return_value = _resp(200, {"retCode": 10001, "retMsg": "bad", "result": {}})
    c = BybitPublicClient(session=sess, max_retries=2)
    with pytest.raises(BybitError):
        c.get("/v5/market/tickers")
    assert sess.get.call_count == 2


def test_bybit_parse_rows():
    rows = [
        {"symbol": "BTCUSDT", "fundingRate": "0.0002", "fundingRateTimestamp": "1735718400000"},
        {"symbol": "BTCUSDT", "fundingRate": "0.0001", "fundingRateTimestamp": "1735689600000"},
    ]
    df = parse_funding_rows("BTCUSDT", rows)
    assert list(df["funding_rate"]) == [0.0001, 0.0002]
    assert isinstance(df["ts"].dtype, pd.DatetimeTZDtype) and str(df["ts"].dtype.tz) == "UTC"
    k = parse_kline_rows("BTCUSDT", [["1735689600000", "95000", "96000", "94000", "95500", "10", "955000"]])
    assert k.loc[0, "close"] == 95500.0 and k.loc[0, "symbol"] == "BTCUSDT"


# ---------------------------------------------------------------- Gate

def test_gate_symbol_mapping():
    assert to_gate("BTCUSDT") == "BTC_USDT"
    assert to_gate("BTC_USDT") == "BTC_USDT"
    assert canonical("BTC_USDT") == "BTCUSDT" and canonical("BTC-USDT-SWAP") == "BTCUSDT"


def test_gate_allowlist_blocks_everything_else():
    sess = MagicMock()
    c = GatePublicClient(session=sess)
    for path in ["/api/v4/futures/usdt/orders", "/api/v4/futures/usdt/positions", "/api/v4/spot/orders",
                 "/api/v4/wallet/total_balance", "/api/v4/futures/usdt/accounts"]:
        with pytest.raises(GateForbidden):
            c.get(path)
    sess.get.assert_not_called()
    assert sess.post.call_count == 0


def test_gate_only_get_and_no_credentials():
    sess = MagicMock()
    sess.get.return_value = _resp(200, [{"contract": "BTC_USDT", "last": "100", "mark_price": "100.1", "volume_24h_settle": "5", "funding_rate": "0.0001"}])
    c = GatePublicClient(session=sess)
    t = c.perp_ticker("BTCUSDT")
    assert t == Ticker(symbol="BTCUSDT", last_price=100.0, mark_price=100.1, turnover_24h=5.0, funding_rate=0.0001)
    assert sess.post.call_count == 0
    for call in sess.get.call_args_list:
        s = str(call).lower()
        assert "sign" not in s and "key" not in s


def test_gate_error_label_raises(monkeypatch):
    monkeypatch.setattr("src.data.gate_client.time.sleep", lambda s: None)
    sess = MagicMock()
    sess.get.return_value = _resp(200, {"label": "INVALID_PARAM_VALUE", "message": "from time exceeds 180-day limit"})
    c = GatePublicClient(session=sess, max_retries=2)
    with pytest.raises(GateError):
        c.get("/api/v4/futures/usdt/funding_rate", {"contract": "BTC_USDT"})


def test_gate_funding_history_pages_in_windows(monkeypatch):
    monkeypatch.setattr("src.data.gate_client.time.sleep", lambda s: None)
    calls: list[dict] = []

    def fake_get(path, params=None):
        calls.append(params)
        base = params["from"]
        return [{"t": base + k * 28800, "r": "0.0001"} for k in range(3)]

    c = GatePublicClient()
    monkeypatch.setattr(c, "get", fake_get)
    import time as _t
    end_ms = int(_t.time()) * 1000
    start_ms = end_ms - 100 * 86_400_000
    df = c.funding_history("BTCUSDT", start_ms, end_ms)
    assert len(calls) == 4  # 100 days / 29-day windows
    assert all(p["contract"] == "BTC_USDT" for p in calls)
    assert len(df) == 12 and df["ts"].is_monotonic_increasing and df["symbol"].iloc[0] == "BTCUSDT"


def test_gate_history_is_capped_at_180_days(monkeypatch):
    calls: list[dict] = []
    c = GatePublicClient()
    monkeypatch.setattr(c, "get", lambda path, params=None: calls.append(params) or [])
    import time as _t
    end_ms = int(_t.time()) * 1000
    c.funding_history("ETHUSDT", end_ms - 400 * 86_400_000, end_ms)
    assert calls and calls[0]["from"] >= int(_t.time()) - 180 * 86_400


def test_gate_parse_funding_rows():
    df = GatePublicClient.parse_funding_rows("BTC_USDT", [{"t": 1735718400, "r": "0.0002"}, {"t": 1735689600, "r": "0.0001"}])
    assert df["symbol"].iloc[0] == "BTCUSDT" and list(df["funding_rate"]) == [0.0001, 0.0002]


# ---------------------------------------------------------------- universe

def test_universe_selection_core_first_then_turnover():
    def t(sym, vol):
        return Ticker(symbol=sym, last_price=1, mark_price=1, turnover_24h=vol)

    tickers = [t("DOGEUSDT", 900), t("BTCUSDT", 1000), t("ETHUSDT", 800), t("SOLUSDT", 10), t("XRPUSDT", 700),
               t("BTCUSDC", 5000), t("ADAUSDT", 600)]
    cfg = UniverseConfig(core=["BTCUSDT", "ETHUSDT", "SOLUSDT"], size=5)
    assert select_universe(tickers, cfg) == ["BTCUSDT", "ETHUSDT", "SOLUSDT", "DOGEUSDT", "XRPUSDT"]
