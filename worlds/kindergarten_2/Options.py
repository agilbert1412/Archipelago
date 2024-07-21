from dataclasses import dataclass

from Options import Choice, DeathLink, PerGameCommonOptions, Toggle, NamedRange


class Goal(Choice):
    """Goal for this playthrough"""
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


class FillerItems(Choice):
    """What to use as filler items?
    Nothing: All filler items are empty
    Pocket Change: Fillers are money bundles, but smaller than the progression ones
    Money: Filler generates extra money items
    Random Pocket Change: Fillers are a random mix of "Nothing" and "Pocket Change" items
    Random Pocket Change: Fillers are a random mix of "Nothing" and "Starting Money" items"""
    internal_name = "filler_items"
    display_name = "Filler Items"
    default = 1
    option_nothing = 0
    option_pocket_change = 1
    option_money = 2
    option_random_pocket_change = 3
    option_random_money = 4


@dataclass
class Kindergarten2Options(PerGameCommonOptions):
    goal: Goal
    shuffle_money: ShuffleMoney
    shuffle_monstermon: ShuffleMonstermon
    shuffle_outfits: ShuffleOutfits
    filler_items: FillerItems
    death_link: DeathLink
