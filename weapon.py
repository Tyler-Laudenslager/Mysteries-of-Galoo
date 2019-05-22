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
        
        if attributes == 'dusty':
            self._attributes = armor_dusty_attributes()
        if attributes == 'clean':
            self._attributes = armor_clean_attributes()
        if attributes == 'shiny':
            self._attributes = armor_shiny_attributes()
        if attributes == 'forsaken':
            self._attributes = armor_forsaken_attributes()
        if attributes == 'radiant':
            self._attributes = armor_radiant_attributes()
            
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
 
