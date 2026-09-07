"""Telegram notification. Silently disabled when TELEGRAM_TOKEN / TELEGRAM_CHAT_ID are unset."""
from __future__ import annotations

import logging
import os

import requests

log = logging.getLogger(__name__)

API = "https://api.telegram.org/bot{token}/sendMessage"


def telegram_enabled() -> bool:
    return bool(os.environ.get("TELEGRAM_TOKEN") and os.environ.get("TELEGRAM_CHAT_ID"))


def send_telegram(text: str, session: requests.Session | None = None, timeout: float = 10.0) -> bool:
    token, chat_id = os.environ.get("TELEGRAM_TOKEN"), os.environ.get("TELEGRAM_CHAT_ID")
    if not token or not chat_id:
        log.info("telegram disabled (no TELEGRAM_TOKEN / TELEGRAM_CHAT_ID)")
        return False
    sess = session or requests.Session()
    try:
        # Telegram caps messages at 4096 chars.
        resp = sess.post(
            API.format(token=token),
            json={"chat_id": chat_id, "text": text[:4000], "parse_mode": "Markdown", "disable_web_page_preview": True},
            timeout=timeout,
        )
        resp.raise_for_status()
        return True
    except requests.RequestException as exc:
        log.error("telegram send failed: %s", exc)
        return False
