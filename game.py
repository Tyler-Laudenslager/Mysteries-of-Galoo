# Kandu! Entertainment est. 6/30/2018
# This is the main module for Mysteries of Galoo.

import random
from story import *
from time import sleep
import enemy_hero_creator as en


def intro():
    print("""
Welcome to the Universe of Galoo

You are at the center of the Solar System!

As the action bar on the bottom states
move your player according to the actions
provided below

UP: Press 1
Down: Press 2
Left: Press 3
Right: Press 4
Move to Another Map: Press 5

8 dungeons per map / 25 maps per world / 8 worlds in the Solar System

Quick Maths thats 1600 dungeons. Oh man....I guess I know what I'll be doing this weekend!

Each 'Dungeon' you will start a fight with a random enemy *4 unique enemies so far*

After you defeat the enemy with your strong weapon the developer has graciously provided,
you will then take the enemy's loot and it will be added to your inventory.

Plays like Dungeons and Dragons your 'Dice Roll' determines what will happen.

This is your Map. Don't Lose It! Have Fun!""")


def enter_galoo():
    clear_buffer()
    print("Manifesting Character in Galoo", end=" ")
    for i in range(6):
        print(".", end=" ")
        sleep(.25)
    print("Done!")
    sleep(.25)


defense = random.randint(10, 15)
strength = random.randint(20, 28)

enemy_strength = random.randint(5, 10)
enemy_defense = random.randint(1, 5)

treasure_chest = {'Gold': 40, 'Health Potion': 1, 'Ruby Necklace': 1, 'Autographed Picture of Pee-wee Herman': 1, \
                  'Sapphire': 1}

regular_loot = {'Gold': 3, 'Dirty Clothes': 1}

starting_loot = {'Gold': 0}

dust_loot = {'Dust': 2}

diamond_chest = {'Diamond': 1, 'Gold': 100}

loot = {'treasure': treasure_chest, 'regular': regular_loot, 'dust': dust_loot, 'diamond_chest': diamond_chest,
        'starting_loot': starting_loot}

start_new = {'health': 100, 'energy': 50, 'strength': 5, 'defense': 5}

dusty_enemy = en.Enemy('dusty')

clean_enemy = en.Enemy('clean')

shiny_enemy = en.Enemy('shiny')

forsaken_enemy = en.Enemy('forsaken')

radiant_enemy = en.Enemy('radiant')

thunderous_enemy = en.Enemy('thunderous')

immortal_enemy = en.Enemy('immortal')

legendary_enemy = en.Enemy('legendary')

dusty_hero = en.Hero('dusty')

radiant_char = en.Hero('radiant')

dusty_enemy = dusty_enemy.generate_stats()

clean_enemy = clean_enemy.generate_stats()

shiny_enemy = shiny_enemy.generate_stats()

forsaken_enemy = forsaken_enemy.generate_stats()

radiant_enemy = radiant_enemy.generate_stats()

thunderous_enemy = thunderous_enemy.generate_stats()

immortal_enemy = immortal_enemy.generate_stats()

legendary_enemy = legendary_enemy.generate_stats()

dusty_hero = dusty_hero.generate_stats()

radiant_char = radiant_char.generate_stats()

child = {'health': 50000, 'energy': 100, 'strength': enemy_strength, 'defense': enemy_defense}

basic_staff = {'health': 5, 'energy': 10, 'strength': 5, 'defense': 1}

legendary_stats = {'health': 5000, 'energy': 2500, 'strength': 7000, 'defense': 3500, 'color': 'orange'}


