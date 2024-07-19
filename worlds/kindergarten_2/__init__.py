from typing import Union

from BaseClasses import Tutorial, ItemClassification
from worlds.AutoWorld import WebWorld, World
from .Items import ItemData, item_table, items_by_group, Group
from .ItemsCreation import create_items
from .ItemsClasses import Kindergarten2Item
from .Locations import Kindergarten2Location, location_table, create_locations
from .Options import Kindergarten2Options, Goal, ShuffleMoney, ShuffleMonstermon, ShuffleOutfits, ExtraLocations
from .Regions import create_regions
from .Rules import set_rules
from .strings.world_strings import GAME_NAME

client_version = 0


class Kindergarten2WebWorld(WebWorld):
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Kindergarten 2 game on your computer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kaito Kid"]
    )
    tutorials = [setup_en]


class Kindergarten2World(World):
    """
    Kindergarten 2 is a puzzle game where the player repeats the same Tuesday at Kindergarten over and over, discovering items and information to help other characters complete their missions
    """
    game = GAME_NAME
    topology_present = False
    web = Kindergarten2WebWorld()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = location_table

    options_dataclass = Kindergarten2Options
    options: Kindergarten2Options

    def create_regions(self):
        create_regions(self.multiworld, self.player, self.options)
        create_locations(self.multiworld, self.player, self.options)

    def set_rules(self):
        set_rules(self.multiworld, self.player, self.options)

    def create_event(self, event: str):
        return Kindergarten2Item(event, ItemClassification.progression_skip_balancing, None, self.player)

    def create_items(self):
        locations_count = len([location for location in self.multiworld.get_locations(self.player) if not location.advancement])

        items_to_exclude = [excluded_items for excluded_items in self.multiworld.precollected_items[self.player]]

        created_items = create_items(self, self.options, locations_count + len(items_to_exclude), self.multiworld.random)

        self.multiworld.itempool += created_items

        for item in items_to_exclude:
            if item in self.multiworld.itempool:
                self.multiworld.itempool.remove(item)

    def create_item(self, item: Union[str, ItemData], classification: ItemClassification = None) -> Kindergarten2Item:
        if isinstance(item, str):
            item = item_table[item]
        if classification is None:
            classification = item.classification

        return Kindergarten2Item(item.name, classification, item.code, self.player)

    def get_filler_item_name(self) -> str:
        trap = self.multiworld.random.choice(items_by_group[Group.Trap])
        return trap.name

    def fill_slot_data(self):
        options_dict = self.options.as_dict(
            Goal.internal_name,
            ShuffleMoney.internal_name,
            ShuffleMonstermon.internal_name,
            ShuffleOutfits.internal_name,
            ExtraLocations.internal_name,
            "death_link"
        )
        options_dict.update({
            "seed": self.random.randrange(99999999)
        })
        return options_dict
