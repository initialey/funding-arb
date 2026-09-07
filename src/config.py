"""Typed configuration loaded from config.toml."""
from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


@dataclass(frozen=True)
class UniverseConfig:
    core: list[str] = field(default_factory=lambda: ["BTCUSDT", "ETHUSDT", "SOLUSDT"])
    size: int = 10
    quote: str = "USDT"
    history_days: int = 365


@dataclass(frozen=True)
class CapitalConfig:
    total_usdt: float = 10_000.0
    leverage: float = 1.0


@dataclass(frozen=True)
class CostConfig:
    taker_fee: float = 0.00055
    spread: float = 0.0002

    @property
    def per_fill(self) -> float:
        return self.taker_fee + self.spread

    @property
    def round_trip(self) -> float:
        """Total cost of open+close on both legs, as a fraction of one leg's notional."""
        return 4 * self.per_fill


@dataclass(frozen=True)
class StrategyConfig:
    lookback: int = 3
    thresholds: list[float] = field(default_factory=lambda: [0.00005, 0.0001, 0.0002])
    default_threshold: float = 0.0001


@dataclass(frozen=True)
class WalkForwardConfig:
    train_days: int = 90
    test_days: int = 30
    step_days: int = 30


@dataclass(frozen=True)
class PaperConfig:
    db_path: str = "paper.db"
    maintenance_margin_rate: float = 0.005


@dataclass(frozen=True)
class PathsConfig:
    data_dir: str = "data"
    reports_dir: str = "reports"
    site_dir: str = "docs"


@dataclass(frozen=True)
class Config:
    universe: UniverseConfig = field(default_factory=UniverseConfig)
    capital: CapitalConfig = field(default_factory=CapitalConfig)
    costs: CostConfig = field(default_factory=CostConfig)
    strategy: StrategyConfig = field(default_factory=StrategyConfig)
    walkforward: WalkForwardConfig = field(default_factory=WalkForwardConfig)
    paper: PaperConfig = field(default_factory=PaperConfig)
    paths: PathsConfig = field(default_factory=PathsConfig)

    @property
    def data_dir(self) -> Path:
        return ROOT / self.paths.data_dir

    @property
    def reports_dir(self) -> Path:
        return ROOT / self.paths.reports_dir

    @property
    def site_data_dir(self) -> Path:
        return ROOT / self.paths.site_dir / "data"

    @property
    def db_path(self) -> Path:
        return ROOT / self.paper.db_path

    @property
    def slot_usdt(self) -> float:
        """Capital assigned to one symbol (spot leg + perp margin)."""
        return self.capital.total_usdt / self.universe.size

    @property
    def leg_notional(self) -> float:
        """Notional of each leg; spot and perp are sized equally at 1x."""
        return self.slot_usdt / (1 + 1 / self.capital.leverage)


def load_config(path: Path | None = None) -> Config:
    path = path or ROOT / "config.toml"
    raw = tomllib.loads(path.read_text()) if path.exists() else {}
    return Config(
        universe=UniverseConfig(**raw.get("universe", {})),
        capital=CapitalConfig(**raw.get("capital", {})),
        costs=CostConfig(**raw.get("costs", {})),
        strategy=StrategyConfig(**raw.get("strategy", {})),
        walkforward=WalkForwardConfig(**raw.get("walkforward", {})),
        paper=PaperConfig(**raw.get("paper", {})),
        paths=PathsConfig(**raw.get("paths", {})),
    )
