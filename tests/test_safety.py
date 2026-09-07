"""Static guarantee: the codebase contains no order / account / position endpoints and no signed requests."""
from __future__ import annotations

import re
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "src"

FORBIDDEN_PATHS = [
    r"/v5/order",
    r"/v5/position",
    r"/v5/account",
    r"/v5/asset",
    r"/v5/user",
    r"/v5/spot-margin",
    r"/v5/lending",
    r"/private/",
]
FORBIDDEN_TOKENS = [
    r"X-BAPI-SIGN",
    r"X-BAPI-API-KEY",
    r"api_secret",
    r"apiSecret",
    r"place_order",
    r"create_order",
    r"cancel_order",
    r"set_leverage",
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


def test_bybit_requests_are_get_only():
    """Only the Telegram notifier may POST, and never to a Bybit host."""
    for f in _py_files():
        text = f.read_text()
        if "bybit" in f.as_posix() or "bybit" in text.lower():
            assert not re.search(r"\.(post|put|delete|patch)\(", text), f
        for m in re.finditer(r"\.post\(", text):
            assert "telegram" in f.as_posix(), f"unexpected POST in {f}: {text[max(0, m.start() - 80): m.end()]}"
