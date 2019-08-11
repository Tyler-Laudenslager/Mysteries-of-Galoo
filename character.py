# Kandu! Entertainment est. 6/30/2018
# This is the character module for Mysteries of Galoo.
# This module will set up all characters for the game including all spells.

import random
from time import sleep


class Character:
    def __init__(self, setup_new, name):

        for key, value in setup_new.items():
            if key == 'Health':
                self._base_health = value
            if key == 'Energy':
                self._base_energy = value
            if key == 'Strength':
                self._base_strength = value
            if key == 'Defense':
                self._base_defense = value

        self._inventory = {}
        self._equipment = []
        self._name = name
        self._gold = 0
        self._type = self.__class__.__name__
        self._strength_weapon = 0
        self._defense_weapon = 0
        self._energy_weapon = 0
        self._health_weapon = 0
        self._game_item = None
        self._fight_strength = 0 + self._base_strength
        self._fight_defense = 0 + self._base_defense
        self._fight_energy = 0 + self._base_energy
        self._fight_health = 0 + self._base_health
        self._experience_points = 0
        self._experience_to_go = 2000
        self._experience_cap = 2000
        self._level = 1

    def equip(self, game_item, position):
        self._game_item = game_item
        for key, value in self._game_item.items():
            self._equipment.insert(position, game_item)
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

    def remove_item(self, game_item, position):
        self._game_item = game_item
        for item_key, value in self._game_item.items():
            self._equipment.pop(position)
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

    def remove_inventory_item(self, item, quantity):
        delete_item = False
        for item_key, value in self._inventory.items():
            if item_key == item:
                if value == quantity:
                    delete_item = True
                else:
                    self._inventory[item_key] -= quantity
            else:
                continue
        if delete_item:
            del self._inventory[item]
        else:
            pass

    def attack(self, target):
        attack_power = random.randint(0, self._fight_strength)
        target._fight_health -= attack_power
        return attack_power

    def defend(self):

        self._health += self._fight_defense

    def update_experience_to_go(self):

        self._experience_to_go = self._experience_cap - self._experience_points

    def increase_experience_ceiling(self):

        self._experience_cap += self._level * 2000

    def check_level(self):

        if self._experience_points >= self._experience_cap:
            self.level_up()
            print("Congratulations You Reached....Level " + str(self._level))
            return True
        else:
            return False

    def add_experience_points(self):

        self._experience_points += 500

    def level_up(self):

        self._level += 1

    def playerinfo(self):
        print()
        print("<Player Information>")
        print("Name: " + self._name)
        print("Class: " + self._type)
        print()
        print("Attributes----------")
        print("Health...... " + str(self._fight_health))
        print("Energy........ " + str(self._fight_energy))
        print("Strength.... " + str(self._fight_strength))
        print("Defense..... " + str(self._fight_defense))
        print()
        print("Level....... " + str(self._level))
        print("Experience Needed to Level Up: " + str(self._experience_to_go))
        print()
        self.display_inventory()
        self.display_equipment()

    def display_equipment(self):
        print()
        print("Equipment:")
        equipment = list(self._equipment)
        for equipment in equipment:
            print(equipment)

    def display_inventory(self):
        print("Inventory:")
        for key, value in self._inventory.items():
            print(str(value) + " " + key)

    def add_to_inventory(self, added_items):
        for key, value in added_items.items():
            self._inventory.setdefault(key, 0)
            self._inventory[key] += value
            if key == 'Gold':
                self._gold += value




class Gorilla(Character):

    def rampage(self, target):
        self._health += self._defense
        for i in range(0, 2):
            self.attack(target)


class Harambe(Gorilla):

    def syringe_of_detergent(self, target):
        for i in range(0, 2):
            self.attack(target)


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


class Goblin(Character):

    def need_action(self, target):
        None


class Dark_Fairy(Character):

    def need_action(self, target):
        None


class Troll(Character):

    def need_action(self, target):
        None


class Sea_serpent(Character):
    def need_action(self, target):
        None


class Trigger_happy_bunny(Character):
    def need_action(self, target):
        None


class Dark_wisp(Character):
    def need_action(self, target):
        None


class Icy_sorcerer(Character):
    def need_action(self, target):
        None


class Tree(Character):
    def need_action(self, target):
        None


class Necromancer(Character):
    def need_action(self, target):
        None