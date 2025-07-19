from abc import ABC
from dataclasses import dataclass
from typing import ClassVar

from .base import FeatureBase, always_disabled
from ...data.requirement import MuseumCompletionRequirement


@dataclass(frozen=True)
class MuseumsanityFeature(FeatureBase, ABC):
    is_enabled: ClassVar[bool]


class MuseumsanityNone(MuseumsanityFeature):
    is_enabled = False
    disabled_requirements = {MuseumCompletionRequirement: always_disabled}


@dataclass(frozen=True)
class MuseumsanityMilestones(MuseumsanityFeature):
    is_enabled = True


@dataclass(frozen=True)
class MuseumsanityRandomized(MuseumsanityFeature):
    is_enabled = True


@dataclass(frozen=True)
class MuseumsanityAll(MuseumsanityFeature):
    is_enabled = True
