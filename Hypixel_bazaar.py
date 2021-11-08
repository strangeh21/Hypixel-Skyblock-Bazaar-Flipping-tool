# Self refreshing CMD window with profitable bazaar flips, and sells to NPC. 
from typing import Counter
import requests
import time
from datetime import datetime
from os import system, name
import sys

npc_sell_prices = {
    "INK_SACK:3": 3, 
    "BROWN_MUSHROOM": 4, 
    "SPOOKY_SHARD": 0, 
    "INK_SACK:4": 1, 
    "TARANTULA_WEB": 1, 
    "CARROT_ITEM": 1, 
    "ENCHANTED_POTATO": 160, 
    "EXP_BOTTLE": 5, 
    "JERRY_BOX_GREEN": 0, 
    "ENCHANTED_SLIME_BALL": 800, 
    "ENCHANTED_RED_MUSHROOM": 640, 
    "ENCHANTED_GOLDEN_CARROT": 20608, 
    "ENCHANTED_RABBIT_HIDE": 2880, 
    "FLAWED_AMETHYST_GEM": 320, 
    "PERFECT_JADE_GEM": 10240000, 
    "ENCHANTED_BIRCH_LOG": 320, 
    "ENCHANTED_GUNPOWDER": 640, 
    "ENCHANTED_MELON": 160,
    "ENCHANTED_SUGAR": 320,
    "CACTUS": 1,
    "ENCHANTED_BLAZE_ROD": 230400,
    "FLAWED_JASPER_GEM": 320,
    "ENCHANTED_CAKE": 2700,
    "PUMPKIN": 4,
    "ENCHANTED_BROWN_MUSHROOM": 640,
    "GOBLIN_EGG_YELLOW": 0,
    "WHEAT": 1,
    "NURSE_SHARK_TOOTH": 0,
    "FLAWED_AMBER_GEM": 320,
    "ENCHANTED_RAW_SALMON": 1600,
    "ENCHANTED_GLISTERING_MELON": 1000,
    "PRISMARINE_SHARD": 5,
    "PROTECTOR_FRAGMENT": 0,
    "ENCHANTED_EMERALD": 960,
    "ENCHANTED_SPIDER_EYE": 480,
    "RED_MUSHROOM": 4,
    "GRAND_EXP_BOTTLE": 480,
    "ENCHANTED_MELON_BLOCK": 25600,
    "MUTTON": 5,
    "POWER_CRYSTAL": 1920,
    "RAW_SOULFLOW": 0,
    "DIAMOND": 8,
    "WISE_FRAGMENT": 0,
    "SHARK_FIN": 0,
    "COBBLESTONE": 1,
    "REFINED_MITHRIL": 256000,
    "SPIDER_EYE": 3,
    "RAW_FISH": 6,
    "PERFECT_RUBY_GEM": 10240000,
    "ENCHANTED_PUFFERFISH": 2400,
    "YOGGIE": 100,
    "PERFECT_JASPER_GEM": 10240000,
    "POTATO_ITEM": 1,
    "ENCHANTED_NETHERRACK": 160,
    "ENCHANTED_HARD_STONE": 576,
    "ENCHANTED_HUGE_MUSHROOM_1": 2300,
    "REFINED_DIAMOND": 4096,
    "ENCHANTED_COBBLESTONE": 160,
    "TIGHTLY_TIED_HAY_BALE": 187200,
    "ENCHANTED_HUGE_MUSHROOM_2": 2300,
    "PORK": 5,
    "PRISMARINE_CRYSTALS": 5,
    "ICE": 0.5,
    "TIGER_SHARK_TOOTH": 0,
    "HUGE_MUSHROOM_1": 4,
    "HUGE_MUSHROOM_2": 4,
    "ICE_BAIT": 3,
    "LOG_2:1": 2,
    "ENCHANTED_SNOW_BLOCK": 600,
    "STRING": 3,
    "GOLDEN_TOOTH": 128,
    "CHEESE_FUEL": 500,
    "HYPER_CATALYST": 500,
    "RABBIT_FOOT": 5,
    "REDSTONE": 1,
    "JERRY_BOX_GOLDEN": 0,
    "PUMPKIN_GUTS": 0,
    "ENCHANTED_CACTUS_GREEN": 160,
    "BOOSTER_COOKIE": 0,
    "ENCHANTED_CARROT_ON_A_STICK": 0, # Enchanted_carrot_stick is the right one. Something something, bug fix. 2 bazaar entries for the same item.
    "ENCHANTED_ENDSTONE": 320,
    "ENCHANTED_LAPIS_LAZULI_BLOCK": 25600,
    "ENCHANTED_COOKIE": 61500,
    "COLOSSAL_EXP_BOTTLE": 5000,
    "ENCHANTED_SAND": 320,
    "ENCHANTED_STRING": 576,
    "STRONG_FRAGMENT": 0,
    "SLIME_BALL": 5,
    "HOLY_FRAGMENT": 0,
    "ENCHANTED_ACACIA_LOG": 320,
    "SNOW_BALL": 1,
    "ENCHANTED_EGG": 432,
    "SAND": 2,
    "SOUL_FRAGMENT": 0,
    "FINE_JADE_GEM": 25600,
    "FLAWED_RUBY_GEM": 320,
    "RAW_CHICKEN": 4,
    "FLAWLESS_JASPER_GEM": 2048000,
    "ANCIENT_CLAW": 200,
    "PLASMA_BUCKET": 50000,
    "ENCHANTED_LAPIS_LAZULI": 160,
    "ENCHANTED_GHAST_TEAR": 80,
    "ENCHANTED_COCOA": 480,
    "CARROT_BAIT": 7,
    "FINE_TOPAZ_GEM": 25600,
    "SEEDS": 0.5,
    "FINE_RUBY_GEM": 25600,
    "ENCHANTED_LEATHER": 1700,
    "ENCHANTED_SHARK_FIN": 0,
    "ENCHANTED_SPONGE": 2000,
    "PERFECT_AMBER_GEM": 10240000,
    "HAY_BLOCK": 9,
    "INK_SACK": 2,
    "FLINT": 4,
    "ENCHANTED_ROTTEN_FLESH": 320,
    "ENCHANTED_SPRUCE_LOG": 320,
    "WOLF_TOOTH": 1,
    "ENCHANTED_GRILLED_PORK": 128000,
    "ENCHANTED_NETHER_STALK": 480,
    "ENCHANTED_REDSTONE_BLOCK": 25600,
    "ENCHANTED_ANCIENT_CLAW": 0,
    "ENCHANTED_QUARTZ_BLOCK": 102400,
    "GREEN_CANDY": 0,
    "ENCHANTED_REDSTONE": 160,
    "ENCHANTED_REDSTONE_LAMP": 30720,
    "TREASURITE": 5000,
    "DWARVEN_COMPACTOR": 100000,
    "GREAT_WHITE_SHARK_TOOTH": 0,
    "GRAVEL": 3,
    "MELON": 0.5,
    "ENCHANTED_LAVA_BUCKET": 50000,
    "ENCHANTED_PACKED_ICE": 12800,
    "RAW_FISH:3": 15,
    "ENCHANTED_PRISMARINE_SHARD": 400,
    "ENCHANTED_IRON_BLOCK": 76800,
    "RECOMBOBULATOR_3000": 0,
    "ENCHANTED_CARROT_STICK": 10240,
    "BONE": 2,
    "RAW_FISH:2": 20,
    "RAW_FISH:1": 10,
    "REVENANT_FLESH": 1,
    "ENCHANTED_PORK": 800,
    "ENCHANTED_GLOWSTONE": 61000,
    "GOBLIN_EGG_RED": 0,
    "ROUGH_JASPER_GEM": 4,
    "FEATHER": 3,
    "WHALE_BAIT": 80,
    "NETHERRACK": 1,
    "SPONGE": 50,
    "BLAZE_ROD": 9,
    "ENCHANTED_DARK_OAK_LOG": 320,
    "YOUNG_FRAGMENT": 0,
    "FLAWLESS_TOPAZ_GEM": 2048000,
    "ENCHANTED_CLOWNFISH": 3200,
    "REFINED_MINERAL": 0,
    "ENCHANTED_GOLD": 640,
    "ENCHANTED_RAW_CHICKEN": 640,
    "ENCHANTED_WATER_LILY": 1600,
    "ROUGH_AMETHYST_GEM": 4,
    "ROUGH_RUBY_GEM": 4,
    "GOBLIN_EGG_BLUE": 0,
    "NULL_ATOM": 33333,
    "FLAWLESS_RUBY_GEM": 2048000,
    "LOG:1": 2,
    "TITANIUM_ORE": 20,
    "CATALYST": 500,
    "BLUE_SHARK_TOOTH": 0,
    "LOG:3": 2,
    "LOG:2": 2,
    "BLESSED_BAIT": 42,
    "ENCHANTED_GLOWSTONE_DUST": 320,
    "ENCHANTED_INK_SACK": 160,
    "ENCHANTED_CACTUS": 25600,
    "ENCHANTED_SUGAR_CANE": 51200,
    "FLAWLESS_SAPPHIRE_GEM": 2048000,
    "ENCHANTED_COOKED_SALMON": 256000,
    "ENCHANTED_SEEDS": 80,
    "CONCENTRATED_STONE": 200000,
    "LOG": 2,
    "JACOBS_TICKET": 0,
    "ENCHANTED_BONE_BLOCK": 0,
    "GHAST_TEAR": 16,
    "ABSOLUTE_ENDER_PEARL": 11200,
    "UNSTABLE_FRAGMENT": 0,
    "ENCHANTED_ENDER_PEARL": 140,
    "PURPLE_CANDY": 0,
    "SPIKED_BAIT": 20,
    "POLISHED_PUMPKIN": 102400,
    "ENCHANTED_FERMENTED_SPIDER_EYE": 31000,
    "ROUGH_JADE_GEM": 4,
    "ENCHANTED_GOLD_BLOCK": 102000,
    "ENCHANTED_JUNGLE_LOG": 320,
    "ENCHANTED_FLINT": 640,
    "IRON_INGOT": 3,
    "ENCHANTED_EMERALD_BLOCK": 153600,
    "NULL_OVOID": 0,
    "ENCHANTED_CLAY_BALL": 480,
    "ROUGH_SAPPHIRE_GEM": 4,
    "GLOWSTONE_DUST": 2,
    "GOLD_INGOT": 4,
    "REVENANT_VISCERA": 128,
    "PERFECT_AMETHYST_GEM": 10240000,
    "TARANTULA_SILK": 128,
    "TITANIC_EXP_BOTTLE": 5000,
    "ENCHANTED_MUTTON": 800,
    "NULL_SPHERE": 0,
    "ENCHANTED_IRON": 480,
    "SUPER_COMPACTOR_3000": 50000,
    "SUPER_EGG": 0,
    "MITHRIL_ORE": 10,
    "STOCK_OF_STONKS": 0,
    "ENCHANTED_HAY_BLOCK": 1300,
    "ENCHANTED_BONE": 320,
    "ENCHANTED_PAPER": 384,
    "ENCHANTED_TITANIUM": 3200,
    "ENCHANTED_DIAMOND_BLOCK": 204800,
    "SPOOKY_BAIT": 10,
    "SUPERIOR_FRAGMENT": 0,
    "MAGMA_BUCKET": 50000,
    "EMERALD": 6,
    "GOBLIN_EGG_GREEN": 0,
    "ENCHANTED_RABBIT_FOOT": 800,
    "LIGHT_BAIT": 16,
    "ENCHANTED_ICE": 80,
    "HOT_POTATO_BOOK": 13000,
    "CLAY_BALL": 3,
    "ARACHNE_KEEPER_FRAGMENT": 0,
    "OLD_FRAGMENT": 0,
    "GREEN_GIFT": 0,
    "WORM_MEMBRANE": 0,
    "FLAWLESS_AMETHYST_GEM": 2048000,
    "ROUGH_TOPAZ_GEM": 4,
    "PACKED_ICE": 4.5,
    "ROUGH_AMBER_GEM": 4,
    "WATER_LILY": 10,
    "HAMSTER_WHEEL": 20000,
    "LOG_2": 2,
    "ENCHANTED_OBSIDIAN": 1440,
    "FINE_AMBER_GEM": 25600,
    "ENCHANTED_COAL": 320,
    "COAL": 2,
    "ENCHANTED_QUARTZ": 640,
    "ENDER_PEARL": 7,
    "ENCHANTED_COAL_BLOCK": 51000,
    "WEREWOLF_SKIN": 0,
    "PERFECT_TOPAZ_GEM": 10240000,
    "ENCHANTED_PRISMARINE_CRYSTALS": 400,
    "GOBLIN_EGG": 0,
    "DAEDALUS_STICK": 250000,
    "ENCHANTED_WET_SPONGE": 80000,
    "FLAWED_JADE_GEM": 320,
    "ENCHANTED_RAW_FISH": 960,
    "ENDER_STONE": 2,
    "QUARTZ": 4,
    "FOUL_FLESH": 25000,
    "JERRY_BOX_PURPLE": 0,
    "RAW_BEEF": 4,
    "SLUDGE_JUICE": 0,
    "ENCHANTED_EYE_OF_ENDER": 3520,
    "ECTOPLASM": 0,
    "MAGMA_CREAM": 8,
    "SUGAR_CANE": 2,
    "SHARK_BAIT": 0,
    "RED_GIFT": 0,
    "ENCHANTED_MITHRIL": 1600,
    "JERRY_BOX_BLUE": 0,
    "ENCHANTED_RAW_BEEF": 640,
    "ENCHANTED_FEATHER": 480,
    "ENCHANTED_SLIME_BLOCK": 128000,
    "ENCHANTED_OAK_LOG": 320,
    "RABBIT_HIDE": 5,
    "WHITE_GIFT": 0,
    "RABBIT": 4,
    "NETHER_STALK": 3,
    "FINE_SAPPHIRE_GEM": 25600,
    "SULPHUR": 4,
    "DARK_BAIT": 8,
    "ENCHANTED_CARROT": 160,
    "ENCHANTED_PUMPKIN": 640,
    "GRIFFIN_FEATHER": 1000,
    "ROTTEN_FLESH": 2,
    "ENCHANTED_COOKED_FISH": 150000,
    "OBSIDIAN": 7,
    "SOULFLOW": 1,
    "MINNOW_BAIT": 12,
    "ENCHANTED_MAGMA_CREAM": 1280,
    "ENCHANTED_FIREWORK_ROCKET": 41000,
    "STARFALL": 15,
    "FLAWLESS_JADE_GEM": 2048000,
    "HARD_STONE": 1,
    "FLAWED_TOPAZ_GEM": 320,
    "LEATHER": 3,
    "ENCHANTED_COOKED_MUTTON": 128000,
    "FINE_AMETHYST_GEM": 25600,
    "REFINED_TITANIUM": 51200,
    "ENCHANTED_RABBIT": 640,
    "SOUL_STRING": 0,
    "MUTANT_NETHER_STALK": 76800,
    "ENCHANTED_BREAD": 60,
    "FUMING_POTATO_BOOK": 0,
    "FINE_JASPER_GEM": 25600,
    "FLAWLESS_AMBER_GEM": 2048000,
    "ENCHANTED_CHARCOAL": 320,
    "FLAWED_SAPPHIRE_GEM": 320,
    "ENCHANTED_BLAZE_POWDER": 1440,
    "SUMMONING_EYE": 0,
    "PERFECT_SAPPHIRE_GEM": 10240000,
    "FISH_BAIT": 20,
    "SNOW_BLOCK": 4,
    "ENCHANTED_BAKED_POTATO": 25600,
    "COMPACTOR": 640,
    "ENCHANTED_DIAMOND": 1280,
    "BAZAAR_COOKIE": 0, #Non-existing item.
    }

