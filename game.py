#Kandu! Entertainment est. 6/30/2018
#This is the main module for Mysteries of Galoo.


from character import *
import random
from time import sleep
from story import *
import sys
from weapon import *
from armory import *


def random_enemy():

    None

def enter_galoo():
    print()
    print ("Manifesting Character in Galoo", end='')
    sleep(.25)
    print (".", end='')
    sleep(.25)
    print (".", end='')
    sleep(.25)
    print (".", end='')
    sleep(.25)
    print (".", end='')
    sleep(.25)
    print (".", end='')
    sleep(.25)
    print (".", end='')
    sleep(.25)
    print ('Done', end='')


def start_menu():
    print("Mysteries of Galoo")
    print("Press 1 for New Game")
    print("Press 2 to Exit")
    choice = str(input("Choice: "))
    if choice == '1':
        print("Choose your character")
        print("Press 1 for Gorilla")
        print("Press 2 for Tunneler")
        print("Press 3 for Archer")
        print("Press 4 for Alchemist")
        print("Press 5 for Knight")
        print("Press 6 for Botanist")
        print("Press 7 for Priest")
        print("Press 8 for Magician")
        choice = str(input("Choice: "))
        if choice == '1':
            name = input("Enter name for your Gorilla: ")
            gorilla = Gorilla(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '2':
            name = input("Enter name for your Tunneler: ")
            tunneler = Tunneler(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '3':
            name = input("Enter name for your Archer: ")
            archer = Archer(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '4':
            name = input("Enter name for your Alchemist: ")
            alchemist = Alchemist(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '5':
            name = input("Enter name for your Knight: ")
            knight = Knight(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '6':
            name = input("Enter name for your Botanist: ")
            botanist = Botanist(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '7':
            name = input("Enter name for your Priest: ")
            priest = Priest(start_new, name)
            enter_galoo()
            welcome_to_galoo()

        if choice == '8':
            name = input("Enter name for your Magician: ")
            magician = Magician(start_new, name)
            kathun = Dragon(start_new, 'Kathun the Enforcer')
            boo = Dragon(start_new, 'Boo the Terrible')
            kathun.add_to_inventory(loot['treasure'])
            boo.add_to_inventory(loot['regular'])
            enter_galoo()
            welcome_to_galoo()
            magician.fight(kathun)
            kathun.playerinfo()



    elif choice == '2':
        sys.exit()

    else:
        print("Choose again")

defense = random.randint(10, 15)
strength = random.randint(20, 28)

enemy_strength = random.randint(5, 10)
enemy_defense = random.randint(1, 5)


treasure_chest = {'Gold':40, 'Health Potion':1, 'Ruby_Necklace':1, 'Autographed Picture of Pee-wee Herman':1, \
                    'Sapphire':1}

regular_loot = {'Gold':3, 'Dirty Clothes':1}

loot = {'treasure':treasure_chest,'regular':regular_loot}

start_new = {'health':100, 'energy':50, 'strength':5, 'defense':5}

start_new_enemy = {'health':500, 'energy':25, 'strength':20, 'defense':10}


child = {'health':50000, 'energy':100, 'strength':enemy_strength, 'defense':enemy_defense}

basic_staff = {'health':5, 'energy':10, 'strength':5, 'defense':1}

legendary_stats = {'health':5000, 'energy':2500, 'strength':7000, 'defense':3500, 'color':'orange'}




basic_sword = Weapon('Dusty Sword', 'dusty')
basic_staff = Weapon('Dusty Oak Staff', 'dusty')
armory = {'Trainer Staff':basic_staff, 'Trainer Sword':basic_sword}


three_year_old = Child(child, 'Child That Fell into Enclosure')



magician = Magician(start_new, 'Merlin')
harambe = Gorilla(start_new_enemy, 'Harambe')

harambe.add_to_inventory(loot['treasure'])
    
new_weapon = Armory.get_weapon(magician._type)
new_weapon3 = Armory.get_weapon(magician._type)
new_weapon2 = Armory.get_weapon(harambe._type)

magician.equip(new_weapon)

magician.playerinfo()

magician.remove_item(new_weapon)

magician.playerinfo()


input("Press Enter to Exit")



