#Kandu! Entertainment est. 6/30/2018
#This is the enemy character creator class

from weapon import *

class Enemy:
    
    def __init__(self, attributes):
        
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

    def generate_stats(self):

        return self._attributes

class Hero(Enemy):

    def need_action(self):
        None
