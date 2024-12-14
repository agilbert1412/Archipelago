import functools
import typing

RetType = typing.TypeVar("RetType")
S = typing.TypeVar("S")
T = typing.TypeVar("T")


# TODO delete once https://github.com/ArchipelagoMW/Archipelago/pull/4667 is merged
def cache_self1(function: typing.Callable[[S, T], RetType]) -> typing.Callable[[S, T], RetType]:
    """Specialized cache for self + 1 arg. Does not keep global ref to self and skips building a dict key tuple."""

    assert function.__code__.co_argcount == 2, "Can only cache 2 argument functions with this cache."

    cache_name = f"__cache_{function.__name__}__"

    @functools.wraps(function)
    def wrap(self: S, arg: T) -> RetType:
        cache: dict[T, RetType] | None = getattr(self, cache_name, None)
        if cache is None:
            res = function(self, arg)
            setattr(self, cache_name, {arg: res})
            return res
        try:
            return cache[arg]
        except KeyError:
            res = function(self, arg)
            cache[arg] = res
            return res

    wrap.__defaults__ = function.__defaults__

    return wrap
