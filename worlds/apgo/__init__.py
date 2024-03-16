from typing import Mapping, Any, Union, Dict, Optional

from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld

from .Regions import create_regions
from .Options import APGOOptions
from .Items import APGOItem, item_table, APGOItemData, create_items
from .Locations import APGOLocation, location_table, create_locations
from .Trips import generate_trips, Trip

GAME_NAME = "Archipela-Go!"


class APGOWebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up an Archipela-Go! game on your device",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kaito Kid"]
    )
    setup_fr = Tutorial(
        "Guide de configuration MultiWorld",
        "Un guide pour configurer Archipela-Go! sur votre appareil.",
        "Français",
        "setup_fr.md",
        "setup/fr",
        ["Kaito Kid"]
    )
    tutorials = [setup_en, setup_fr]


class APGOWorld(World):
    """
    Archipela-Go is an exercise game designed around walking or jogging outside to unlock progression
    """
    game = GAME_NAME
    web = APGOWebWorld()

    item_name_to_id = {name: data.id for name, data in item_table.items()}
    location_name_to_id = {name: id for name, id in location_table.items()}

    options_dataclass = APGOOptions
    options: APGOOptions

    trips: Dict[Trip, int]

    def generate_early(self):
        self.trips = generate_trips(self.options.as_dict(*[option_name for option_name in self.options_dataclass.type_hints]), self.random)

    def create_regions(self) -> None:
        world_regions = create_regions(self.multiworld, self.player, self.options, self.trips)

        def create_location(name: str, code: Optional[int], region: str):
            region = world_regions[region]
            location = APGOLocation(self.player, name, code, region)
            location.access_rule = lambda _: True
            region.locations.append(location)

        create_locations(create_location, self.trips)

    def create_items(self) -> None:
        created_items = create_items(self.create_item, self.trips, self.options, self.random)
        self.multiworld.itempool += created_items

    def create_item(self, item: Union[str, APGOItemData]) -> APGOItem:
        if isinstance(item, str):
            item = item_table[item]

        return APGOItem(item.name, item.classification, item.id, self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            self.options.goal.internal_name: self.options.goal,
            self.options.minimum_distance.internal_name: self.options.minimum_distance,
            self.options.maximum_distance.internal_name: self.options.maximum_distance,
            self.options.speed_requirement.internal_name: self.options.speed_requirement,
            "trips": self.trips,
        }
