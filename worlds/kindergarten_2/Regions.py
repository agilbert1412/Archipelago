from typing import List, Union

from BaseClasses import Entrance, MultiWorld, Region
from .Options import Kindergarten2Options, Goal
from .Locations import Kindergarten2Location, location_table
from .Rules import create_event_item
from .constants.mission_names import Mission, mission, start_mission, win_mission, mission_complete


def create_regions(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options):
    new_region(multiworld, player, "Menu", None, ["Load Game"])
    new_region(multiworld, player, "Bedroom", "Load Game",
               ["Go To School", "Go To School With A+", "Go To School With A+ And Laser", start_mission(Mission.tale_of_janitors), start_mission(Mission.flowers_for_diana),
                start_mission(Mission.hitman_guard), start_mission(Mission.cain_not_able),
                start_mission(Mission.opposites_attract), start_mission(Mission.dodge_a_nugget),
                start_mission(Mission.things_go_boom), start_mission(Mission.breaking_sad),
                start_mission(Mission.creature_feature), start_mission(Mission.secret_ending)])

    new_mission_region(multiworld, player, Mission.tale_of_janitors, ["Enter Weapons Closet For Chainsaw", "Go To Girl's Bathroom"])
    new_mission_region(multiworld, player, Mission.flowers_for_diana, ["Shake Beehive On Penny", "Replace Yellow Flower With Blue", "Negociate With Monty", "Ask For Vegan Lunch", "Give Gravy To Cindy"])
    new_mission_region(multiworld, player, Mission.hitman_guard, "Return To The Broken Wheelchair")
    new_mission_region(multiworld, player, Mission.cain_not_able, ["Enter Weapons Closet For Murder Shovel", "Show Ted The Contract"])
    new_mission_region(multiworld, player, Mission.opposites_attract, ["Janitor Unclogs Toilet"])
    new_mission_region(multiworld, player, Mission.dodge_a_nugget, ["Nuget is 'Special'", "Enter Weapons Closet For Nugget Cave Shovel", "Give Tenders To Nugget", "Go To Science Class With A Leg", "Distract Applegate", "Buy All Burgers"])
    new_mission_region(multiworld, player, Mission.things_go_boom, "Enter Weapons Closet For Device")
    new_mission_region(multiworld, player, Mission.breaking_sad, ["Applegate Meltdown"])
    new_mission_region(multiworld, player, Mission.creature_feature, ["Enter Weapons Closet With A Bomb", "Enter Lockdown", "Enter Secret Lab", "Check Billy's Box"])
    new_mission_region(multiworld, player, Mission.secret_ending)

    new_mission_complete_region(multiworld, player, Mission.tale_of_janitors)
    new_mission_complete_region(multiworld, player, Mission.flowers_for_diana)
    new_mission_complete_region(multiworld, player, Mission.hitman_guard)
    new_mission_complete_region(multiworld, player, Mission.cain_not_able)
    new_mission_complete_region(multiworld, player, Mission.opposites_attract)
    new_mission_complete_region(multiworld, player, Mission.dodge_a_nugget)
    new_mission_complete_region(multiworld, player, Mission.things_go_boom)
    new_mission_complete_region(multiworld, player, Mission.breaking_sad)
    new_mission_complete_region(multiworld, player, Mission.creature_feature)
    new_mission_complete_region(multiworld, player, Mission.secret_ending)

    new_region(multiworld, player, "Dumb Tuesday", "Go To School", ["Push Monty Up The Ramp", "Touch The Red Book", "Go To Gym", "Go To Science Class", "Go To Recess", "Go To Lunch", "Give Nugget Fidget Spinner"])
    new_region(multiworld, player, "Smart Class", "Go To School With A+", ["Give Toilet Paper To Ozzy"])
    new_region(multiworld, player, "Smart Class With Laser", "Go To School With A+ And Laser", ["Give Penny's Laser To Monty"])
    new_region(multiworld, player, "Broken Wheelchair", ["Return To The Broken Wheelchair"], [])
    new_region(multiworld, player, "Handicap Ramp", ["Push Monty Up The Ramp", "Nuget is 'Special'"], ["Get Lost In The Woods"])
    new_region(multiworld, player, "Weapons Closet", ["Enter Weapons Closet For Chainsaw", "Enter Weapons Closet For Murder Shovel",
                                                      "Enter Weapons Closet For Nugget Cave Shovel", "Enter Weapons Closet For Device",
                                                      "Enter Weapons Closet With A Bomb"], [])
    new_region(multiworld, player, "Tenders", ["Give Tenders To Nugget"], [])
    new_region(multiworld, player, "Science Class With Leg", ["Go To Science Class With A Leg"], [])
    new_region(multiworld, player, "Gym", ["Go To Gym"], ["Give Bugs A Soda", "Go To Toy Chest"])
    new_region(multiworld, player, "Bugs Soda", ["Give Bugs A Soda"], [])
    new_region(multiworld, player, "Science Class", ["Go To Science Class"], ["Examine Fish Tank Slide", "Examine Plant Slide"])
    new_region(multiworld, player, "Fish Tank Microscope", ["Examine Fish Tank Slide"], [])
    new_region(multiworld, player, "Plant Microscope", ["Examine Plant Slide"], [])
    new_region(multiworld, player, "Steal From Cubbies", ["Distract Applegate", "Applegate Meltdown"], [])
    new_region(multiworld, player, "Recess", ["Go To Recess"], ["Play Monstermon", "Give Smoky To Hall Monitor"])
    new_region(multiworld, player, "Monstermon Battle", ["Play Monstermon"], [])
    new_region(multiworld, player, "Girl's bathroom", ["Go To Girl's Bathroom"], [])
    new_region(multiworld, player, "Lockdown", ["Enter Lockdown"], [])
    new_region(multiworld, player, "Smoky", ["Give Smoky To Hall Monitor"], [])
    new_region(multiworld, player, "Fallen Beehive", ["Shake Beehive On Penny"], [])
    new_region(multiworld, player, "Replace Lounge Flower", ["Replace Yellow Flower With Blue"], [])
    new_region(multiworld, player, "Negociated With Monty", ["Negociate With Monty"], [])
    new_region(multiworld, player, "Toilet Paper To Ozzy", ["Give Toilet Paper To Ozzy"], [])
    new_region(multiworld, player, "Behind Lunch Counter", ["Buy All Burgers", "Ask For Vegan Lunch"], [])
    new_region(multiworld, player, "Woods Puzzle", ["Get Lost In The Woods"], [])
    new_region(multiworld, player, "Nugget Fidget Spinner", ["Give Nugget Fidget Spinner"], [])
    new_region(multiworld, player, "Red Book", ["Touch The Red Book"], [])
    new_region(multiworld, player, "Gravy", ["Give Gravy To Cindy"], [])
    new_region(multiworld, player, "Secret Lab", ["Enter Secret Lab"], [])
    new_region(multiworld, player, "Cafeteria", ["Go To Lunch"], [])
    new_region(multiworld, player, "Toy Chest During Gym", ["Go To Toy Chest"], [])
    new_region(multiworld, player, "Monty Laser", ["Give Penny's Laser To Monty"], [])
    new_region(multiworld, player, "Kill Felix", ["Show Ted The Contract"], [])
    new_region(multiworld, player, "Billy's Box", ["Check Billy's Box"], [])
    new_region(multiworld, player, "Unclogged Toilet", ["Janitor Unclogs Toilet"], [])


