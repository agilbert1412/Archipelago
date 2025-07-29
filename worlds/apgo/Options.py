from dataclasses import dataclass

from Options import DeathLink, NamedRange, PerGameCommonOptions, Range, Toggle, Choice

standard_race_lengths = {
    "2k": 2000,
    "5k": 5000,
    "10k": 10000,
    "half_marathon": 21098,
    "marathon": 42195,
    "50k": 50000,
    "50_miler": 80467,
    "100k": 100000,
    "100_miler": 160934
}

standard_race_speeds = {
    "no_speed_requirements": 0,
    "slow_walk": 2,
    "fast_walk": 5,
    "slow_jog": 7,
    "fast_jog": 9,
    "slow_run": 10,
    "fast_run": 14,
    "sprint": 16,
    "slow_bicycle": 15,
    "medium_bicycle": 22,
    "fast_bicycle": 30,
}


class Goal(Choice):
    """The completion condition for the slot
    One Hard Travel: Your victory condition will be a trip at maximum distance and maximum speed (chosen from the other settings)
    Allsanity: Obtain every check
    Short MacGuffin: The slot will contain items that are the letters for "Ap-Go!". Collecting all 6 is victory
    Long MacGuffin: The slot will contain items that are the letters for "Archipela-Go!". Collecting all 13 is victory
    """
    internal_name = "goal"
    display_name = "Goal"
    option_one_hard_travel = 0
    option_allsanity = 1
    option_short_macguffin = 2
    option_long_macguffin = 3
    default = 2


class NumberOfTrips(Range):
    """The number of checks to generate in the world.
    Most items in this game are flexible, so the more checks you have, the more of each item you will get, but each will be less powerful.
    If you pick a MacGuffin goal, you need at least enough checks to fit the goal items. If not, they will be placed in your start_inventory"""
    internal_name = "number_of_trips"
    display_name = "Number of Checks"
    range_start = 1
    range_end = 1000
    default = 10


class MinimumDistance(NamedRange):
    """The minimum distance in meters you will be expected to go to for a check.
    Keep in mind that you might have to travel twice that to come back home afterwards.
    Even Distance reduction items will not make distances cross this threshold"""
    internal_name = "minimum_distance"
    display_name = "Minimum Distance"
    range_start = 100
    range_end = 5000
    default = 500
    special_range_names = standard_race_lengths


class MaximumDistance(NamedRange):
    """The maximum distance in meters you will be expected to go to for a check.
    Keep in mind that you might have to travel twice that to come back home afterwards.
    Some checks can appear outside of this range at first, but will only be in-logic after distance has been reduced below this threshold
    The generator does not know in advance about hills in your area, so make sure you consider them in your distance commitment"""
    internal_name = "maximum_distance"
    display_name = "Maximum Distance"
    range_start = 1000
    range_end = 50000
    default = 5000
    special_range_names = standard_race_lengths


class NumberOfLocks(NamedRange):
    """
    This will place "keys" in the item pools, and some checks will start out locked behind a random number of keys
    If there are not enough checks to hold all the keys you need, this option will be reduced by force
    """
    internal_name = "number_of_locks"
    display_name = "NumberOfLocks"
    range_start = 0
    range_end = 10
    default = 3
    special_range_names = {
        "none": 0
    }


class SpeedRequirement(NamedRange):
    """[Not currently implemented]
    Every check will generate a random minimum speed in km/h you must travel at in order to be allowed to get it.
    This setting will be an upper bound for this speed requirement. The lower bound will scale with the choice as well.
    If you reach the check too slowly, you will need to go back home and try again.
    The generator does not know in advance about hills in your area, so make sure you consider them in your speed commitment.
    """
    internal_name = "speed_requirement"
    display_name = "Speed Requirement"
    range_start = 0
    range_end = 20
    default = 5
    special_range_names = standard_race_speeds


class EnableDistanceReductions(Toggle):
    """
    [Not currently implemented in the app]
    Whether some checks will spawn further than the maximum distance, and distance reduction items are in the pool
    """
    internal_name = "enable_distance_reductions"
    display_name = "Enable Distance Reductions"


class EnableScoutingDistanceBonuses(Toggle):
    """[Not currently implemented]
    Whether the item pool can contain permanent bonuses to scouting distance
    """
    internal_name = "enable_scouting_distance_bonuses"
    display_name = "Enable Scouting Distance Bonuses"


class EnableCollectionDistanceBonuses(Toggle):
    """[Not currently implemented]
    Whether the item pool can contain permanent bonuses to collection distance
    """
    internal_name = "enable_collection_distance_bonuses"
    display_name = "Enable Collection Distance Bonuses"


class TrapRate(NamedRange):
    """
    What percentage of the remaining item pool should be traps. Some traps may be honor-system based and rely on the player to execute them
    """
    internal_name = "trap_rate"
    display_name = "Trap Rate"
    range_start = 0
    range_end = 100
    default = 50
    special_range_names = {
        "none": 0,
        "quarter": 25,
        "half": 50,
        "all": 100,
    }


# class ApGoProgressionBalancing(ProgressionBalancing):


@dataclass
class APGOOptions(PerGameCommonOptions):
    goal: Goal
    number_of_trips: NumberOfTrips
    minimum_distance: MinimumDistance
    maximum_distance: MaximumDistance
    speed_requirement: SpeedRequirement
    number_of_locks: NumberOfLocks
    enable_distance_reductions: EnableDistanceReductions
    enable_scouting_distance_bonuses: EnableScoutingDistanceBonuses
    enable_collection_distance_bonuses: EnableCollectionDistanceBonuses
    trap_rate: TrapRate
    # progression_balancing: ApGoProgressionBalancing
    death_link: DeathLink