def get_bazaar_update():
    try:
        data = requests.get("https://api.hypixel.net/skyblock/bazaar").json()
        return data
    except:
        print("Failed to obtain bazaar data.")

def compare_items_for_profit(buy_price, sell_price): #function for finding bazaar items with greater spread than 5% profit. 
    try: 
        profit_percent = buy_price / sell_price * 100
        profit_percent = round(profit_percent, 2)
        return profit_percent
    except Exception as e:
        do_nothing = ""
    
def check_npc_list_for_missing():
    print("Checking for missing bazaar items in NPC sell prices list.....")
    products_not_in_NPC_list = [item for item in bazaar_data_products if item not in npc_sell_prices] #Check NPC_sell_prices keys against bazaar_data_products keys and list all missing from NPC_sell_prices.
    if products_not_in_NPC_list == []:
        print("All bazaar products are listed in the NPC sell prices list! Good job.")
        print("")
        print("")
        time.sleep(1)
        system("cls")
    else:
        print("MISSING ITEMS:")
        print(products_not_in_NPC_list)
        print("You should update the dictionary \"npc_sell_prices\". Continuing after 10 seconds.")
        time.sleep(1)

bazaar_data = get_bazaar_update()
bazaar_data_products = bazaar_data["products"]
profitable_items = {}
profitable_items_buy_price = {}
profitable_items_sell_price = {}
profitable_npc_items = {}
profitable_npc_items_buy_price = {}
profitable_npc_items_sell_price = {}
profitable_bazaar_spreads_text_list = {}
profitable_npc_sell_text_list = {}

