#Kandu! Entertaiment est. 6/30/2018
#This is the store module for Mysteries of Galoo.
#This module will set up the store to buy sell inventory using gold
from armory import *
from character import *
from setup import *
import re

class Store:
    def __init__(self, classtype):
        self._classtype = classtype
        self._equipment = setup.starting_character._equipment
        self._inventory = None
        self._in_store = True

    def generate_item(self):
        new_armor_1 = Armory.get_armor(setup.starting_character._type)
        new_armor_2 = Armory.get_armor(setup.starting_character._type)
        new_armor_3 = Armory.get_armor(setup.starting_character._type)
        new_weapon_1 = Armory.get_weapon(setup.starting_character._type)
        new_weapon_2 = Armory.get_weapon(setup.starting_character._type)
        new_weapon_3 = Armory.get_weapon(setup.starting_character._type)
        new_amulet_1 = Armory.get_amulet(setup.starting_character._type)
        new_amulet_2 = Armory.get_amulet(setup.starting_character._type)
        new_amulet_3 = Armory.get_amulet(setup.starting_character._type)

        self._inventory = [[new_armor_1, new_armor_2, new_armor_3],
                           [new_weapon_1, new_weapon_2, new_weapon_3],
                           [new_amulet_1, new_amulet_2, new_amulet_3]]
        return self._inventory[random.randint(0,2)][random.randint(0,2)]
    
    def display_item(self,item):
        print(item)
    def bought_equipped(self):
        print()
        print("Your item has been bought and equipped")
        print()
    def buy_item(self,item):
        self._item = item
        player_item = None
        type_collecter = []
        for key_item, value in self._item.items():
            for key, value in value.items():
                if key == "Worth":
                        gold_value = value

        if setup.starting_character._inventory['Gold'] >= gold_value:
            for item in setup.starting_character._equipment:
                for item_name, attributes in item.items():
                    for attribute_name, attribute_value in attributes.items():
                        if attribute_name == 'Type':
                            type_collecter.append(attribute_value)
                    
            for item_name, value in self._item.items():
                for key, value in value.items():
                    if key == 'Type':
                        bought_value = value
                    if key == 'Worth':
                        worth_value = value

            def index_indicator():
                index = 1
                for type in type_collecter:
                    if bought_value == type:
                        return index
                    else:
                        index += 1
            if index_indicator() == 1:
                player_item = setup.new_equipment_1
            elif index_indicator() == 2:
                player_item = setup.new_equipment_2
            elif index_indicator() == 3:
                player_item = setup.new_equipment_3
            elif index_indicator() == 4:
                player_item = setup.new_equipment_4
            elif index_indicator() == 5:
                player_item = setup.new_equipment_5
            elif index_indicator() == 6:
                player_item = setup.new_equipment_6
            elif index_indicator() == 7:
                player_item = setup.new_equipment_7

            for item_name, attributes in player_item.items():
                for attribute_name, attribute_value in attributes.items():
                    if attribute_name == 'Worth':
                        player_item_worth = attribute_value
            print(player_item_worth)
            print(gold_value)
            setup.starting_character.remove_item(player_item, index_indicator()-1)
            setup.starting_character.equip(self._item, index_indicator()-1)
            setup.starting_character._inventory['Gold'] -= gold_value
            setup.starting_character._inventory['Gold'] += player_item_worth
                            

                        
        else:
            print("You dont have enought gold yet")
    
    def display(self):
        choice = None
        while(choice != 'x'):
            print()
            print("<Welcome to the Store>")
            print("Press 1 to Buy Armor, Weapons, and Amulets")
            print("Press 2 to Sell Armor, Weapons, and Amulets")
            print("Press 3 to Sell Inventory")
            print("Press 'x' to exit the Store")
            choice = str(input("Choice: "))
            
            if choice == "1":
                
                print("Buy Any Item You Wish")
                item_1 = self.generate_item()
                item_2 = self.generate_item()
                item_3 = self.generate_item()
                item_4 = self.generate_item()
                item_5 = self.generate_item()
                print()
                self.display_item(item_1)
                print()
                self.display_item(item_2)
                print()
                self.display_item(item_3)
                print()
                self.display_item(item_4)
                print()
                self.display_item(item_5)
                print()
                print("To Buy an Item Enter the Number [Top to Bottom]")
                option = str(input("Choice: "))
                if(option == '1'):
                    self.buy_item(item_1)
                if(option == '2'):
                    self.buy_item(item_2)
                if(option == '3'):
                    self.buy_item(item_3)
                if(option == '4'):
                    self.buy_item(item_4)
                if(option == '5'):
                    self.buy_item(item_5)
               
            if choice == "3":
                print()
                print("Welcome to the Zizzle's Inventory Bazzar")
                print("Buy Any Item You Wish")
                print("Under Constuction")

              
            else:
               return

        
