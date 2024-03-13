from BaseClasses import MultiWorld, Region
from .options import APGOOptions


def create_regions(multiworld: MultiWorld, player: int, options: APGOOptions) -> None:
    multiworld.regions.append(Region("Menu", player, multiworld))

