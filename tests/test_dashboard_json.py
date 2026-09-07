"""The JSON payloads consumed by docs/index.html must be valid and carry the keys the page reads."""
from __future__ import annotations

import json
from datetime import datetime, timedelta, timezone

from src.backtest.engine import run_backtest
from src.backtest.metrics import summarise
from src.backtest.report import write_backtest_json
from src.backtest.walkforward import run_walkforward
from src.paper import db as pdb
from src.paper.report import write_paper_json
from src.paper.runner import run_step
from tests.conftest import FakeSource


def test_backtest_json_shape(tmp_path, funding_df, cfg):
    results = {t: run_backtest(funding_df, t, cfg) for t in cfg.strategy.thresholds}
    summaries = [summarise(r, cfg.capital.total_usdt, 4) for r in results.values()]
    wf = run_walkforward(funding_df, cfg)
    path = write_backtest_json(results, summaries, wf, cfg, funding_df, tmp_path / "data" / "backtest.json")
    text = path.read_text()
    assert "NaN" not in text and "Infinity" not in text  # browsers reject non-strict JSON
    b = json.loads(text)
    assert b["exchange"] == cfg.exchange.name
    assert set(b) >= {"generated_at", "data", "config", "best_threshold", "thresholds", "curves", "per_symbol", "walkforward"}
    assert b["best_threshold"] in [t["threshold"] for t in b["thresholds"]]
    assert len(b["curves"]) == len(cfg.strategy.thresholds)
    curve = next(iter(b["curves"].values()))
    assert curve and set(curve[0]) == {"t", "equity", "n_open"}
    assert len(curve) <= 366  # one point per day
    assert len(b["per_symbol"]) == 4 and {"symbol", "net_pnl", "apr_on_slot"} <= set(b["per_symbol"][0])
    assert b["walkforward"]["windows"] and b["walkforward"]["curve"]
    assert {"apr", "max_drawdown", "trades"} <= set(b["walkforward"]["oos"])


def test_paper_json_shape(tmp_path, cfg):
    now = datetime(2025, 6, 1, 0, 10, tzinfo=timezone.utc)
    prices = {"BTCUSDT": 100_000.0, "ETHUSDT": 3_000.0, "SOLUSDT": 150.0}
    client = FakeSource(now, {s: [0.0003] * 10 for s in prices}, prices)
    conn = pdb.connect(tmp_path / "p.db")
    run_step(client, conn, cfg, now=now)
    client.now = now + timedelta(hours=8)
    summary = run_step(client, conn, cfg, now=client.now)
    path = write_paper_json(summary, conn, cfg, tmp_path / "data" / "paper.json")
    p = json.loads(path.read_text())
    assert p["run_id"] == 2 and p["n_open"] == 3
    assert len(p["equity_history"]) == 2 and set(p["equity_history"][0]) == {"t", "equity", "n_open"}
    assert len(p["states"]) == 3 and {"symbol", "held", "signal", "margin_ratio", "liq_distance"} <= set(p["states"][0])
    assert len(p["recent_trades"]) == 3 and p["recent_trades"][0]["side"] == "OPEN"
    assert p["funding_total"] > 0 and p["apr"] is None  # < 1 day of history
