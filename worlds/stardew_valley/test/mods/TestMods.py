from .mod_testing_decorators import must_test_all_mods, is_testing_mod
from .. import SVTestBase, SVTestCase, solo_multiworld
from ..TestGeneration import get_all_permanent_progression_items
from ..assertion import ModAssertMixin, WorldAssertMixin
from ..options import presets
from ..options.presets import allsanity_mods_6_x_x
from ... import options
from ...items import Group
from ...mods.mod_data import ModNames


class TestCanGenerateAllsanityWithMods(WorldAssertMixin, ModAssertMixin, SVTestCase):

    def test_allsanity_all_mods_when_generate_then_basic_checks(self):
        with solo_multiworld(allsanity_mods_6_x_x()) as (multi_world, _):
            self.assert_basic_checks(multi_world)

    def test_allsanity_all_mods_exclude_island_when_generate_then_basic_checks(self):
        world_options = allsanity_mods_6_x_x()
        world_options.update({options.ExcludeGingerIsland.internal_name: options.ExcludeGingerIsland.option_true})
        with solo_multiworld(world_options) as (multi_world, _):
            self.assert_basic_checks(multi_world)


@must_test_all_mods
class TestCanGenerateWithEachMod(WorldAssertMixin, ModAssertMixin, SVTestCase):

    @is_testing_mod(ModNames.deepwoods)
    def test_given_deepwoods_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.deepwoods)

    @is_testing_mod(ModNames.tractor)
    def test_given_tractor_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.tractor)

    @is_testing_mod(ModNames.big_backpack)
    def test_given_big_backpack_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.big_backpack)

    @is_testing_mod(ModNames.luck_skill)
    def test_given_luck_skill_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.luck_skill)

    @is_testing_mod(ModNames.magic)
    def test_given_magic_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.magic)

    @is_testing_mod(ModNames.socializing_skill)
    def test_given_socializing_skill_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.socializing_skill)

    @is_testing_mod(ModNames.archaeology)
    def test_given_archaeology_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.archaeology)

    @is_testing_mod(ModNames.cooking_skill)
    def test_given_cooking_skill_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.cooking_skill)

    @is_testing_mod(ModNames.binning_skill)
    def test_given_binning_skill_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.binning_skill)

    @is_testing_mod(ModNames.juna)
    def test_given_juna_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.juna)

    @is_testing_mod(ModNames.jasper)
    def test_given_jasper_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.jasper)

    @is_testing_mod(ModNames.alec)
    def test_given_alec_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.alec)

    @is_testing_mod(ModNames.yoba)
    def test_given_yoba_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.yoba)

    @is_testing_mod(ModNames.eugene)
    def test_given_eugene_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.eugene)

    @is_testing_mod(ModNames.wellwick)
    def test_given_wellwick_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.wellwick)

    @is_testing_mod(ModNames.ginger)
    def test_given_ginger_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.ginger)

    @is_testing_mod(ModNames.shiko)
    def test_given_shiko_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.shiko)

    @is_testing_mod(ModNames.delores)
    def test_given_delores_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.delores)

    @is_testing_mod(ModNames.ayeisha)
    def test_given_ayeisha_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.ayeisha)

    @is_testing_mod(ModNames.riley)
    def test_given_riley_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.riley)

    @is_testing_mod(ModNames.skull_cavern_elevator)
    def test_given_skull_cavern_elevator_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.skull_cavern_elevator)

    @is_testing_mod(ModNames.sve)
    def test_given_sve_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.sve)

    @is_testing_mod(ModNames.alecto)
    def test_given_alecto_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.alecto)

    @is_testing_mod(ModNames.distant_lands)
    def test_given_distant_lands_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.distant_lands)

    @is_testing_mod(ModNames.lacey)
    def test_given_lacey_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.lacey)

    @is_testing_mod(ModNames.boarding_house)
    def test_given_boarding_house_when_generate_with_all_vanilla_content_then_basic_checks(self):
        self.perform_basic_checks_on_mod_with_all_vanilla_content(ModNames.boarding_house)

    def perform_basic_checks_on_mod_with_all_vanilla_content(self, mod: str):
        world_options = {options.Mods: mod, options.ExcludeGingerIsland: options.ExcludeGingerIsland.option_false}
        with solo_multiworld(world_options) as (multi_world, _):
            self.assert_basic_checks(multi_world)
            self.assert_stray_mod_items(mod, multi_world)


