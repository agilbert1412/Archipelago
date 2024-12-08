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
    for unique_name in trip_template.get_unique_names():
        location_table[unique_name] = offset + i
        i += 1

a = 5


class APGOLocationFactory(Protocol):
    def __call__(self, name: str, code: Optional[int], region: str) -> None:
        raise NotImplementedError


def create_locations(location_factory: APGOLocationFactory, trips: Dict[str, Trip]) -> None:
    for location_name, trip in trips.items():
        trip_id = location_table[location_name]
        trip_region = area_number(trip.template.key_needed)
        location_factory(location_name, trip_id, trip_region)
