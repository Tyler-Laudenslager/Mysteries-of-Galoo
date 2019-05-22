#Kandu! Entertainment est. 6/30/2018
#This is the weapons/armor/amulet module for Galoo.
import random
import sys
from generator import *
class Weapon:
    
    def __init__(self, name, attributes):
        
        if attributes == 'dusty':
            self._attributes = weapon_dusty_attributes()
        if attributes == 'clean':
            self._attributes = weapon_clean_attributes()
        if attributes == 'shiny':
            self._attributes = weapon_shiny_attributes()
        if attributes == 'forsaken':
            self._attributes = weapon_forsaken_attributes()
        if attributes == 'radiant':
            self._attributes = weapon_radiant_attributes()
            
        self._identity = {name:self._attributes}
        
    def get_id(self):
        return self._identity

class Armor:
    
    def __init__(self, name, attributes):
        
        if attributes == 'dusty' and "Chestplate" in name:
            self._attributes = armor_dusty_attributes('Chestplate')
        elif attributes == 'clean' and "Chestplate" in name:
            self._attributes = armor_clean_attributes('Chestplate')
        elif attributes == 'shiny' and "Chestplate" in name:
            self._attributes = armor_shiny_attributes('Chestplate')
        elif attributes == 'forsaken'and "Chestplate" in name:
            self._attributes = armor_forsaken_attributes('Chestplate')
        elif attributes == 'radiant' and "Chestplate" in name:
            self._attributes = armor_radiant_attributes('Chestplate')
            
        elif attributes == 'dusty' and "Legs" in name:
            self._attributes = armor_dusty_attributes('Legs')
        elif attributes == 'clean' and "Legs" in name:
            self._attributes = armor_clean_attributes('Legs')
        elif attributes == 'shiny' and "Legs" in name:
            self._attributes = armor_shiny_attributes('Legs')
        elif attributes == 'forsaken'and "Legs" in name:
            self._attributes = armor_forsaken_attributes('Legs')
        elif attributes == 'radiant' and "Legs" in name:
            self._attributes = armor_radiant_attributes('Legs')

        elif attributes == 'dusty' and "Gloves" in name:
            self._attributes = armor_dusty_attributes('Gloves')
        elif attributes == 'clean' and "Gloves" in name:
            self._attributes = armor_clean_attributes('Gloves')
        elif attributes == 'shiny' and "Gloves" in name:
            self._attributes = armor_shiny_attributes('Gloves')
        elif attributes == 'forsaken'and "Gloves" in name:
            self._attributes = armor_forsaken_attributes('Gloves')
        elif attributes == 'radiant' and "Gloves" in name:
            self._attributes = armor_radiant_attributes('Gloves')

        elif attributes == 'dusty' and "Helmet" in name:
            self._attributes = armor_dusty_attributes('Helmet')
        elif attributes == 'clean' and "Helmet" in name:
            self._attributes = armor_clean_attributes('Helmet')
        elif attributes == 'shiny' and "Helmet" in name:
            self._attributes = armor_shiny_attributes('Helmet')
        elif attributes == 'forsaken'and "Helmet" in name:
            self._attributes = armor_forsaken_attributes('Helmet')
        elif attributes == 'radiant' and "Helmet" in name:
            self._attributes = armor_radiant_attributes('Helmet')

        elif attributes == 'dusty' and "Boots" in name:
            self._attributes = armor_dusty_attributes('Boots')
        elif attributes == 'clean' and "Boots" in name:
            self._attributes = armor_clean_attributes('Boots')
        elif attributes == 'shiny' and "Boots" in name:
            self._attributes = armor_shiny_attributes('Boots')
        elif attributes == 'forsaken'and "Boots" in name:
            self._attributes = armor_forsaken_attributes('Boots')
        elif attributes == 'radiant' and "Boots" in name:
            self._attributes = armor_radiant_attributes('Boots')
        self._identity = {name:self._attributes}
        
    def get_id(self):
        return self._identity
    
class Amulet:
    
    def __init__(self, name, attributes):
        
        if attributes == 'dusty':
            self._attributes = amulet_dusty_attributes()
        if attributes == 'clean':
            self._attributes = amulet_clean_attributes()
        if attributes == 'shiny':
            self._attributes = amulet_shiny_attributes()
        if attributes == 'forsaken':
            self._attributes = amulet_forsaken_attributes()
        if attributes == 'radiant':
            self._attributes = amulet_radiant_attributes()
            
        self._identity = {name:self._attributes}
        
    def get_id(self):
        return self._identity
 
