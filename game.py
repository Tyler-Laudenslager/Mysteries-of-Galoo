#Kandu! Entertainment est. 6/30/2018
#This is the main module for Mysteries of Galoo.

from character import *
import random
from time import sleep
from story import *
import sys
from weapon import *
from armory import *
from enemy_hero_creator import *
from generator import *
from map_creator import *

    
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
    print ("Manifesting Character in Galoo", end = " ")
    for i in range(6):
        print (".", end = " ")            
        sleep(.25)
    print ("Done!")
    sleep(.25)
    
    
            

defense = random.randint(10, 15)
strength = random.randint(20, 28)

enemy_strength = random.randint(5, 10)
enemy_defense = random.randint(1, 5)


treasure_chest = {'Gold':40, 'Health Potion':1, 'Ruby_Necklace':1, 'Autographed Picture of Pee-wee Herman':1, \
                    'Sapphire':1}

regular_loot = {'Gold':3, 'Dirty Clothes':1}

starting_loot = {'Gold':0}

dust_loot = {'Dust':2}

diamond_chest = {'Diamond':1, 'Gold':100}

loot = {'treasure':treasure_chest,'regular':regular_loot,'dust':dust_loot,'diamond_chest':diamond_chest,'starting_loot':starting_loot}

start_new = {'health':100, 'energy':50, 'strength':5, 'defense':5}

dusty_enemy = Enemy('dusty')

clean_enemy = Enemy('clean')

shiny_enemy = Enemy('shiny')

forsaken_enemy = Enemy('forsaken')

radiant_enemy = Enemy('radiant')

dusty_hero = Hero('dusty')

clean_enemy = clean_enemy.generate_stats()

radiant_char = Hero('radiant')

dusty_enemy = dusty_enemy.generate_stats()

radiant_char = radiant_char.generate_stats()

child = {'health':50000, 'energy':100, 'strength':enemy_strength, 'defense':enemy_defense}

basic_staff = {'health':5, 'energy':10, 'strength':5, 'defense':1}

legendary_stats = {'health':5000, 'energy':2500, 'strength':7000, 'defense':3500, 'color':'orange'}



##basic_sword = Weapon('Dusty Sword', 'dusty')
##basic_staff = Weapon('Dusty Oak Staff', 'dusty')
##armory = {'Trainer Staff':basic_staff, 'Trainer Sword':basic_sword}
##
##
##magician = Magician(radiant_char, 'Merlin')
##harambe = Gorilla(dusty_enemy, 'Harambe')
##
##harambe.add_to_inventory(loot['treasure'])
##    
##new_weapon = Armory.get_weapon(magician._type)
##new_weapon3 = Armory.get_weapon(magician._type)
##new_weapon2 = Armory.get_weapon(harambe._type)
##
##magician.equip(new_weapon)
##magician.fight(harambe)
##magician.playerinfo()
##
##magician.remove_item(new_weapon)
##
##magician.playerinfo()
##
##magician.playerinfo()
##harambe.playerinfo()
##input("Press Enter to Exit")
