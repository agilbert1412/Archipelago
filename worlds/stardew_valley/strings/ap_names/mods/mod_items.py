from typing import List


class SVEQuestItem:
    aurora_vineyard_tablet = "Aurora Vineyard Tablet"
    iridium_bomb = "Iridium Bomb"
    void_soul = "Krobus' Protection"
    kittyfish_spell = "Kittyfish Spell"
    scarlett_job_offer = "Scarlett's Job Offer"
    morgan_schooling = "Morgan's Schooling"
    diamond_wand = "Diamond Wand"
    marlon_boat_paddle = "Marlon's Boat Paddle"
    fable_reef_portal = "Fable Reef Portal"

    sve_quest_items: List[str] = [aurora_vineyard_tablet, iridium_bomb, void_soul, kittyfish_spell, scarlett_job_offer, morgan_schooling]
    sve_quest_items_ginger_island: List[str] = [diamond_wand, marlon_boat_paddle, fable_reef_portal]


class SVELocation:
    tempered_galaxy_sword = "Tempered Galaxy Sword"
    tempered_galaxy_hammer = "Tempered Galaxy Hammer"
    tempered_galaxy_dagger = "Tempered Galaxy Dagger"
    diamond_wand = "Lance's Diamond Wand"
    monster_crops = "Monster Crops"


class SVERunes:
    nexus_guild = "Nexus: Adventurer's Guild Runes"
    nexus_junimo_outpost = "Nexus: Junimo and Outpost Runes"
    nexus_aurora = "Nexus: Aurora Vineyard Runes"
    nexus_spring = "Nexus: Sprite Spring Runes"
    nexus_farm_wizard = "Nexus: Farm and Wizard Runes"

    nexus_items: List[str] = [nexus_farm_wizard, nexus_spring, nexus_aurora, nexus_guild, nexus_junimo_outpost]
