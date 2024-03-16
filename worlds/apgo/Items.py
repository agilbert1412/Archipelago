from random import Random
from typing import Protocol, Union, List, Dict

from attr import dataclass

from BaseClasses import Item, ItemClassification
from . import APGOOptions
from .ItemNames import ItemName
from .Options import Goal, EnableLocks, EnableDistanceReductions, EnableCollectionDistanceBonuses, EnableScoutingDistanceBonuses
from .Trips import Trip

all_trap_names = [ItemName.shuffle_trap, ItemName.silence_trap, ItemName.fog_of_war_trap,
                  ItemName.push_up_trap, ItemName.socializing_trap, ItemName.sit_up_trap, ItemName.jumping_jack_trap, ItemName.touch_grass_trap]

class APGOItem(Item):
    game = "Archipela-Go!"


@dataclass(frozen=True)
class APGOItemData:
    name: str
    classification: ItemClassification
    id: int


class APGOItemFactory(Protocol):
    def __call__(self, item_data: Union[str, APGOItemData]) -> APGOItem:
        raise NotImplementedError


# [Centimeters in a marathon] * [Centimeters in a half-marathon]
offset = 8902301100000

all_items = [
    APGOItemData(ItemName.distance_reduction, ItemClassification.progression, offset + 1),
    APGOItemData(ItemName.key, ItemClassification.progression, offset + 2),
    APGOItemData(ItemName.scouting_distance, ItemClassification.useful, offset + 3),
    APGOItemData(ItemName.collection_distance, ItemClassification.useful, offset + 4),

    APGOItemData(ItemName.shuffle_trap, ItemClassification.trap, offset + 101),
    APGOItemData(ItemName.silence_trap, ItemClassification.trap, offset + 102),
    APGOItemData(ItemName.fog_of_war_trap, ItemClassification.trap, offset + 103),

    APGOItemData(ItemName.push_up_trap, ItemClassification.trap, offset + 151),
    APGOItemData(ItemName.socializing_trap, ItemClassification.trap, offset + 152),
    APGOItemData(ItemName.sit_up_trap, ItemClassification.trap, offset + 153),
    APGOItemData(ItemName.jumping_jack_trap, ItemClassification.trap, offset + 154),
    APGOItemData(ItemName.touch_grass_trap, ItemClassification.trap, offset + 155),

    APGOItemData(ItemName.macguffin_A, ItemClassification.progression, offset + 201),
    APGOItemData(ItemName.macguffin_r, ItemClassification.progression, offset + 202),
    APGOItemData(ItemName.macguffin_c, ItemClassification.progression, offset + 203),
    APGOItemData(ItemName.macguffin_h, ItemClassification.progression, offset + 204),
    APGOItemData(ItemName.macguffin_i, ItemClassification.progression, offset + 205),
    APGOItemData(ItemName.macguffin_p, ItemClassification.progression, offset + 206),
    APGOItemData(ItemName.macguffin_e, ItemClassification.progression, offset + 207),
    APGOItemData(ItemName.macguffin_l, ItemClassification.progression, offset + 208),
    APGOItemData(ItemName.macguffin_a, ItemClassification.progression, offset + 209),
    APGOItemData(ItemName.macguffin_hyphen, ItemClassification.progression, offset + 210),
    APGOItemData(ItemName.macguffin_G, ItemClassification.progression, offset + 211),
    APGOItemData(ItemName.macguffin_o, ItemClassification.progression, offset + 212),
    APGOItemData(ItemName.macguffin_exclamation, ItemClassification.progression, offset + 213),
]


item_table = {item.name: item for item in all_items}


def create_items(item_factory: APGOItemFactory, trips: Dict[Trip, int], options: APGOOptions, random: Random) -> List[APGOItem]:
    items = []
    create_goal_items(item_factory, items, options)
    create_keys(item_factory, items, trips, options)
    number_items_left = options.number_of_checks - len(items)
    create_traps(item_factory, items, number_items_left, options, random)
    create_additional_items(item_factory, items, options, random)

    return items


def create_goal_items(item_factory: APGOItemFactory, items: List[APGOItem], options: APGOOptions) -> None:
    create_long_macguffin_items(item_factory, items, options)
    create_short_macguffin_items(item_factory, items, options)


def create_long_macguffin_items(item_factory: APGOItemFactory, items: List[APGOItem], options: APGOOptions) -> None:
    if options.goal != Goal.option_long_macguffin:
        return
    items.append(item_factory(ItemName.macguffin_A))
    items.append(item_factory(ItemName.macguffin_r))
    items.append(item_factory(ItemName.macguffin_c))
    items.append(item_factory(ItemName.macguffin_h))
    items.append(item_factory(ItemName.macguffin_i))
    items.append(item_factory(ItemName.macguffin_p))
    items.append(item_factory(ItemName.macguffin_e))
    items.append(item_factory(ItemName.macguffin_l))
    items.append(item_factory(ItemName.macguffin_a))
    items.append(item_factory(ItemName.macguffin_hyphen))
    items.append(item_factory(ItemName.macguffin_G))
    items.append(item_factory(ItemName.macguffin_o))
    items.append(item_factory(ItemName.macguffin_exclamation)),


def create_short_macguffin_items(item_factory: APGOItemFactory, items: List[APGOItem], options: APGOOptions) -> None:
    if options.goal != Goal.option_short_macguffin:
        return
    items.append(item_factory(ItemName.macguffin_A))
    items.append(item_factory(ItemName.macguffin_p))
    items.append(item_factory(ItemName.macguffin_hyphen))
    items.append(item_factory(ItemName.macguffin_G))
    items.append(item_factory(ItemName.macguffin_o))
    items.append(item_factory(ItemName.macguffin_exclamation)),


def create_keys(item_factory: APGOItemFactory, items: List[APGOItem], trips: Dict[Trip, int], options: APGOOptions) -> None:
    if options.enable_area_locks == EnableLocks.option_false:
        return

    max_key = 0
    for trip in trips:
        if trip.key_needed > max_key:
            max_key = trip.key_needed
    items.extend([item_factory(item) for item in [ItemName.key] * max_key])


def create_traps(item_factory: APGOItemFactory, items: List[APGOItem], number_filler_items: int, options: APGOOptions, random: Random) -> None:
    trap_rate = options.trap_rate.value
    number_of_traps = (number_filler_items * trap_rate) // 100
    if number_of_traps <= 0:
        return

    chosen_traps = random.choices(all_trap_names, k=number_of_traps)
    items.extend([item_factory(item) for item in chosen_traps])


def create_additional_items(item_factory: APGOItemFactory, items: List[APGOItem], options: APGOOptions, random: Random) -> None:
    number_items_left = options.number_of_checks - len(items)
    if number_items_left <= 0:
        return
    random_items = []
    if options.enable_distance_reductions == EnableDistanceReductions.option_true:
        random_items.append(ItemName.distance_reduction)
    if options.enable_scouting_distance_bonuses == EnableScoutingDistanceBonuses.option_true:
        random_items.append(ItemName.scouting_distance)
    if options.enable_collection_distance_bonuses == EnableCollectionDistanceBonuses.option_true:
        random_items.append(ItemName.collection_distance)
    if len(random_items) == 0:
        random_items.append(ItemName.key)
    chosen_items = random.choices(random_items, k=number_items_left)
    items.extend([item_factory(item) for item in chosen_items])
