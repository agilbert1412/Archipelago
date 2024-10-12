import math

from BaseClasses import ItemClassification
from worlds.generic.Rules import add_rule, item_name_in_locations, set_rule
from . import Options, ItemName
from .Trips import get_max_distance_tier
from .distance import get_reductions_needed_to_be_reachable


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

    num_distance_reductions = world.number_distance_reductions
    max_distance_tier = get_max_distance_tier(world.trips.values())

    for trip_name, trip in world.trips.items():
        if trip.template.distance_tier <= 1:
            continue
        location = world.get_location(trip_name, player)
        distance_reductions_needed = get_reductions_needed_to_be_reachable(trip, world_options.maximum_distance, num_distance_reductions, max_distance_tier)
        set_rule(location, lambda state: state.has(ItemName.distance_reduction, player, distance_reductions_needed))
