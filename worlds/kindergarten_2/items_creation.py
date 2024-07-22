from random import Random
from typing import List

from BaseClasses import ItemClassification
from .ItemsClasses import Group, Kindergarten2Item
from .Options import Kindergarten2Options, FillerItems
from .Items import items_by_group
from .constants.money import Money


def create_items(world, world_options: Kindergarten2Options, locations_count: int, random: Random) -> List[Kindergarten2Item]:
    created_items = []
    created_items.extend(world.create_item(item) for item in items_by_group[Group.InventoryItem])
    create_money(created_items, world, world_options)
    create_monstermon_cards(created_items, world, world_options)
    create_outfits(created_items, world, world_options)
    create_fillers(created_items, world, world_options, locations_count, random)
    return created_items


def create_money(created_items, world, world_options: Kindergarten2Options) -> None:
    if world_options.shuffle_money <= 0:
        return
    value = world_options.shuffle_money
    number_of_money_items = Money.minimum_progression_money // value
    progression_money_names = [Money.starting_money] * number_of_money_items
    created_items.extend(world.create_item(item, ItemClassification.progression) for item in progression_money_names)


def create_monstermon_cards(created_items, world, world_options: Kindergarten2Options) -> None:
    if not world_options.shuffle_monstermon:
        return
    created_items.extend(world.create_item(item) for item in items_by_group[Group.MonstermonCard])


def create_outfits(created_items, world, world_options: Kindergarten2Options):
    if not world_options.shuffle_outfits:
        return
    created_items.extend(world.create_item(item) for item in items_by_group[Group.Outfit])


def create_fillers(created_items, world, world_options: Kindergarten2Options, locations_count: int, random: Random) -> None:
    if locations_count <= len(created_items):
        return
    valid_filler = get_valid_filler_items(world_options)
    number_of_filler = locations_count - len(created_items)
    chosen_filler = random.choices(valid_filler, k=number_of_filler)
    created_filler = [world.create_item(item, ItemClassification.progression) for item in chosen_filler]
    created_items.extend(created_filler)


def get_valid_filler_items(world_options: Kindergarten2Options) -> List[str]:
    valid_filler = []
    if world_options.filler_items == FillerItems.option_nothing or \
            world_options.filler_items == FillerItems.option_random_pocket_change or \
            world_options.filler_items == FillerItems.option_random_money:
        valid_filler.append("Nothing")
    if world_options.filler_items == FillerItems.option_pocket_change or \
            world_options.filler_items == FillerItems.option_random_pocket_change:
        valid_filler.append(Money.pocket_change)
    if world_options.filler_items == FillerItems.option_money or \
            world_options.filler_items == FillerItems.option_random_money:
        valid_filler.append(Money.starting_money)
    return valid_filler
