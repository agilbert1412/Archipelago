import math
from typing import List, Callable, Any

from BaseClasses import ItemClassification, MultiWorld
from worlds.generic.Rules import set_rule
from .items_classes import Kindergarten2Item
from .options import Kindergarten2Options, Goal, ShuffleMonstermon
from .constants.inventory_item_names import InventoryItem
from .constants.mission_names import start_mission, Mission, win_mission
from .constants.money import Cost
from .constants.money import Money
from .constants.monstermon_card_names import all_cards


def create_event_item(player, event: str) -> Kindergarten2Item:
    return Kindergarten2Item(event, ItemClassification.progression, None, player)


def set_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    set_extra_locations_rules(multiworld, player, world_options)
    set_mission_rules(multiworld, player, world_options)
    set_extra_entrance_rules(multiworld, player, world_options)
    set_monstermon_card_rules(multiworld, player, world_options)
    set_outfit_rules(multiworld, player, world_options)


def set_extra_locations_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    set_rule(multiworld.get_location("Win A Bet With Carla", player),
             has_starting_money(Cost.monty_push, player, world_options))


def set_mission_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    set_start_mission_rules(multiworld, player, world_options)
    set_complete_mission_rules(multiworld, player, world_options)

    all_missions = [Mission.tale_of_janitors,
                    Mission.flowers_for_diana,
                    Mission.hitman_guard,
                    Mission.breaking_sad,
                    Mission.dodge_a_nugget,
                    Mission.cain_not_able,
                    Mission.opposites_attract,
                    Mission.things_go_boom,
                    Mission.creature_feature,
                    ]
    if world_options.goal == Goal.option_all_missions:
        set_rule(multiworld.get_location("Victory", player),
                 lambda state: all([state.can_reach_location(mission, player) for mission in all_missions]))

    # elif world_options.goal == Goal.option_all_missions_and_secret_ending:
    #     set_rule(multiworld.get_location("Victory", player),
    #              lambda state: all([state.can_reach_location(mission, player) for mission in all_missions]) and
    #                            has_monstermon_cards(state, 50, player, world_options))


def set_start_mission_rules(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options) -> None:
    set_rule(multiworld.get_entrance(start_mission(Mission.opposites_attract), player),
             has_items([InventoryItem.bob_toolbelt, InventoryItem.an_a_plus], player))
    set_rule(multiworld.get_entrance(start_mission(Mission.dodge_a_nugget), player),
             has_items([InventoryItem.bob_toolbelt, InventoryItem.prestigious_pin], player))
    set_rule(multiworld.get_entrance(start_mission(Mission.cain_not_able), player),
             has_items([InventoryItem.an_a_plus, InventoryItem.prestigious_pin], player))

    set_rule(multiworld.get_entrance(start_mission(Mission.things_go_boom), player),
             has_items([InventoryItem.laser_beam, InventoryItem.an_a_plus, InventoryItem.monstermon_plushie], player))
    set_rule(multiworld.get_entrance(start_mission(Mission.breaking_sad), player),
             has_items([InventoryItem.monstermon_plushie, InventoryItem.strange_chemical], player))

    set_rule(multiworld.get_entrance(start_mission(Mission.creature_feature), player),
             has_items([InventoryItem.laser_bomb, InventoryItem.monstermon_plushie, InventoryItem.faculty_remote], player))

    set_rule(multiworld.get_entrance(start_mission(Mission.secret_ending), player),
             has_monstermon_cards_rule(50, player, world_options))


def set_complete_mission_rules(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options) -> None:
    set_rule(multiworld.get_entrance(win_mission(Mission.tale_of_janitors), player),
             has_starting_money(Cost.carla_distract_lunch_lady, player, world_options))
    set_rule(multiworld.get_entrance(win_mission(Mission.flowers_for_diana), player),
             has_starting_money(Cost.monty_push + Cost.carla_distract_steve + Cost.science_class, player, world_options))
    set_rule(multiworld.get_entrance(win_mission(Mission.hitman_guard), player),
             has_starting_money(Cost.battery + Cost.burger + Cost.science_class, player, world_options))

    set_rule(multiworld.get_entrance(win_mission(Mission.opposites_attract), player),
             has_starting_money(Cost.science_class, player, world_options))
    set_rule(multiworld.get_entrance(win_mission(Mission.dodge_a_nugget), player),
             has_starting_money(Cost.lighter_into_school + Cost.burger + Cost.soda_machine, player, world_options))
    set_rule(multiworld.get_entrance(win_mission(Mission.cain_not_able), player),
             has_starting_money(Cost.hand_sanitizer + Cost.monty_read, player, world_options))

    set_rule(multiworld.get_entrance(win_mission(Mission.things_go_boom), player),
             has_starting_money(Cost.burger + Cost.science_class, player, world_options))
    set_rule(multiworld.get_entrance(win_mission(Mission.breaking_sad), player),
             has_starting_money(Cost.monty_push + Cost.scissors + Cost.burger + Cost.science_class, player, world_options))

    set_rule(multiworld.get_entrance(win_mission(Mission.creature_feature), player),
             has_starting_money(Cost.battery, player, world_options))


