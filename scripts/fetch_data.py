"""Fetch one year of funding history + daily klines for the universe into data/*.parquet.

Usage: python scripts/fetch_data.py [--days 365] [--symbols BTCUSDT,ETHUSDT]
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.config import load_config  # noqa: E402
from src.data import make_source  # noqa: E402
from src.data.fetch import fetch_all, update_parquet  # noqa: E402
from src.data.universe import fetch_universe  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--symbols", help="comma-separated override of the universe")
    ap.add_argument("--verbose", action="store_true")
    args = ap.parse_args()
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    cfg = load_config()
    source = make_source(cfg)
    logging.info("exchange: %s (history up to %d days)", source.name, source.max_history_days)
    if args.symbols:
        symbols = [s.strip().upper() for s in args.symbols.split(",") if s.strip()]
    else:
        try:
            symbols = fetch_universe(source, cfg.universe)
        except Exception as exc:
            logging.error("could not fetch tickers for universe selection: %s", exc)
            return 2
    logging.info("universe: %s", symbols)

    result = fetch_all(source, symbols, cfg)
    update_parquet(result, cfg)
    cfg.data_dir.mkdir(parents=True, exist_ok=True)
    (cfg.data_dir / "universe.json").write_text(
        json.dumps({"exchange": source.name, "symbols": symbols, "skipped": result.skipped}, indent=2)
    )
    logging.info("saved %d funding rows, %d kline rows; skipped=%s", len(result.funding), len(result.klines), result.skipped)
    return 0 if len(result.funding) else 1


if __name__ == "__main__":
    raise SystemExit(main())
