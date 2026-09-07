"""Parquet persistence for funding history and daily klines."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

FUNDING_COLUMNS = ["symbol", "ts", "funding_rate"]
KLINE_COLUMNS = ["symbol", "ts", "open", "high", "low", "close", "volume", "turnover"]


def funding_path(data_dir: Path) -> Path:
    return data_dir / "funding_history.parquet"


def kline_path(data_dir: Path) -> Path:
    return data_dir / "klines_daily.parquet"


def save_parquet(df: pd.DataFrame, path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_parquet(path, index=False)
    return path


def load_parquet(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"{path} not found; run scripts/fetch_data.py first")
    return pd.read_parquet(path)


def merge_funding(existing: pd.DataFrame | None, new: pd.DataFrame) -> pd.DataFrame:
    """Union of old and new rows, de-duplicated on (symbol, ts), sorted."""
    frames = [f for f in (existing, new) if f is not None and not f.empty]
    if not frames:
        return pd.DataFrame(columns=FUNDING_COLUMNS)
    df = pd.concat(frames, ignore_index=True)
    df = df.drop_duplicates(subset=["symbol", "ts"], keep="last")
    return df.sort_values(["symbol", "ts"]).reset_index(drop=True)
