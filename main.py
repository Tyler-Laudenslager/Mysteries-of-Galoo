#Kandu! Entertainment 6/30/2018
#This is the main module to run world of Galoo
#! python3
from character import *
import random
from time import sleep
from story import *
import sys
from weapon import *
from armory import *
from enemy_hero_creator import *
from map_creator import *
from game import *
from generator import *
import setup
def setup_character():
    setup.new_equipment_1 = Armory.get_weapon(setup.starting_character._type)
    setup.new_equipment_2 = Armory.get_armor(setup.starting_character._type)
    setup.new_equipment_3 = Armory.get_armor(setup.starting_character._type)
    setup.new_equipment_4 = Armory.get_armor(setup.starting_character._type)
    setup.new_equipment_5 = Armory.get_armor(setup.starting_character._type)
    setup.new_equipment_6 = Armory.get_armor(setup.starting_character._type)
    setup.starting_character.equip(setup.new_equipment_1, 0)
    setup.starting_character.equip(setup.new_equipment_2, 1)
    setup.starting_character.equip(setup.new_equipment_3, 2)
    setup.starting_character.equip(setup.new_equipment_4, 3)
    setup.starting_character.equip(setup.new_equipment_5, 4)
    setup.starting_character.equip(setup.new_equipment_6, 5)
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
            setup.starting_character = Gorilla(radiant_char, name)
            setup.armor_locator = 0

        if choice == '2':
            name = input("Enter name for your Tunneler: ")
            setup.starting_character = Tunneler(radiant_char, name)
            setup.armor_locator = 0
        if choice == '3':
            name = input("Enter name for your Archer: ")
            setup.starting_character = Archer(radiant_char, name)
            setup.armor_locator = 0
        if choice == '4':
            name = input("Enter name for your Alchemist: ")
            setup.starting_character = Alchemist(radiant_char, name)
            setup.armor_locator = 0
        if choice == '5':
            name = input("Enter name for your Knight: ")
            setup.starting_character = Knight(radiant_char, name)
            setup.armor_locator = 0
        if choice == '6':
            name = input("Enter name for your Botanist: ")
            setup.starting_character = Botanist(radiant_char, name)
            setup.armor_locator = 0
        if choice == '7':
            name = input("Enter name for your Priest: ")
            setup.starting_character = Priest(radiant_char, name)
            setup.armor_locator = 0
        if choice == '8':
            name = input("Enter name for your Magician: ")
            setup.starting_character = Magician(radiant_char, name)
            setup.armor_locator = 0
        setup_character()
        enter_galoo()
        intro()
        play_solar_system()
    elif choice == '2':
        sys.exit()

    else:
        print("Choose again")
start_menu()

