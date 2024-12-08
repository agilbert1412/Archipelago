from random import Random, random
from unittest import TestCase

from . import APGOTestBase, complete_options_with_default
from .. import Options, APGOOptions, APGOWorld
from ..Trips import generate_trips, Trip


def create_seed() -> int:
    return int(random() * pow(10, 18) - 1)


def create_random(seed: int = 0) -> Random:
    if seed == 0:
        seed = create_seed()
    return Random(seed)


step = 40


class TestGenerateTrips(TestCase):

    def test_not_enough_keys_reduces_trips(self):
        for desired_trips in range(1, 1001, step):
            for desired_keys in range(0, 11):
                with self.subTest(f"{desired_trips} trips | {desired_keys} keys"):
                    options = complete_options_with_default({Options.NumberOfTrips.internal_name: desired_trips,
                                             Options.NumberOfLocks.internal_name: desired_keys,
                                             Options.SpeedRequirement.internal_name: 0})
                    APGOWorld.force_change_options_if_incompatible(options, 1, "Tester")
                    trips = generate_trips(options.as_dict(*[option_name for option_name in APGOOptions.type_hints]), create_random())
                    total_trips = len(trips)
                    self.assertLessEqual(total_trips, 210 + (desired_keys * 100))

    def test_not_enough_trips_reduces_keys(self):
        for desired_trips in range(1, 1001, step):
            for desired_keys in range(0, 11):
                with self.subTest(f"{desired_trips} trips | {desired_keys} keys"):
                    options = complete_options_with_default({Options.NumberOfTrips.internal_name: desired_trips,
                                             Options.NumberOfLocks.internal_name: desired_keys,
                                             Options.SpeedRequirement.internal_name: 0})
                    APGOWorld.force_change_options_if_incompatible(options, 1, "Tester")
                    trips = generate_trips(options.as_dict(*[option_name for option_name in APGOOptions.type_hints]), create_random())
                    total_trips = len(trips)
                    for trip in trips:
                        self.assertLessEqual(trip.template.key_needed, total_trips / 2)
