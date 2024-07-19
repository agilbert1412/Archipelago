from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, Toggle


class Goal(Choice):
    """Goal for this playthrough"""
    internal_name = "goal"
    display_name = "Goal"
    default = 0
    option_creature_feature = 0
    option_all_missions = 1
    option_secret_ending = 2


class ShuffleMoney(Toggle):
    """If turned on, you will start days with 0.00$, and will receive starting money as items.
    Additional Locations will be added to the various ways to obtain money during the day"""
    internal_name = "shuffle_money"
    display_name = "Shuffle Money"
    default = 1


class ShuffleMonstermon(Toggle):
    """Whether every Monstermon card is a location to be checked, and has an item in the pool."""
    internal_name = "shuffle_monstermon"
    display_name = "Shuffle Monstermon"
    default = 1


class ShuffleOutfits(Toggle):
    """Whether to shuffle the outfits, and add locations for each of them"""
    internal_name = "shuffle_outfits"
    display_name = "Shuffle Outfits"
    default = 0


@dataclass
class Kindergarten2Options(PerGameCommonOptions):
    goal: Goal
    shuffle_money: ShuffleMoney
    shuffle_monstermon: ShuffleMonstermon
    shuffle_outfits: ShuffleOutfits
    death_link: DeathLink
