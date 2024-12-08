import logging
from dataclasses import dataclass
from random import Random
from typing import Dict, List, Union, Optional, Iterable, Tuple

from .Options import NumberOfTrips, NumberOfLocks, SpeedRequirement, EnableDistanceReductions

logger = logging.getLogger(__name__)


@dataclass(frozen=True)
class TripTemplate:
    distance_tier: int
    speed_tier: int
    key_needed: int

    def get_name_unique(self, unique_identifier: int) -> str:
        return f"{self.get_description()} #{unique_identifier}"

    def get_max_number_of_this_trip(self) -> int:
        number_of_this_trip = max(1, (11 - self.key_needed) // 2)
        if self.speed_tier == 0:
            number_of_this_trip = min(20, number_of_this_trip * 4)
        return number_of_this_trip

    def get_unique_names(self) -> List[str]:
        number_of_this_trip = self.get_max_number_of_this_trip()
        return [f"{self.get_description()} #{i}" for i in range(1, number_of_this_trip+1)]

    def get_description(self) -> str:
        name = f"Trip Distance {self.distance_tier}"
        if self.key_needed > 0:
            name += f" (Area {self.key_needed})"
        if self.speed_tier > 0:
            name += f" (Speed {self.speed_tier})"
        return name


@dataclass(frozen=True)
class Trip:
    location_name: str
    template: TripTemplate

    def get_number(self) -> int:
        return int(self.location_name.split("#")[-1])

    def as_dict(self) -> Dict[str, int]:
        return {
            "distance_tier": self.template.distance_tier,
            "key_needed": self.template.key_needed,
            "speed_tier": self.template.speed_tier,
        }


all_trip_templates = []

max_per_category = 10
for distance in range(1, max_per_category + 1):
    for speed in range(0, max_per_category + 1):
        for key in range(0, max_per_category + 1):
            all_trip_templates.append(TripTemplate(distance, speed, key))


def generate_trips(options: Dict[str, int], random: Random) -> List[Trip]:
    valid_trip_templates = []
    enable_speed = options[SpeedRequirement.internal_name] > 0
    number_of_keys = options[NumberOfLocks.internal_name]
    for trip in all_trip_templates:
        has_speed = trip.speed_tier > 0
        if enable_speed != has_speed:
            continue
        if trip.key_needed > number_of_keys:
            continue
        valid_trip_templates.append(trip)
    number_of_trips = options[NumberOfTrips.internal_name]
    if number_of_trips <= len(valid_trip_templates):
        chosen_trip_templates = random.sample(valid_trip_templates, k=number_of_trips)
        chosen_trip_amounts = {template: 1 for template in chosen_trip_templates}
    else:
        chosen_trip_templates = valid_trip_templates
        chosen_trip_amounts = {template: 1 for template in chosen_trip_templates}
        trips_to_add = number_of_trips - len(valid_trip_templates)
        while trips_to_add > 0:
            trips_to_increment = random.choices(valid_trip_templates, k=trips_to_add)
            changed = False
            for trip in trips_to_increment:
                if trip.get_max_number_of_this_trip() > chosen_trip_amounts[trip]:
                    chosen_trip_amounts[trip] += 1
                    trips_to_add -= 1
                    changed = True
            if not changed:
                logger.warning(
                    f"Could not generate all the requested trips. Generated as many as possible and breaking early")
                break


    make_sure_all_key_tiers_have_at_least_one_trip(chosen_trip_amounts, number_of_keys)
    make_sure_all_distance_tiers_have_at_least_one_trip(chosen_trip_amounts)

    trips = []
    for trip_template in chosen_trip_amounts:
        for i in range(1, chosen_trip_amounts[trip_template] + 1):
            trips.append(Trip(trip_template.get_name_unique(i), trip_template))
    return trips


def make_sure_all_key_tiers_have_at_least_one_trip(trip_amounts: Dict[TripTemplate, int], number_of_keys: int) -> None:
    if number_of_keys <= 0:
        return
    for missing_key_tier in range(0, number_of_keys + 1):
        if find_trip_with_key_tier(trip_amounts, missing_key_tier):
            continue
        for higher_key_tier in range(number_of_keys, missing_key_tier - 1, -1):
            if missing_key_tier == higher_key_tier:
                return
            trip_to_downgrade = find_trip_with_key_tier(trip_amounts, higher_key_tier)
            if trip_to_downgrade is None:
                continue
            trip_amounts[trip_to_downgrade] -= 1
            trip_amounts[TripTemplate(trip_to_downgrade.distance_tier, trip_to_downgrade.speed_tier, missing_key_tier)] = 1
            break


def find_trip_with_key_tier(trip_amounts: Dict[TripTemplate, int], tier: int) -> Optional[TripTemplate]:
    for trip in trip_amounts:
        if trip.key_needed == tier and trip_amounts[trip] > 0:
            return trip
    return None


def make_sure_all_distance_tiers_have_at_least_one_trip(trip_amounts: Dict[TripTemplate, int]) -> None:
    for missing_distance_tier in range(1, 11):
        if find_trip_with_distance_tier(trip_amounts, missing_distance_tier):
            continue
        for higher_distance_tier in range(10, missing_distance_tier - 1, -1):
            if missing_distance_tier == higher_distance_tier:
                continue
            trip_to_downgrade = find_trip_with_distance_tier(trip_amounts, higher_distance_tier)
            if trip_to_downgrade is None:
                continue
            trip_amounts[trip_to_downgrade] -= 1
            trip_amounts[TripTemplate(missing_distance_tier, trip_to_downgrade.speed_tier, trip_to_downgrade.key_needed)] = 1
            break


def find_trip_with_distance_tier(trip_amounts: Dict[TripTemplate, int], tier: int) -> Optional[TripTemplate]:
    for trip in trip_amounts:
        if trip.distance_tier == tier and trip_amounts[trip] > 0:
            return trip
    return None


def get_max_distance_tier(trips: Iterable[Trip]) -> int:
    return max([trip.template.distance_tier for trip in trips])
