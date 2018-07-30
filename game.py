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


def random_enemy():

    None

def enter_galoo():

    for i in range(6):
        clear_buffer()
        print ("Manifesting Character in Galoo", end='', flush=True)
        for k in range(i):
            print (".", end='', flush=True)            
        blank_lines(10)
        sleep(.25)
    clear_buffer()
    print ("Manifesting Character in Galoo.....Done!", end='', flush=True)
    blank_lines(10)
    sleep(.75)

def start_menu():

    clear_buffer()

    print("Mysteries of Galoo")
    blank_lines(1)
    print("\tPress 1 for New Game")
    print("\tPress 2 to Exit")
    blank_lines(1)
    choice = str(input("Choice: "))
    clear_buffer()

    if choice == '1':
        print("New Game!")
        blank_lines(1)
        print("Choose your character:")
        print("Choose: 1) for Gorilla")
        print("\t2) for Tunneler")
        print("\t3) for Archer")
        print("\t4) for Alchemist")
        print("\t5) for Knight")
        print("\t6) for Botanist")
        print("\t7) for Priest")
        print("\t8) for Magician")
        blank_lines(1)
        choice = str(input("Choice: "))
        if choice == '1':
            name = input("Enter name for your Gorilla: ")
            character = Gorilla(radiant_char, name)

        if choice == '2':
            name = input("Enter name for your Tunneler: ")
            character = Tunneler(radiant_char, name)

        if choice == '3':
            name = input("Enter name for your Archer: ")
            character = Archer(radiant_char, name)

        if choice == '4':
            name = input("Enter name for your Alchemist: ")
            character = Alchemist(radiant_char, name)

        if choice == '5':
            name = input("Enter name for your Knight: ")
            character = Knight(radiant_char, name)

        if choice == '6':
            name = input("Enter name for your Botanist: ")
            character = Botanist(radiant_char, name)
            
        if choice == '7':
            name = input("Enter name for your Priest: ")
            character = Priest(radiant_char, name)

        if choice == '8':
            name = input("Enter name for your Magician: ")
            character = Magician(radiant_char, name)

    elif choice == '2':
        sys.exit()

    else:
        print("Choose again")
    
    new_weapon = Armory.get_weapon(character._type)
    kathun = Dragon(dusty_enemy, 'Kathun the Enforcer')
    kathun.add_to_inventory(loot['regular'])
    character.equip(new_weapon)
    enter_galoo()
    welcome_to_galoo()
    character.fight(kathun)
    character.playerinfo()

defense = random.randint(10, 15)
strength = random.randint(20, 28)

enemy_strength = random.randint(5, 10)
enemy_defense = random.randint(1, 5)


treasure_chest = {'Gold':40, 'Health Potion':1, 'Ruby_Necklace':1, 'Autographed Picture of Pee-wee Herman':1, \
                    'Sapphire':1}

regular_loot = {'Gold':3, 'Dirty Clothes':1}

loot = {'treasure':treasure_chest,'regular':regular_loot}

start_new = {'health':100, 'energy':50, 'strength':5, 'defense':5}

dusty_enemy = Enemy('dusty')

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


start_menu()
