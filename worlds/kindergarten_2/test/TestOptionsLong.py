import random
from typing import Dict

from BaseClasses import MultiWorld, get_seed
from Options import NamedRange, Range
from . import Kindergarten2TestBase, setup_kindergarten_solo_multiworld_with_fill
from .option_names import options_to_include
from .checks.world_checks import assert_can_win, assert_same_number_items_locations


def basic_checks(tester: Kindergarten2TestBase, multiworld: MultiWorld):
    assert_can_win(tester, multiworld)
    assert_same_number_items_locations(tester, multiworld)


def get_option_choices(option) -> Dict[str, int]:
    if issubclass(option, NamedRange):
        return option.special_range_names
    if issubclass(option, Range):
        return {f"{val}": val for val in range(option.range_start, option.range_end + 1)}
    elif option.options:
        return option.options
    return {}


class TestGenerateDynamicOptions(Kindergarten2TestBase):
    def test_given_option_pair_when_generate_then_basic_checks(self):
        num_options = len(options_to_include)
        for option1_index in range(0, num_options):
            for option2_index in range(option1_index + 1, num_options):
                option1 = options_to_include[option1_index]
                option2 = options_to_include[option2_index]
                option1_choices = get_option_choices(option1)
                option2_choices = get_option_choices(option2)
                for key1 in option1_choices:
                    for key2 in option2_choices:
                        with self.subTest(f"{option1.internal_name}: {key1}, {option2.internal_name}: {key2}"):
                            choices = {option1.internal_name: option1_choices[key1],
                                       option2.internal_name: option2_choices[key2]}
                            multiworld = setup_kindergarten_solo_multiworld_with_fill(choices)
                            basic_checks(self, multiworld)

    def test_given_option_truple_when_generate_then_basic_checks(self):
        num_options = len(options_to_include)
        for option1_index in range(0, num_options):
            for option2_index in range(option1_index + 1, num_options):
                for option3_index in range(option2_index + 1, num_options):
                    option1 = options_to_include[option1_index]
                    option2 = options_to_include[option2_index]
                    option3 = options_to_include[option3_index]
                    option1_choices = get_option_choices(option1)
                    option2_choices = get_option_choices(option2)
                    option3_choices = get_option_choices(option3)
                    for key1 in option1_choices:
                        for key2 in option2_choices:
                            for key3 in option3_choices:
                                with self.subTest(f"{option1.internal_name}: {key1}, {option2.internal_name}: {key2}, {option3.internal_name}: {key3}"):
                                    choices = {option1.internal_name: option1_choices[key1],
                                               option2.internal_name: option2_choices[key2],
                                               option3.internal_name: option3_choices[key3]}
                                    multiworld = setup_kindergarten_solo_multiworld_with_fill(choices)
                                    basic_checks(self, multiworld)

    def test_given_option_quartet_when_generate_then_basic_checks(self):
        num_options = len(options_to_include)
        for option1_index in range(0, num_options):
            for option2_index in range(option1_index + 1, num_options):
                for option3_index in range(option2_index + 1, num_options):
                    for option4_index in range(option3_index + 1, num_options):
                        option1 = options_to_include[option1_index]
                        option2 = options_to_include[option2_index]
                        option3 = options_to_include[option3_index]
                        option4 = options_to_include[option4_index]
                        option1_choices = get_option_choices(option1)
                        option2_choices = get_option_choices(option2)
                        option3_choices = get_option_choices(option3)
                        option4_choices = get_option_choices(option4)
                        for key1 in option1_choices:
                            for key2 in option2_choices:
                                for key3 in option3_choices:
                                    for key4 in option4_choices:
                                        with self.subTest(
                                                f"{option1.internal_name}: {key1}, {option2.internal_name}: {key2}, {option3.internal_name}: {key3}, {option4.internal_name}: {key4}"):
                                            choices = {option1.internal_name: option1_choices[key1],
                                                       option2.internal_name: option2_choices[key2],
                                                       option3.internal_name: option3_choices[key3],
                                                       option4.internal_name: option4_choices[key4]}
                                            multiworld = setup_kindergarten_solo_multiworld_with_fill(choices)
                                            basic_checks(self, multiworld)


def generate_random_world_options(seed: int) -> Dict[str, int]:
    num_options = len(options_to_include)
    world_options = dict()
    rng = random.Random(seed)
    for option_index in range(0, num_options):
        option = options_to_include[option_index]
        option_choices = get_option_choices(option)
        if not option_choices:
            continue
        chosen_option_value = rng.choice(list(option_choices.values()))
        world_options[option.internal_name] = chosen_option_value
    return world_options


def get_number_log_steps(number_worlds: int) -> int:
    if number_worlds <= 10:
        return 2
    if number_worlds <= 100:
        return 5
    if number_worlds <= 500:
        return 10
    if number_worlds <= 1000:
        return 20
    if number_worlds <= 5000:
        return 25
    if number_worlds <= 10000:
        return 50
    return 100


class TestGenerateManyWorlds(Kindergarten2TestBase):
    def test_generate_many_worlds_without_fill_then_check_results(self):
        number_worlds = 1000
        seed = get_seed()
        self.generate_and_check_many_worlds(number_worlds, seed, fill=False)

    def test_generate_many_worlds_with_fill_then_check_results(self):
        number_worlds = 200
        seed = get_seed()
        self.generate_and_check_many_worlds(number_worlds, seed, fill=True)

    def generate_and_check_many_worlds(self, number_worlds: int, seed: int, fill: bool = False):
        num_steps = get_number_log_steps(number_worlds)
        log_step = number_worlds / num_steps

        fill_message = "with Fill" if fill else "without Fill"

        print(f"Generating {number_worlds} Solo Multiworlds {fill_message} [Start Seed: {seed}] for Kindergarten 2...")
        for world_number in range(0, number_worlds + 1):

            world_seed = world_number + seed
            world_options = generate_random_world_options(world_seed)

            with self.subTest(f"Multiworld: {world_seed}"):
                multiworld = setup_kindergarten_solo_multiworld_with_fill(world_options, seed=seed, fill=fill)
                basic_checks(self, multiworld)

            if world_number > 0 and world_number % log_step == 0:
                print(f"Generated and Verified {world_number}/{number_worlds} worlds {fill_message} [{(world_number * 100) // number_worlds}%]")

        print(f"Finished generating and verifying {number_worlds} Solo Multiworlds {fill_message} for Kindergarten 2")
