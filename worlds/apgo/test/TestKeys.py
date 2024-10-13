import math
from random import Random, random
from typing import Dict, List, Iterable, Tuple
from unittest import TestCase

from BaseClasses import Location
from . import APGOTestBase
from .. import Options, APGOWorld, APGOItem
from ..ItemNames import ItemName
from ..Trips import generate_trips, Trip, get_max_distance_tier
from ..distance import get_current_distance, get_reductions_needed_to_be_reachable

FEW_TRIPS = 10
MANY_TRIPS = 100
MAX_EXTRA_REDUCTIONS = 20


def create_seed() -> int:
    return int(random() * pow(10, 18) - 1)


def create_random(seed: int = 0) -> Random:
    if seed == 0:
        seed = create_seed()
    return Random(seed)


def get_real_locations(test_base: APGOTestBase) -> List[Location]:
    return [location for location in test_base.multiworld.get_locations(test_base.player) if not location.is_event]


step = 5


class TestFewTripsNoLocks(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: FEW_TRIPS,
               Options.NumberOfLocks.internal_name: 0,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_keys_exist(self):
        self.assertEqual(self.world.number_keys, 0)
        for item in self.multiworld.get_items():
            self.assertNotEqual(item.name, ItemName.key)

    def test_everything_is_in_area_0(self):
        for trip in self.world.trips.values():
            self.assertEqual(trip.template.key_needed, 0)

    def test_can_reach_everything(self):
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            self.assertTrue(can_reach)


class TestFewTripsFewLocks(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: FEW_TRIPS,
               Options.NumberOfLocks.internal_name: 2,
               Options.EnableDistanceReductions.internal_name: False}

    def test_2_keys_exist(self):
        self.assertEqual(self.world.number_keys, 2)
        key_count = 0
        for item in self.multiworld.get_items():
            if item.name == ItemName.key:
                key_count += 1
        self.assertEqual(key_count, 2)

    def test_everything_is_in_area_0_to_2(self):
        count_by_area = {}
        for trip in self.world.trips.values():
            self.assertLessEqual(trip.template.key_needed, 2)
            if trip.template.key_needed not in count_by_area:
                count_by_area[trip.template.key_needed] = 0
            count_by_area[trip.template.key_needed] += 1
        for key in count_by_area:
            self.assertGreaterEqual(count_by_area[key], 1)

    def test_can_reach_everything_with_progressive_keys(self):
        locations_by_keys = {}
        for location in get_real_locations(self):
            if self.world.trips[location.name].template.key_needed not in locations_by_keys:
                locations_by_keys[self.world.trips[location.name].template.key_needed] = []
            locations_by_keys[self.world.trips[location.name].template.key_needed].append(location)
        keys = [item for item in self.multiworld.get_items() if item.name == ItemName.key]
        for i in range(0, len(locations_by_keys)):
            with self.subTest(f"Test Key #{i}"):
                if i > 0:
                    for location in locations_by_keys[i]:
                        can_reach = self.multiworld.state.can_reach(location)
                        self.assertFalse(can_reach)
                    self.collect(keys[i-1])
                for location in locations_by_keys[i]:
                    can_reach = self.multiworld.state.can_reach(location)
                    self.assertTrue(can_reach)


class TestManyTripsFewLocks(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: MANY_TRIPS,
               Options.NumberOfLocks.internal_name: 2,
               Options.EnableDistanceReductions.internal_name: False}

    def test_2_keys_exist(self):
        self.assertEqual(self.world.number_keys, 2)
        key_count = 0
        for item in self.multiworld.get_items():
            if item.name == ItemName.key:
                key_count += 1
        self.assertEqual(key_count, 2)

    def test_everything_is_in_area_0_to_2(self):
        count_by_area = {}
        for trip in self.world.trips.values():
            self.assertLessEqual(trip.template.key_needed, 2)
            if trip.template.key_needed not in count_by_area:
                count_by_area[trip.template.key_needed] = 0
            count_by_area[trip.template.key_needed] += 1
        for key in count_by_area:
            self.assertGreaterEqual(count_by_area[key], 1)

    def test_can_reach_everything_with_progressive_keys(self):
        locations_by_keys = {}
        for location in get_real_locations(self):
            if self.world.trips[location.name].template.key_needed not in locations_by_keys:
                locations_by_keys[self.world.trips[location.name].template.key_needed] = []
            locations_by_keys[self.world.trips[location.name].template.key_needed].append(location)
        keys = [item for item in self.multiworld.get_items() if item.name == ItemName.key]
        for i in range(0, len(locations_by_keys)):
            with self.subTest(f"Test Key #{i}"):
                if i > 0:
                    for location in locations_by_keys[i]:
                        can_reach = self.multiworld.state.can_reach(location)
                        self.assertFalse(can_reach)
                    self.collect(keys[i-1])
                for location in locations_by_keys[i]:
                    can_reach = self.multiworld.state.can_reach(location)
                    self.assertTrue(can_reach)


class TestManyTripsManyLocks(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: MANY_TRIPS,
               Options.NumberOfLocks.internal_name: 8,
               Options.EnableDistanceReductions.internal_name: False}

    def test_2_keys_exist(self):
        self.assertEqual(self.world.number_keys, 8)
        key_count = 0
        for item in self.multiworld.get_items():
            if item.name == ItemName.key:
                key_count += 1
        self.assertEqual(key_count, 8)

    def test_everything_is_in_area_0_to_8(self):
        count_by_area = {}
        for trip in self.world.trips.values():
            self.assertLessEqual(trip.template.key_needed, 8)
            if trip.template.key_needed not in count_by_area:
                count_by_area[trip.template.key_needed] = 0
            count_by_area[trip.template.key_needed] += 1
        for key in count_by_area:
            self.assertGreaterEqual(count_by_area[key], 1)

    def test_can_reach_everything_with_progressive_keys(self):
        locations_by_keys = {}
        for location in get_real_locations(self):
            if self.world.trips[location.name].template.key_needed not in locations_by_keys:
                locations_by_keys[self.world.trips[location.name].template.key_needed] = []
            locations_by_keys[self.world.trips[location.name].template.key_needed].append(location)
        keys = [item for item in self.multiworld.get_items() if item.name == ItemName.key]
        for i in range(0, len(locations_by_keys)):
            with self.subTest(f"Test Key #{i}"):
                if i > 0:
                    for location in locations_by_keys[i]:
                        can_reach = self.multiworld.state.can_reach(location)
                        self.assertFalse(can_reach)
                    self.collect(keys[i-1])
                for location in locations_by_keys[i]:
                    can_reach = self.multiworld.state.can_reach(location)
                    self.assertTrue(can_reach)