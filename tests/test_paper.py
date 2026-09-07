"""Paper-trading loop against the fake client: open, accrue, close, skip, risk metrics, report."""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

import pytest

from src.paper import db as pdb
from src.paper.portfolio import (
    basis_pnl,
    liquidation_distance,
    short_liquidation_price,
    short_margin_ratio,
    size_pair,
)
from src.paper.report import telegram_text, write_paper_report
from src.paper.runner import run_step
from tests.conftest import FakeSource

NOW = datetime(2025, 6, 1, 0, 10, tzinfo=timezone.utc)
PRICES = {"BTCUSDT": 100_000.0, "ETHUSDT": 3_000.0, "SOLUSDT": 150.0, "XRPUSDT": 2.0}


def _client(high: set[str], now=NOW, fail=None) -> FakeSource:
    rates = {s: ([0.0003] * 10 if s in high else [0.00001] * 10) for s in PRICES}
    return FakeSource(now, rates, PRICES, fail=fail)


def test_short_risk_math():
    liq = short_liquidation_price(100.0, leverage=1.0, mmr=0.005)
    assert liq == pytest.approx(200 / 1.005)
    assert short_margin_ratio(1.0, 100.0, 100.0, margin=100.0, mmr=0.005) == pytest.approx(0.005)
    assert short_margin_ratio(1.0, 100.0, liq, margin=100.0, mmr=0.005) == pytest.approx(1.0)
    assert liquidation_distance(liq, 100.0) == pytest.approx(liq / 100 - 1)
    s = size_pair(500.0, 100.0, 100.05, 1.0, 0.00075)
    assert s.spot_qty == pytest.approx(5.0) and s.perp_margin == 500.0 and s.open_fees == pytest.approx(0.75)
    assert basis_pnl(1, 100, 110, 1, 100, 110) == pytest.approx(0.0)  # equal move nets to zero


def test_open_accrue_close_cycle(tmp_path, cfg):
    conn = pdb.connect(tmp_path / "p.db")
    client = _client(high={"BTCUSDT", "ETHUSDT"})

    s1 = run_step(client, conn, cfg, now=NOW)
    assert s1.n_open == 2 and {s.symbol for s in s1.states if s.action == "OPEN"} == {"BTCUSDT", "ETHUSDT"}
    pos = pdb.open_positions(conn)["BTCUSDT"]
    assert pos["perp_qty"] * pos["perp_entry"] == pytest.approx(cfg.leg_notional)
    assert pos["fees_paid"] == pytest.approx(2 * cfg.costs.per_fill * cfg.leg_notional)
    btc = next(s for s in s1.states if s.symbol == "BTCUSDT")
    assert btc.liq_distance is not None and 0.9 < btc.liq_distance < 1.0  # ~+99% at 1x
    assert btc.margin_ratio == pytest.approx(cfg.paper.maintenance_margin_rate, rel=1e-3)
    # equity right after opening = capital - open fees (basis MTM zero because prices unchanged)
    assert s1.equity == pytest.approx(cfg.capital.total_usdt - 2 * pos["fees_paid"], rel=1e-6)

    # 8h later, one settlement happened
    client.now = NOW + timedelta(hours=8)
    s2 = run_step(client, conn, cfg, now=client.now)
    assert s2.funding_received == pytest.approx(2 * cfg.leg_notional * 0.0003, rel=1e-3)
    assert conn.execute("SELECT COUNT(*) FROM funding_events").fetchone()[0] == 2

    # re-running the same instant must not double count
    s2b = run_step(client, conn, cfg, now=client.now)
    assert s2b.funding_received == 0.0
    assert conn.execute("SELECT COUNT(*) FROM funding_events").fetchone()[0] == 2

    # rates collapse -> close both
    client.rates = {s: [0.00001] * 10 for s in PRICES}
    client.now = NOW + timedelta(hours=16)
    s3 = run_step(client, conn, cfg, now=client.now)
    assert s3.n_open == 0 and {s.symbol for s in s3.states if s.action == "CLOSE"} == {"BTCUSDT", "ETHUSDT"}
    closes = conn.execute("SELECT realized FROM trades WHERE side='CLOSE'").fetchall()
    assert len(closes) == 2
    expected_per_pair = cfg.leg_notional * (0.0003 + 0.00001) - cfg.costs.round_trip * cfg.leg_notional
    assert sum(r[0] for r in closes) == pytest.approx(2 * expected_per_pair, rel=0.02)
    assert s3.equity == pytest.approx(cfg.capital.total_usdt + s3.realized_total, rel=1e-6)
    assert pdb.last_run(conn)["n_open"] == 0


def test_failed_symbol_is_skipped_and_position_kept(tmp_path, cfg):
    conn = pdb.connect(tmp_path / "p.db")
    client = _client(high={"SOLUSDT"})
    run_step(client, conn, cfg, now=NOW)
    assert "SOLUSDT" in pdb.open_positions(conn)

    client.fail = {"SOLUSDT"}
    client.now = NOW + timedelta(hours=8)
    s = run_step(client, conn, cfg, now=client.now)
    assert "SOLUSDT" in s.skipped
    assert "SOLUSDT" in pdb.open_positions(conn)  # untouched
    assert conn.execute("SELECT COUNT(*) FROM skips").fetchone()[0] == 1
    assert next(x for x in s.states if x.symbol == "SOLUSDT").action == "SKIP"


def test_report_and_telegram_text(tmp_path, cfg):
    conn = pdb.connect(tmp_path / "p.db")
    client = _client(high={"BTCUSDT"})
    s = run_step(client, conn, cfg, now=NOW)
    client.now = NOW + timedelta(hours=8)
    s = run_step(client, conn, cfg, now=client.now)
    path = write_paper_report(s, conn, cfg, tmp_path / "reports")
    md = path.read_text()
    assert "BTCUSDT | yes" in md and "liq. distance" in md
    assert (tmp_path / "reports" / "paper_equity.png").exists()
    txt = telegram_text(s, cfg)
    assert "Equity" in txt and "Tightest liq: BTCUSDT" in txt
