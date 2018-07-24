#Kandu! Entertainment est. 6/30/2018
#This is the armory module for Galoo.

from weapon import *
class Armory:
    
    def get_weapon(classtype):
    
        dusty_sword = Weapon('Dusty Sword', 'dusty')
        dusty_staff = Weapon('Dusty Oak Staff', 'dusty')
        dusty_shield = Weapon('Dusty Shield', 'dusty')
        dusty_dagger = Weapon('Dusty Dagger', 'dusty')

        clean_sword = Weapon('Clean Sword', 'clean')
        clean_staff = Weapon('Clean Staff', 'clean')
        clean_shield = Weapon('Clean Shield', 'clean')
        clean_dagger = Weapon('Clean Dagger', 'clean')

        shiny_sword = Weapon('Shiny Sword', 'shiny')
        shiny_staff = Weapon('Shiny Staff', 'shiny')
        shiny_shield = Weapon('Shiny Shield', 'shiny')
        shiny_dagger = Weapon('Shiny Dagger', 'shiny')

        forsaken_sword = Weapon('Forsaken Sword', 'forsaken')
        forsaken_staff = Weapon('Forsaken Staff', 'forsaken')
        forsaken_shield = Weapon('Forsaken Shield', 'forsaken')
        forsaken_dagger = Weapon('Forsaken Dagger', 'forsaken')

        armory = [[dusty_sword,dusty_staff,dusty_shield,dusty_dagger],

              [clean_sword,clean_staff,clean_shield,clean_dagger],

              [shiny_sword,shiny_staff,shiny_shield,shiny_dagger],
                  
              [forsaken_sword,forsaken_staff,forsaken_shield,forsaken_dagger]]

        
        if classtype == 'Magician':
            
            weapon_picked = armory[random.randint(0,3)][random.randint(0,1)]

        if classtype == 'Gorilla':

            weapon_picked = armory[0][random.randint(2,3)]

        return weapon_picked.get_id()
    
    
    def pick_armor():

        None


    def pick_amulet():

        None

