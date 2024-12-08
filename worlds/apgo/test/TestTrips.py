from random import Random, random
from unittest import TestCase

from . import APGOTestBase
from .. import Options
from ..Trips import generate_trips, Trip


def create_seed() -> int:
    return int(random() * pow(10, 18) - 1)


def create_random(seed: int = 0) -> Random:
    if seed == 0:
        seed = create_seed()
    return Random(seed)


step = 5


class TestGenerateTrips(TestCase):

    def test_generates_only_distance_trips(self):
        for desired_trips in range(step, 101, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 0,
                           Options.SpeedRequirement.internal_name: 0}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                for trip in trips:
                    self.assertGreater(trip.template.distance_tier, 0)
                    self.assertEqual(trip.template.speed_tier, 0)
                    self.assertEqual(trip.template.key_needed, 0)

    def test_generates_distance_speed_trips(self):
        for desired_trips in range(step, 101, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 0,
                           Options.SpeedRequirement.internal_name: 5}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                no_speed_trips = 0
                for trip in trips:
                    self.assertGreater(trip.template.distance_tier, 0)
                    self.assertGreater(trip.template.speed_tier, 0)
                    self.assertEqual(trip.template.key_needed, 0)

    def test_generates_distance_keys_trips(self):
        for desired_trips in range(step, 105, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 2,
                           Options.SpeedRequirement.internal_name: 0}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                at_least_one_tiers = set()
                highest_key_tier = 0
                for trip in trips:
                    self.assertGreater(trip.template.distance_tier, 0)
                    self.assertEqual(trip.template.speed_tier, 0)
                    highest_key_tier = max(highest_key_tier, trip.template.key_needed)
                    if trip.template.key_needed not in at_least_one_tiers:
                        at_least_one_tiers.add(trip.template.key_needed)
                for i in range(highest_key_tier + 1):
                    self.assertIn(i, at_least_one_tiers)

    def test_never_generates_too_many_of_one_type_without_keys_without_speed(self):
        for desired_trips in range(step, 101, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 0,
                           Options.SpeedRequirement.internal_name: 0}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                for trip in trips:
                    number = trip.get_number()
                    self.assertLessEqual(number, trip.template.get_max_number_of_this_trip())

    def test_never_generates_too_many_of_one_type_without_keys_with_speed(self):
        for desired_trips in range(step, 201, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 0,
                           Options.SpeedRequirement.internal_name: 5}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                for trip in trips:
                    number = trip.get_number()
                    self.assertLessEqual(number, trip.template.get_max_number_of_this_trip())

    def test_never_generates_too_many_of_one_type_with_keys_without_speed(self):
        for desired_trips in range(step, 201, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 10,
                           Options.SpeedRequirement.internal_name: 0}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                for trip in trips:
                    number = trip.get_number()
                    self.assertLessEqual(number, trip.template.get_max_number_of_this_trip())

    def test_never_generates_too_many_of_one_type_with_keys_with_speed(self):
        for desired_trips in range(step, 1001, step):
            with self.subTest(f"{desired_trips} trips"):
                options = {Options.NumberOfTrips.internal_name: desired_trips,
                           Options.NumberOfLocks.internal_name: 10,
                           Options.SpeedRequirement.internal_name: 5}
                trips = generate_trips(options, create_random())
                total_trips = len(trips)
                self.assertEqual(total_trips, desired_trips)
                for trip in trips:
                    number = trip.get_number()
                    self.assertLessEqual(number, trip.template.get_max_number_of_this_trip())
