from typing import Dict, List

from BaseClasses import ItemClassification
from .items_classes import ItemData, Group
from .constants.inventory_item_names import InventoryItem
from .constants.money import Money
from .constants.monstermon_card_names import blue_cards, red_cards, green_cards, yellow_cards, purple_cards
from .constants.outfit_names import Outfit

inventory_items = [
    InventoryItem.bob_toolbelt,
    InventoryItem.an_a_plus,
    InventoryItem.prestigious_pin,
    InventoryItem.strange_chemical,
    InventoryItem.laser_beam,
    InventoryItem.monstermon_plushie,
    InventoryItem.laser_bomb,
    InventoryItem.faculty_remote,
]


def create_inventory_items_data(start_index: int) -> List[ItemData]:
    return [ItemData(start_index + i, inventory_item, progression, {Group.InventoryItem}) for i, inventory_item in enumerate(inventory_items)]


monstermon_items = [
    *blue_cards,
    *red_cards,
    *green_cards,
    *yellow_cards,
    *purple_cards,
]


def create_monstermon_items_data(start_index: int) -> List[ItemData]:
    return [ItemData(start_index + i, monstermon_item, progression, {Group.MonstermonCard}) for i, monstermon_item in enumerate(monstermon_items)]


outfit_items = [
    Outfit.default,
    Outfit.nugget,
    Outfit.cindy,
    Outfit.ted,
    Outfit.carla,
    Outfit.monty,
    Outfit.felix,
    Outfit.ozzy,
    Outfit.penny,
    Outfit.lily,
    Outfit.billy,
    Outfit.jerome,
    Outfit.buggs,
    Outfit.lily_undercover,
    Outfit.billy_undercover,
    Outfit.ms_applegate,
    Outfit.dr_danner,
    Outfit.the_janitor,
    Outfit.bob,
    Outfit.principal,
    Outfit.agnes,
    Outfit.lunch_lady,
    Outfit.hall_monitor,
    Outfit.stevie,
    Outfit.monster,
    Outfit.ron,
    Outfit.madison,
    Outfit.alice,
    Outfit.seasonal,
    Outfit.cultist,
]


def create_outfits_items_data(start_index: int) -> List[ItemData]:
    return [ItemData(start_index + i, outfit_item, ItemClassification.filler, {Group.Outfit}) for i, outfit_item in enumerate(outfit_items)]


progression = ItemClassification.progression

all_items: List[ItemData] = [
    *create_inventory_items_data(1),
    ItemData(201, Money.starting_money, progression, {Group.Money}),
    ItemData(202, Money.pocket_change, progression, {Group.Money}),
    *create_monstermon_items_data(301),
    *create_outfits_items_data(401),
    ItemData(501, "Nothing", ItemClassification.filler, {}),
    ItemData(502, "Janitor Trap", ItemClassification.trap, {Group.Trap}),
]


item_table: Dict[str, ItemData] = {}
items_by_group: Dict[Group, List[ItemData]] = {}


def initialize_item_table():
    item_table.update({item.name: item for item in all_items})


def initialize_groups():
    for item in all_items:
        for group in item.groups:
            item_group = items_by_group.get(group, list())
            item_group.append(item)
            items_by_group[group] = item_group


initialize_item_table()
initialize_groups()
