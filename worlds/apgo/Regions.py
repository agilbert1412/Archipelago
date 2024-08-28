from typing import Dict, List

from BaseClasses import MultiWorld, Region
from .Trips import Trip
from .Options import APGOOptions


def create_regions(multiworld: MultiWorld, player: int, options: APGOOptions, trips: Dict[str, Trip]) -> Dict[str, Region]:
    created_regions = dict()
    created_regions["Menu"] = Region("Menu", player, multiworld)
    created_regions[area_number(0)] = Region(area_number(0), player, multiworld)
    created_regions["Menu"].connect(created_regions[area_number(0)])

    max_key = 0
    for trip in trips.values():
        if trip.template.key_needed > max_key:
            max_key = trip.template.key_needed

    for i in range(1, max_key + 1):
        name = area_number(i)
        created_regions[name] = Region(name, player, multiworld)
        previous_name = area_number(i-1)
        created_regions[previous_name].connect(created_regions[name])

    for region in created_regions:
        multiworld.regions.append(created_regions[region])
    return created_regions


def area_number(key_number: int) -> str:
    return f"Area {key_number}"

