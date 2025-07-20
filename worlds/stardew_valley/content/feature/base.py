import inspect
from abc import ABC, ABCMeta
from collections.abc import Mapping
from dataclasses import dataclass
from types import MappingProxyType
from typing import ClassVar, Self, TYPE_CHECKING, Protocol

from ...data.game_item import Source, Requirement

if TYPE_CHECKING:
    from ... import StardewContent


class DisableSourceHook(Protocol):
    def __call__(self, source: Source, /, *, content: "StardewContent") -> bool:
        """Return True if the source should be disabled by this feature."""
        ...


class DisableRequirementHook(Protocol):
    def __call__(self, requirement: Requirement, /, *, content: "StardewContent") -> bool:
        """Return True if the requirement should be disabled by this feature."""
        ...


def wrap_optional_content_arg(hook):
    """Wraps a hook to ensure it has the correct signature."""
    if "content" in hook.__annotations__:
        return hook

    def wrapper(*args, content: "StardewContent", **kwargs):
        return hook(*args, **kwargs)

    return wrapper


class FeatureMeta(ABCMeta):

    def __new__(mcs: type[Self], name: str, bases: tuple[type, ...], namespace: dict[str, object]) -> type:
        mcs.__handle_disable_hooks(namespace)
        return super().__new__(mcs, name, bases, namespace)

    @staticmethod
    def __handle_disable_hooks(namespace: dict[str, object]):
        disable_source_hooks = {}
        disable_requirement_hooks = {}
        for attribute_name, attribute in namespace.items():
            if not attribute_name.startswith("_disable_") or not callable(attribute):
                continue

            sig = inspect.signature(attribute)

            if (source_param := sig.parameters.get("source")) is not None:
                source_type = source_param.annotation
                disable_source_hooks[source_type] = wrap_optional_content_arg(attribute)
                continue

            if (requirement_param := sig.parameters.get("requirement")) is not None:
                source_type = requirement_param.annotation
                disable_requirement_hooks[source_type] = wrap_optional_content_arg(attribute)
                continue

            raise "Invalid disable hook signature: " + attribute_name + ". Expected a parameter named \"source\" or \"requirement\"."

        namespace["disable_source_hooks"] = MappingProxyType(disable_source_hooks)
        namespace["disable_requirement_hooks"] = MappingProxyType(disable_requirement_hooks)


@dataclass(frozen=True)
class FeatureBase(ABC, metaclass=FeatureMeta):
    disable_source_hooks: "ClassVar[Mapping[type[Source], DisableSourceHook]]"
    """All hooks to call when a source is created to check if it has to be disabled by this feature."""
    disable_requirement_hooks: "ClassVar[Mapping[type[Requirement], DisableRequirementHook]]"
    """All hooks to call when a source is created to check if it has to be disabled by this feature."""
