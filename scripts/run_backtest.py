"""Run the threshold comparison + walk-forward on data/funding_history.parquet and write reports/.

Usage: python scripts/run_backtest.py [--thresholds 0.00005,0.0001,0.0002] [--no-walkforward]
"""
from __future__ import annotations

import argparse
import json
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.backtest.engine import run_backtest  # noqa: E402
from src.backtest.metrics import summarise  # noqa: E402
from src.backtest.report import write_backtest_json, write_backtest_report  # noqa: E402
from src.backtest.walkforward import run_walkforward  # noqa: E402
from src.config import load_config  # noqa: E402
from src.data.storage import funding_path, load_parquet  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--thresholds", help="comma-separated per-interval thresholds, e.g. 0.00005,0.0001,0.0002")
    ap.add_argument("--no-walkforward", action="store_true")
    ap.add_argument("--data", help="override parquet path")
    args = ap.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

    cfg = load_config()
    thresholds = [float(x) for x in args.thresholds.split(",")] if args.thresholds else cfg.strategy.thresholds
    funding = load_parquet(Path(args.data) if args.data else funding_path(cfg.data_dir))
    funding = funding.dropna(subset=["funding_rate"]).sort_values(["symbol", "ts"]).reset_index(drop=True)
    n_sym = funding["symbol"].nunique()
    logging.info("loaded %d events for %d symbols", len(funding), n_sym)

    results = {thr: run_backtest(funding, thr, cfg) for thr in thresholds}
    summaries = [summarise(r, cfg.capital.total_usdt, n_sym) for r in results.values()]
    for s in summaries:
        logging.info("threshold %.4f%%: APR %.2f%% maxDD %.2f%% exposure %.1f%% trades %d",
                     s.threshold * 100, s.apr * 100, s.max_drawdown * 100, s.exposure_days_ratio * 100, s.trades)

    wf = None if args.no_walkforward else run_walkforward(funding, cfg, thresholds)
    if wf is not None:
        logging.info("walk-forward OOS APR %.2f%% over %d windows", wf.oos_summary.apr * 100, len(wf.windows))

    path = write_backtest_report(results, summaries, wf, cfg, funding, cfg.reports_dir)
    write_backtest_json(results, summaries, wf, cfg, funding, cfg.site_data_dir / "backtest.json")
    (cfg.reports_dir / "backtest_summary.json").write_text(
        json.dumps(
            {
                "thresholds": [s.as_dict() for s in summaries],
                "walkforward_oos": wf.oos_summary.as_dict() if wf else None,
            },
            indent=2,
            default=str,
        )
    )
    logging.info("report written to %s", path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
