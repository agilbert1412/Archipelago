from random import Random, random
from typing import List, Iterable, Tuple
from unittest import TestCase

from BaseClasses import Location
from . import APGOTestBase
from .. import Options, APGOWorld
from ..ItemNames import ItemName
from ..Trips import generate_trips, get_max_distance_tier
from ..distance import get_current_distance, get_reductions_needed_to_be_reachable

FEW_TRIPS = 20
MANY_TRIPS = 100
MAX_EXTRA_REDUCTIONS = 20


def create_seed() -> int:
    return int(random() * pow(10, 18) - 1)


def create_random(seed: int = 0) -> Random:
    if seed == 0:
        seed = create_seed()
    return Random(seed)


def count_trips_below_max_distance_no_reductions(world: APGOWorld, locations: Iterable[Location]):
    return count_trips_below_max_distance(world, locations, 0)


def count_trips_below_max_distance_all_reductions(world: APGOWorld, locations: Iterable[Location]):
    return count_trips_below_max_distance(world, locations, world.number_distance_reductions)


def count_trips_below_max_distance(world: APGOWorld, locations: Iterable[Location], active_reductions: int):
    options = world.options
    num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(world)
    number_available_trips = 0
    for location in locations:
        trip = world.trips[location.name]
        distance = get_current_distance(trip, active_reductions, options.maximum_distance, num_distance_reductions, max_distance_tier)
        if distance <= options.maximum_distance:
            number_available_trips += 1
    return number_available_trips


def get_distance_reductions_and_tiers(world: APGOWorld) -> Tuple[int, int]:
    return world.number_distance_reductions, get_max_distance_tier(world.trips.values())


def get_real_locations(test_base: APGOTestBase) -> List[Location]:
    return [location for location in test_base.multiworld.get_locations(test_base.player) if not location.is_event]


step = 5


class TestFewTripsNoDistanceReductions(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: FEW_TRIPS,
               Options.NumberOfLocks.internal_name: 0,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_reduction_exists(self):
        self.assertEqual(self.world.number_distance_reductions, 0)

    def test_all_trips_are_below_max(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in get_real_locations(self):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, 0, options.maximum_distance, num_distance_reductions, max_distance_tier)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_trips_are_reachable_with_no_reductions(self):
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            self.assertTrue(can_reach)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in get_real_locations(self):
            trip = self.world.trips[location.name]
            for i in range(0, MAX_EXTRA_REDUCTIONS, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance,
                                                           num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance,
                                                          num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)


class TestManyTripsNoDistanceReductions(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: MANY_TRIPS,
               Options.NumberOfLocks.internal_name: 0,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_reduction_exists(self):
        self.assertEqual(self.world.number_distance_reductions, 0)

    def test_all_trips_are_below_max(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in get_real_locations(self):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, 0, options.maximum_distance, num_distance_reductions, max_distance_tier)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_trips_are_reachable_with_no_reductions(self):
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            self.assertTrue(can_reach)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in get_real_locations(self):
            trip = self.world.trips[location.name]
            for i in range(0, MAX_EXTRA_REDUCTIONS, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance,
                                                          num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)


class TestFewTripsWithDistanceReductions(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: FEW_TRIPS,
               Options.NumberOfLocks.internal_name: 0,
               Options.EnableDistanceReductions.internal_name: True}

    def test_at_least_one_reduction_exists(self):
        self.assertGreater(self.world.number_distance_reductions, 0)

    def test_some_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, get_real_locations(self))
        self.assertGreater(number_available_trips, 0)

    def test_not_all_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, get_real_locations(self))
        self.assertLess(number_available_trips, len(self.world.trips))

    def test_all_trips_are_below_max_with_all_reductions(self):
        number_available_trips = count_trips_below_max_distance_all_reductions(self.world, get_real_locations(self))
        self.assertEqual(number_available_trips, len(self.world.trips))

    def test_some_trips_are_reachable_with_no_reductions(self):
        can_reach_one = False
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            if can_reach:
                can_reach_one = True
        self.assertTrue(can_reach_one)

    def test_not_all_trips_are_reachable_with_no_reductions(self):
        cant_reach_one = False
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            if not can_reach:
                cant_reach_one = True
        self.assertTrue(cant_reach_one)

    def test_all_trips_are_reachable_with_all_reductions(self):
        distance_reduction_items = [item for item in self.multiworld.get_items() if item.name == ItemName.distance_reduction]
        for item in distance_reduction_items:
            self.collect(item)
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            self.assertTrue(can_reach)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in get_real_locations(self):
            trip = self.world.trips[location.name]
            for i in range(0, self.world.number_distance_reductions * 2, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)


