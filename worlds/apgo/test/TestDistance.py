import math
from random import Random, random
from typing import Dict, List, Iterable, Tuple
from unittest import TestCase

from BaseClasses import Location
from . import APGOTestBase
from .. import Options, APGOWorld
from ..ItemNames import ItemName
from ..Trips import generate_trips, Trip
from ..distance import get_current_distance, get_reductions_needed_to_be_reachable

FEW_TRIPS = 5
MANY_TRIPS = 100
MAX_EXTRA_REDUCTIONS = 20


def create_seed() -> int:
    return int(random() * pow(10, 18) - 1)


def create_random(seed: int = 0) -> Random:
    if seed == 0:
        seed = create_seed()
    return Random(seed)


def get_max_distance_tier(trips: Iterable[Trip]) -> int:
    return max([trip.template.distance_tier for trip in trips])


def get_distance_reductions_and_tiers(world: APGOWorld) -> Tuple[int, int]:
    return world.number_distance_reductions, get_max_distance_tier(world.trips.values())


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


step = 5


class TestFewTripsNoDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: FEW_TRIPS,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_reduction_exists(self):
        self.assertEqual(self.world.number_distance_reductions, 0)

    def test_all_trips_are_below_max(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in self.multiworld.get_locations(self.player):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, 0, options.maximum_distance, num_distance_reductions, max_distance_tier)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, MAX_EXTRA_REDUCTIONS, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance,
                                                           num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance,
                                                          num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)


class TestManyTripsNoDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: MANY_TRIPS,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_reduction_exists(self):
        self.assertEqual(self.world.number_distance_reductions, 0)

    def test_all_trips_are_below_max(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in self.multiworld.get_locations(self.player):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, 0, options.maximum_distance, num_distance_reductions, max_distance_tier)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, MAX_EXTRA_REDUCTIONS, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance,
                                                          num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)


class TestFewTripsWithDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: FEW_TRIPS,
               Options.EnableDistanceReductions.internal_name: True}

    def test_at_least_one_reduction_exists(self):
        self.assertGreater(self.world.number_distance_reductions, 0)

    def test_some_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, self.multiworld.get_locations(self.player))
        self.assertGreater(number_available_trips, 0)

    def test_not_all_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, self.multiworld.get_locations(self.player))
        self.assertLess(number_available_trips, len(self.world.trips))

    def test_all_trips_are_below_max_with_all_reductions(self):
        number_available_trips = count_trips_below_max_distance_all_reductions(self.world, self.multiworld.get_locations(self.player))
        self.assertEqual(number_available_trips, len(self.world.trips))

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, self.world.number_distance_reductions * 2, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    distance_after = get_current_distance(trip, i + 1, options.maximum_distance, num_distance_reductions, max_distance_tier)
                    self.assertGreater(distance_before, distance_after)
                    self.assertGreaterEqual(distance_after, options.minimum_distance)


class TestManyTripsWithDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: MANY_TRIPS,
               Options.EnableDistanceReductions.internal_name: True}

    def test_at_least_one_reduction_exists(self):
        self.assertGreater(self.world.number_distance_reductions, 0)

    def test_some_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, self.multiworld.get_locations(self.player))
        self.assertGreater(number_available_trips, 0)

    def test_not_all_trips_are_below_max_with_no_reductions(self):
        number_available_trips = count_trips_below_max_distance_no_reductions(self.world, self.multiworld.get_locations(self.player))
        self.assertLess(number_available_trips, len(self.world.trips))

    def test_all_trips_are_below_max_with_all_reductions(self):
        number_available_trips = count_trips_below_max_distance_all_reductions(self.world, self.multiworld.get_locations(self.player))
        self.assertEqual(number_available_trips, len(self.world.trips))

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        num_distance_reductions, max_distance_tier = get_distance_reductions_and_tiers(self.world)
        for location in self.multiworld.get_locations(self.player):
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
                options = {Options.NumberOfChecks.internal_name: desired_trips,
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
