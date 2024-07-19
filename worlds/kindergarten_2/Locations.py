from collections import Counter

from BaseClasses import Location, MultiWorld, Region
from .Options import Kindergarten2Options, Goal
from .Rules import create_event_item
from .constants.world_strings import GAME_NAME
from .constants.mission_names import Mission, mission_complete, mission
from .constants.monstermon_card_names import MonstermonCard


class Kindergarten2Location(Location):
    game: str = GAME_NAME


class LocationData():
    name: str
    id_without_offset: int
    region: str

    def __init__(self, name: str, region: str, id_without_offset: int = -1):
        self.name = name
        self.id_without_offset = id_without_offset
        self.region = region


offset = 0

mission_locations = [
    LocationData(Mission.tale_of_janitors, mission_complete(Mission.tale_of_janitors)),
    LocationData(Mission.flowers_for_diana, mission_complete(Mission.flowers_for_diana)),
    LocationData(Mission.hitman_guard, mission_complete(Mission.hitman_guard)),  # Need 4$
    LocationData(Mission.cain_not_able, mission_complete(Mission.cain_not_able)),
    LocationData(Mission.opposites_attract, mission_complete(Mission.opposites_attract)),
    LocationData(Mission.dodge_a_nugget, mission_complete(Mission.dodge_a_nugget)),
    LocationData(Mission.things_go_boom, mission_complete(Mission.things_go_boom)),
    LocationData(Mission.breaking_sad, mission_complete(Mission.breaking_sad)),
    LocationData(Mission.creature_feature, mission_complete(Mission.creature_feature)),
    LocationData(Mission.secret_ending, mission_complete(Mission.secret_ending)),
]

monstermon_locations = [
    LocationData(MonstermonCard.celestial_slug, "Broken Wheelchair"),
    LocationData(MonstermonCard.hard_boogar, "Handicap Ramp"),
    LocationData(MonstermonCard.bucket_o_water, "Weapons Closet"),
    LocationData(MonstermonCard.pale_tuna, "Tenders"),
    LocationData(MonstermonCard.ultralodon, "Science Class With Leg"),
    LocationData(MonstermonCard.carnivorous_nimbus, "Bugs Soda"),
    LocationData(MonstermonCard.tiny_squid, "Fish Tank Microscope"),
    LocationData(MonstermonCard.coral_that_looks_like_hand, "Monstermon Battle"),  # Carla
    LocationData(MonstermonCard.hermit_frog, "Steal From Cubbies"),  # This one can be obtained out of logic due to a bug, by going during Gym
    LocationData(MonstermonCard.castle_of_sand, "Recess"),
    LocationData(MonstermonCard.man_on_fire, mission_complete(Mission.breaking_sad)),
    LocationData(MonstermonCard.chair_of_spikes, "Girl's bathroom"),
    LocationData(MonstermonCard.cigaretmon, "Lockdown"),
    LocationData(MonstermonCard.dune_worm, mission_complete(Mission.dodge_a_nugget)),
    LocationData(MonstermonCard.stressed_llama, mission_complete(Mission.hitman_guard)),
    LocationData(MonstermonCard.cyclops_duckling, "Recess"),
    LocationData(MonstermonCard.teenage_mutant_zombie, "Monstermon Battle"),  # Nugget
    LocationData(MonstermonCard.lonely_dragon, "Smoky"),
    LocationData(MonstermonCard.million_head_hydra, "Monstermon Battle"),  # Ozzy
    LocationData(MonstermonCard.dab_hero, "Gym"),
    LocationData(MonstermonCard.monstrous_flytrap, mission_complete(Mission.flowers_for_diana)),
    LocationData(MonstermonCard.the_tallest_tree, "Fallen Beehive"),
    LocationData(MonstermonCard.chill_stump, "Plant Microscope"),
    LocationData(MonstermonCard.gnome_of_garden, "Replace Lounge Flower"),
    LocationData(MonstermonCard.ofaka_tornado, mission_complete(Mission.things_go_boom)),
    LocationData(MonstermonCard.literally_grass, "Negociated With Monty"),
    LocationData(MonstermonCard.doodoo_bug, "Toilet Paper To Ozzy"),
    LocationData(MonstermonCard.mystical_tomato, "Behind Lunch Counter"),
    LocationData(MonstermonCard.hissing_fauna, "Monstermon Battle"),  # Monty
    LocationData(MonstermonCard.legendary_sword, "Woods Puzzle"),
    LocationData(MonstermonCard.golden_dewdrop, "Monstermon Battle"),  # Jerome
    LocationData(MonstermonCard.zen_octopus, "Nugget Fidget Spinner"),
    LocationData(MonstermonCard.forbidden_book, "Red Book"),
    LocationData(MonstermonCard.marshmallow, "Monstermon Battle"),  # Cindy
    LocationData(MonstermonCard.pot_of_grease, "Gravy"),
    LocationData(MonstermonCard.lamb_with_cleaver, mission_complete(Mission.tale_of_janitors)),
    LocationData(MonstermonCard.treasure_chest, mission_complete(Mission.cain_not_able)),
    LocationData(MonstermonCard.mr_nice_guy, "Girl's bathroom"),
    LocationData(MonstermonCard.the_slurper, "Secret Lab"),
    LocationData(MonstermonCard.rare_jewel, "Monstermon Battle"),  # Felix
    LocationData(MonstermonCard.onion, "Cafeteria"),
    LocationData(MonstermonCard.killer_eye, mission_complete(Mission.opposites_attract)),
    LocationData(MonstermonCard.purple_plush, "Toy Chest During Gym"),
    LocationData(MonstermonCard.spiky_flim_flam, "Monstermon Battle"),  # Buggs
    LocationData(MonstermonCard.monster_ghost, "Monty Laser"),
    LocationData(MonstermonCard.knight_who_turned_evil, "Kill Felix"),
    LocationData(MonstermonCard.evil_thwarter, "Monstermon Battle"),  # Agnes
    LocationData(MonstermonCard.mysterious_package, "Billy's Box"),
    LocationData(MonstermonCard.oglebop_ogre, "Unclogged Toilet"),
    LocationData(MonstermonCard.dank_magician, mission_complete(Mission.creature_feature)),
]

