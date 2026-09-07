"""Virtual position arithmetic: sizing, margin ratio, liquidation distance, basis PnL.

Perp leg is an isolated-margin short. With leverage ``L`` and maintenance margin
rate ``m``:

    margin           = qty * entry / L
    unrealized       = qty * (entry - mark)
    maintenance      = m * qty * mark
    margin_ratio     = maintenance / (margin + unrealized)      (>= 1 -> liquidated)
    liquidation      = entry * (1 + 1/L) / (1 + m)              (short is liquidated when mark rises here)
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PairSizing:
    notional: float
    spot_qty: float
    perp_qty: float
    perp_margin: float
    open_fees: float


def size_pair(notional: float, spot_price: float, perp_price: float, leverage: float, per_fill_cost: float) -> PairSizing:
    if spot_price <= 0 or perp_price <= 0:
        raise ValueError("prices must be positive")
    return PairSizing(
        notional=notional,
        spot_qty=notional / spot_price,
        perp_qty=notional / perp_price,
        perp_margin=notional / leverage,
        open_fees=2 * per_fill_cost * notional,
    )


def short_liquidation_price(entry: float, leverage: float, mmr: float) -> float:
    return entry * (1 + 1 / leverage) / (1 + mmr)


def short_margin_ratio(perp_qty: float, entry: float, mark: float, margin: float, mmr: float) -> float:
    unrealized = perp_qty * (entry - mark)
    equity = margin + unrealized
    if equity <= 0:
        return float("inf")
    return mmr * perp_qty * mark / equity


def liquidation_distance(liq_price: float, mark: float) -> float:
    """Fractional move in mark price needed to reach liquidation (positive = safe headroom)."""
    return (liq_price - mark) / mark if mark > 0 else float("nan")


def basis_pnl(spot_qty: float, spot_entry: float, spot_now: float, perp_qty: float, perp_entry: float, mark: float) -> float:
    """Mark-to-market of the pair: spot long gains + perp short gains."""
    return spot_qty * (spot_now - spot_entry) + perp_qty * (perp_entry - mark)


def funding_amount(perp_qty: float, mark: float, rate: float) -> float:
    """Funding received by the short (positive rate -> longs pay shorts)."""
    return perp_qty * mark * rate
