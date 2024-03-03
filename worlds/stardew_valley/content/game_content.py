from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, Iterable, Set, Any

from .feature.friendsanity import FriendsanityFeature
from ..data.villagers_data import Villager


@dataclass(frozen=True)
class StardewContent:
    features: StardewFeatures

    registered_packs: Set[str] = field(default_factory=set)

    # items -> To use with has rule
    # regions -> To be used with can reach rule

    villagers: Dict[str, Villager] = field(default_factory=dict)
    skills: Dict[str, Any] = field(default_factory=dict)
    quests: Dict[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class StardewFeatures:
    friendsanity: FriendsanityFeature


@dataclass(frozen=True)
class ContentPack:
    name: str

    dependencies: Iterable[str] = ()
    """ Hard requirement, generation will fail if it's missing. """
    weak_dependencies: Iterable[str] = ()
    """ Not a strict dependency, only used only for ordering the packs to make sure patches are applied correctly. """

    # items
    # def item_hook
    # ...

    villagers: Iterable[Villager] = ()

    def villager_hook(self, content: StardewContent):
        ...

    skills: Iterable[Any] = ()

    def skill_hook(self, content: StardewContent):
        ...

    quests: Iterable[Any] = ()

    def quest_hook(self, content: StardewContent):
        ...