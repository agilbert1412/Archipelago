from dataclasses import dataclass

from Options import DeathLink, NamedRange, PerGameCommonOptions, Range, Toggle

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


class NumberOfChecks(Range):
    """The number of checks to generate in the world."""
    internal_name = "number_of_checks"
    display_name = "Number of Checks"
    range_start = 1
    range_end = 1000
    default = 5


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


class SpeedRequirement(NamedRange):
    """Every check will generate a random minimum speed in km/h you must travel at in order to be allowed to get it.
    This setting will be an upper bound for this speed requirement. The lower bound will scale with the choice as well.
    If you reach the check too slowly, you will need to go back home and try again.
    The generator does not know in advance about hills in your area, so make sure you consider them in your speed commitment"""
    internal_name = "speed_requirement"
    display_name = "Speed Requirement"
    range_start = 0
    range_end = 20
    default = 5
    special_range_names = standard_race_speeds


class EnableAreaLocks(Toggle):
    """
    Whether some checks are hard locked at the start, and require a "key" item to unlock
    """
    internal_name = "enable_scouting_bonuses"
    display_name = "Enable Scouting Bonuses"


class EnableDistanceReductions(Toggle):
    """
    Whether some checks will spawn further than the maximum distance, and distance reduction items are in the pool
    """
    internal_name = "enable_distance_reductions"
    display_name = "Enable Distance Reductions"


class EnableTimeBonuses(Toggle):
    """
    Whether the item can contain items that add time to your clock to reach checks
    """
    internal_name = "enable_time_bonuses"
    display_name = "Enable Time Bonuses"


class EnableScoutingDistanceBonuses(Toggle):
    """
    Whether the item pool can contain permanent bonuses to scouting distance
    """
    internal_name = "enable_scouting_distance_bonuses"
    display_name = "Enable Scouting Distance Bonuses"


class EnableCollectionDistanceBonuses(Toggle):
    """
    Whether the item pool can contain permanent bonuses to collection distance
    """
    internal_name = "enable_collection_distance_bonuses"
    display_name = "Enable Collection Distance Bonuses"


class EnableTraps(Toggle):
    """
    Whether the item pool can contain traps. Some traps may be honor-system based and rely on the player to execute them
    """
    internal_name = "enable_traps"
    display_name = "Enable Traps"


@dataclass
class APGOOptions(PerGameCommonOptions):
    number_of_checks: NumberOfChecks
    minimum_distance: MinimumDistance
    maximum_distance: MaximumDistance
    speed_requirement: SpeedRequirement
    enable_area_locks: EnableAreaLocks
    enable_distance_reductions: EnableDistanceReductions
    enable_time_bonuses: EnableTimeBonuses
    enable_scouting_distance_bonuses: EnableScoutingDistanceBonuses
    enable_collection_distance_bonuses: EnableCollectionDistanceBonuses
    enable_traps: EnableTraps
    death_link: DeathLink