def new_mission_region(multiworld: MultiWorld, player: int, mission_name: str, exits: Union[None, str, List[str]] = None) -> Region:
    if exits is None:
        exits = [win_mission(mission_name)]
    elif isinstance(exits, str):
        exits = [win_mission(mission_name), exits]
    else:
        exits = [win_mission(mission_name), *exits]
    return new_region(multiworld, player, mission(mission_name), start_mission(mission_name), exits)


def new_mission_complete_region(multiworld: MultiWorld, player: int, mission_name: str) -> Region:
    return new_region(multiworld, player, mission_complete(mission_name), win_mission(mission_name), [])


def new_region(multiworld: MultiWorld, player: int, region_name: str, parent_entrances: Union[None, str, List[str]], exits: Union[str, List[str]]) -> Region:
    region = Region(region_name, player, multiworld)

    if isinstance(exits, str):
        exits = [exits]
    region.exits = [Entrance(player, exit_name, region) for exit_name in exits]

    multiworld.regions.append(region)

    if parent_entrances is None:
        return region
    if isinstance(parent_entrances, str):
        parent_entrances = [parent_entrances]
    for parent_entrance in parent_entrances:
        multiworld.get_entrance(parent_entrance, player).connect(region)

    return region


def conditional_location(condition: bool, location: str) -> List[str]:
    return conditional_locations(condition, [location])


def conditional_locations(condition: bool, locations: List[str]) -> List[str]:
    return locations if condition else []
