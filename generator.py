#Kandu! Entertainment est. 6/30/2018
#This is the generator module for Galoo.

import random

def generate_dusty_attributes():
    Health = random.randint(5,10)
    Energy = random.randint(10,15)
    Strength = random.randint(12,20)
    Defense = random.randint(7,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Dusty'}
    return attributes

def generate_clean_attributes():
    Health = random.randint(35,40)
    Energy = random.randint(35,37)
    Strength = random.randint(40,57)
    Defense = random.randint(5,10)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Clean'}
    return attributes

def generate_shiny_attributes():
    Health = random.randint(450,5000)
    Energy = random.randint(250,300)
    Strength = random.randint(500,1500)
    Defense = random.randint(200,800)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Shiny'}
    return attributes

def generate_forsaken_attributes():
    Health = random.randint(500000,750000)
    Energy = random.randint(200000,300000)
    Strength = random.randint(2000000,350000000)
    Defense = random.randint(700000,1000000)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Forsaken'}
    return attributes

def generate_radiant_attributes():
    Health = random.randint(23432,26533)
    Energy = random.randint(30000,40000)
    Strength = random.randint(120000,250000)
    Defense = random.randint(60000,65000)
    attributes = {'Health':Health, 'Energy':Energy, 'Strength':Strength, 'Defense':Defense, 'Type': 'Radiant'}
    return attributes

