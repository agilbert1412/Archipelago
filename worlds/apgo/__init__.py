import json
from typing import Mapping, Any, Union, Dict, Optional, List

from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld
from .ItemNames import ItemName, long_macguffins, short_macguffins

from .Regions import create_regions, area_number
from .Options import APGOOptions, Goal
from .Items import APGOItem, item_table, APGOItemData, create_items
from .Locations import APGOLocation, location_table, create_locations
from .Trips import generate_trips, Trip
from .rules import set_rules
from ..generic.Rules import set_rule

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

    data_version = 0

    options_dataclass = APGOOptions
    options: APGOOptions

    trips: Dict[str, Trip]
    number_distance_reductions: int
    number_keys: int

    def generate_early(self):
        generated_trips = generate_trips(self.options.as_dict(*[option_name for option_name in self.options_dataclass.type_hints]), self.random)
        self.trips = {trip.location_name: trip for trip in generated_trips}
        self.number_distance_reductions = 0
        self.number_keys = 0
        for trip in self.trips.values():
            if trip.template.key_needed > self.number_keys:
                self.number_keys = trip.template.key_needed

    def create_regions(self) -> None:
        world_regions = create_regions(self)

        def create_location(name: str, code: Optional[int], region: str):
            region = world_regions[region]
            location = APGOLocation(self.player, name, code, region)
            location.access_rule = lambda _: True
            region.locations.append(location)

        create_locations(create_location, self.trips)

    def create_items(self) -> None:
        created_items = create_items(self.create_item, self.trips, self.options, self.random)
        self.multiworld.itempool += created_items

        # This is a weird way to count but it works...
        self.number_distance_reductions += sum(item.name == ItemName.distance_reduction for item in created_items)
        self.setup_victory()

    def set_rules(self) -> None:
        set_rules(self, self.player, self.options)

    def create_item(self, item: Union[str, APGOItemData]) -> APGOItem:
        if isinstance(item, str):
            item = item_table[item]

        return APGOItem(item.name, item.classification, item.id, self.player)

    def setup_victory(self):
        last_region = self.multiworld.get_region(area_number(self.number_keys), self.player)
        victory_location = APGOLocation(self.player, "Goal", None, last_region)
        last_region.locations.append(victory_location)
        if self.options.goal == Goal.option_one_hard_travel or self.options.goal == Goal.option_allsanity:
            set_rule(victory_location, lambda state: state.has(ItemName.distance_reduction, self.player, self.number_distance_reductions))
        elif self.options.goal == Goal.option_long_macguffin:
            set_rule(victory_location, lambda state: all([state.has(macguffin, self.player) for macguffin in long_macguffins]))
        elif self.options.goal == Goal.option_short_macguffin:
            set_rule(victory_location, lambda state: all([state.has(macguffin, self.player) for macguffin in short_macguffins]))

        victory_location.place_locked_item(APGOItem("Victory", ItemClassification.progression, None, self.player))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def fill_slot_data(self) -> Mapping[str, Any]:
        trips_dictionary = {location_name: trip.as_dict() for location_name, trip in self.trips.items()}
        slot_data = {
            self.options.goal.internal_name: self.options.goal.value,
            self.options.minimum_distance.internal_name: self.options.minimum_distance.value,
            self.options.maximum_distance.internal_name: self.options.maximum_distance.value,
            self.options.speed_requirement.internal_name: self.options.speed_requirement.value,
            "trips": trips_dictionary,
        }
        return slot_data
