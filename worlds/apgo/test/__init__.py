from typing import ClassVar

from test.bases import WorldTestBase
from .. import APGOWorld, GAME_NAME, APGOOptions


class APGOTestBase(WorldTestBase):
    game = GAME_NAME
    world: APGOWorld
    player: ClassVar[int] = 1

    def world_setup(self, *args, **kwargs):
        super().world_setup(*args, **kwargs)
        if self.constructed:
            self.world = self.multiworld.worlds[self.player]  # noqa

    @property
    def run_default_tests(self) -> bool:
        # world_setup is overridden, so it'd always run default tests when importing DLCQuestTestBase
        is_not_apgo_test = type(self) is not APGOTestBase
        should_run_default_tests = is_not_apgo_test and super().run_default_tests
        return should_run_default_tests


def complete_options_with_default(options_to_complete=None) -> APGOOptions:
    if options_to_complete is None:
        options_to_complete = {}

    for name, option in APGOOptions.type_hints.items():
        options_to_complete[name] = option.from_any(options_to_complete.get(name, option.default))

    return APGOOptions(**options_to_complete)