class TestManyTripsWithDistanceReductions(APGOTestBase):
    options = {Options.NumberOfTrips.internal_name: MANY_TRIPS,
               Options.NumberOfLocks.internal_name: 0,
               Options.EnableDistanceReductions.internal_name: True}

    def test_at_least_one_reduction_exists(self):
        self.assertGreater(self.world.number_distance_reductions, 0)

    def test_some_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, get_real_locations(self))
        self.assertGreater(number_available_trips, 0)

    def test_not_all_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, get_real_locations(self))
        self.assertLess(number_available_trips, len(self.world.trips))

    def test_all_trips_are_below_max_with_all_reductions(self):
        number_available_trips = count_trips_below_max_distance_all_reductions(self.world, get_real_locations(self))
        self.assertEqual(number_available_trips, len(self.world.trips))

    def test_some_trips_are_reachable_with_no_reductions(self):
        can_reach_one = False
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            if can_reach:
                can_reach_one = True
        self.assertTrue(can_reach_one)

    def test_not_all_trips_are_reachable_with_no_reductions(self):
        cant_reach_one = False
        for location in get_real_locations(self):
            num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
            max_distance = self.world.options.maximum_distance
            trip = self.world.trips[location.name]
            distance_zero_reductions = get_current_distance(trip, 0, max_distance, num_distance_reductions, max_distance_tier)
            can_reach = self.multiworld.state.can_reach(location)
            if not can_reach:
                cant_reach_one = True
        self.assertTrue(cant_reach_one)

    def test_all_trips_are_reachable_with_all_reductions(self):
        distance_reduction_items = [item for item in self.multiworld.get_items() if item.name == ItemName.distance_reduction]
        for item in distance_reduction_items:
            self.collect(item)
        for location in get_real_locations(self):
            can_reach = self.multiworld.state.can_reach(location)
            self.assertTrue(can_reach)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in get_real_locations(self):
            trip = self.world.trips[location.name]
            for i in range(0, self.world.number_distance_reductions * 2, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)


class TestReductionsRequiredFitDistanceAlgorithm(TestCase):

    def test_correct_number_of_reductions_needed(self):
        for desired_trips in range(5, 105, 20):
            for max_distance in range(1000, 20000, 1000):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 0,
                           Options.SpeedRequirement.internal_name: 0,
                           Options.MaximumDistance: max_distance,
                           Options.EnableDistanceReductions: True}
                trips = generate_trips(options, create_random())
                max_distance_tier = get_max_distance_tier(trips)
                tested_trips = set()
                for trip in trips:
                    if trip.template.distance_tier in tested_trips:
                        continue
                    tested_trips.add(trip.template.distance_tier)
                    for number_distance_reductions in range(1, max(2, desired_trips // 2), max(1, desired_trips // 8)):
                        with self.subTest(f"Trips: {desired_trips}, MaxDistance: {max_distance}, Trip: {trip}, Reductions: {number_distance_reductions}"):
                            reductions_needed = get_reductions_needed_to_be_reachable(trip, max_distance, number_distance_reductions, max_distance_tier)
                            distance_with_reductions = get_current_distance(trip, reductions_needed, max_distance, number_distance_reductions,
                                                                            max_distance_tier)
                            distance_without_any_reductions = get_current_distance(trip, 0, max_distance, number_distance_reductions, max_distance_tier)
                            self.assertLessEqual(distance_with_reductions, max_distance)
                            if reductions_needed == 0:
                                print(f"APGO - Options: {options}\n"
                                      f"With {number_distance_reductions} Total Reductions\n"
                                      f"Requires NO reductions to reduce trip [{trip}]\n"
                                      f"From {distance_without_any_reductions}m\n")
                                continue

                            distance_without_reduction = get_current_distance(trip, reductions_needed - 1, max_distance,
                                                                               number_distance_reductions, max_distance_tier)
                            self.assertGreaterEqual(distance_without_reduction, max_distance)
                            self.assertGreaterEqual(distance_without_any_reductions, max_distance)
                            print(f"APGO - Options: {options}\n"
                                  f"With {number_distance_reductions} Total Reductions\n"
                                  f"Requires {reductions_needed} reductions to reduce trip [{trip}]\n"
                                  f"From {distance_without_any_reductions}m to {distance_with_reductions}m\n")
