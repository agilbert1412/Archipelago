from BaseClasses import Location, MultiWorld
from .Options import Kindergarten2Options, Goal
from .strings.world_strings import GAME_NAME
from .strings.mission_names import Mission, mission_complete, mission
from .strings.monstermon_card_names import MonstermonCard


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
    LocationData(MonstermonCard.celestial_slug, mission(Mission.hitman_guard)),  # After dismantling Monty's Wheelchair - Need 3$
    LocationData(MonstermonCard.hard_boogar, "Handicap Ramp"),
    LocationData(MonstermonCard.bucket_o_water, "Janitor's Closet"),
    LocationData(MonstermonCard.pale_tuna, "Nuggets -> Tenders To Nugget"),
    LocationData(MonstermonCard.ultralodon, "Show Leg From Nugget Cave to Danner"),
    LocationData(MonstermonCard.carnivorous_nimbus, "Bugs Soda At Gym"),
    LocationData(MonstermonCard.tiny_squid, "Microscope Fish Tank Sample"),
    LocationData(MonstermonCard.coral_that_looks_like_hand, "Beat Carla At Monstermon"),
    LocationData(MonstermonCard.hermit_frog, "Dumb Class Cubby"),
    LocationData(MonstermonCard.castle_of_sand, "Top Of The Rock Wall At Recess"),
    LocationData(MonstermonCard.man_on_fire, "Help Monty Make Pills"),
    LocationData(MonstermonCard.chair_of_spikes, "Couch in girl's bathroom"),
    LocationData(MonstermonCard.cigaretmon, "Lighter to Hall Monitor during lockdown"),
    LocationData(MonstermonCard.dune_worm, "Help Nugget win dodgeball"),
    LocationData(MonstermonCard.stressed_llama, "From Ted after Killing Ozzy"),
    LocationData(MonstermonCard.cyclops_duckling, "Swing Puzzle At Recess"),
    LocationData(MonstermonCard.teenage_mutant_zombie, "Beat Nugget At Monstermon"),
    LocationData(MonstermonCard.lonely_dragon, "Burger -> Smoky to Hall Monitor"),
    LocationData(MonstermonCard.million_head_hydra, "Beat Ozzy At Monstermon"),
    LocationData(MonstermonCard.dab_hero, "Help Jerome get the basketball from Carla"),
    LocationData(MonstermonCard.monstrous_flytrap, "Feed Dr Danner's Plant correctly"),
    LocationData(MonstermonCard.the_tallest_tree, "Beehive after shaken down"),
    LocationData(MonstermonCard.chill_stump, "Microscope Plant Sample"),
    LocationData(MonstermonCard.gnome_of_garden, "Replace Yellow Flower with blue one in Teacher's Lounge"),
    LocationData(MonstermonCard.ofaka_tornado, "Help Carla Build a bomb"),
    LocationData(MonstermonCard.literally_grass, "Given by monty for negociating well for Felix's stuff"),
    LocationData(MonstermonCard.doodoo_bug, "Give toilet paper to Ozzy"),
    LocationData(MonstermonCard.mystical_tomato, "Behind Lunch Counter in Back Corner"),
    LocationData(MonstermonCard.hissing_fauna, "Beat Monty at Monstermon"),
    LocationData(MonstermonCard.legendary_sword, "Woods Puzzle"),
    LocationData(MonstermonCard.golden_dewdrop, "Beat Jerome at Monstermon"),
    LocationData(MonstermonCard.zen_octopus, "Give Nugget Fidget Spinner"),
    LocationData(MonstermonCard.forbidden_book, "Red Book In Principal's Office"),
    LocationData(MonstermonCard.marshmallow, "Beat Cindy At Monstermon"),
    LocationData(MonstermonCard.pot_of_grease, "Vegan Meal -> Gravy to Cindy"),
    LocationData(MonstermonCard.lamb_with_cleaver, "Help Janitor Cover Up Some Murders"),
    LocationData(MonstermonCard.treasure_chest, "Complete Cain's Not Able"),
    LocationData(MonstermonCard.mr_nice_guy, "Tell Bob About Janitor's Plan at morning time"),
    LocationData(MonstermonCard.the_slurper, "Back Corner of Secret Lab"),
    LocationData(MonstermonCard.rare_jewel, "Beat Felix At Monstermon"),
    LocationData(MonstermonCard.onion, "In Ozzy's Lunch Bag"),
    LocationData(MonstermonCard.killer_eye, "Give Buggs His Knife Back"),
    LocationData(MonstermonCard.purple_plush, "In Toy Chest during Gym"),
    LocationData(MonstermonCard.spiky_flim_flam, "Beat Buggs at Monstermon"),
    LocationData(MonstermonCard.monster_ghost, "Give Monty Penny's laser during morning time"),
    LocationData(MonstermonCard.knight_who_turned_evil, "Show Ted Felix's Contract during morning time"),
    LocationData(MonstermonCard.evil_thwarter, "Beat Agnes at monstermon"),
    LocationData(MonstermonCard.mysterious_package, "In The Box Billy was hiding in"),
    LocationData(MonstermonCard.oglebop_ogre, "From Janitor after he unclogs the toilet while gaining cindy's doll during Opposites Attract"),
    LocationData(MonstermonCard.dank_magician, "From Lily for saving the school"),
]

all_locations = []
for i, mission_location in enumerate(mission_locations):
    mission_location.id_without_offset = 1 + i
    all_locations.append(mission_location)

for i, monstermon_location in enumerate(monstermon_locations):
    monstermon_location.id_without_offset = 101 + i
    all_locations.append(monstermon_location)

location_table = dict()

location_table.update({location_data.name: offset + i for i, location_data in enumerate(all_locations)})


def create_locations(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options) -> None:
    excluded_location = ""
    if world_options.goal == Goal.option_creature_feature:
        excluded_location = Mission.creature_feature
    elif world_options.goal == Goal.option_secret_ending:
        excluded_location = Mission.secret_ending
    for location_data in mission_locations:
        if location_data.name == excluded_location:
            continue
        name = location_data.name
        region = multiworld.get_region(location_data.region, player)
        location = Kindergarten2Location(player, name, location_table[name], region)
        region.locations.append(location)
