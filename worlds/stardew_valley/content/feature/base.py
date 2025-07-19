from abc import ABC
from collections.abc import Mapping, Callable
from types import MappingProxyType
from typing import ClassVar

from ...data.game_item import Source, Requirement

always_disabled = lambda source_or_requirement: True


class FeatureBase(ABC):
    disabled_sources: ClassVar[Mapping[type[Source], Callable[[Source], bool]]] = MappingProxyType({})
    disabled_requirements: ClassVar[Mapping[type[Requirement], Callable[[Requirement], bool]]] = MappingProxyType({})
