#Kandu! Entertainment est. 6/30/2018
#This is the enemy character creator class

from weapon import *

class Enemy:
    
    def __init__(self, attributes):
        
        if attributes == 'dusty':
            self._attributes = enemy_dusty_attributes()
        if attributes == 'clean':
            self._attributes = enemy_clean_attributes()
        if attributes == 'shiny':
            self._attributes = enemy_shiny_attributes()
        if attributes == 'forsaken':
            self._attributes = enemy_forsaken_attributes()
        if attributes == 'radiant':
            self._attributes = enemy_radiant_attributes()

    def generate_stats(self):

        return self._attributes

class Hero(Enemy):

    def need_action(self):
        None
