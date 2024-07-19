blue_cards = []
red_cards = []
green_cards = []
yellow_cards = []
purple_cards = []


def blue(card_name: str) -> str:
    blue_cards.append(card_name)
    return card_name


def red(card_name: str) -> str:
    red_cards.append(card_name)
    return card_name


def green(card_name: str) -> str:
    green_cards.append(card_name)
    return card_name


def yellow(card_name: str) -> str:
    yellow_cards.append(card_name)
    return card_name


def purple(card_name: str) -> str:
    purple_cards.append(card_name)
    return card_name


class MonstermonCard:
    celestial_slug = blue("Celestial Slug")
    hard_boogar = blue("Hard Boogar")
    bucket_o_water = blue("Bucket O Water")
    pale_tuna = blue("Pale Tuna")
    ultralodon = blue("Ultralodon")
    carnivorous_nimbus = blue("Carnivorous Nimbus")
    tiny_squid = blue("Tiny Squid")
    coral_that_looks_like_hand = blue("Coral That Looks Like Hand")
    hermit_frog = blue("Hermit Frog")
    castle_of_sand = blue("Castle Of Sand")

    man_on_fire = red("Man On Fire")
    chair_of_spikes = red("Chair of Spikes")
    cigaretmon = red("Cigaretmon")
    dune_worm = red("Dune Worm")
    stressed_llama = red("Stressed Llama")
    cyclops_duckling = red("Cyclops Duckling")
    teenage_mutant_zombie = red("Teenage Mutant Zombie")
    lonely_dragon = red("Lonely Dragon")
    million_head_hydra = red("Million-Head Hydra")
    dab_hero = red("Dab Hero")

    monstrous_flytrap = green("Monstrous Flytrap")
    the_tallest_tree = green("The Tallest Tree")
    chill_stump = green("Chill Stump")
    gnome_of_garden = green("Gnome of Garden")
    ofaka_tornado = green("Ofaka Tornado")
    literally_grass = green("Literally Grass")
    doodoo_bug = green("Doodoo Bug")
    mystical_tomato = green("Mystical Tomato")
    hissing_fauna = green("Hissing Fauna")
    legendary_sword = green("Legendary Sword")

    golden_dewdrop = yellow("Golden Dewdrop")
    zen_octopus = yellow("Zen Octopus")
    forbidden_book = yellow("Forbidden Book")
    marshmallow = yellow("Marshmallow")
    pot_of_grease = yellow("Pot of Grease")
    lamb_with_cleaver = yellow("Lamb With Cleaver")
    treasure_chest = yellow("Treasure Chest")
    mr_nice_guy = yellow("Mr. Nice Guy")
    the_slurper = yellow("The Slurper")
    rare_jewel = yellow("Rare Jewel")

    onion = purple("Onion")
    killer_eye = purple("Killer Eye")
    purple_plush = purple("Purple Plush")
    spiky_flim_flam = purple("Spiky Flim Flam")
    monster_ghost = purple("Monster Ghost")
    knight_who_turned_evil = purple("Knight Who Turned Evil")
    evil_thwarter = purple("Evil Thwarter")
    mysterious_package = purple("Mysterious Package")
    oglebop_ogre = purple("Oglebop Ogre")
    dank_magician = purple("Dank Magician")
