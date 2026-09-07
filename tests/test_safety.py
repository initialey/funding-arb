"""Static guarantee: no order / account / position endpoints and no signed requests anywhere in src/."""
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"

FORBIDDEN_PATHS = [
    # Bybit private namespaces
    r"/v5/order", r"/v5/position", r"/v5/account", r"/v5/asset", r"/v5/user", r"/v5/spot-margin", r"/v5/lending",
    # Gate private namespaces
    r"/api/v4/futures/usdt/orders", r"/api/v4/futures/usdt/positions", r"/api/v4/futures/usdt/accounts",
    r"/api/v4/spot/orders", r"/api/v4/spot/accounts", r"/api/v4/wallet", r"/api/v4/margin", r"/api/v4/unified",
    r"/private/",
]
FORBIDDEN_TOKENS = [
    r"X-BAPI-SIGN", r"X-BAPI-API-KEY", r"api_secret", r"apiSecret",
    r"['\"]KEY['\"]", r"['\"]SIGN['\"]", r"['\"]Timestamp['\"]",   # Gate auth headers
    r"place_order", r"create_order", r"cancel_order", r"set_leverage", r"hmac",
]


def _py_files():
    return sorted(SRC.rglob("*.py"))


def test_no_forbidden_endpoints_or_secrets():
    offenders = []
    for f in _py_files():
        text = f.read_text()
        for pat in FORBIDDEN_PATHS + FORBIDDEN_TOKENS:
            if re.search(pat, text, flags=re.IGNORECASE):
                offenders.append((f.relative_to(SRC).as_posix(), pat))
    assert not offenders, offenders


def test_exchange_requests_are_get_only():
    """Only the Telegram notifier may POST, and never to an exchange host."""
    for f in _py_files():
        text = f.read_text()
        if any(v in text.lower() for v in ("bybit", "gateio", "gate.io")):
            assert not re.search(r"\.(post|put|delete|patch)\(", text), f
        for m in re.finditer(r"\.post\(", text):
            assert "telegram" in f.as_posix(), f"unexpected POST in {f}: {text[max(0, m.start() - 80): m.end()]}"
