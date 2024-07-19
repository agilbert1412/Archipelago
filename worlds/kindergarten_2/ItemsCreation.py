from random import Random

from .ItemsClasses import Group
from .Options import Kindergarten2Options
from .Items import items_by_group
from .constants.money import Money


def create_items(world, world_options: Kindergarten2Options, locations_count: int, random: Random):
    created_items = []
    created_items.extend(world.create_item(item) for item in items_by_group[Group.InventoryItem])
    if world_options.shuffle_money:
        created_items.extend(world.create_item(item) for item in [Money.starting_money] * Money.number_of_shuffled_money_items)
    if world_options.shuffle_monstermon:
        created_items.extend(world.create_item(item) for item in items_by_group[Group.MonstermonCard])
    # if world_options.shuffle_outfits:
    #     created_items.extend(world.create_item(item) for item in items_by_group[Group.Outfit])
    if locations_count > len(created_items):
        created_items.extend(world.create_item(item) for item in [Money.starting_money] * (locations_count - len(created_items)))
    return created_items
