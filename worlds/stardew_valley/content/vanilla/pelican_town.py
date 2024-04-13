from ..game_content import ContentPack
from ...data import villagers_data, fish_data
from ...data.game_item import PermanentSource
from ...data.harvest import ForagingSource, SeasonalForagingSource
from ...data.shop import ShopSource
from ...strings.book_names import Book
from ...strings.crop_names import Fruit
from ...strings.fish_names import WaterItem
from ...strings.forageable_names import Forageable, Mushroom
from ...strings.fruit_tree_names import Sapling
from ...strings.material_names import Material
from ...strings.metal_names import Mineral
from ...strings.region_names import Region
from ...strings.season_names import Season
from ...strings.seed_names import Seed, TreeSeed

pelican_town = ContentPack(
    "Pelican Town (Vanilla)",
    harvest_sources={
        # Spring
        Forageable.daffodil: (
            ForagingSource(seasons=(Season.spring,), regions=(Region.bus_stop, Region.town, Region.railroad)),
        ),
        Forageable.dandelion: (
            ForagingSource(seasons=(Season.spring,), regions=(Region.bus_stop, Region.forest, Region.railroad)),
        ),
        Forageable.leek: (
            ForagingSource(seasons=(Season.spring,), regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.railroad)),
        ),
        Forageable.wild_horseradish: (
            ForagingSource(seasons=(Season.spring,), regions=(Region.backwoods, Region.mountain, Region.forest, Region.secret_woods)),
        ),
        Forageable.salmonberry: (
            SeasonalForagingSource(season=Season.spring, days=(15, 16, 17, 18),
                                   regions=(Region.backwoods, Region.mountain, Region.town, Region.forest, Region.tunnel_entrance, Region.railroad)),
        ),
        Forageable.spring_onion: (
            ForagingSource(seasons=(Season.spring,), regions=(Region.forest,)),
        ),

        # Summer
        Fruit.grape: (
            ForagingSource(seasons=(Season.summer,), regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.railroad)),
        ),
        Forageable.spice_berry: (
            ForagingSource(seasons=(Season.summer,), regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.forest, Region.railroad)),
        ),
        Forageable.sweet_pea: (
            ForagingSource(seasons=(Season.summer,), regions=(Region.bus_stop, Region.town, Region.forest, Region.railroad)),
        ),
        Forageable.fiddlehead_fern: (
            ForagingSource(seasons=(Season.summer,), regions=(Region.secret_woods,)),
        ),

        # Fall
        Forageable.blackberry: (
            ForagingSource(seasons=(Season.fall,), regions=(Region.backwoods, Region.town, Region.forest, Region.railroad)),
            SeasonalForagingSource(season=Season.fall, days=(8, 9, 10, 11),
                                   regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.town, Region.forest, Region.tunnel_entrance,
                                            Region.railroad)),
        ),
        Forageable.hazelnut: (
            ForagingSource(seasons=(Season.fall,), regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.railroad)),
        ),
        Forageable.wild_plum: (
            ForagingSource(seasons=(Season.fall,), regions=(Region.mountain, Region.bus_stop, Region.railroad)),
        ),

        # Winter
        Forageable.crocus: (
            ForagingSource(seasons=(Season.winter,),
                           regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.town, Region.forest, Region.secret_woods)),
        ),
        Forageable.crystal_fruit: (
            ForagingSource(seasons=(Season.winter,),
                           regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.town, Region.forest, Region.railroad)),
        ),
        Forageable.holly: (
            ForagingSource(seasons=(Season.winter,),
                           regions=(Region.backwoods, Region.mountain, Region.bus_stop, Region.town, Region.forest, Region.railroad)),
        ),
        Forageable.snow_yam: (
            ForagingSource(seasons=(Season.winter,),
                           regions=(Region.farm, Region.backwoods, Region.mountain, Region.bus_stop, Region.town, Region.forest, Region.railroad,
                                    Region.secret_woods, Region.beach),
                           requires_hoe=True),
        ),
        Forageable.winter_root: (
            ForagingSource(seasons=(Season.winter,),
                           regions=(Region.farm, Region.backwoods, Region.mountain, Region.bus_stop, Region.town, Region.forest, Region.railroad,
                                    Region.secret_woods, Region.beach), requires_hoe=True),
        ),

        # Mushrooms
        Mushroom.common: (
            ForagingSource(seasons=(Season.spring,), regions=(Region.secret_woods,)),
            ForagingSource(seasons=(Season.fall,), regions=(Region.backwoods, Region.mountain, Region.forest)),
        ),
        Mushroom.chanterelle: (
            ForagingSource(seasons=(Season.fall,), regions=(Region.secret_woods,)),
        ),
        Mushroom.morel: (
            ForagingSource(seasons=(Season.spring, Season.fall), regions=(Region.secret_woods,)),
        ),
        Mushroom.red: (
            ForagingSource(seasons=(Season.summer, Season.fall), regions=(Region.secret_woods,)),
        ),

        # Beach
        WaterItem.coral: (
            ForagingSource(regions=(Region.tide_pools,)),
            SeasonalForagingSource(season=Season.summer, days=(12, 13, 14), regions=(Region.beach,)),
        ),
        WaterItem.nautilus_shell: (
            ForagingSource(seasons=(Season.winter,), regions=(Region.beach,)),
        ),
        Forageable.rainbow_shell: (
            ForagingSource(seasons=(Season.summer,), regions=(Region.beach,)),
        ),
        WaterItem.sea_urchin: (
            ForagingSource(regions=(Region.tide_pools,)),
        ),

        Seed.mixed: (
            ForagingSource(seasons=(Season.spring, Season.summer, Season.fall,), regions=(Region.town, Region.farm, Region.forest)),
        ),

        Seed.mixed_flower: (
            ForagingSource(seasons=(Season.summer,), regions=(Region.town, Region.farm, Region.forest)),
        ),

        # Books
        Book.jack_be_nimble_jack_be_thick: (ForagingSource(regions=(Region.forest, Region.backwoods, Region.bus_stop, Region.farm, Region.mountain),
                                                           seasons=Season.all, requires_hoe=True),),
        # Needs a condition for owning an axe. Plus maybe the abysmal drop rate with a time gate?
        Book.woodys_secret: (ForagingSource(regions=(Region.forest, Region.mountain), seasons=Season.all),),
    },
    shop_sources={
        # Saplings
        Sapling.apple: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        Sapling.apricot: (ShopSource(money_price=2000, shop_region=Region.pierre_store),),
        Sapling.cherry: (ShopSource(money_price=3400, shop_region=Region.pierre_store),),
        Sapling.orange: (ShopSource(money_price=4000, shop_region=Region.pierre_store),),
        Sapling.peach: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),
        Sapling.pomegranate: (ShopSource(money_price=6000, shop_region=Region.pierre_store),),

        # Crop seeds, assuming they are bought in season, otherwise price is different with missing stock list.
        Seed.parsnip: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.bean: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.cauliflower: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.potato: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.tulip: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.kale: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.jazz: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.garlic: (ShopSource(money_price=40, shop_region=Region.pierre_store, seasons=(Season.spring,)),),
        Seed.rice: (ShopSource(money_price=40, shop_region=Region.pierre_store, seasons=(Season.spring,)),),

        Seed.melon: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.tomato: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.blueberry: (ShopSource(money_price=80, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.pepper: (ShopSource(money_price=40, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.wheat: (ShopSource(money_price=10, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)),),
        Seed.radish: (ShopSource(money_price=40, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.poppy: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.spangle: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.hops: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.summer,)),),
        Seed.corn: (ShopSource(money_price=150, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)),),
        Seed.sunflower: (ShopSource(money_price=200, shop_region=Region.pierre_store, seasons=(Season.summer, Season.fall)),),
        Seed.red_cabbage: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.summer,)),),

        Seed.eggplant: (ShopSource(money_price=20, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.pumpkin: (ShopSource(money_price=100, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.bok_choy: (ShopSource(money_price=50, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.yam: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.cranberry: (ShopSource(money_price=240, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.fairy: (ShopSource(money_price=200, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.amaranth: (ShopSource(money_price=70, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.grape: (ShopSource(money_price=60, shop_region=Region.pierre_store, seasons=(Season.fall,)),),
        Seed.artichoke: (ShopSource(money_price=30, shop_region=Region.pierre_store, seasons=(Season.fall,)),),

        Seed.broccoli: (ShopSource(items_price=(Material.moss,), shop_region=Region.raccoon_shop),),
        Seed.carrot: (ShopSource(items_price=(TreeSeed.maple,), shop_region=Region.raccoon_shop),),
        Seed.powdermelon: (ShopSource(items_price=(TreeSeed.acorn,), shop_region=Region.raccoon_shop),),
        Seed.summer_squash: (ShopSource(items_price=(Material.sap,), shop_region=Region.raccoon_shop),),

        Seed.strawberry: (ShopSource(money_price=100, shop_region=Region.egg_festival, seasons=(Season.spring,)),),
        Seed.rare_seed: (ShopSource(money_price=1000, shop_region=Region.traveling_cart, seasons=(Season.spring, Season.summer)),),

        # Books
        Book.animal_catalogue: (ShopSource(money_price=5000, shop_region=Region.ranch),),
        Book.book_of_mysteries: (# Needs a MysteryBoxSource, THIS ONE IS INVALID RIGHT NOW
                                 ShopSource(money_price=999999999, shop_region=Region.blacksmith),),
        Book.dwarvish_safety_manual: (ShopSource(money_price=4000, shop_region=Region.mines_dwarf_shop),
                                      ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.friendship_101: (# ShopSource(money_price=20000, shop_region=Region.bookseller_rares),  # You can get this one in the prize machine, but how do I logic that :(
                              ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.horse_the_book: (ShopSource(money_price=25000, shop_region=Region.bookseller_2),),
        Book.jack_be_nimble_jack_be_thick: (ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.jewels_of_the_sea: (# Needs a source for Fishing Treasure Chests
                                  ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.mapping_cave_systems: (PermanentSource(regions=Region.adventurer_guild_bedroom),
                                    ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.monster_compendium: (# Needs a source for monster drops
                                  ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.ol_slitherlegs: (ShopSource(money_price=25000, shop_region=Region.bookseller_2),),
        Book.price_catalogue: (ShopSource(money_price=3000, shop_region=Region.bookseller_2),),
        Book.the_alleyway_buffet: (PermanentSource(regions=Region.town),
                                   ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.the_art_o_crabbing: (# Needs a source for the SquidFest Iridium Tier,
                                  ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.treasure_appraisal_guide: (# Needs a source for artifact troves and mystery boxes,
                                        ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.raccoon_journal: (# Needs a source for the AP item you'll get for completion of the 2nd raccoon bundle,
                               ShopSource(money_price=20000, shop_region=Region.bookseller_3),
                               ShopSource(items_price=(Material.fiber,), shop_region=Region.raccoon_shop),), # This one is 999 Fiber, should maybe add time?
        Book.way_of_the_wind_pt_1: (ShopSource(money_price=15000, shop_region=Region.bookseller_2),),
        Book.way_of_the_wind_pt_2: (ShopSource(money_price=35000, shop_region=Region.bookseller_2),), # This one requires the first book. If randomized, should have logic?
        Book.woodys_secret: (ShopSource(money_price=20000, shop_region=Region.bookseller_3),),
        Book.queen_of_sauce_cookbook: (ShopSource(money_price=50000, shop_region=Region.bookseller_2),), # Worst book ever

        # Experience Books
        Book.book_of_stars: (ShopSource(money_price=5000, shop_region=Region.bookseller_1),),
        Book.bait_and_bobber: (ShopSource(money_price=5000, shop_region=Region.bookseller_1),),
        Book.combat_quarterly: (ShopSource(money_price=5000, shop_region=Region.bookseller_1),),
        Book.mining_monthly: (ShopSource(money_price=5000, shop_region=Region.bookseller_1),),
        Book.stardew_valley_almanac: (ShopSource(money_price=5000, shop_region=Region.bookseller_1),),
        Book.woodcutters_weekly: (ShopSource(money_price=5000, shop_region=Region.bookseller_1),),
    },
    fishes=(
        fish_data.albacore,
        fish_data.anchovy,
        fish_data.bream,
        fish_data.bullhead,
        fish_data.carp,
        fish_data.catfish,
        fish_data.chub,
        fish_data.dorado,
        fish_data.eel,
        fish_data.flounder,
        fish_data.goby,
        fish_data.halibut,
        fish_data.herring,
        fish_data.largemouth_bass,
        fish_data.lingcod,
        fish_data.midnight_carp,  # Ginger island override
        fish_data.octopus,
        fish_data.perch,
        fish_data.pike,
        fish_data.pufferfish,  # Ginger island override
        fish_data.rainbow_trout,
        fish_data.red_mullet,
        fish_data.red_snapper,
        fish_data.salmon,
        fish_data.sardine,
        fish_data.sea_cucumber,
        fish_data.shad,
        fish_data.slimejack,
        fish_data.smallmouth_bass,
        fish_data.squid,
        fish_data.sturgeon,
        fish_data.sunfish,
        fish_data.super_cucumber,  # Ginger island override
        fish_data.tiger_trout,
        fish_data.tilapia,  # Ginger island override
        fish_data.tuna,  # Ginger island override
        fish_data.void_salmon,
        fish_data.walleye,
        fish_data.woodskip,
        fish_data.blob_fish,
        fish_data.midnight_squid,
        fish_data.spook_fish,

        # Legendaries
        fish_data.angler,
        fish_data.crimsonfish,
        fish_data.glacierfish,
        fish_data.legend,
        fish_data.mutant_carp,

        # Crab pot
        fish_data.clam,
        fish_data.cockle,
        fish_data.crab,
        fish_data.crayfish,
        fish_data.lobster,
        fish_data.mussel,
        fish_data.oyster,
        fish_data.periwinkle,
        fish_data.shrimp,
        fish_data.snail,
    ),
    villagers=(
        villagers_data.josh,
        villagers_data.elliott,
        villagers_data.harvey,
        villagers_data.sam,
        villagers_data.sebastian,
        villagers_data.shane,
        villagers_data.best_girl,
        villagers_data.emily,
        villagers_data.hoe,
        villagers_data.leah,
        villagers_data.nerd,
        villagers_data.penny,
        villagers_data.caroline,
        villagers_data.clint,
        villagers_data.demetrius,
        villagers_data.gilf,
        villagers_data.boomer,
        villagers_data.gus,
        villagers_data.jas,
        villagers_data.jodi,
        villagers_data.kent,
        villagers_data.krobus,
        villagers_data.lewis,
        villagers_data.linus,
        villagers_data.marnie,
        villagers_data.pam,
        villagers_data.pierre,
        villagers_data.milf,
        villagers_data.vincent,
        villagers_data.willy,
        villagers_data.wizard,
    )
)