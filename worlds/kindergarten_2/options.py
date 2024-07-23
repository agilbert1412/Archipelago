from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, Toggle, NamedRange, OptionSet
from worlds.kindergarten_2.constants.filler_names import Filler


class Goal(Choice):
    """Goal for this playthrough.
    Either completing the final mission "Creature Feature", All Missions,
    or getting the Monstermon Secret Ending"""
    internal_name = "goal"
    display_name = "Goal"
    default = 0
    option_creature_feature = 0
    option_all_missions = 1
    option_secret_ending = 2


class ShuffleMoney(NamedRange):
    """If turned on, you will start days with 0.00$, and will receive starting money as items.
    Additional Locations will be added to the various ways to obtain money during the day
    Picking 0 makes the money unshuffled and behave like vanilla
    Picking 1-4 will make it so bundles of progressive starting money are worth that amount"""
    internal_name = "shuffle_money"
    display_name = "Shuffle Money"
    default = 1
    range_start = 0
    range_end = 4


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


class FillerItems(OptionSet):
    """What to use as filler items?
    Nothing: All filler items are empty
    Pocket Change: Fillers are money bundles, but smaller than the progression ones
    Money: Filler generates extra money items
    Traps: Filler generates some traps
    """
    internal_name = "filler_items"
    display_name = "Filler Items"
    valid_keys = frozenset({Filler.nothing, Filler.pocket_change, Filler.money, Filler.traps})
    preset_none = frozenset()
    preset_all = valid_keys
    default = frozenset({Filler.pocket_change, Filler.traps})


@dataclass
class Kindergarten2Options(PerGameCommonOptions):
    goal: Goal
    shuffle_money: ShuffleMoney
    shuffle_monstermon: ShuffleMonstermon
    shuffle_outfits: ShuffleOutfits
    filler_items: FillerItems
    death_link: DeathLink
