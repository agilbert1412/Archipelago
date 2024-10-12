import math
from typing import Union, Tuple

from . import Trip
from .Options import MinimumDistance, MaximumDistance


def get_reduction_percents(expected_number_of_reductions: int) -> Tuple[float, float]:
    reduction_percent = 1 / (expected_number_of_reductions + 4)
    remainder_percent = 1 - reduction_percent
    return reduction_percent, remainder_percent


def get_distance_per_tier_out_of_logic(maximum_distance: int, remainder_percent: float, expected_number_of_reductions: int, expected_number_of_tiers: int) -> int:
    smallest_distance_multiplier = math.pow(remainder_percent, expected_number_of_reductions)
    distance_range_out_of_logic = maximum_distance / smallest_distance_multiplier
    distance_range_per_tier_out_of_logic = distance_range_out_of_logic / expected_number_of_tiers
    return int(distance_range_per_tier_out_of_logic)


def get_scaling_distance_factors(maximum_distance: int, expected_number_of_reductions: int, expected_number_of_tiers: int) -> Tuple[float, int]:
    reduction_percent, remainder_percent = get_reduction_percents(expected_number_of_reductions)

    if maximum_distance <= 0:
        distance_range_per_tier_out_of_logic = 1
    else:
        distance_range_per_tier_out_of_logic = get_distance_per_tier_out_of_logic(maximum_distance, remainder_percent, expected_number_of_reductions, expected_number_of_tiers)
    return remainder_percent, distance_range_per_tier_out_of_logic


def get_current_distance(trip: Trip, distance_reductions: int,
                         maximum_distance: Union[int, MaximumDistance],
                         expected_number_of_reductions: int,
                         expected_number_of_tiers: int) -> int:
    distance_tier = trip.template.distance_tier
    remainder_percent, distance_range_per_tier_out_of_logic = get_scaling_distance_factors(maximum_distance, expected_number_of_reductions, expected_number_of_tiers)

    distance_multiplier = math.pow(remainder_percent, distance_reductions)

    reduced_range_per_tier = distance_range_per_tier_out_of_logic * distance_multiplier
    extra_distance = distance_tier * reduced_range_per_tier
    final_distance = int(extra_distance)
    return final_distance


def get_reductions_needed_to_be_reachable(trip: Trip,
                                          maximum_distance: Union[int, MaximumDistance],
                                          expected_number_of_reductions: int,
                                          expected_number_of_tiers: int) -> int:
    distance_tier = trip.template.distance_tier
    remainder_percent, distance_range_per_tier_out_of_logic = get_scaling_distance_factors(maximum_distance, expected_number_of_reductions, expected_number_of_tiers)

    # Initial distance without reductions
    initial_distance = int(distance_tier * distance_range_per_tier_out_of_logic)

    if initial_distance <= maximum_distance:
        return 0  # No reductions needed if initial distance is already within max distance.

    # Calculate reductions needed using the formula derived above
    required_ratio = maximum_distance / (distance_tier * distance_range_per_tier_out_of_logic)

    if required_ratio <= 0:
        return expected_number_of_reductions  # All the reductions needed if the ratio is invalid (shouldn't happen in normal cases)

    reductions_needed = math.log(required_ratio) / math.log(remainder_percent)

    return math.ceil(reductions_needed)  # Round up to ensure we meet or exceed the target reduction
