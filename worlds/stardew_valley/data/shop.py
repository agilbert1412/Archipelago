from dataclasses import dataclass
from typing import Tuple, Optional

from .game_item import Source, kw_only, Requirement
from ..strings.season_names import Season

ItemPrice = Tuple[int, str]


@dataclass(frozen=True, **kw_only)
class ShopSource(Source):
    shop_region: str
    money_price: Optional[int] = None
    items_price: Optional[Tuple[ItemPrice, ...]] = None
    seasons: Tuple[str, ...] = Season.all
    other_requirements: Tuple[Requirement, ...] = ()

    def __post_init__(self):
        assert self.money_price is not None or self.items_price is not None, "At least money price or items price need to be defined."
        assert self.items_price is None or all(isinstance(p, tuple) for p in self.items_price), "Items price should be a tuple."


@dataclass(frozen=True, **kw_only)
class MysteryBoxSource(Source):
    amount: int


@dataclass(frozen=True, **kw_only)
class ArtifactTroveSource(Source):
    amount: int


@dataclass(frozen=True, **kw_only)
class PrizeMachineSource(Source):
    amount: int


@dataclass(frozen=True, **kw_only)
class FishingTreasureChestSource(Source):
    amount: int
