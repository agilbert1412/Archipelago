import math

from BaseClasses import ItemClassification
from worlds.generic.Rules import add_rule, item_name_in_locations, set_rule
from . import Options, ItemName


def set_rules(world, player: int, world_options: Options.APGOOptions):
    set_key_rules(world, player, world_options)
    set_distance_rules(world, player, world_options)


def set_key_rules(world, player: int, world_options: Options.APGOOptions):
    if world_options.number_of_locks <= 0:
        return

    for lock in range(1, world_options.number_of_locks+1):
        set_rule(world.get_entrance(f"Area {lock-1} -> Area {lock}", player), lambda state: state.has(ItemName.key, player, lock))


def set_distance_rules(world, player: int, world_options: Options.APGOOptions):
    if not world_options.enable_distance_reductions:
        return

    for trip_name, trip in world.trips.items():
        set_rule(world.get_entrance(f"Area {lock-1} -> Area {lock}", player), lambda state: state.has(ItemName.key, player, lock))
