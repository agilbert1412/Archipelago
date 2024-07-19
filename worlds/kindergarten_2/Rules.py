from typing import List

from BaseClasses import ItemClassification, MultiWorld
from worlds.generic.Rules import set_rule
from . import Kindergarten2Item, Kindergarten2Options, Goal
from .strings.inventory_item_names import InventoryItem
from .strings.mission_names import start_mission, Mission


def create_event_item(player, event: str) -> Kindergarten2Item:
    return Kindergarten2Item(event, ItemClassification.progression, None, player)


def set_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    set_mission_rules(multiworld, player, world_options)
    set_monstermon_card_rules(multiworld, player, world_options)
    set_outfit_rules(multiworld, player, world_options)


def set_mission_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    set_rule(multiworld.get_entrance(start_mission(Mission.opposites_attract), player),
             has_items([InventoryItem.bob_toolbelt, InventoryItem.an_a_plus], player))
    set_rule(multiworld.get_entrance(start_mission(Mission.dodge_a_nugget), player),
             has_items([InventoryItem.bob_toolbelt, InventoryItem.prestigious_pin], player))
    set_rule(multiworld.get_entrance(start_mission(Mission.cain_not_able), player),
             has_items([InventoryItem.an_a_plus, InventoryItem.prestigious_pin], player))

    set_rule(multiworld.get_entrance(start_mission(Mission.things_go_boom), player),
             has_items([InventoryItem.laser_beam, InventoryItem.monstermon_plushie], player))
    set_rule(multiworld.get_entrance(start_mission(Mission.breaking_sad), player),
             has_items([InventoryItem.monstermon_plushie, InventoryItem.strange_chemical], player))

    set_rule(multiworld.get_entrance(start_mission(Mission.creature_feature), player),
             has_items([InventoryItem.laser_bomb, InventoryItem.monstermon_plushie, InventoryItem.faculty_remote], player))

    if world_options.goal == Goal.option_all_missions:
        set_rule(multiworld.get_location("Victory", player),
                 has_items([InventoryItem.bob_toolbelt, InventoryItem.an_a_plus, InventoryItem.prestigious_pin,
                            InventoryItem.laser_beam, InventoryItem.monstermon_plushie, InventoryItem.strange_chemical,
                            InventoryItem.laser_bomb, InventoryItem.faculty_remote], player))


def has_items(items: List[str], player):
    return lambda state: all([state.has(item, player) for item in items])


def set_monstermon_card_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    pass


def set_outfit_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    pass


