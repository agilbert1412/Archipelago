from . import Kindergarten2TestBase
from .. import options, Money
from ..constants.inventory_item_names import InventoryItem
from ..constants.monstermon_card_names import all_cards, MonstermonCard


class TestAccessibilityRules(Kindergarten2TestBase):
    options = {options.Goal.internal_name: options.Goal.option_creature_feature,
               options.ShuffleMonstermon.internal_name: options.ShuffleMonstermon.option_true,
               options.ShuffleMoney.internal_name: 1}

    def test_mystical_tomato(self):
        self.assertFalse(self.multiworld.state.can_reach_location(MonstermonCard.mystical_tomato, self.player))

        money = self.get_item_by_name(Money.starting_money)
        self.collect(money)
        self.collect(money)

        pin = self.get_item_by_name(InventoryItem.prestigious_pin)
        toolbelt = self.get_item_by_name(InventoryItem.bob_toolbelt)
        self.collect(pin)
        self.collect(toolbelt)

        self.assertFalse(self.multiworld.state.can_reach_location(MonstermonCard.mystical_tomato, self.player))
        self.collect(money)
        self.assertTrue(self.multiworld.state.can_reach_location(MonstermonCard.mystical_tomato, self.player))

    def test_pale_tuna(self):
        self.assertFalse(self.multiworld.state.can_reach_location(MonstermonCard.pale_tuna, self.player))

        money = self.get_item_by_name(Money.starting_money)
        self.collect(money)
        self.collect(money)
        self.collect(money)
        self.assertFalse(self.multiworld.state.can_reach_location(MonstermonCard.pale_tuna, self.player))

        pin = self.get_item_by_name(InventoryItem.prestigious_pin)
        toolbelt = self.get_item_by_name(InventoryItem.bob_toolbelt)
        self.collect(pin)
        self.collect(toolbelt)
        self.assertTrue(self.multiworld.state.can_reach_location(MonstermonCard.pale_tuna, self.player))
