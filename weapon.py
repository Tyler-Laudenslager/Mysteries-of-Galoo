#Kandu! Entertainment est. 6/30/2018
#This is the weapons module for Galoo.
import random
import sys
from generator import *
class Weapon:
    
    def __init__(self, name, attributes):
        
        if attributes == 'dusty':
            self._attributes = generate_dusty_attributes()
        if attributes == 'clean':
            self._attributes = generate_clean_attributes()
        if attributes == 'shiny':
            self._attributes = generate_shiny_attributes()
        if attributes == 'forsaken':
            self._attributes = generate_forsaken_attributes()
        if attributes == 'radiant':
            self._attributes = generate_radiant_attributes()
            
        self._identity = {name:self._attributes}
        
    def get_id(self):
        return self._identity


 
