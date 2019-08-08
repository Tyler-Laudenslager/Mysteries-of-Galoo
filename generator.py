# Kandu! Entertainment est. 6/30/2018
# This is the generator module for Galoo.

import random


def weapon_dusty_attributes():
    health = random.randint(5, 10)
    energy = random.randint(10, 15)
    strength = random.randint(12, 20)
    defense = random.randint(7, 10)
    gold = random.randint(1, 5)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Weapon', 
                  'Worth': gold}
    return attributes


def weapon_clean_attributes():
    health = random.randint(35, 40)
    energy = random.randint(35, 37)
    strength = random.randint(40, 57)
    defense = random.randint(5, 10)
    gold = random.randint(5, 10)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Weapon', 
                  'Worth': gold}
    return attributes


def weapon_shiny_attributes():
    health = random.randint(450, 500)
    energy = random.randint(250, 300)
    strength = random.randint(50, 150)
    defense = random.randint(20, 80)
    gold = random.randint(10, 15)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Weapon',
                  'Worth': gold}
    return attributes


def weapon_forsaken_attributes():
    health = random.randint(5000, 7500)
    energy = random.randint(200000, 300000)
    strength = random.randint(200, 350)
    defense = random.randint(25, 100)
    gold = random.randint(12, 50)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Weapon', 
                  'Worth': gold}
    return attributes


def weapon_radiant_attributes():
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Weapon', 
                  'Worth': gold}
    return attributes


def armor_dusty_attributes(armor_type):
    health = random.randint(5, 10)
    energy = random.randint(10, 15)
    strength = random.randint(12, 20)
    defense = random.randint(7, 10)
    gold = random.randint(1, 5)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': armor_type, 
                  'Worth': gold}
    return attributes


def armor_clean_attributes(armor_type):
    health = random.randint(35, 40)
    energy = random.randint(35, 37)
    strength = random.randint(40, 57)
    defense = random.randint(5, 10)
    gold = random.randint(5, 10)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': armor_type,
                  'Worth': gold}
    return attributes


def armor_shiny_attributes(armor_type):
    health = random.randint(450, 500)
    energy = random.randint(250, 300)
    strength = random.randint(50, 150)
    defense = random.randint(20, 80)
    gold = random.randint(10, 15)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': armor_type, 
                  'Worth': gold}
    return attributes


def armor_forsaken_attributes(armor_type):
    health = random.randint(5000, 7500)
    energy = random.randint(200000, 300000)
    strength = random.randint(200, 350)
    defense = random.randint(25, 100)
    gold = random.randint(12, 50)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': armor_type, 
                  'Worth': gold}
    return attributes


def armor_radiant_attributes(armor_type):
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': armor_type,
                  'Worth': gold}
    return attributes


def amulet_dusty_attributes():
    health = random.randint(5, 10)
    energy = random.randint(10, 15)
    strength = random.randint(12, 20)
    defense = random.randint(7, 10)
    gold = random.randint(1, 5)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Amulet', 
                  'Worth': gold}
    return attributes


def amulet_clean_attributes():
    health = random.randint(35, 40)
    energy = random.randint(35, 37)
    strength = random.randint(40, 57)
    defense = random.randint(5, 10)
    gold = random.randint(5, 10)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Amulet', 
                  'Worth': gold}
    return attributes


def amulet_shiny_attributes():
    health = random.randint(450, 500)
    energy = random.randint(250, 300)
    strength = random.randint(50, 150)
    defense = random.randint(20, 80)
    gold = random.randint(10, 15)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Amulet',
                  'Worth': gold}
    return attributes


def amulet_forsaken_attributes():
    health = random.randint(5000, 7500)
    energy = random.randint(200000, 300000)
    strength = random.randint(200, 350)
    defense = random.randint(25, 100)
    gold = random.randint(12, 50)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Amulet',
                  'Worth': gold}
    return attributes


def amulet_radiant_attributes():
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Type': 'Amulet', 
                  'Worth': gold}
    return attributes


def enemy_dusty_attributes():
    health = random.randint(5, 10)
    energy = random.randint(10, 15)
    strength = random.randint(12, 20)
    defense = random.randint(7, 10)
    gold = random.randint(1, 5)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_clean_attributes():
    health = random.randint(35, 40)
    energy = random.randint(35, 37)
    strength = random.randint(40, 57)
    defense = random.randint(5, 10)
    gold = random.randint(5, 10)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_shiny_attributes():
    health = random.randint(450, 500)
    energy = random.randint(250, 300)
    strength = random.randint(50, 150)
    defense = random.randint(20, 80)
    gold = random.randint(10, 15)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_forsaken_attributes():
    health = random.randint(5000, 7500)
    energy = random.randint(200000, 300000)
    strength = random.randint(200, 350)
    defense = random.randint(25, 100)
    gold = random.randint(12, 50)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_radiant_attributes():
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_thunderous_attributes():
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_immortal_attributes():
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes


def enemy_legendary_attributes():
    health = random.randint(23432, 26533)
    energy = random.randint(300, 4000)
    strength = random.randint(1200, 2500)
    defense = random.randint(60000, 65000)
    gold = random.randint(10, 120)
    attributes = {'Health': health, 'Energy': energy, 'Strength': strength, 'Defense': defense, 'Worth': gold}
    return attributes
