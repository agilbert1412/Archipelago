import math
from typing import Union

from . import Trip
from .Options import MinimumDistance, MaximumDistance


def get_current_distance(trip: Trip, distance_reductions: int,
                         minimum_distance: Union[int, MinimumDistance],
                         maximum_distance: Union[int, MaximumDistance],
                         expected_number_of_reductions: int,
                         expected_number_of_tiers: int) -> int:
    distance_tier = trip.template.distance_tier

    reduction_percent = 1 / (expected_number_of_reductions + 4)
    remainder_percent = 1 - reduction_percent

    distance_range = maximum_distance - minimum_distance
    if distance_range <= 0:
        return minimum_distance
    smallest_distance_multiplier = math.pow(remainder_percent, expected_number_of_reductions)
    distance_range_out_of_logic = distance_range / smallest_distance_multiplier
    distance_range_per_tier_out_of_logic = distance_range_out_of_logic / expected_number_of_tiers

    distance_multiplier = math.pow(remainder_percent, distance_reductions)

    reduced_range_per_tier = distance_range_per_tier_out_of_logic * distance_multiplier
    extra_distance = distance_tier * reduced_range_per_tier
    final_distance = minimum_distance + int(extra_distance)
    return final_distance


def get_reductions_needed_to_be_reachable(trip: Trip,
                                          minimum_distance: Union[int, MinimumDistance],
                                          maximum_distance: Union[int, MaximumDistance],
                                          expected_number_of_reductions: int,
                                          expected_number_of_tiers: int) -> int:
    distance_tier = trip.template.distance_tier

    reduction_percent = 1 / (expected_number_of_reductions + 4)
    remainder_percent = 1 - reduction_percent

    distance_range = maximum_distance - minimum_distance
    if distance_range <= 0:
        return 0
    smallest_distance_multiplier = math.pow(remainder_percent, expected_number_of_reductions)
    distance_range_out_of_logic = distance_range / smallest_distance_multiplier
    distance_range_per_tier_out_of_logic = distance_range_out_of_logic / expected_number_of_tiers

    # Initial distance without reductions
    initial_distance = minimum_distance + int(distance_tier * distance_range_per_tier_out_of_logic)

    if initial_distance <= maximum_distance:
        return 0  # No reductions needed if initial distance is already within max distance.

    # Calculate reductions needed using the formula derived above
    required_ratio = distance_range / (distance_tier * distance_range_per_tier_out_of_logic)

    if required_ratio <= 0:
        return int('inf')  # Infinite reductions needed if the ratio is invalid (shouldn't happen in normal cases)

    reductions_needed = math.log(required_ratio) / math.log(remainder_percent)

    return math.ceil(reductions_needed)  # Round up to ensure we meet or exceed the target reduction

    # distance_range_per_tier_in_logic = distance_range / expected_number_of_tiers
    # required_multiplier = distance_range_per_tier_in_logic / distance_range_per_tier_out_of_logic

    # distance_reductions = math.log(required_multiplier, remainder_percent)
    # return math.ceil(distance_reductions)

    # reduced_range_per_tier = distance_range_per_tier_out_of_logic * distance_multiplier
    # extra_distance = distance_tier * reduced_range_per_tier
    # final_distance = minimum_distance + int(extra_distance)
    # return distance_reductions
