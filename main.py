# Kandu! Entertainment 6/30/2018
# This is the main module to run world of Galoo
# ! python3
from enemy_hero_creator import *
from game import *
from map_creator import *
import save
from os import path
import time

def setup_character():
    setup.new_equipment_1 = get_weapon(setup.starting_character._type)
    setup.new_equipment_2 = get_armor(setup.starting_character._type)
    setup.new_equipment_3 = get_armor(setup.starting_character._type)
    setup.new_equipment_4 = get_armor(setup.starting_character._type)
    setup.new_equipment_5 = get_armor(setup.starting_character._type)
    setup.new_equipment_6 = get_armor(setup.starting_character._type)
    setup.new_equipment_7 = get_amulet(setup.starting_character._type)
    setup.starting_character.equip(setup.new_equipment_1, 0)
    setup.starting_character.equip(setup.new_equipment_2, 1)
    setup.starting_character.equip(setup.new_equipment_3, 2)
    setup.starting_character.equip(setup.new_equipment_4, 3)
    setup.starting_character.equip(setup.new_equipment_5, 4)
    setup.starting_character.equip(setup.new_equipment_6, 5)
    setup.starting_character.equip(setup.new_equipment_7, 6)
    setup.starting_character.add_to_inventory(loot['starting_loot'])
    setup.starting_character.add_to_inventory({'Gold': 10000})


def setup_returning_character(character):
    setup.new_equipment_1 = character._equipment[0]
    setup.new_equipment_2 = character._equipment[1]
    setup.new_equipment_3 = character._equipment[2]
    setup.new_equipment_4 = character._equipment[3]
    setup.new_equipment_5 = character._equipment[4]
    setup.new_equipment_6 = character._equipment[5]
    setup.new_equipment_7 = character._equipment[6]


def start_menu():
    clear_buffer()
    print("Mysteries of Galoo")
    blank_lines(1)
    print("\tPress 1 for New Game")
    if path.exists('save_file.pkl'):
        print("\tPress 2 to Continue")
    blank_lines(1)
    choice = str(input("Choice: "))
    clear_buffer()
    if choice == '1':
        print("New Game!")
        blank_lines(1)
        print("Choose your character:")
        print("Choose: ")
        print("\t1) for Gorilla")
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
            setup.starting_character = Gorilla(dusty_hero, name)
            setup.armor_locator = 0

        elif choice == '2':
            name = input("Enter name for your Tunneler: ")
            setup.starting_character = Tunneler(dusty_hero, name)
            setup.armor_locator = 0
        elif choice == '3':
            name = input("Enter name for your Archer: ")
            setup.starting_character = Archer(dusty_hero, name)
            setup.armor_locator = 0
        elif choice == '4':
            name = input("Enter name for your Alchemist: ")
            setup.starting_character = Alchemist(dusty_hero, name)
            setup.armor_locator = 0
        elif choice == '5':
            name = input("Enter name for your Knight: ")
            setup.starting_character = Knight(dusty_hero, name)
            setup.armor_locator = 0
        elif choice == '6':
            name = input("Enter name for your Botanist: ")
            setup.starting_character = Botanist(dusty_hero, name)
            setup.armor_locator = 0
        elif choice == '7':
            name = input("Enter name for your Priest: ")
            setup.starting_character = Priest(dusty_hero, name)
            setup.armor_locator = 0
        elif choice == '8':
            name = input("Enter name for your Magician: ")
            setup.starting_character = Magician(dusty_hero, name)
            setup.armor_locator = 0
        setup_character()
        enter_galoo()
        intro()
        setup.solar_system = SolarSystem(solar_system)
        setup.solar_system.play_solar_system()
    elif choice == '2' and path.exists('save_file.pkl') and path.exists('solar_system.pkl'):
        setup.starting_character = save.reload_object('save_file.pkl')
        print("Welcome Back to Galoo!")
        sleep(1)
        setup.starting_character.playerinfo()
        setup.armor_locator = 5
        setup_returning_character(setup.starting_character)
        setup.solar_system = save.reload_object('solar_system.pkl')
        setup.solar_system.play_solar_system()

    else:
        print("Choose again")
        time.sleep(0.6)
        start_menu()

if __name__ == '__main__':
    start_menu()
