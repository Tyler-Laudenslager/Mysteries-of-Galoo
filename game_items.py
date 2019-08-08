
from inventory import *

health_potion = Item('Health Potion', 3)
defense_potion = Item('Defense Potion', 3)
energy_potion = Item('Energy Potion', 2)
strength_potion = Item('Strength Potion', 4)
sapphire = Item('Sapphire', 25)
dirty_clothes = Item('Dirty Clothes', 5)
ruby_necklace = Item('Ruby Necklace', 50)
picture = Item('Autographed Picture of Pee-wee Herman', 200)
diamond = Item('Diamond', 300)


def get_inventory_item(item):
    item -= 1
    cabinet = [health_potion, defense_potion, energy_potion, strength_potion, sapphire, dirty_clothes,
               ruby_necklace, picture, diamond]

    return cabinet[item]
