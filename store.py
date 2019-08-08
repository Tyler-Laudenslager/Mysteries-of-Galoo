# Kandu! Entertaiment est. 6/30/2018
# This is the store module for Mysteries of Galoo.
# This module will set up the store to buy sell inventory using gold
from armory import get_armor, get_amulet, get_weapon
from character import *
from game_items import *
import setup


class Store:
    def __init__(self, classtype):
        self._classtype = classtype
        self._equipment = setup.starting_character._equipment
        self._inventory = None
        self._in_store = True
        self._item = None

    def generate_armory_item(self):
        new_armor_1 = get_armor(setup.starting_character._type)
        new_armor_2 = get_armor(setup.starting_character._type)
        new_armor_3 = get_armor(setup.starting_character._type)
        new_weapon_1 = get_weapon(setup.starting_character._type)
        new_weapon_2 = get_weapon(setup.starting_character._type)
        new_weapon_3 = get_weapon(setup.starting_character._type)
        new_amulet_1 = get_amulet(setup.starting_character._type)
        new_amulet_2 = get_amulet(setup.starting_character._type)
        new_amulet_3 = get_amulet(setup.starting_character._type)

        self._inventory = [[new_armor_1, new_armor_2, new_armor_3],
                           [new_weapon_1, new_weapon_2, new_weapon_3],
                           [new_amulet_1, new_amulet_2, new_amulet_3]]
        return self._inventory[random.randint(0, 2)][random.randint(0, 2)]


    def display_item(self, item):
        print(item)

    def bought_equipped(self):
        print()
        print("Your item has been bought and equipped")
        print()

    def bought_inventory(self):
        print()
        print("Your item has been bought and added to your inventory")
        print()
    def sell_inventory_item(self, item, quantity):
        self._item = item
        self._item.zero()
        self._item.increment_quantity(quantity)
        price = self._item.get_price()
        setup.starting_character._inventory['Gold'] += price

    def buy_inventory_item(self, item, quantity):
        self._item = item
        self._item.increment_quantity(quantity)
        price = self._item.get_price()
        if setup.starting_character._inventory['Gold'] >= price:
            setup.starting_character._inventory['Gold'] -= price
            setup.starting_character.add_to_inventory(self._item.get_item())
        else:
            print("You do not have enough gold to purchase that item")




    def buy_armor_item(self, item):
        self._item = item
        player_item = None
        type_collector = []
        for key_item, value in self._item.items():
            for key, value in value.items():
                if key == "Worth":
                    gold_value = value

        if setup.starting_character._inventory['Gold'] >= gold_value:
            for item in setup.starting_character._equipment:
                for item_name, attributes in item.items():
                    for attribute_name, attribute_value in attributes.items():
                        if attribute_name == 'Type':
                            type_collector.append(attribute_value)

            for item_name, value in self._item.items():
                for key, value in value.items():
                    if key == 'Type':
                        bought_value = value
                    if key == 'Worth':
                        worth_value = value

            def index_indicator():
                index = 1
                for type in type_collector:
                    if bought_value == type:
                        return index
                    else:
                        index += 1

            if index_indicator() == 1:
                player_item = setup.new_equipment_1
            elif index_indicator() == 2:
                player_item = setup.new_equipment_2
            elif index_indicator() == 3:
                player_item = setup.new_equipment_3
            elif index_indicator() == 4:
                player_item = setup.new_equipment_4
            elif index_indicator() == 5:
                player_item = setup.new_equipment_5
            elif index_indicator() == 6:
                player_item = setup.new_equipment_6
            elif index_indicator() == 7:
                player_item = setup.new_equipment_7

            for item_name, attributes in player_item.items():
                for attribute_name, attribute_value in attributes.items():
                    if attribute_name == 'Worth':
                        player_item_worth = attribute_value

            setup.starting_character.remove_item(player_item, index_indicator() - 1)
            setup.starting_character.equip(self._item, index_indicator() - 1)
            setup.starting_character._inventory['Gold'] -= gold_value
            setup.starting_character._inventory['Gold'] += player_item_worth



        else:
            print("You dont have enought gold yet")

    def display(self):
        choice = None
        while choice != 'x':
            print()
            print("<Welcome to the Store>")
            print("Press 1 to Buy Armor, Weapons, and Amulets")
            print("Press 2 to Buy or Sell Inventory")
            print("Press 'x' to exit the Store")
            choice = str(input("Choice: "))

            if choice == "1":
                while choice != 'x':
                    item_1 = self.generate_armory_item()
                    item_2 = self.generate_armory_item()
                    item_3 = self.generate_armory_item()
                    item_4 = self.generate_armory_item()
                    item_5 = self.generate_armory_item()
                    print()
                    print("""Welcome to Zizzle's Armory
                    
Buy any item you wish there are only five items to choose from...
Once you buy a item from the store that same type of armor, weapon or amulet in your equipment 
will then be sold to the store and replaced with the armor, weapon, or amulet you purchase
                    
Happy Hunting! (press x to exit)""")
                    sleep(8)
                    print()
                    self.display_item(item_1)
                    sleep(2)
                    print()
                    self.display_item(item_2)
                    sleep(2)
                    print()
                    self.display_item(item_3)
                    sleep(2)
                    print()
                    self.display_item(item_4)
                    sleep(2)
                    print()
                    self.display_item(item_5)
                    sleep(2)
                    print()
                    try:
                        print("To Buy an Item Enter the Number [Top to Bottom]")
                        choice = str(input("Choice: "))
                        choices = ['1', '2', '3', '4', '5']
                        if choice in choices:
                            if choice == '1':

                                self.buy_armor_item(item_1)

                            elif choice == '2':

                                self.buy_armor_item(item_2)

                            elif choice == '3':

                                self.buy_armor_item(item_3)

                            elif choice == '4':

                                self.buy_armor_item(item_4)

                            elif choice == '5':

                                self.buy_armor_item(item_5)
                            self.bought_equipped()
                            buy_again = input("Do you wish to buy another item?: ")
                            if buy_again in ['n', 'N', 'No']:
                                choice = 'x'
                            else:
                                continue
                            sleep(2)
                        else:
                            print()
                            print("Please select a piece of equipment from above or press x to exit the store")
                            sleep(2)
                    except TypeError:
                        print("Please select and enter a number from the items above")
                        sleep(2)
                    except ValueError:
                        print("Please select and enter a number from the items above")
                        sleep(2)
            if choice == "2":
                print("Press 1 to Buy Inventory")
                print("Press 2 to Sell Inventory")
                choice = input("Choice: ")

                if choice == '1':

                    while choice != 'x':
                        item_1 = get_inventory_item(1)
                        item_2 = get_inventory_item(2)
                        item_3 = get_inventory_item(3)
                        item_4 = get_inventory_item(4)
                        print()
                        print("Welcome to the Zizzle's Inventory Bazzar")
                        print("Buy Any Item You Wish")
                        print("Health Potion")
                        print("Defense Potion")
                        print("Energy Potion")
                        print("Strength Potion")
                        try:
                            print("To Buy an Item Enter the Number [Top to Bottom]")
                            choice = str(input("Choice: "))
                            choices = ['1', '2', '3', '4']
                            if choice in choices:
                                if choice == '1':
                                    quantity = int(input("How many do you want?: "))
                                    self.buy_inventory_item(item_1, quantity)

                                elif choice == '2':
                                    quantity = int(input("How many do you want?: "))
                                    self.buy_inventory_item(item_2, quantity)

                                elif choice == '3':
                                    quantity = int(input("How many do you want?: "))
                                    self.buy_inventory_item(item_3, quantity)

                                elif choice == '4':
                                    quantity = int(input("How many do you want?: "))
                                    self.buy_inventory_item(item_4, quantity)

                                self.bought_inventory()
                                buy_again = input("Do you wish to buy another item?: ")
                                if buy_again in ['n', 'N', 'No']:
                                    choice = 'x'
                                else:
                                    continue
                                sleep(2)
                            else:
                                print()
                                print("Please select an item from above or press x to exit the store")
                                sleep(2)
                        except ValueError:
                            print("Please select and enter a number from the items above")
                            sleep(2)

                if choice == '2':
                    while choice != 'x':
                        print()
                        print("Which item do you wish to sell from inventory")
                        print("Type name of item and quantity")
                        setup.starting_character.display_inventory()
                        try:
                            item = input("Choice of Item ex...(Health Potion): ")
                            quantity = int(input("Quantity to remove ex..(2, 3, 4): "))
                            setup.starting_character.remove_inventory_item(item, quantity)
                            if item == 'Health Potion':
                                item = get_inventory_item(1)
                            elif item == 'Defense Potion':
                                item = get_inventory_item(2)
                            elif item == 'Energy Potion':
                                item = get_inventory_item(3)
                            elif item == 'Strength Potion':
                                item = get_inventory_item(4)
                            elif item == 'Sapphire':
                                item = get_inventory_item(5)
                            elif item == 'Dirty Clothes':
                                item = get_inventory_item(6)
                            elif item == 'Ruby Necklace':
                                item = get_inventory_item(7)
                            elif item == 'Autographed Picture of Pee-wee Herman':
                                item = get_inventory_item(8)
                            elif item == 'Diamond':
                                item = get_inventory_item(9)
                            self.sell_inventory_item(item, quantity)
                            print("Transaction Completed")
                            print()
                            sell_again = input("Would you like to sell another item?: ")
                            if sell_again in ['n', 'N', 'no', 'No']:
                                choice = 'x'
                            else:
                                continue
                        except ValueError:
                            print("Try again")
            else:
                return
