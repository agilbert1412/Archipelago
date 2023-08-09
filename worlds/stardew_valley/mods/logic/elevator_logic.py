from typing import Iterable

from ...logic.received_logic import ReceivedLogic
from ...stardew_rule import StardewRule, True_
from ...mods.mod_data import ModNames
from ... import options


class ModElevatorLogic:
    player: int
    elevator_option: int
    mods: Iterable[str]
    received: ReceivedLogic

    def __init__(self, player: int, elevator_option: int, mods: Iterable[str], received: ReceivedLogic):
        self.player = player
        self.elevator_option = elevator_option
        self.mods = mods
        self.received = received

    def has_skull_cavern_elevator_to_floor(self, floor: int) -> StardewRule:
        if self.elevator_option != options.ElevatorProgression.option_vanilla and ModNames.skull_cavern_elevator in self.mods:
            return self.received("Progressive Skull Cavern Elevator", floor // 25)
        return True_()