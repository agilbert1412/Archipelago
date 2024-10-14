from dataclasses import dataclass

from .game_item import kw_only, Source


@dataclass(frozen=True, **kw_only)
class MachineSource(Source):
    item: str  # this should be optional (worm bin)
    machine: str
    # seasons
