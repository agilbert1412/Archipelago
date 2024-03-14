from typing import ClassVar

from test.bases import WorldTestBase
from .. import APGOWorld, GAME_NAME


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
