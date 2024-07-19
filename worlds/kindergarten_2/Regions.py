from typing import List, Union

from BaseClasses import Entrance, MultiWorld, Region
from .Options import Kindergarten2Options, Goal
from .Locations import Kindergarten2Location, location_table
from .Rules import create_event_item
from .strings.mission_names import Mission, mission, start_mission, win_mission, mission_complete


def create_regions(multiworld: MultiWorld, player: int, world_options: Kindergarten2Options):
    new_region(multiworld, player, "Menu", None, ["Load Game"])
    new_region(multiworld, player, "Bedroom", "Load Game",
               ["Go To School", start_mission(Mission.tale_of_janitors), start_mission(Mission.flowers_for_diana),
                start_mission(Mission.hitman_guard), start_mission(Mission.cain_not_able),
                start_mission(Mission.opposites_attract), start_mission(Mission.dodge_a_nugget),
                start_mission(Mission.things_go_boom), start_mission(Mission.breaking_sad),
                start_mission(Mission.creature_feature), start_mission(Mission.secret_ending)])

    new_region(multiworld, player, "Aimless Tuesday", "Go To School", [])

    new_mission_region(multiworld, player, Mission.tale_of_janitors)
    new_mission_region(multiworld, player, Mission.flowers_for_diana)
    new_mission_region(multiworld, player, Mission.hitman_guard)
    new_mission_region(multiworld, player, Mission.cain_not_able)
    new_mission_region(multiworld, player, Mission.opposites_attract)
    new_mission_region(multiworld, player, Mission.dodge_a_nugget)
    new_mission_region(multiworld, player, Mission.things_go_boom)
    new_mission_region(multiworld, player, Mission.breaking_sad)
    new_mission_region(multiworld, player, Mission.creature_feature)
    new_mission_region(multiworld, player, Mission.secret_ending)

    new_mission_complete_region(multiworld, player, Mission.tale_of_janitors)
    new_mission_complete_region(multiworld, player, Mission.flowers_for_diana)
    new_mission_complete_region(multiworld, player, Mission.hitman_guard)
    new_mission_complete_region(multiworld, player, Mission.cain_not_able)
    new_mission_complete_region(multiworld, player, Mission.opposites_attract)
    new_mission_complete_region(multiworld, player, Mission.dodge_a_nugget)
    new_mission_complete_region(multiworld, player, Mission.things_go_boom)
    new_mission_complete_region(multiworld, player, Mission.breaking_sad)
    region_creature_feature_complete = new_mission_complete_region(multiworld, player, Mission.creature_feature)
    region_secret_ending_complete = new_mission_complete_region(multiworld, player, Mission.secret_ending)
    if world_options.goal == Goal.option_creature_feature:
        create_victory_event(region_creature_feature_complete, player)
    elif world_options.goal == Goal.option_secret_ending:
        create_victory_event(region_secret_ending_complete, player)
    else:
        region_victory = region_creature_feature_complete if world_options.goal == Goal.option_all_missions else region_secret_ending_complete
        create_victory_event(region_victory, player)


def new_mission_region(multiworld: MultiWorld, player: int, mission_name: str) -> Region:
    return new_region(multiworld, player, mission(mission_name), start_mission(mission_name), win_mission(mission_name))


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


def create_victory_event(region_victory: Region, player: int):
    location_victory = Kindergarten2Location(player, "Victory", None, region_victory)
    region_victory.locations.append(location_victory)
    location_victory.place_locked_item(create_event_item(player, "Victory"))

# new_region(multiworld, player, "Bedroom", "Load Game", ["Go To School", "Activate Button"], [])
# new_region(multiworld, player, "School Yard", "Go To School", ["Morning Bell (Dumb Class)", "Morning Bell (Smart Class)", "Be Handicapped"], [])
# new_region(multiworld, player, "Handicapped Ramp", "Be Handicapped", ["Get Lost In The Woods", "Enter Handicapped Entrance"], [])
# new_region(multiworld, player, "Secret Ending", "Activate Button", ["Watch Credits"], [])
# new_region(multiworld, player, "Dumb Class", "Morning Bell (Dumb Class)", ["Leave Dumb Class (Study Hall)", "Lunch Bell (Dumb Class)"], [])
# new_region(multiworld, player, "Smart Class", "Morning Bell (Smart Class)", ["Leave Smart Class", "Lunch Bell (Smart Class)"], [])
# new_region(multiworld, player, "The Woods", "Get Lost In The Woods", [], [])
# new_region(multiworld, player, "Downstairs Hall (Before School)", "Enter Handicapped Entrance", ["Go Upstairs (Before School)"], [])
# new_region(multiworld, player, "Credits", "Watch Credits", [], [])
# new_region(multiworld, player, "Downstairs Hall (Morning Time) (Study Hall)", "Leave Dumb Class (Study Hall)", ["Enter Boys Bathroom (Morning Time) (Study Hall)", "Go Upstairs (Morning Time) (Study Hall)", "Lunch Bell (Dumb Class) (Study Hall)"], [])
# new_region(multiworld, player, "Cafeteria (Lunch)", ["Lunch Bell (Dumb Class)", "Lunch Bell (Smart Class)"], ["Leave Lunch", "Enter Teacher's Lounge (Lunch)"], [])
# new_region(multiworld, player, "Upstairs Hall (Morning Time)", "Leave Smart Class", [], [])
# new_region(multiworld, player, "Upstairs Hall (Before School)", "Go Upstairs (Before School)", [], [])
# new_region(multiworld, player, "Boys Bathroom (Morning Time) (Study Hall)", "Enter Boys Bathroom (Morning Time) (Study Hall)", [], [])
# new_region(multiworld, player, "Upstairs Hall (Morning Time) (Study Hall)", "Go Upstairs (Morning Time) (Study Hall)", [], [])
# new_region(multiworld, player, "Cafeteria (Lunch) (Study Hall)", "Lunch Bell (Dumb Class) (Study Hall)", [], [])
# new_region(multiworld, player, "Downstairs Hall (Lunch)", "Leave Lunch", [], [])
# new_region(multiworld, player, "Teacher's Lounge (Lunch)", "Enter Teacher's Lounge (Lunch)", [], [])
