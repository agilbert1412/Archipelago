from attr import dataclass

from BaseClasses import Item, ItemClassification
from .item_names import ItemName


class APGOItem(Item):
    game = "Archipela-Go!"


@dataclass(frozen=True)
class APGOItemData:
    name: str
    classification: ItemClassification
    id: int


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
]


items_table = {item.name: item.id for item in all_items}
