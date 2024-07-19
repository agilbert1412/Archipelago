import enum
from dataclasses import dataclass, field
from typing import Set

from BaseClasses import Item, ItemClassification
from .strings.world_strings import GAME_NAME


class Kindergarten2Item(Item):
    game: str = GAME_NAME


offset = 0


class Group(enum.Enum):
    InventoryItem = enum.auto()
    MonstermonCard = enum.auto()
    Outfit = enum.auto()
    Money = enum.auto()
    Trap = enum.auto()
    Deprecated = enum.auto()


@dataclass(frozen=True)
class ItemData:
    code_without_offset: offset
    name: str
    classification: ItemClassification
    groups: Set[Group] = field(default_factory=frozenset)

    def __post_init__(self):
        if not isinstance(self.groups, frozenset):
            super().__setattr__("groups", frozenset(self.groups))

    @property
    def code(self):
        return offset + self.code_without_offset if self.code_without_offset is not None else None

    def has_any_group(self, *group: Group) -> bool:
        groups = set(group)
        return bool(groups.intersection(self.groups))
