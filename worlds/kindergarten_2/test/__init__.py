from typing import ClassVar

from typing import Dict, FrozenSet, Tuple, Any
from argparse import Namespace

from BaseClasses import MultiWorld
from test.bases import WorldTestBase
from .. import GAME_NAME, Kindergarten2World
from test.general import gen_steps, setup_solo_multiworld as setup_base_solo_multiworld
from worlds.AutoWorld import call_all


class Kindergarten2TestBase(WorldTestBase):
    game = GAME_NAME
    world: Kindergarten2World
    player: ClassVar[int] = 1

    def world_setup(self, *args, **kwargs):
        super().world_setup(*args, **kwargs)
        if self.constructed:
            self.world = self.multiworld.worlds[self.player]  # noqa


def setup_kindergarten_solo_multiworld(test_options=None, seed=None, _cache: Dict[FrozenSet[Tuple[str, Any]], MultiWorld] = {}) -> MultiWorld: #noqa
    if test_options is None:
        test_options = {}

    # Yes I reuse the worlds generated between tests, its speeds the execution by a couple seconds
    frozen_options = frozenset(test_options.items()).union({seed})
    if frozen_options in _cache:
        return _cache[frozen_options]

    multiworld = setup_base_solo_multiworld(Kindergarten2World, (), seed=seed)
    # print(f"Seed: {multiworld.seed}") # Uncomment to print the seed for every test
    args = Namespace()
    for name, option in Kindergarten2World.options_dataclass.type_hints.items():
        value = option(test_options[name]) if name in test_options else option.from_any(option.default)
        setattr(args, name, {1: value})
    multiworld.set_options(args)
    for step in gen_steps:
        call_all(multiworld, step)

    _cache[frozen_options] = multiworld

    return multiworld
