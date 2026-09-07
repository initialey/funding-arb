"""Performance metrics: annualised return, max drawdown, exposure ratio."""
from __future__ import annotations

from dataclasses import asdict, dataclass

import numpy as np
import pandas as pd

from src.backtest.engine import BacktestResult


@dataclass
class Summary:
    threshold: float
    days: float
    net_pnl: float
    funding_pnl: float
    costs: float
    apr: float           # net_pnl / capital * 365 / days
    max_drawdown: float  # fraction of capital, negative number
    exposure_days_ratio: float  # days with >=1 open position / total days
    avg_slot_utilisation: float  # mean fraction of symbols in position per event
    trades: int

    def as_dict(self) -> dict:
        return asdict(self)


def span_days(ts: pd.Series) -> float:
    if len(ts) < 2:
        return 0.0
    return float((ts.max() - ts.min()).total_seconds() / 86_400)


def max_drawdown(equity: pd.Series, capital: float) -> float:
    if equity.empty:
        return 0.0
    peak = equity.cummax()
    dd = (equity - peak) / capital
    return float(dd.min())


def exposure_days_ratio(equity: pd.DataFrame) -> float:
    if equity.empty:
        return 0.0
    days = equity.assign(day=equity["ts"].dt.floor("D")).groupby("day")["n_open"].max()
    return float((days > 0).mean())


def summarise(result: BacktestResult, capital: float, n_symbols: int) -> Summary:
    eq = result.equity
    days = span_days(eq["ts"]) if not eq.empty else 0.0
    tot = result.totals()
    apr = (tot["net_pnl"] / capital) * (365.0 / days) if days > 0 else 0.0
    util = float((eq["n_open"] / n_symbols).mean()) if not eq.empty and n_symbols else 0.0
    return Summary(
        threshold=result.threshold,
        days=days,
        net_pnl=tot["net_pnl"],
        funding_pnl=tot["funding_pnl"],
        costs=tot["costs"],
        apr=apr,
        max_drawdown=max_drawdown(eq["equity"], capital),
        exposure_days_ratio=exposure_days_ratio(eq),
        avg_slot_utilisation=util,
        trades=int(tot["trades"]),
    )


def per_symbol_table(result: BacktestResult, capital_per_symbol: float) -> pd.DataFrame:
    rows = []
    for sym, r in result.per_symbol.items():
        days = span_days(r.events["ts"])
        held_ratio = float(r.events["held"].mean()) if len(r.events) else 0.0
        apr = (r.net_pnl / capital_per_symbol) * (365.0 / days) if days > 0 and capital_per_symbol else np.nan
        rows.append(
            {
                "symbol": sym,
                "events": len(r.events),
                "trades": r.trades,
                "held_ratio": held_ratio,
                "funding_pnl": r.funding_pnl,
                "costs": r.costs,
                "net_pnl": r.net_pnl,
                "apr_on_slot": apr,
                "mean_rate": float(r.events["funding_rate"].mean()) if len(r.events) else np.nan,
            }
        )
    return pd.DataFrame(rows).sort_values("net_pnl", ascending=False).reset_index(drop=True)
