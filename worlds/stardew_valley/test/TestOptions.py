import itertools
from typing import ClassVar

from BaseClasses import ItemClassification
from test.param import classvar_matrix
from .assertion import WorldAssertMixin
from .bases import SVTestCase, SVTestBase, solo_multiworld
from .options.option_names import all_option_choices
from .options.presets import allsanity_no_mods_6_x_x, allsanity_mods_6_x_x
from .. import items_by_group, Group
from ..locations import locations_by_tag, LocationTags, location_table
from ..options import ExcludeGingerIsland, ToolProgression, Goal, SeasonRandomization, TrapDifficulty, SpecialOrderLocations, ArcadeMachineLocations
from ..strings.goal_names import Goal as GoalName
from ..strings.season_names import Season
from ..strings.special_order_names import SpecialOrder
from ..strings.tool_names import ToolMaterial, Tool, APTool

SEASONS = {Season.spring, Season.summer, Season.fall, Season.winter}
TOOLS = {"Hoe", "Pickaxe", "Axe", "Watering Can", "Trash Can", "Fishing Rod"}


@classvar_matrix(option_and_choice=all_option_choices)
class TestGenerateDynamicOptions(WorldAssertMixin, SVTestCase):
    option_and_choice: ClassVar[tuple[str, str]]

    def test_given_option_and_choice_when_generate_then_basic_checks(self):
        option, choice = self.option_and_choice
        world_options = {option: choice}
        with solo_multiworld(world_options) as (multiworld, stardew_world):
            self.assert_basic_checks(multiworld)


@classvar_matrix(goal_and_location=[
    ("community_center", GoalName.community_center),
    ("grandpa_evaluation", GoalName.grandpa_evaluation),
    ("bottom_of_the_mines", GoalName.bottom_of_the_mines),
    ("cryptic_note", GoalName.cryptic_note),
    ("master_angler", GoalName.master_angler),
    ("complete_collection", GoalName.complete_museum),
    ("full_house", GoalName.full_house),
    ("perfection", GoalName.perfection),
])
class TestGoal(SVTestCase):
    goal_and_location: ClassVar[tuple[str, str]]

    def test_given_goal_when_generate_then_victory_is_in_correct_location(self):
        goal, location = self.goal_and_location
        world_options = {Goal.internal_name: goal}
        with solo_multiworld(world_options) as (multi_world, _):
            victory = multi_world.find_item("Victory", 1)
            self.assertEqual(victory.name, location)


class TestSeasonRandomization(SVTestCase):
    def test_given_disabled_when_generate_then_all_seasons_are_precollected(self):
        world_options = {SeasonRandomization.internal_name: SeasonRandomization.option_disabled}
        with solo_multiworld(world_options) as (multi_world, _):
            precollected_items = {item.name for item in multi_world.precollected_items[1]}
            self.assertTrue(all([season in precollected_items for season in SEASONS]))

    def test_given_randomized_when_generate_then_all_seasons_are_in_the_pool_or_precollected(self):
        world_options = {SeasonRandomization.internal_name: SeasonRandomization.option_randomized}
        with solo_multiworld(world_options) as (multi_world, _):
            precollected_items = {item.name for item in multi_world.precollected_items[1]}
            items = {item.name for item in multi_world.get_items()} | precollected_items
            self.assertTrue(all([season in items for season in SEASONS]))
            self.assertEqual(len(SEASONS.intersection(precollected_items)), 1)

    def test_given_progressive_when_generate_then_3_progressive_seasons_are_in_the_pool(self):
        world_options = {SeasonRandomization.internal_name: SeasonRandomization.option_progressive}
        with solo_multiworld(world_options) as (multi_world, _):
            items = [item.name for item in multi_world.get_items()]
            self.assertEqual(items.count(Season.progressive), 3)


class TestToolProgression(SVTestBase):
    options = {
        ToolProgression.internal_name: ToolProgression.option_progressive,
    }

    def test_given_progressive_when_generate_then_tool_upgrades_are_locations(self):
        locations = set(self.get_real_location_names())
        for material, tool in itertools.product(ToolMaterial.tiers.values(),
                                                [Tool.hoe, Tool.pickaxe, Tool.axe, Tool.watering_can, Tool.trash_can]):
            if material == ToolMaterial.basic:
                continue
            self.assertIn(f"{material} {tool} Upgrade", locations)
        self.assertIn("Purchase Training Rod", locations)
        self.assertIn("Bamboo Pole Cutscene", locations)
        self.assertIn("Purchase Fiberglass Rod", locations)
        self.assertIn("Purchase Iridium Rod", locations)

    def test_given_progressive_when_generate_then_only_3_trash_can_are_progressive(self):
        trash_cans = self.get_items_by_name(APTool.trash_can)
        progressive_count = sum([1 for item in trash_cans if item.classification == ItemClassification.progression])
        useful_count = sum([1 for item in trash_cans if item.classification == ItemClassification.useful])

        self.assertEqual(progressive_count, 3)
        self.assertEqual(useful_count, 1)


