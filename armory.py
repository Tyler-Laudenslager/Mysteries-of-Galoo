#Kandu! Entertainment est. 6/30/2018
#This is the armory module for Galoo.

from weapon import *
import setup
class Armory:
    def get_weapon(classtype):
    
        dusty_sword = Weapon('Dusty Sword', 'dusty')
        dusty_staff = Weapon('Dusty Oak Staff', 'dusty')
        dusty_shield = Weapon('Dusty Shield', 'dusty')
        dusty_dagger = Weapon('Dusty Dagger', 'dusty')
        dusty_bow = Weapon('Dusty Bow', 'dusty')
        
        clean_sword = Weapon('Clean Sword', 'clean')
        clean_staff = Weapon('Clean Staff', 'clean')
        clean_shield = Weapon('Clean Shield', 'clean')
        clean_dagger = Weapon('Clean Dagger', 'clean')
        clean_bow = Weapon('Clean Bow', 'clean')

        shiny_sword = Weapon('Shiny Sword', 'shiny')
        shiny_staff = Weapon('Shiny Staff', 'shiny')
        shiny_shield = Weapon('Shiny Shield', 'shiny')
        shiny_dagger = Weapon('Shiny Dagger', 'shiny')
        shiny_bow = Weapon('Shiny Bow', 'shiny')

        forsaken_sword = Weapon('Forsaken Sword', 'forsaken')
        forsaken_staff = Weapon('Forsaken Staff', 'forsaken')
        forsaken_shield = Weapon('Forsaken Shield', 'forsaken')
        forsaken_dagger = Weapon('Forsaken Dagger', 'forsaken')
        forsaken_bow = Weapon('Forsaken Bow', 'forsaken')

        radiant_sword = Weapon('Radiant Sword', 'radiant')
        radiant_staff = Weapon('Radiant Staff', 'radiant')
        radiant_shield = Weapon('Radiant Shield', 'radiant')
        radiant_dagger = Weapon('Radiant Dagger', 'radiant')
        radiant_bow = Weapon('Radiant Bow', 'radiant')

        armory = [[dusty_sword,dusty_staff,dusty_shield,dusty_dagger,dusty_bow],

                  [clean_sword,clean_staff,clean_shield,clean_dagger,clean_bow],

                  [shiny_sword,shiny_staff,shiny_shield,shiny_dagger,shiny_bow],
                  
                  [forsaken_sword,forsaken_staff,forsaken_shield,forsaken_dagger,shiny_bow],
                  
                  [radiant_sword, radiant_staff, radiant_shield,radiant_dagger,radiant_bow]]

        
        if classtype == 'Magician':
            
            weapon_picked = armory[random.randint(0,4)][random.randint(0,1)]

        if classtype == 'Gorilla':

            weapon_picked = armory[random.randint(0,1)][2]
            
        if classtype == 'Archer':
            weapon_picked = armory[random.randint(0,4)][4]
            
        if classtype == 'Tunneler':
            weapon_picked = armory[random.randint(0,4)][3]
            
        if classtype == 'Alchemist':
            weapon_picked = armory[random.randint(0,4)][1]

        if classtype == 'Knight':
            weapon_picked = armory[random.randint(0,4)][0]

        if classtype == 'Botanist':
            weapon_picked = armory[random.randint(0,4)][1]

        if classtype == 'Priest':
            weapon_picked = armory[random.randint(0,4)][1]

        return weapon_picked.get_id()
    
    
    def get_armor(classtype):

        dusty_chestplate = Armor('Dusty Chestplate', 'dusty')
        dusty_legs = Armor('Dusty Legs', 'dusty')
        dusty_gloves = Armor('Dusty Gloves', 'dusty')
        dusty_helmet = Armor('Dusty Helmet', 'dusty')
        dusty_boots = Armor('Dusty Boots', 'dusty')
        
        clean_chestplate = Armor('Clean Chestplate', 'clean')
        clean_legs = Armor('Clean Legs', 'clean')
        clean_gloves = Armor('Clean Gloves', 'clean')
        clean_helmet = Armor('Clean Helmet', 'clean')
        clean_boots = Armor('Clean Boots', 'clean')

        shiny_chestplate = Armor('Shiny Chestplate', 'shiny')
        shiny_legs = Armor('Shiny Legs', 'shiny')
        shiny_gloves = Armor('Shiny Gloves', 'shiny')
        shiny_helmet = Armor('Shiny Helmet', 'shiny')
        shiny_boots = Armor('Shiny Boots', 'shiny')

        forsaken_chestplate = Armor('Forsaken Chestplate', 'forsaken')
        forsaken_legs = Armor('Forsaken Legs', 'forsaken')
        forsaken_gloves = Armor('Forsaken Gloves', 'forsaken')
        forsaken_helmet = Armor('Forsaken Helmet', 'forsaken')
        forsaken_boots = Armor('Forsaken Boots', 'forsaken')

        radiant_chestplate = Armor('Radiant Chestplate', 'radiant')
        radiant_legs = Armor('Radiant Legs', 'radiant')
        radiant_gloves = Armor('Radiant Gloves', 'radiant')
        radiant_helmet = Armor('Radiant Helmet', 'radiant')
        radiant_boots = Armor('Radiant Boots', 'radiant')


        armory = [[dusty_chestplate,dusty_legs,dusty_gloves,dusty_helmet,dusty_boots],
                  [clean_chestplate,clean_legs,clean_gloves,clean_helmet,clean_boots],
                  [shiny_chestplate,shiny_legs,shiny_gloves,shiny_helmet,shiny_boots],
                  [forsaken_chestplate,forsaken_legs,forsaken_gloves,forsaken_helmet,forsaken_boots],
                  [radiant_chestplate,radiant_legs,radiant_gloves,radiant_helmet,radiant_boots]]
                  
        if classtype == 'Magician':
            
            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.randint(0,4)]
        if classtype == 'Gorilla':
            
            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.randint(0,4)]
        if classtype == 'Archer':
            
            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.randint(0,4)]
            
        if classtype == 'Tunneler':

            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.randint(0,4)]
            
        if classtype == 'Alchemist':

            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.randint(0,4)]

        if classtype == 'Knight':
            
            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.randint(0,4)]


        if classtype == 'Botanist':

            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.raint(0,4)]
        if classtype == 'Priest':

            if setup.armor_locator < 5:
                armor_picked = armory[random.randint(0,4)][setup.armor_locator]
                setup.armor_locator += 1
            else:
                armor_picked = armory[random.randint(0,4)][random.raint(0,4)]

        return armor_picked.get_id()


    def get_amulet(classtype):

        dusty_amulet = Amulet('Rock of the Coast', 'dusty')

        clean_amulet = Amulet('Gem of Ohra', 'clean')
        

        shiny_amulet = Amulet('Glow of Boorathis', 'shiny')

        forsaken_amulet = Amulet('Dark Wisp of Nootros', 'forsaken')

        radiant_amulet = Amulet('Tatron the Gravity Well', 'radiant')
        

        armory = [[dusty_amulet],

                  [clean_amulet],

                  [shiny_amulet],

                  [forsaken_amulet],
                  
                  [radiant_amulet]]

        
        if classtype == 'Magician':
            
            amulet_picked = armory[random.randint(0,4)][0]

        if classtype == 'Gorilla':

            amulet_picked = armory[random.randint(0,4)][0]
            
        if classtype == 'Archer':
            
            amulet_picked = armory[random.randint(0,4)][0]
            
        if classtype == 'Tunneler':
            
            amulet_picked = armory[random.randint(0,4)][0]
            
        if classtype == 'Alchemist':
            
            amulet_picked = armory[random.randint(0,4)][0]

        if classtype == 'Knight':

            amulet_picked = armory[random.randint(0,4)][0]

        if classtype == 'Botanist':
            
            amulet_picked= armory[random.randint(0,4)][0]

        if classtype == 'Priest':
            
            amulet_picked = armory[random.randint(0,4)][0]

        return amulet_picked.get_id()

