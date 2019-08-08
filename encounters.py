#Kandu! Entertainment est. 6/30/2018
#This is the module that controls all the enemies

import game
from character import *


def lvl_1_random_enemy():
    enemy_catalog = [kathun(game.shiny_enemy),
                     goblin(game.shiny_enemy),
                     dark_fairy(game.shiny_enemy),
                     troll(game.shiny_enemy),
                     sea_serpent(game.shiny_enemy),
                     trigger_happy_bunny(game.shiny_enemy),
                     dark_wisp(game.shiny_enemy),
                     icy_sorcerer(game.shiny_enemy),
                     dirty_tree(game.shiny_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_2_random_enemy():
    enemy_catalog = [kathun(game.clean_enemy),
                     goblin(game.clean_enemy),
                     dark_fairy(game.clean_enemy),
                     troll(game.clean_enemy),
                     sea_serpent(game.clean_enemy),
                     trigger_happy_bunny(game.clean_enemy),
                     dark_wisp(game.clean_enemy),
                     icy_sorcerer(game.clean_enemy),
                     dirty_tree(game.clean_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_3_random_enemy():
    enemy_catalog = [kathun(game.shiny_enemy),
                     goblin(game.shiny_enemy),
                     dark_fairy(game.shiny_enemy),
                     troll(game.shiny_enemy),
                     sea_serpent(game.shiny_enemy),
                     trigger_happy_bunny(game.shiny_enemy),
                     dark_wisp(game.shiny_enemy),
                     icy_sorcerer(game.shiny_enemy),
                     dirty_tree(game.shiny_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_4_random_enemy():
    enemy_catalog = [kathun(game.forsaken_enemy),
                     goblin(game.forsaken_enemy),
                     dark_fairy(game.forsaken_enemy),
                     troll(game.forsaken_enemy),
                     sea_serpent(game.forsaken_enemy),
                     trigger_happy_bunny(game.forsaken_enemy),
                     dark_wisp(game.forsaken_enemy),
                     icy_sorcerer(game.forsaken_enemy),
                     dirty_tree(game.forsaken_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_5_random_enemy():
    enemy_catalog = [kathun(game.radiant_enemy),
                     goblin(game.radiant_enemy),
                     dark_fairy(game.radiant_enemy),
                     troll(game.radiant_enemy),
                     sea_serpent(game.radiant_enemy),
                     trigger_happy_bunny(game.radiant_enemy),
                     dark_wisp(game.radiant_enemy),
                     icy_sorcerer(game.radiant_enemy),
                     dirty_tree(game.radiant_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_6_random_enemy():
    enemy_catalog = [kathun(game.thunderous_enemy),
                     goblin(game.thunderous_enemy),
                     dark_fairy(game.thunderous_enemy),
                     troll(game.thunderous_enemy),
                     sea_serpent(game.thunderous_enemy),
                     trigger_happy_bunny(game.thunderous_enemy),
                     dark_wisp(game.thunderous_enemy),
                     icy_sorcerer(game.thunderous_enemy),
                     dirty_tree(game.thunderous_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_7_random_enemy():
    enemy_catalog = [kathun(game.immortal_enemy),
                     goblin(game.immortal_enemy),
                     dark_fairy(game.immortal_enemy),
                     troll(game.immortal_enemy),
                     sea_serpent(game.immortal_enemy),
                     trigger_happy_bunny(game.immortal_enemy),
                     dark_wisp(game.immortal_enemy),
                     icy_sorcerer(game.immortal_enemy),
                     dirty_tree(game.immortal_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def lvl_8_random_enemy():
    enemy_catalog = [kathun(game.legendary_enemy),
                     goblin(game.legendary_enemy),
                     dark_fairy(game.legendary_enemy),
                     troll(game.legendary_enemy),
                     sea_serpent(game.legendary_enemy),
                     trigger_happy_bunny(game.legendary_enemy),
                     dark_wisp(game.legendary_enemy),
                     icy_sorcerer(game.legendary_enemy),
                     dirty_tree(game.legendary_enemy)]
    chosen_enemy = enemy_catalog[random.randint(0, len(enemy_catalog) - 1)]
    return chosen_enemy


def kathun(enemy_attribute):
    kathun = Dragon(enemy_attribute, 'Kathun the Enforcer')
    kathun.add_to_inventory(game.loot['diamond_chest'])
    return kathun


def goblin(enemy_attribute):
    goblin = Goblin(enemy_attribute, 'Kothen the Goblin')
    goblin.add_to_inventory(game.loot['treasure'])
    return goblin


def dark_fairy(enemy_attribute):
    dark_fairy = Dark_Fairy(enemy_attribute, 'Oolefia the Dark Fairy')
    dark_fairy.add_to_inventory(game.loot['regular'])
    return dark_fairy


def troll(enemy_attribute):
    troll = Troll(enemy_attribute, 'Chigon the Troll')
    troll.add_to_inventory(game.loot['dust'])
    return troll


def sea_serpent(enemy_attribute):
    serpent = Sea_serpent(enemy_attribute, 'Jojax The Serpent')
    serpent.add_to_inventory(game.loot['regular'])
    return serpent


def trigger_happy_bunny(enemy_attribute):
    bunny = Trigger_happy_bunny(enemy_attribute, 'Huula The Bunny')
    bunny.add_to_inventory(game.loot['regular'])
    return bunny


def dark_wisp(enemy_attribute):
    wisp = Dark_wisp(enemy_attribute, 'Wisp of Imagined Light')
    wisp.add_to_inventory(game.loot['regular'])
    return wisp


def icy_sorcerer(enemy_attribute):
    icy = Icy_sorcerer(enemy_attribute, 'Ewthen the Icy Sorcerer')
    icy.add_to_inventory(game.loot['regular'])
    return icy


def dirty_tree(enemy_attribute):
    tree = Tree(enemy_attribute, 'Bookar The Burnt Tree')
    tree.add_to_inventory(game.loot['regular'])
    return tree