@classvar_matrix(option_and_choice=all_option_choices)
class TestGenerateAllOptionsWithExcludeGingerIsland(WorldAssertMixin, SVTestCase):
    option_and_choice: ClassVar[tuple[str, str]]

    def test_given_choice_when_generate_exclude_ginger_island_then_ginger_island_is_properly_excluded(self):
        option, option_choice = self.option_and_choice

        if option == ExcludeGingerIsland.internal_name:
            self.skipTest("ExcludeGingerIsland is forced to true")

        world_options = {
            ExcludeGingerIsland.internal_name: ExcludeGingerIsland.option_true,
            option: option_choice
        }

        with solo_multiworld(world_options) as (multiworld, stardew_world):

            if stardew_world.options.exclude_ginger_island != ExcludeGingerIsland.option_true:
                self.skipTest("Some options, like goals, will force Ginger island back in the game. We want to skip testing those.")

            self.assert_basic_checks(multiworld)
            self.assert_no_ginger_island_content(multiworld)


class TestTraps(SVTestCase):
    def test_given_no_traps_when_generate_then_no_trap_in_pool(self):
        world_options = allsanity_no_mods_6_x_x().copy()
        world_options[TrapDifficulty.internal_name] = TrapDifficulty.option_no_traps
        with solo_multiworld(world_options) as (multi_world, _):
            trap_items = [item_data.name for item_data in items_by_group[Group.TRAP]]
            multiworld_items = [item.name for item in multi_world.get_items()]

            for item in trap_items:
                with self.subTest(f"{item}"):
                    self.assertNotIn(item, multiworld_items)

    def test_given_traps_when_generate_then_all_traps_in_pool(self):
        trap_option = TrapDifficulty
        for value in trap_option.options:
            if value == "no_traps":
                continue
            world_options = allsanity_mods_6_x_x()
            world_options.update({TrapDifficulty.internal_name: trap_option.options[value]})
            with solo_multiworld(world_options) as (multi_world, _):
                trap_items = [item_data.name for item_data in items_by_group[Group.TRAP] if
                              Group.DEPRECATED not in item_data.groups and item_data.mod_name is None]
                multiworld_items = [item.name for item in multi_world.get_items()]
                for item in trap_items:
                    with self.subTest(f"Option: {value}, Item: {item}"):
                        self.assertIn(item, multiworld_items)


class TestSpecialOrders(SVTestCase):
    def test_given_disabled_then_no_order_in_pool(self):
        world_options = {SpecialOrderLocations.internal_name: SpecialOrderLocations.option_vanilla}
        with solo_multiworld(world_options) as (multi_world, _):
            locations_in_pool = {location.name for location in multi_world.get_locations() if location.name in location_table}
            for location_name in locations_in_pool:
                location = location_table[location_name]
                self.assertNotIn(LocationTags.SPECIAL_ORDER_BOARD, location.tags)
                self.assertNotIn(LocationTags.SPECIAL_ORDER_QI, location.tags)

    def test_given_board_only_then_no_qi_order_in_pool(self):
        world_options = {SpecialOrderLocations.internal_name: SpecialOrderLocations.option_board}
        with solo_multiworld(world_options) as (multi_world, _):

            locations_in_pool = {location.name for location in multi_world.get_locations() if location.name in location_table}
            for location_name in locations_in_pool:
                location = location_table[location_name]
                self.assertNotIn(LocationTags.SPECIAL_ORDER_QI, location.tags)

            for board_location in locations_by_tag[LocationTags.SPECIAL_ORDER_BOARD]:
                if board_location.mod_name:
                    continue
                self.assertIn(board_location.name, locations_in_pool)

    def test_given_board_and_qi_then_all_orders_in_pool(self):
        world_options = {SpecialOrderLocations.internal_name: SpecialOrderLocations.option_board_qi,
                         ArcadeMachineLocations.internal_name: ArcadeMachineLocations.option_victories,
                         ExcludeGingerIsland.internal_name: ExcludeGingerIsland.option_false}
        with solo_multiworld(world_options) as (multi_world, _):

            locations_in_pool = {location.name for location in multi_world.get_locations()}
            for qi_location in locations_by_tag[LocationTags.SPECIAL_ORDER_QI]:
                if qi_location.mod_name:
                    continue
                self.assertIn(qi_location.name, locations_in_pool)

            for board_location in locations_by_tag[LocationTags.SPECIAL_ORDER_BOARD]:
                if board_location.mod_name:
                    continue
                self.assertIn(board_location.name, locations_in_pool)

    def test_given_board_and_qi_without_arcade_machines_then_lets_play_a_game_not_in_pool(self):
        world_options = {SpecialOrderLocations.internal_name: SpecialOrderLocations.option_board_qi,
                         ArcadeMachineLocations.internal_name: ArcadeMachineLocations.option_disabled,
                         ExcludeGingerIsland.internal_name: ExcludeGingerIsland.option_false}
        with solo_multiworld(world_options) as (multi_world, _):
            locations_in_pool = {location.name for location in multi_world.get_locations()}
            self.assertNotIn(SpecialOrder.lets_play_a_game, locations_in_pool)
