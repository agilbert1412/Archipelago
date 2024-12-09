from typing import List, Union

from BaseClasses import Entrance, MultiWorld, Region
from .options import Kindergarten2Options
from .constants.mission_names import Mission, mission, start_mission, win_mission, mission_complete


def create_regions(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options):
    new_region(multiworld, player, "Menu", None, ["Load Game"])
    new_region(multiworld, player, "Bedroom", "Load Game",
               ["Go To School", "Go To School With A+", "Go To School With A+ And Laser", start_mission(Mission.tale_of_janitors), start_mission(Mission.flowers_for_diana),
                start_mission(Mission.hitman_guard), start_mission(Mission.cain_not_able),
                start_mission(Mission.opposites_attract), start_mission(Mission.dodge_a_nugget),
                start_mission(Mission.things_go_boom), start_mission(Mission.breaking_sad),
                start_mission(Mission.creature_feature), start_mission(Mission.secret_ending)])

    new_mission_region(multiworld, player, Mission.tale_of_janitors, ["Enter Weapons Closet For Chainsaw", "Go To Girl's Bathroom", "Escape Lunch After Bob Died"])
    new_mission_region(multiworld, player, Mission.flowers_for_diana, ["Shake Beehive On Penny", "Replace Yellow Flower With Blue", "Negociate With Monty", "Ask For Vegan Lunch", "Give Gravy To Cindy", "Give Love Letter"])
    new_mission_region(multiworld, player, Mission.hitman_guard, ["Sell Inhaler"])
    new_mission_region(multiworld, player, Mission.cain_not_able, ["Enter Weapons Closet For Murder Shovel", "Show Ted The Contract", "Borrow Money"])
    new_mission_region(multiworld, player, Mission.opposites_attract, ["Janitor Unclogs Toilet"])
    new_mission_region(multiworld, player, Mission.dodge_a_nugget, ["Nuget is 'Special'", "Smuggle Lighter Into The School"])
    new_mission_region(multiworld, player, Mission.things_go_boom, ["Enter Weapons Closet For Device", "Squeak The Plushie (Things Go Boom)"])
    new_mission_region(multiworld, player, Mission.breaking_sad, ["Applegate Meltdown", "Squeak The Plushie (Breaking Sad)"])
    new_mission_region(multiworld, player, Mission.creature_feature, ["Enter Weapons Closet With A Bomb", "Enter Lockdown", "Enter Secret Lab", "Squeak The Plushie (Creature Feature)"])
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

    new_region(multiworld, player, "Dumb Tuesday", "Go To School", ["Push Monty Up The Ramp", "Visit Principal's Office", "Go To Gym", "Go To Science Class", "Go To Recess", "Go To Lunch", "Give Nugget Fidget Spinner"])
    new_region(multiworld, player, "Smart Class", "Go To School With A+", ["Give Toilet Paper To Ozzy"])
    new_region(multiworld, player, "Smart Class With Laser", "Go To School With A+ And Laser", ["Give Penny's Laser To Monty"])
    new_region(multiworld, player, "Handicap Ramp (Monty)", ["Push Monty Up The Ramp"], ["Be Handicapped"])
    new_region(multiworld, player, "Handicap Ramp", ["Be Handicapped", "Nuget is 'Special'"], ["Get Lost In The Woods"])
    new_region(multiworld, player, "Lighter Into School", ["Smuggle Lighter Into The School"], ["Distract Applegate", "Enter Weapons Closet For Nugget Cave Shovel", "Buy All Burgers"])
    new_region(multiworld, player, "Lunch Lady Gets More Burgers", ["Buy All Burgers"], ["Enter Nugget Cave", "Bury Nugget In Nuggets", "Grab Nuggets While Lunch Lady Gets Burgers", "Go Behind The Counter While Lunch Lady Gets Burgers"])
    new_region(multiworld, player, "Weapons Closet", ["Enter Weapons Closet For Chainsaw", "Enter Weapons Closet For Murder Shovel",
                                                      "Enter Weapons Closet For Nugget Cave Shovel", "Enter Weapons Closet For Device",
                                                      "Enter Weapons Closet With A Bomb"], [])
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
    new_region(multiworld, player, "Smoky", ["Give Smoky To Hall Monitor"], ["Bring Smoky To Microwave", "Find Smoky A Home"])
    new_region(multiworld, player, "Fallen Beehive", ["Shake Beehive On Penny"], ["See Something Gross"])
    new_region(multiworld, player, "Something Gross", ["See Something Gross"], [])
    new_region(multiworld, player, "Replace Lounge Flower", ["Replace Yellow Flower With Blue"], [])
    new_region(multiworld, player, "Negociated With Monty", ["Negociate With Monty"], [])
    new_region(multiworld, player, "Toilet Paper To Ozzy", ["Give Toilet Paper To Ozzy"], [])
    new_region(multiworld, player, "Lunch Lady Cooks Something Vegan", ["Ask For Vegan Lunch"], ["Go Behind The Counter While Lunch Lady Cooks"])
    new_region(multiworld, player, "Behind Lunch Lady Counter", ["Go Behind The Counter While Lunch Lady Gets Burgers", "Go Behind The Counter While Lunch Lady Cooks"], [])
    new_region(multiworld, player, "Obtained Nuggets", ["Grab Nuggets While Lunch Lady Gets Burgers"], ["Give Tenders To Nugget", "Bring Tenders To Microwave"])
    new_region(multiworld, player, "Tenders", ["Give Tenders To Nugget"], ["Find Tenders A Home"])
    new_region(multiworld, player, "Woods Puzzle", ["Get Lost In The Woods"], [])
    new_region(multiworld, player, "Nugget Fidget Spinner", ["Give Nugget Fidget Spinner"], [])
    new_region(multiworld, player, "Principal's Office", ["Visit Principal's Office"], [])
    new_region(multiworld, player, "Gravy", ["Give Gravy To Cindy"], ["Bring Gravy To Microwave", "Find Gravy A Home"])
    new_region(multiworld, player, "Secret Lab", ["Enter Secret Lab"], [])
    new_region(multiworld, player, "Cafeteria", ["Go To Lunch"], [])
    new_region(multiworld, player, "Toy Chest During Gym", ["Go To Toy Chest"], [])
    new_region(multiworld, player, "Monty Laser", ["Give Penny's Laser To Monty"], [])
    new_region(multiworld, player, "Dead Felix", ["Show Ted The Contract"], [])
    new_region(multiworld, player, "Lily And Billy Out Of Hiding", ["Squeak The Plushie (Things Go Boom)", "Squeak The Plushie (Breaking Sad)", "Squeak The Plushie (Creature Feature)"], ["Check Billy's Box"])
    new_region(multiworld, player, "Billy's Box", ["Check Billy's Box"], [])
    new_region(multiworld, player, "Unclogged Toilet", ["Janitor Unclogs Toilet"], [])
    new_region(multiworld, player, "Love Letter", ["Give Love Letter"], [])
    new_region(multiworld, player, "Sold Inhaler", ["Sell Inhaler"], ["Return To The Broken Wheelchair", "Electrocute Cindy"])
    new_region(multiworld, player, "Broken Wheelchair", ["Return To The Broken Wheelchair"], [])
    new_region(multiworld, player, "Borrowed Money", ["Borrow Money"], [])
    new_region(multiworld, player, "Nugget Cave", ["Enter Nugget Cave"], ["Go To Science Class With A Leg"])
    new_region(multiworld, player, "Science Class With Leg", ["Go To Science Class With A Leg"], [])
    new_region(multiworld, player, "Cat At Microwave", ["Bring Smoky To Microwave", "Bring Tenders To Microwave", "Bring Gravy To Microwave", ], [])
    new_region(multiworld, player, "Buried Nugget", ["Bury Nugget In Nuggets"], [])
    new_region(multiworld, player, "Electrocuted Cindy", ["Electrocute Cindy"], [])
    new_region(multiworld, player, "Dead Bob", ["Escape Lunch After Bob Died"], [])
    new_region(multiworld, player, "Adopted Cat", ["Find Tenders A Home", "Find Smoky A Home", "Find Gravy A Home"], [])


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
