from dataclasses import dataclass
from random import Random
from typing import Dict, List, Union, Optional, Iterable, Tuple

from .Options import NumberOfTrips, NumberOfLocks, SpeedRequirement


@dataclass(frozen=True)
class TripTemplate:
    distance_tier: int
    speed_tier: int
    key_needed: int

    def get_name_unique(self, unique_identifier: int) -> str:
        return f"{self.get_description()} #{unique_identifier}"

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
    chosen_trip_templates = random.choices(valid_trip_templates, k=options[NumberOfTrips.internal_name])

    make_sure_all_key_tiers_have_at_least_one_trip(chosen_trip_templates, number_of_keys)

    trip_counts = dict()
    for trip_template in chosen_trip_templates:
        if trip_template not in trip_counts:
            trip_counts[trip_template] = 0
        trip_counts[trip_template] += 1
    trips = []
    for trip_template in trip_counts:
        for i in range(1, trip_counts[trip_template] + 1):
            trips.append(Trip(trip_template.get_name_unique(i), trip_template))
    return trips


def make_sure_all_key_tiers_have_at_least_one_trip(chosen_trip_templates: List[TripTemplate], number_of_keys: int) -> None:
    if number_of_keys <= 0:
        return
    for missing_key_tier in range(0, number_of_keys + 1):
        if find_trip_with_key_tier(chosen_trip_templates, missing_key_tier):
            continue
        for higher_key_tier in range(number_of_keys, missing_key_tier - 1, -1):
            if missing_key_tier == higher_key_tier:
                return
            trip_to_downgrade = find_trip_with_key_tier(chosen_trip_templates, higher_key_tier)
            if trip_to_downgrade is None:
                continue
            chosen_trip_templates.remove(trip_to_downgrade)
            chosen_trip_templates.append(TripTemplate(trip_to_downgrade.distance_tier, trip_to_downgrade.speed_tier, missing_key_tier))
            break


def find_trip_with_key_tier(trips: List[TripTemplate], tier: int) -> Optional[TripTemplate]:
    for trip in trips:
        if trip.key_needed == tier:
            return trip

    return None


def get_max_distance_tier(trips: Iterable[Trip]) -> int:
    return max([trip.template.distance_tier for trip in trips])
