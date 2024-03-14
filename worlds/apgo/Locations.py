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
