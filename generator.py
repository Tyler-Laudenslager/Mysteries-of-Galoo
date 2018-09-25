#Kandu! Entertainment est. 6/30/2018
#This is the generator module for Galoo.

import random

def generate_dusty_attributes():
    Health = random.randint(5,10)
    Energy = random.randint(10,15)
    Strength = random.randint(12,20)
    Defense = random.randint(7,10)
    Gold = random.randint(1,5)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Dusty','Worth': Gold}
    return attributes

def generate_clean_attributes():
    Health = random.randint(35,40)
    Energy = random.randint(35,37)
    Strength = random.randint(40,57)
    Defense = random.randint(5,10)
    Gold = random.randint(5,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Clean', 'Worth': Gold}
    return attributes

def generate_shiny_attributes():
    Health = random.randint(450,500)
    Energy = random.randint(250,300)
    Strength = random.randint(50,150)
    Defense = random.randint(20,80)
    Gold = random.randint(10,15)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Shiny', 'Worth': Gold}
    return attributes

def generate_forsaken_attributes():
    Health = random.randint(5000,7500)
    Energy = random.randint(200000,300000)
    Strength = random.randint(200,350)
    Defense = random.randint(25,100)
    Gold = random.randint(12,50)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Forsaken', 'Worth': Gold}
    return attributes

def generate_radiant_attributes():
    Health = random.randint(23432,26533)
    Energy = random.randint(300,4000)
    Strength = random.randint(1200,2500)
    Defense = random.randint(60000,65000)
    Gold = random.randint(10,120)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Radiant', 'Worth': Gold}
    return attributes

