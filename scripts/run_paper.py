"""Execute one paper-trading step, write reports/paper_latest.md + PNG, notify Telegram.

Usage: python scripts/run_paper.py [--threshold 0.0001] [--no-notify]
Environment: TELEGRAM_TOKEN, TELEGRAM_CHAT_ID (optional).
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import load_config  # noqa: E402
from src.data.bybit_client import BybitPublicClient  # noqa: E402
from src.notify.telegram import send_telegram  # noqa: E402
from src.paper import db as pdb  # noqa: E402
from src.paper.report import telegram_text, write_paper_report  # noqa: E402
from src.paper.runner import run_step  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--threshold", type=float, help="override per-interval entry/exit threshold")
    ap.add_argument("--no-notify", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    cfg = load_config()
    conn = pdb.connect(cfg.db_path)
    try:
        summary = run_step(BybitPublicClient(), conn, cfg, threshold=args.threshold)
        path = write_paper_report(summary, conn, cfg, cfg.reports_dir)
    finally:
        conn.close()
    logging.info("run #%d equity %.2f open %d skipped %d -> %s", summary.run_id, summary.equity, summary.n_open, len(summary.skipped), path)
    if not args.no_notify:
        send_telegram(telegram_text(summary, cfg))
    # Exit non-zero only when nothing at all could be fetched (all symbols skipped).
    fetched = [s for s in summary.states if s.action != "SKIP"]
    return 0 if fetched else 1


if __name__ == "__main__":
    raise SystemExit(main())
