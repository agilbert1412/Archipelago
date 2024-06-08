from typing import Optional, Protocol, Dict, List

from BaseClasses import Location
from .Regions import area_number
from .Trips import Trip, all_trip_templates


class APGOLocation(Location):
    game = "Archipela-Go!"


# [Centimeters in a marathon] * [Centimeters in a half-marathon]
offset = 8902301100000

location_table = {
    "Goal": offset,
}

i = 1
for trip_template in all_trip_templates:
    for unique_identifier in range(1, 10):
        location_table[trip_template.get_name_unique(unique_identifier)] = offset + i
        i += 1


class APGOLocationFactory(Protocol):
    def __call__(self, name: str, code: Optional[int], region: str) -> None:
        raise NotImplementedError


def create_locations(location_factory: APGOLocationFactory, trips: List[Trip]) -> None:
    for trip in trips:
        trip_name = trip.location_name
        trip_id = location_table[trip_name]
        trip_region = area_number(trip.template.key_needed)
        location_factory(trip_name, trip_id, trip_region)
