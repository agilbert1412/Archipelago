import math
from random import Random, random
from typing import Dict, List
from unittest import TestCase

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


def get_max_distance_tier(trips: List[Trip]) -> int:
    return max([trip.template.distance_tier for trip in trips])


step = 5


class TestFewTripsNoDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: FEW_TRIPS,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_reduction_exists(self):
        self.assertEqual(self.world.number_distance_reductions, 0)

    def test_all_trips_are_between_min_and_max(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, 0, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                                get_max_distance_tier(self.world.trips.values()))
                self.assertGreaterEqual(distance, options.minimum_distance)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, MAX_EXTRA_REDUCTIONS, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.minimum_distance, options.maximum_distance,
                                                           self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    distance_after = get_current_distance(trip, i + 1, options.minimum_distance, options.maximum_distance,
                                                          self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    self.assertGreater(distance_before, distance_after)
                    self.assertGreaterEqual(distance_after, options.minimum_distance)


class TestManyTripsNoDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: MANY_TRIPS,
               Options.EnableDistanceReductions.internal_name: False}

    def test_no_reduction_exists(self):
        self.assertEqual(self.world.number_distance_reductions, 0)

    def test_all_trips_are_between_min_and_max(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, 0, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                                get_max_distance_tier(self.world.trips.values()))
                self.assertGreaterEqual(distance, options.minimum_distance)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, MAX_EXTRA_REDUCTIONS, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                                           get_max_distance_tier(self.world.trips.values()))
                    distance_after = get_current_distance(trip, i + 1, options.minimum_distance, options.maximum_distance,
                                                          self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    self.assertGreater(distance_before, distance_after)
                    self.assertGreaterEqual(distance_after, options.minimum_distance)


class TestFewTripsWithDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: FEW_TRIPS,
               Options.EnableDistanceReductions.internal_name: True}

    def test_at_least_one_reduction_exists(self):
        self.assertGreater(self.world.number_distance_reductions, 0)

    def test_some_trips_are_below_max_with_no_reductions(self):
        options = self.world.options
        number_available_trips = 0
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            distance = get_current_distance(trip, 0, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                            get_max_distance_tier(self.world.trips.values()))
            self.assertGreaterEqual(distance, options.minimum_distance)
            if distance <= options.maximum_distance:
                number_available_trips += 1
        self.assertGreater(number_available_trips, 0)

    def test_not_all_trips_are_below_max_with_no_reductions(self):
        options = self.world.options
        number_available_trips = 0
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            distance = get_current_distance(trip, 0, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                            get_max_distance_tier(self.world.trips.values()))
            self.assertGreaterEqual(distance, options.minimum_distance)
            if distance <= options.maximum_distance:
                number_available_trips += 1
        self.assertLess(number_available_trips, len(self.world.trips))

    def test_all_trips_are_between_min_and_max_with_all_reductions(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, self.world.number_distance_reductions, options.minimum_distance, options.maximum_distance,
                                                self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                self.assertGreaterEqual(distance, options.minimum_distance)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, self.world.number_distance_reductions * 2, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.minimum_distance, options.maximum_distance,
                                                           self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    distance_after = get_current_distance(trip, i + 1, options.minimum_distance, options.maximum_distance,
                                                          self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    self.assertGreater(distance_before, distance_after)
                    self.assertGreaterEqual(distance_after, options.minimum_distance)


class TestManyTripsWithDistanceReductions(APGOTestBase):
    options = {Options.NumberOfChecks.internal_name: MANY_TRIPS,
               Options.EnableDistanceReductions.internal_name: True}

    def test_at_least_one_reduction_exists(self):
        self.assertGreater(self.world.number_distance_reductions, 0)

    def test_some_trips_are_below_max_with_no_reductions(self):
        options = self.world.options
        number_available_trips = 0
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            distance = get_current_distance(trip, 0, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                            get_max_distance_tier(self.world.trips.values()))
            self.assertGreaterEqual(distance, options.minimum_distance)
            if distance <= options.maximum_distance:
                number_available_trips += 1
        self.assertGreater(number_available_trips, 0)

    def test_not_all_trips_are_below_max_with_no_reductions(self):
        options = self.world.options
        number_available_trips = 0
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            distance = get_current_distance(trip, 0, options.minimum_distance, options.maximum_distance, self.world.number_distance_reductions,
                                            get_max_distance_tier(self.world.trips.values()))
            self.assertGreaterEqual(distance, options.minimum_distance)
            if distance <= options.maximum_distance:
                number_available_trips += 1
        self.assertLess(number_available_trips, len(self.world.trips))

    def test_all_trips_are_between_min_and_max_with_all_reductions(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            with self.subTest(f"location: {location}"):
                trip = self.world.trips[location.name]
                distance = get_current_distance(trip, self.world.number_distance_reductions, options.minimum_distance, options.maximum_distance,
                                                self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                self.assertGreaterEqual(distance, options.minimum_distance)
                self.assertLessEqual(distance, options.maximum_distance)

    def test_all_distance_reductions_do_something(self):
        options = self.world.options
        for location in self.multiworld.get_locations(self.player):
            trip = self.world.trips[location.name]
            for i in range(0, self.world.number_distance_reductions * 2, 5):
                with self.subTest(f"Location: {location}, Distance Reduction: {i}"):
                    distance_before = get_current_distance(trip, i, options.minimum_distance, options.maximum_distance,
                                                           self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    distance_after = get_current_distance(trip, i + 1, options.minimum_distance, options.maximum_distance,
                                                          self.world.number_distance_reductions, get_max_distance_tier(self.world.trips.values()))
                    self.assertGreater(distance_before, distance_after)
                    self.assertGreaterEqual(distance_after, options.minimum_distance)


class TestKeysRequiredFitDistanceAlgorithm(TestCase):

    def test_correct_number_of_reductions_needed(self):
        for desired_trips in range(5, 105, 20):
            for min_distance in range(1000, 5000, 1000):
                for max_distance in range(min_distance, 10000, 1000):
                    options = {Options.NumberOfChecks.internal_name: desired_trips,
                               Options.NumberOfLocks.internal_name: 0,
                               Options.SpeedRequirement.internal_name: 0,
                               Options.MinimumDistance: min_distance,
                               Options.MaximumDistance: max_distance,
                               Options.EnableDistanceReductions: True}
                    trips = generate_trips(options, create_random())
                    max_distance_tier = get_max_distance_tier(trips)
                    for trip in trips:
                        for number_distance_reductions in range(1, max(2, desired_trips // 4), max(1, desired_trips // 8)):
                            with self.subTest(f"Trips: {desired_trips}, Distances: [{min_distance},{max_distance}], Trip: {trip}, Reductions: {number_distance_reductions}"):
                                reductions_needed = get_reductions_needed_to_be_reachable(trip, min_distance, max_distance, number_distance_reductions,
                                                                                          max_distance_tier)
                                distance_with_reductions = get_current_distance(trip, reductions_needed, min_distance, max_distance, number_distance_reductions,
                                                                                max_distance_tier)
                                self.assertLessEqual(distance_with_reductions, max_distance)
                                if reductions_needed == 0:
                                    continue

                                distance_without_reductions = get_current_distance(trip, reductions_needed - 1, min_distance, max_distance,
                                                                                   number_distance_reductions,
                                                                                   max_distance_tier)
                                self.assertGreater(distance_without_reductions, max_distance)
