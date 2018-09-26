#Kandu! Entertaiment est. 6/30/2018
#This is the store module for Mysteries of Galoo.
#This module will set up the store to buy sell inventory using gold
from armory import *
from character import *
from setup import *

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
        for key_item, value in self._item.items():
            for key, value in value.items():
                if key == 'Worth':
                    if setup.starting_character._gold >= value:
                        setup.starting_character.playerinfo()
                        replace = str(input("Type which piece you wish to replace: "))
                        setup.starting_character._inventory['Gold'] -= value
                        if(replace == '1'):
                            setup.starting_character.remove_item(setup.new_equipment_1, 0)
                            setup.new_equipment_1 = self._item
                            setup.starting_character.equip(setup.new_equipment_1, 0)
                            self.bought_equipped()
                        if(replace == '2'):
                            setup.starting_character.remove_item(setup.new_equipment_2, 1)
                            setup.new_equipment_2 = self._item
                            setup.starting_character.equip(setup.new_equipment_2, 1)
                            self.bought_equipped()
                        if(replace == '3'):
                            setup.starting_character.remove_item(setup.new_equipment_3, 2)
                            setup.new_equipment_3 = self._item
                            setup.starting_character.equip(setup.new_equipment_3, 2)
                            self.bought_equipped()
                        if(replace == '4'):
                            setup.starting_character.remove_item(setup.new_equipment_4, 3)
                            setup.new_equipment_4 = self._item
                            setup.starting_character.equip(setup.new_equipment_4, 3)
                            self.bought_equipped()
                        if(replace == '5'):
                            setup.starting_character.remove_item(setup.new_equipment_5, 4)
                            setup.new_equipment_5 = self._item
                            setup.starting_character.equip(setup.new_equipment_5, 4)
                            self.bought_equipped()
                        if(replace == '6'):
                            setup.starting_character.remove_item(setup.new_equipment_6, 5)
                            setup.new_equipment_6 = self._item
                            setup.starting_character.equip(setup.new_equipment_6, 5)
                            self.bought_equipped()
                        
                    else:
                        print("You dont have enought gold yet")
                        
           
    def display_store(self):
        print()
        print("<Welcome to the Store>")
        print("Buy Sell and Window Shop")
        item_1 = self.generate_item()
        item_2 = self.generate_item()
        item_3 = self.generate_item()
        self.display_item(item_1)
        self.display_item(item_2)
        self.display_item(item_3)
        print("To Buy an Item choose which item you wish to buy then type it in top to bottom")
        choice = str(input("Choice: "))
        if(choice == '1'):
            self.buy_item(item_1)
            return
        if(choice == '2'):
            self.buy_item(item_2)
            return
        if(choice == '3'):
            self.buy_item(item_3)
            return
           
           
        

        
