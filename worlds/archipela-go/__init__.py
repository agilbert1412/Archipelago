from BaseClasses import Region, Location, Item, ItemClassification, Tutorial
from worlds.AutoWorld import World, WebWorld

from .regions import create_regions
from .options import APGOOptions
from .items import APGOItem


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
    game = "Archipela-Go!"
    web = APGOWebWorld()
    location_id_to_name = {}
    item_id_to_name = {}

    options_dataclass = APGOOptions
    options: APGOOptions

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.options)

    def create_items(self) -> None:
        pass

    def create_item(self, name: str) -> "Item":
        item_class = self.get_item_classification(name)
        return APGOItem(name, item_class, self.item_id_to_name.get(name, None), self.player)

    def get_item_classification(self, name: str) -> ItemClassification:
        return ItemClassification.progression
