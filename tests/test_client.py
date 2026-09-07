"""Client behaviour: endpoint allow-list, retries, response parsing, universe ranking."""
from __future__ import annotations

from unittest.mock import MagicMock

import pandas as pd
import pytest
import requests

from src.config import UniverseConfig
from src.data.bybit_client import BybitError, BybitPublicClient, ForbiddenEndpoint
from src.data.fetch import parse_funding_rows, parse_kline_rows
from src.data.universe import select_universe


def _resp(status=200, body=None):
    r = MagicMock()
    r.status_code = status
    r.json.return_value = body or {"retCode": 0, "retMsg": "OK", "result": {"list": []}}
    r.raise_for_status = MagicMock()
    return r


def test_forbidden_endpoint_never_hits_network():
    sess = MagicMock()
    c = BybitPublicClient(session=sess)
    for path in ["/v5/order/create", "/v5/position/list", "/v5/account/wallet-balance", "/v5/order/cancel"]:
        with pytest.raises(ForbiddenEndpoint):
            c.get(path)
    sess.get.assert_not_called()
    assert not hasattr(sess, "post") or not sess.post.called


def test_retry_then_success(monkeypatch):
    monkeypatch.setattr("src.data.bybit_client.time.sleep", lambda s: None)
    sess = MagicMock()
    sess.get.side_effect = [requests.ConnectionError("boom"), _resp(500), _resp(200, {"retCode": 0, "result": {"list": [1]}})]
    c = BybitPublicClient(session=sess, max_retries=4)
    assert c.get("/v5/market/tickers", {"category": "linear"}) == {"list": [1]}
    assert sess.get.call_count == 3


def test_retry_exhausted_raises(monkeypatch):
    monkeypatch.setattr("src.data.bybit_client.time.sleep", lambda s: None)
    sess = MagicMock()
    sess.get.return_value = _resp(200, {"retCode": 10001, "retMsg": "bad", "result": {}})
    c = BybitPublicClient(session=sess, max_retries=2)
    with pytest.raises(BybitError):
        c.get("/v5/market/tickers")
    assert sess.get.call_count == 2


def test_only_get_is_used():
    sess = MagicMock()
    sess.get.return_value = _resp()
    c = BybitPublicClient(session=sess)
    c.tickers("linear")
    c.funding_history("BTCUSDT", limit=5)
    c.kline("BTCUSDT")
    assert sess.get.call_count == 3
    assert sess.post.call_count == 0
    for call in sess.get.call_args_list:
        assert "api_key" not in str(call).lower()
        assert "sign" not in str(call).lower()


def test_parse_funding_rows_sorted_and_typed():
    rows = [
        {"symbol": "BTCUSDT", "fundingRate": "0.0002", "fundingRateTimestamp": "1735718400000"},
        {"symbol": "BTCUSDT", "fundingRate": "0.0001", "fundingRateTimestamp": "1735689600000"},
    ]
    df = parse_funding_rows("BTCUSDT", rows)
    assert list(df["funding_rate"]) == [0.0001, 0.0002]
    assert isinstance(df["ts"].dtype, pd.DatetimeTZDtype) and str(df["ts"].dtype.tz) == "UTC"


def test_parse_kline_rows():
    rows = [["1735689600000", "95000", "96000", "94000", "95500", "10", "955000"]]
    df = parse_kline_rows("BTCUSDT", rows)
    assert df.loc[0, "close"] == 95500.0 and df.loc[0, "symbol"] == "BTCUSDT"


def test_universe_selection_core_first_then_turnover():
    tickers = [
        {"symbol": "DOGEUSDT", "turnover24h": "900"},
        {"symbol": "BTCUSDT", "turnover24h": "1000"},
        {"symbol": "ETHUSDT", "turnover24h": "800"},
        {"symbol": "SOLUSDT", "turnover24h": "10"},
        {"symbol": "XRPUSDT", "turnover24h": "700"},
        {"symbol": "BTCUSDT-27DEC24", "turnover24h": "5000"},  # dated future, excluded
        {"symbol": "BTCUSDC", "turnover24h": "5000"},  # wrong quote
        {"symbol": "ADAUSDT", "turnover24h": "600"},
    ]
    cfg = UniverseConfig(core=["BTCUSDT", "ETHUSDT", "SOLUSDT"], size=5)
    assert select_universe(tickers, cfg) == ["BTCUSDT", "ETHUSDT", "SOLUSDT", "DOGEUSDT", "XRPUSDT"]