class TestBaseLocationDependencies(SVTestBase):
    options = {
        options.Mods.internal_name: frozenset(options.Mods.valid_keys),
        options.ToolProgression.internal_name: options.ToolProgression.option_progressive,
        options.SeasonRandomization.internal_name: options.SeasonRandomization.option_randomized
    }


class TestBaseItemGeneration(SVTestBase):
    options = {
        options.SeasonRandomization.internal_name: options.SeasonRandomization.option_progressive,
        options.SkillProgression.internal_name: options.SkillProgression.option_progressive_with_masteries,
        options.ExcludeGingerIsland.internal_name: options.ExcludeGingerIsland.option_false,
        options.SpecialOrderLocations.internal_name: options.SpecialOrderLocations.option_board_qi,
        options.Friendsanity.internal_name: options.Friendsanity.option_all_with_marriage,
        options.Shipsanity.internal_name: options.Shipsanity.option_everything,
        options.Chefsanity.internal_name: options.Chefsanity.option_all,
        options.Craftsanity.internal_name: options.Craftsanity.option_all,
        options.Booksanity.internal_name: options.Booksanity.option_all,
        options.Walnutsanity.internal_name: options.Walnutsanity.preset_all,
        options.Secretsanity.internal_name: options.Secretsanity.preset_all,
        options.Mods.internal_name: frozenset(options.Mods.valid_keys)
    }

    def test_all_progression_items_are_added_to_the_pool(self):
        all_created_items = self.get_all_created_items()
        progression_items = get_all_permanent_progression_items()
        for progression_item in progression_items:
            with self.subTest(f"{progression_item.name}"):
                self.assertIn(progression_item.name, all_created_items)


class TestNoGingerIslandModItemGeneration(SVTestBase):
    options = {
        options.SeasonRandomization.internal_name: options.SeasonRandomization.option_progressive,
        options.SkillProgression.internal_name: options.SkillProgression.option_progressive_with_masteries,
        options.Friendsanity.internal_name: options.Friendsanity.option_all_with_marriage,
        options.Shipsanity.internal_name: options.Shipsanity.option_everything,
        options.Chefsanity.internal_name: options.Chefsanity.option_all,
        options.Craftsanity.internal_name: options.Craftsanity.option_all,
        options.Booksanity.internal_name: options.Booksanity.option_all,
        options.Secretsanity.internal_name: options.Secretsanity.preset_all,
        options.ExcludeGingerIsland.internal_name: options.ExcludeGingerIsland.option_true,
        options.Mods.internal_name: frozenset(options.Mods.valid_keys)
    }

    def test_all_progression_items_except_island_are_added_to_the_pool(self):
        all_created_items = self.get_all_created_items()
        progression_items = get_all_permanent_progression_items()
        for progression_item in progression_items:
            with self.subTest(f"{progression_item.name}"):
                if Group.GINGER_ISLAND in progression_item.groups:
                    self.assertNotIn(progression_item.name, all_created_items)
                else:
                    self.assertIn(progression_item.name, all_created_items)


class TestVanillaLogicAlternativeWhenQuestsAreNotRandomized(WorldAssertMixin, SVTestBase):
    """We often forget to add an alternative rule that works when quests are not randomized. When this happens, some
    Location are not reachable because they depend on items that are only added to the pool when quests are randomized.
    """
    options = presets.allsanity_mods_6_x_x() | {
        options.QuestLocations.internal_name: options.QuestLocations.special_range_names["none"],
        options.Goal.internal_name: options.Goal.option_perfection,
    }

    def test_given_no_quest_all_mods_when_generate_then_can_reach_everything(self):
        self.collect_everything()
        self.assert_can_reach_everything(self.multiworld)
