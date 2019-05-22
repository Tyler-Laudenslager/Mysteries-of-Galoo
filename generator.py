#Kandu! Entertainment est. 6/30/2018
#This is the generator module for Galoo.

import random

def weapon_dusty_attributes():
    Health = random.randint(5,10)
    Energy = random.randint(10,15)
    Strength = random.randint(12,20)
    Defense = random.randint(7,10)
    Gold = random.randint(1,5)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Weapon','Worth': Gold}
    return attributes

def weapon_clean_attributes():
    Health = random.randint(35,40)
    Energy = random.randint(35,37)
    Strength = random.randint(40,57)
    Defense = random.randint(5,10)
    Gold = random.randint(5,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Weapon', 'Worth': Gold}
    return attributes

def weapon_shiny_attributes():
    Health = random.randint(450,500)
    Energy = random.randint(250,300)
    Strength = random.randint(50,150)
    Defense = random.randint(20,80)
    Gold = random.randint(10,15)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Weapon', 'Worth': Gold}
    return attributes

def weapon_forsaken_attributes():
    Health = random.randint(5000,7500)
    Energy = random.randint(200000,300000)
    Strength = random.randint(200,350)
    Defense = random.randint(25,100)
    Gold = random.randint(12,50)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Weapon', 'Worth': Gold}
    return attributes

def weapon_radiant_attributes():
    Health = random.randint(23432,26533)
    Energy = random.randint(300,4000)
    Strength = random.randint(1200,2500)
    Defense = random.randint(60000,65000)
    Gold = random.randint(10,120)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Weapon', 'Worth': Gold}
    return attributes

def armor_dusty_attributes(armor_type):
    Health = random.randint(5,10)
    Energy = random.randint(10,15)
    Strength = random.randint(12,20)
    Defense = random.randint(7,10)
    Gold = random.randint(1,5)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': armor_type,'Worth': Gold}
    return attributes

def armor_clean_attributes(armor_type):
    Health = random.randint(35,40)
    Energy = random.randint(35,37)
    Strength = random.randint(40,57)
    Defense = random.randint(5,10)
    Gold = random.randint(5,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': armor_type, 'Worth': Gold}
    return attributes

def armor_shiny_attributes(armor_type):
    Health = random.randint(450,500)
    Energy = random.randint(250,300)
    Strength = random.randint(50,150)
    Defense = random.randint(20,80)
    Gold = random.randint(10,15)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': armor_type, 'Worth': Gold}
    return attributes

def armor_forsaken_attributes(armor_type):
    Health = random.randint(5000,7500)
    Energy = random.randint(200000,300000)
    Strength = random.randint(200,350)
    Defense = random.randint(25,100)
    Gold = random.randint(12,50)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': armor_type, 'Worth': Gold}
    return attributes

def armor_radiant_attributes(armor_type):
    Health = random.randint(23432,26533)
    Energy = random.randint(300,4000)
    Strength = random.randint(1200,2500)
    Defense = random.randint(60000,65000)
    Gold = random.randint(10,120)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': armor_type, 'Worth': Gold}
    return attributes

def amulet_dusty_attributes():
    Health = random.randint(5,10)
    Energy = random.randint(10,15)
    Strength = random.randint(12,20)
    Defense = random.randint(7,10)
    Gold = random.randint(1,5)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Amulet','Worth': Gold}
    return attributes

def amulet_clean_attributes():
    Health = random.randint(35,40)
    Energy = random.randint(35,37)
    Strength = random.randint(40,57)
    Defense = random.randint(5,10)
    Gold = random.randint(5,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Amulet', 'Worth': Gold}
    return attributes

def amulet_shiny_attributes():
    Health = random.randint(450,500)
    Energy = random.randint(250,300)
    Strength = random.randint(50,150)
    Defense = random.randint(20,80)
    Gold = random.randint(10,15)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Amulet', 'Worth': Gold}
    return attributes

def amulet_forsaken_attributes():
    Health = random.randint(5000,7500)
    Energy = random.randint(200000,300000)
    Strength = random.randint(200,350)
    Defense = random.randint(25,100)
    Gold = random.randint(12,50)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Amulet', 'Worth': Gold}
    return attributes

def amulet_radiant_attributes():
    Health = random.randint(23432,26533)
    Energy = random.randint(300,4000)
    Strength = random.randint(1200,2500)
    Defense = random.randint(60000,65000)
    Gold = random.randint(10,120)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Amulet', 'Worth': Gold}
    return attributes

def enemy_dusty_attributes():
    Health = random.randint(5,10)
    Energy = random.randint(10,15)
    Strength = random.randint(12,20)
    Defense = random.randint(7,10)
    Gold = random.randint(1,5)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense,'Worth': Gold}
    return attributes

def enemy_clean_attributes():
    Health = random.randint(35,40)
    Energy = random.randint(35,37)
    Strength = random.randint(40,57)
    Defense = random.randint(5,10)
    Gold = random.randint(5,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Worth': Gold}
    return attributes

def enemy_shiny_attributes():
    Health = random.randint(450,500)
    Energy = random.randint(250,300)
    Strength = random.randint(50,150)
    Defense = random.randint(20,80)
    Gold = random.randint(10,15)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Worth': Gold}
    return attributes

def enemy_forsaken_attributes():
    Health = random.randint(5000,7500)
    Energy = random.randint(200000,300000)
    Strength = random.randint(200,350)
    Defense = random.randint(25,100)
    Gold = random.randint(12,50)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Worth': Gold}
    return attributes

def enemy_radiant_attributes():
    Health = random.randint(23432,26533)
    Energy = random.randint(300,4000)
    Strength = random.randint(1200,2500)
    Defense = random.randint(60000,65000)
    Gold = random.randint(10,120)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Worth': Gold}
    return attributes

