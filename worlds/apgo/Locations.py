from typing import Optional, Protocol, Dict

from BaseClasses import Location
from .Trips import Trip, all_trips


class APGOLocation(Location):
    game = "Archipela-Go!"


# [Centimeters in a marathon] * [Centimeters in a half-marathon]
offset = 8902301100000

location_table = {
    "Goal": offset,
}

i = 1
for trip in all_trips:
    for unique_identifier in range(1, 10):
        location_table[trip.get_name_unique(unique_identifier)] = offset + i
        i += 1


class APGOLocationFactory(Protocol):
    def __call__(self, name: str, code: Optional[int], region: str) -> None:
        raise NotImplementedError


def create_locations(location_factory: APGOLocationFactory, trips: Dict[Trip, int]) -> None:
    for trip_type in trips:
        for identifier in range(1, trips[trip_type]+1):
            trip_name = trip_type.get_name_unique(identifier)
            trip_id= location_table[trip_name]
            location_factory(trip_name, trip_id, "Menu")