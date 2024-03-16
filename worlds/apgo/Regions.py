from typing import Dict

from BaseClasses import MultiWorld, Region
from .Options import APGOOptions


def create_regions(multiworld: MultiWorld, player: int, options: APGOOptions) -> Dict[str, Region]:
    menu = Region("Menu", player, multiworld)
    multiworld.regions.append(menu)

    return {region.name: region for region in [menu]}

