"""SQLite persistence for the paper-trading loop."""
from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from typing import Iterator

SCHEMA = """
CREATE TABLE IF NOT EXISTS runs (
    run_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    ts          TEXT NOT NULL,
    equity      REAL NOT NULL,
    cash        REAL NOT NULL,
    n_open      INTEGER NOT NULL,
    note        TEXT
);
CREATE TABLE IF NOT EXISTS positions (
    symbol          TEXT PRIMARY KEY,
    opened_ts       TEXT NOT NULL,
    spot_qty        REAL NOT NULL,
    spot_entry      REAL NOT NULL,
    perp_qty        REAL NOT NULL,
    perp_entry      REAL NOT NULL,
    perp_margin     REAL NOT NULL,
    leverage        REAL NOT NULL,
    last_funding_ts TEXT NOT NULL,
    funding_accrued REAL NOT NULL DEFAULT 0,
    fees_paid       REAL NOT NULL DEFAULT 0
);
CREATE TABLE IF NOT EXISTS trades (
    trade_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    run_id      INTEGER NOT NULL,
    ts          TEXT NOT NULL,
    symbol      TEXT NOT NULL,
    side        TEXT NOT NULL,          -- OPEN / CLOSE
    spot_price  REAL NOT NULL,
    perp_price  REAL NOT NULL,
    notional    REAL NOT NULL,
    fees        REAL NOT NULL,
    realized    REAL,                   -- CLOSE only: funding - fees + basis pnl
    signal      REAL
);
CREATE TABLE IF NOT EXISTS funding_events (
    symbol       TEXT NOT NULL,
    ts           TEXT NOT NULL,
    funding_rate REAL NOT NULL,
    notional     REAL NOT NULL,
    amount       REAL NOT NULL,
    run_id       INTEGER NOT NULL,
    PRIMARY KEY (symbol, ts)
);
CREATE TABLE IF NOT EXISTS snapshots (
    run_id          INTEGER NOT NULL,
    symbol          TEXT NOT NULL,
    mark_price      REAL,
    spot_price      REAL,
    signal          REAL,
    held            INTEGER NOT NULL,
    unrealized      REAL,
    margin_ratio    REAL,
    liq_price       REAL,
    liq_distance    REAL,
    PRIMARY KEY (run_id, symbol)
);
CREATE TABLE IF NOT EXISTS skips (
    run_id  INTEGER NOT NULL,
    ts      TEXT NOT NULL,
    symbol  TEXT,
    reason  TEXT NOT NULL
);
"""


def connect(path: Path) -> sqlite3.Connection:
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.executescript(SCHEMA)
    return conn


@contextmanager
def transaction(conn: sqlite3.Connection) -> Iterator[sqlite3.Connection]:
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise


def last_run(conn: sqlite3.Connection) -> sqlite3.Row | None:
    return conn.execute("SELECT * FROM runs ORDER BY run_id DESC LIMIT 1").fetchone()


def open_positions(conn: sqlite3.Connection) -> dict[str, sqlite3.Row]:
    return {r["symbol"]: r for r in conn.execute("SELECT * FROM positions")}


def realized_total(conn: sqlite3.Connection) -> float:
    row = conn.execute("SELECT COALESCE(SUM(realized), 0) FROM trades WHERE side='CLOSE'").fetchone()
    return float(row[0])


def equity_history(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute("SELECT run_id, ts, equity, n_open FROM runs ORDER BY run_id").fetchall()
