from typing import Dict, List

from BaseClasses import MultiWorld, Region
from .Trips import Trip
from .Options import APGOOptions


def create_regions(world) -> Dict[str, Region]:
    created_regions = dict()
    created_regions["Menu"] = Region("Menu", world.player, world.multiworld)
    created_regions[area_number(0)] = Region(area_number(0), world.player, world.multiworld)
    created_regions["Menu"].connect(created_regions[area_number(0)])

    for i in range(1, world.number_keys + 1):
        name = area_number(i)
        created_regions[name] = Region(name, world.player, world.multiworld)
        previous_name = area_number(i-1)
        created_regions[previous_name].connect(created_regions[name])

    for region in created_regions:
        world.multiworld.regions.append(created_regions[region])
    return created_regions


def area_number(key_number: int) -> str:
    return f"Area {key_number}"

