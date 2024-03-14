from random import Random
from typing import Protocol, Union, List

from attr import dataclass

from BaseClasses import Item, ItemClassification
from . import APGOOptions
from .ItemNames import ItemName
from .Options import Goal


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
    APGOItemData(ItemName.area_unlock, ItemClassification.progression, offset + 2),
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


def create_items(create_item: APGOItemFactory, options: APGOOptions, random : Random) -> List[APGOItem]:
    created_items = []
    create_goal_items(create_item, created_items, options)
    number_items_left = options.number_of_checks - len(created_items)


def create_goal_items(create_item: APGOItemFactory, items: List[APGOItem], options: APGOOptions) -> None:
    create_long_macguffin_items(create_item, items, options)
    create_short_macguffin_items(create_item, items, options)


def create_long_macguffin_items(create_item: APGOItemFactory, items: List[APGOItem], options: APGOOptions) -> None:
    if options.goal != Goal.option_long_macguffin:
        return
    items.append(create_item(ItemName.macguffin_A))
    items.append(create_item(ItemName.macguffin_r))
    items.append(create_item(ItemName.macguffin_c))
    items.append(create_item(ItemName.macguffin_h))
    items.append(create_item(ItemName.macguffin_i))
    items.append(create_item(ItemName.macguffin_p))
    items.append(create_item(ItemName.macguffin_e))
    items.append(create_item(ItemName.macguffin_l))
    items.append(create_item(ItemName.macguffin_a))
    items.append(create_item(ItemName.macguffin_hyphen))
    items.append(create_item(ItemName.macguffin_G))
    items.append(create_item(ItemName.macguffin_o))
    items.append(create_item(ItemName.macguffin_exclamation)),


def create_short_macguffin_items(create_item: APGOItemFactory, items: List[APGOItem], options: APGOOptions) -> None:
    if options.goal != Goal.option_short_macguffin:
        return
    items.append(create_item(ItemName.macguffin_A))
    items.append(create_item(ItemName.macguffin_p))
    items.append(create_item(ItemName.macguffin_hyphen))
    items.append(create_item(ItemName.macguffin_G))
    items.append(create_item(ItemName.macguffin_o))
    items.append(create_item(ItemName.macguffin_exclamation)),
