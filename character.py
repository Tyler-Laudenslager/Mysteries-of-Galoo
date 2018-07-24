#Kandu! Entertainment est. 6/30/2018
#This is the character module for Mysteries of Galoo.
#This module will set up all characters for the game including all spells.

import random
from time import sleep

class Character:
    def __init__(self, setup_new, name):

    
       for key, value in setup_new.items():
           if key == 'health':
               self._base_health = value
           if key == 'energy':
               self._base_energy = value
           if key == 'strength':
               self._base_strength = value
           if key == 'defense':
               self._base_defense = value
               
       self._inventory = {}
       self._equipment = {}
       self._name = name
       self._type = self.__class__.__name__
       self._strength_weapon = 0
       self._defense_weapon = 0
       self._energy_weapon = 0
       self._health_weapon = 0
       self._fight_strength = 0 + self._base_strength
       self._fight_defense = 0 + self._base_defense
       self._fight_energy = 0 + self._base_energy
       self._fight_health = 0 + self._base_health
            

    def equip(self, game_item):
        self._game_item = game_item
        for key, value in game_item.items():
            self._equipment.setdefault(key, value)
            for key, value in value.items():
                if key == 'Strength':
                    self._strength_weapon += value
                    self._fight_strength += value
                if key == 'Health':
                    self._health_weapon += value
                    self._fight_health += value
                if key == 'Energy':
                    self._energy_weapon += value
                    self._fight_energy += value
                if key == 'Defense':
                    self._defense_weapon += value
                    self._fight_defense += value
                    
    def remove_item(self, game_item):
        self._game_item = game_item
        for item_key, value in game_item.items():
            for key, value in value.items():
                if key == 'Strength':
                    self._strength_weapon -= value
                    self._fight_strength -= value
                if key == 'Health':
                    self._health_weapon -= value
                    self._fight_health -= value
                if key == 'Energy':
                    self._energy_weapon -= value
                    self._fight_energy -= value
                if key == 'Defense':
                    self._defense_weapon -= value
                    self._fight_defense -= value
        del self._equipment[item_key]
    def attack(self, target):
        self.target = target
        self.target._fight_health -= self._fight_strength

    def defend(self):
        self._health += self._fight_defense

    def playerinfo(self):
        print()
        print("<Player Information>")
        print("Name: " + self._name)
        print("Type: " + self._type)
        print()
        print("Attributes----------")
        print("Health...... " + str(self._fight_health))
        print("Energy........ " + str(self._fight_energy))
        print("Strength.... " + str(self._fight_strength))
        print("Defense..... " + str(self._fight_defense))
        print()
        self.display_inventory(self._inventory)
        self.display_equipment(self._equipment)

    def display_equipment(self, inventory):
        print()
        print("Equipment:")
        for key in inventory.items():
            print(key)
        print()
    def display_inventory(self, inventory):
        print("Inventory:")
        item_total = 0
        for key, value in inventory.items():
            print(str(value)+ " " + key)
            if key != 'Gold':
                item_total += value
        print("Total number of items: " + str(item_total))

    def add_to_inventory(self, added_items):
        for key, value in added_items.items():
            self._inventory.setdefault(key, 0)
            self._inventory[key] += value

    def fight(self, target):
        self._target = target
        self._defense_counter = 0
        self._target_init_str = self._target._fight_strength
        self._target_init_def = self._target._fight_defense
        self._target_init_ene = self._target._fight_energy
        self._target_init_hea = self._target._fight_health
        self._init_str = self._fight_strength
        self._init_def = self._fight_defense
        self._init_ene = self._fight_energy
        self._init_hea = self._fight_health
        print()
        print("Your fighting %s: " % (self._target._name))

        while self._target._fight_health > 0 and self._fight_health > 0:
            print()
            print("Press Enter to Roll Die")
            print()
            sleep(1)
            choice = str(random.randint(1,4))
            if choice == '1':
                self.attack(self._target)
                print("You did " + str(self._fight_strength) + " damage to %s" % (self._target._name))
                
            elif choice == '2':
                self._fight_health -= self._target._fight_strength
                print("%s did " % (self._target._name) + str(self._target._fight_strength) + " damage to you")
                
            elif choice == '3':
                self._fight_health += self._fight_defense
                self._defense_counter += self._fight_defense
                print("You gained " + str(self._fight_defense) + " armor")
                
            elif choice == '4':
                self._target._fight_health += self._target._fight_defense
                print("%s gained " % (self._target._name) + str(self._target._fight_defense)+ " armor")
                
        self._fight_health = self._init_hea
        self._fight_defense = self._init_def
        self._fight_energy = self._init_ene
        self._fight_strength = self._init_str
            
        self._target._fight_health = self._target_init_hea
        self._target._fight_strength = self._target_init_str
        self._target._fight_defense = self._target_init_def
        self._target._fight_energy = self._target_init_ene
        self.add_to_inventory(self._target._inventory)
        print()
        print("You Defeated %s" % (self._target._name))
        print("You recieved %s's inventory" % (self._target._name))

class Gorilla(Character):

        def rampage(self, target):
            self._health += self._defense
            self.attack(target)
            

class SilverBack(Gorilla):

        def need_action(self, target):
            None

class Tunneler(Character):

        def need_action(self, target):
            None

class Archer(Character):

        def need_action(self, target):
            None

class Alchemist(Character):

        def need_action(self, target):
            None

class Knight(Character):

        def need_action(self, target):
            None

class Botanist(Alchemist):

        def need_action(self, target):
            None

class Priest(Character):

        def need_action(self, target):
            None

class Magician(Character):

        def need_action(self, target):
            None

class Dragon(Character):

        def need_action(self, target):
            None