money_locations = [
    LocationData("Felix's Tip", "Bedroom"),  # 3$
    LocationData("Sell Drugs To Monty", "Bedroom"),  # 5$
    LocationData("Sell Inhaler To Monty", "Bedroom"),  # 2$
    LocationData("Borrow Money From Felix", "Bedroom"),  # 5$
    LocationData("Skeleton Wallet", "Bedroom"),  # 3$
    LocationData("Ted's Cubby", "Bedroom"),  # 3$
]

all_locations = []
for i, mission_location in enumerate(mission_locations):
    mission_location.id_without_offset = 1 + i
    all_locations.append(mission_location)

for i, money_location in enumerate(money_locations):
    money_location.id_without_offset = 101 + i
    all_locations.append(money_location)

for i, monstermon_location in enumerate(monstermon_locations):
    monstermon_location.id_without_offset = 101 + i
    all_locations.append(monstermon_location)

location_table = dict()

location_table.update({location_data.name: offset + i for i, location_data in enumerate(all_locations)})


def create_locations(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options) -> None:
    victory_location = ""
    if world_options.goal == Goal.option_creature_feature:
        victory_location = Mission.creature_feature
    elif world_options.goal == Goal.option_secret_ending:
        victory_location = Mission.secret_ending
    elif world_options.goal == Goal.option_all_missions:
        region_victory = multiworld.get_region(mission_complete(Mission.creature_feature), player)
        create_victory_event(region_victory, player)
    elif world_options.goal == Goal.option_all_missions_and_secret_ending:
        region_victory = multiworld.get_region(mission_complete(Mission.secret_ending), player)
        create_victory_event(region_victory, player)

    for location_data in mission_locations:
        region = multiworld.get_region(location_data.region, player)
        if location_data.name == victory_location:
            create_victory_event(region, player)
            continue

        name = location_data.name
        location = Kindergarten2Location(player, name, location_table[name], region)
        region.locations.append(location)

    if world_options.shuffle_money:
        for location_data in money_locations:
            name = location_data.name
            region = multiworld.get_region(location_data.region, player)
            location = Kindergarten2Location(player, name, location_table[name], region)
            region.locations.append(location)

    for location_data in monstermon_locations:
        name = location_data.name
        region = multiworld.get_region(location_data.region, player)

        if world_options.shuffle_monstermon:
            location = Kindergarten2Location(player, name, location_table[name], region)
        else:
            location = Kindergarten2Location(player, name, None, region)
            location.place_locked_item(create_event_item(player, name))
        region.locations.append(location)


def create_victory_event(region: Region, player: int):
    location_victory = Kindergarten2Location(player, "Victory", None, region)
    region.locations.append(location_victory)
    location_victory.place_locked_item(create_event_item(player, "Victory"))