def set_extra_entrance_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    set_rule(multiworld.get_entrance("Go To School With A+", player),
             has_item(InventoryItem.an_a_plus, player))
    set_rule(multiworld.get_entrance("Go To School With A+ And Laser", player),
             has_items([InventoryItem.an_a_plus, InventoryItem.laser_beam], player))
    set_rule(multiworld.get_entrance("Push Monty Up The Ramp", player),
             has_starting_money(Cost.monty_push, player, world_options))
    set_rule(multiworld.get_entrance("Enter Weapons Closet For Chainsaw", player),
             has_starting_money(Cost.carla_distract_lunch_lady, player, world_options))
    set_rule(multiworld.get_entrance("Enter Weapons Closet For Murder Shovel", player),
             has_starting_money(Cost.hand_sanitizer + Cost.monty_read, player, world_options))
    set_rule(multiworld.get_entrance("Smuggle Lighter Into The School", player),
             has_starting_money(Cost.lighter_into_school, player, world_options))
    set_rule(multiworld.get_entrance("Enter Weapons Closet For Device", player),
             has_starting_money(Cost.burger, player, world_options))
    set_rule(multiworld.get_entrance("Enter Weapons Closet With A Bomb", player),
             has_starting_money(Cost.battery, player, world_options))
    set_rule(multiworld.get_entrance("Give Bugs A Soda", player),
             has_starting_money(Cost.cherry_soda, player, world_options))
    set_rule(multiworld.get_entrance("Go To Science Class", player),
             has_starting_money(Cost.science_class, player, world_options))
    set_rule(multiworld.get_entrance("Go To Science Class With A Leg", player),
             has_starting_money(Cost.science_class, player, world_options))
    set_rule(multiworld.get_entrance("Play Monstermon", player),
             has_monstermon_cards_rule(10, player, world_options))
    set_rule(multiworld.get_entrance("Applegate Meltdown", player),
             has_starting_money(Cost.monty_push, player, world_options))
    set_rule(multiworld.get_entrance("Enter Lockdown", player),
             has_starting_money(Cost.battery, player, world_options))
    set_rule(multiworld.get_entrance("Give Smoky To Hall Monitor", player),
             has_starting_money(Cost.burger, player, world_options))
    set_rule(multiworld.get_entrance("Shake Beehive On Penny", player),
             has_starting_money(Cost.monty_push + Cost.carla_distract_steve, player, world_options))
    set_rule(multiworld.get_entrance("Replace Yellow Flower With Blue", player),
             has_starting_money(Cost.monty_push + Cost.carla_distract_steve, player, world_options))
    set_rule(multiworld.get_entrance("Negociate With Monty", player),
             has_starting_money(Cost.monty_push + Cost.carla_distract_steve, player, world_options))
    set_rule(multiworld.get_entrance("Give Toilet Paper To Ozzy", player),
             has_starting_money(Cost.burger, player, world_options))
    set_rule(multiworld.get_entrance("Buy All Burgers", player),
             has_starting_money(Cost.burger, player, world_options))
    set_rule(multiworld.get_entrance("Ask For Vegan Lunch", player),
             has_starting_money(Cost.monty_push, player, world_options))
    set_rule(multiworld.get_entrance("Give Gravy To Cindy", player),
             has_starting_money(Cost.monty_push, player, world_options))
    set_rule(multiworld.get_entrance("Enter Secret Lab", player),
             has_starting_money(Cost.battery, player, world_options))
    set_rule(multiworld.get_entrance("Show Ted The Contract", player),
             has_starting_money(Cost.hand_sanitizer + Cost.monty_read, player, world_options))
    set_rule(multiworld.get_entrance("Check Billy's Box", player),
             has_starting_money(Cost.battery, player, world_options))
    set_rule(multiworld.get_entrance("Give Love Letter", player),
             has_starting_money(Cost.monty_push, player, world_options))
    set_rule(multiworld.get_entrance("Sell Inhaler", player),
             has_starting_money(Cost.battery + Cost.burger, player, world_options))
    set_rule(multiworld.get_entrance("Borrow Money", player),
             has_starting_money(Cost.hand_sanitizer, player, world_options))
    set_rule(multiworld.get_entrance("Enter Nugget Cave", player),
             has_starting_money(Cost.blueberry_soda, player, world_options))
    set_rule(multiworld.get_entrance("Escape Lunch After Bob Died", player),
             has_starting_money(Cost.carla_distract_lunch_lady, player, world_options))


def set_monstermon_card_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    pass


def set_outfit_rules(multiworld: MultiWorld, player, world_options: Kindergarten2Options):
    pass


def lambda_or(lambda_1: Callable[[Any], bool], lambda_2: Callable[[Any], bool]) -> Callable[[Any], bool]:
    return lambda state: lambda_1(state) or lambda_2(state)


def has_item(item: str, player: int) -> Callable[[Any], bool]:
    return lambda state: state.has(item, player)


def has_items(items: List[str], player: int) -> Callable[[Any], bool]:
    return lambda state: all([state.has(item, player) for item in items])


def has_starting_money(amount: float, player: int, world_options: Kindergarten2Options) -> Callable[[Any], bool]:
    if world_options.shuffle_money > 0:
        return lambda state: state.has(Money.starting_money, player, math.ceil(amount / world_options.shuffle_money))
    return lambda state: True


def has_monstermon_cards_rule(number: int, player: int, world_options: Kindergarten2Options) -> Callable[[Any], bool]:
    return lambda state: has_monstermon_cards(state, number, player, world_options)


def has_monstermon_cards(state, number: int, player: int, world_options: Kindergarten2Options) -> bool:
    if world_options.shuffle_monstermon == ShuffleMonstermon.option_true:
        return state.has_from_list(all_cards, player, number)
    # Cards that are always accessible:
    #   - Climbing The Rock Wall
    #   - Couch in the girl's bathroom
    #   - Swing Puzzle
    #   - Help Jerome get the ball at gym
    #   - Give Nugget A Fidget Spinner
    #   - Red Book In Principal's Office
    #   - Tell Bob About Janitor's Plan
    #   - Ozzy's Lunch Bag
    #   - Toy Chest During Gym
    if number <= 9:
        return True

    # The items still exist, but as events
    return state.has_from_list(all_cards, player, number)