check_npc_list_for_missing()
system("cls")
while True:
    for i in bazaar_data["products"]: # Check buy/sell price of each item under products. Append to dictionary. 
        try:
            data_buy_price = bazaar_data["products"][i]["buy_summary"]
            data_highest_buy_price = data_buy_price[0]["pricePerUnit"]
            data_sell_price = bazaar_data["products"][i]["sell_summary"]
            data_lowest_sell_price = data_sell_price[0]["pricePerUnit"]
        except IndexError:
            continue
        except Exception as e:
            print(f"Error for item: {i}:")
            print(e, file=sys.stderr)
            continue
        profitable_items[i] = compare_items_for_profit(data_highest_buy_price, data_lowest_sell_price)
        profitable_items_buy_price[i] = data_highest_buy_price
        profitable_items_sell_price[i] = data_lowest_sell_price
    
    for i in bazaar_data["products"]: #Check if profitable to sell to NPC, and list profitable items.
        try:
            data_buy_price = bazaar_data["products"][i]["sell_summary"]
            data_highest_buy_price = data_buy_price[0]["pricePerUnit"]
            data_npc_sell_price = npc_sell_prices[i]
        except IndexError:
            continue
        except KeyError as e:
            data_npc_sell_price = "MISSING"
            print(f"Missing item: {e}")
        except Exception as e:
            print(e, file=sys.stderr)
            continue
        if compare_items_for_profit(data_highest_buy_price, data_npc_sell_price) != None:
            profitable_npc_items[i] = compare_items_for_profit(data_npc_sell_price, data_highest_buy_price) - 100
        else:
            profitable_npc_items[i] = 0
        profitable_npc_items_buy_price[i] = data_highest_buy_price
        profitable_npc_items_sell_price[i] = data_npc_sell_price    
        
    num = 0
    print("Items that have large spread. ")
    print("I highly recommend checking if price is stable, and if volume can support your trade first.")
    print("Suggested source: bazaartracker.com")
    for i in dict(sorted(profitable_items.items(),reverse=True, key=lambda item: item[1])): #Sort large spread items and print top 10 in descending order (x% profit for item)
        difference = profitable_items_buy_price[i] - profitable_items_sell_price[i]
        difference = float("{:.2f}".format(difference)) #Round to nearest 2 decimals.
        if num < 10:
            if difference >= 10: #Coin difference from buy/sell
                num = num + 1
                try:
                    print(f"{profitable_items[i]}% profit: {i}. Diff: {difference}. Buy: {profitable_items_sell_price[i]}. Sell: {profitable_items_buy_price[i]}. NPC: {profitable_npc_items_sell_price[i]}")
                except Exception as e:
                    print(e, file=sys.stderr)
    num = 0
    print("")
    print("")
    print("Items to profitably sell to NPC")
    for i in dict(sorted(profitable_npc_items.items(),reverse=True, key=lambda item: item[1])): #Sort profit NPC sells and print top 10 in descending order (x% profit for item)
        if profitable_npc_items_sell_price[i] == "MISSING":
            difference = 0
        else:
            difference = profitable_npc_items_sell_price[i] - profitable_npc_items_buy_price[i]
            difference = float("{:.2f}".format(difference)) #Round to nearest 2 decimals.
        profitable_npc_items[i] = float("{:.2f}".format(profitable_npc_items[i]))
        if num < 10: #Show top 10 profitable NPC sells.
            if difference > 10: #Coin difference from buy/sell
                num = num + 1
                try:
                    print(f"{profitable_npc_items[i]}% profit: {i}. Diff {difference}. Buy: {profitable_npc_items_buy_price[i]}. Sell: {profitable_npc_items_sell_price[i]}.")
                except Exception as e:
                    print(f"Error: {e}")

    print("Last updated: " + datetime.now().strftime("%H:%M:%S"))
    time.sleep(27)
    bazaar_data = get_bazaar_update()
    bazaar_data_products = bazaar_data["products"]
    print("Updating in 3...", end="\r")
    time.sleep(1)
    print("Updating in 2...", end="\r")
    time.sleep(1)
    print("Updating in 1...", end="\r")
    time.sleep(1)
    system("cls")