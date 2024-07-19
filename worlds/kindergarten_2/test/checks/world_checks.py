from typing import List

from BaseClasses import MultiWorld, ItemClassification
from .. import Kindergarten2TestBase
from ... import Options


def get_all_item_names(multiworld: MultiWorld) -> List[str]:
    return [item.name for item in multiworld.itempool]


def get_all_location_names(multiworld: MultiWorld) -> List[str]:
    return [location.name for location in multiworld.get_locations() if not location.is_event]


def assert_victory_exists(tester: Kindergarten2TestBase, multiworld: MultiWorld):
    all_items = [item.name for item in multiworld.get_items()]
    tester.assertIn("Victory", all_items)


def collect_all_then_assert_can_win(tester: Kindergarten2TestBase, multiworld: MultiWorld):
    for item in multiworld.get_items():
        multiworld.state.collect(item)
    tester.assertTrue(multiworld.find_item("Victory", 1).can_reach(multiworld.state))


def assert_can_win(tester: Kindergarten2TestBase, multiworld: MultiWorld):
    assert_victory_exists(tester, multiworld)
    collect_all_then_assert_can_win(tester, multiworld)


def assert_same_number_items_locations(tester: Kindergarten2TestBase, multiworld: MultiWorld):
    non_event_locations = [location for location in multiworld.get_locations() if not location.advancement]
    tester.assertEqual(len(multiworld.itempool), len(non_event_locations))
