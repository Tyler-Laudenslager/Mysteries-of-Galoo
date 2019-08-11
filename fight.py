from time import sleep
import random


def fight(attacker, target):

    target_init_defense = target._fight_defense
    target_init_health = target._fight_health

    attacker_init_defense = attacker._fight_defense
    attacker_init_health = attacker._fight_health
    attacker_init_strength = attacker._fight_strength
    attacker_init_energy = attacker._fight_energy


    print()
    print("You're fighting %s: " % target._name)

    random_turn = random.randint(0,1)
    if random_turn == 0:
        attacker_turn = True
    else:
        attacker_turn = False

    while target._fight_health > 0 and attacker._fight_health > 0:


        print()
        print()
        sleep(1)
        if attacker_turn:
            attacker_choice = input("Your Move: 1 for Attack 2 for Defend 3 to Use Potion: ")
            print()
            if attacker_choice == '1':
                attack_power = attacker.attack(target)
                print("You did " + str(attack_power) + " damage to %s" % target._name)
                attacker_turn = False

            elif attacker_choice == '2':
                attacker_init_health += attacker_init_defense
                print("You gained " + str(attacker_init_defense) + " armor")
                attacker_turn = False

            elif attacker_choice == '3':
                print("Choose which potion to use")

                attacker.display_inventory()

                choice = input("Choose which potion to use ex \"Health Potion\": ")

                if choice == 'Health Potion':
                    if choice in attacker._inventory.keys():
                        if attacker._inventory[choice] > 0:
                            attacker_init_health += 20
                            print("You gained 20 health")
                            attacker.remove_inventory_item('Health Potion', 1)
                            attacker_turn = False
                    else:
                        print('You do not have any Health Potions')


                if choice == 'Defense Potion':
                    if choice in attacker._inventory.keys():
                        if attacker._inventory[choice] > 0:
                            attacker_init_defense += 20
                            print("You gained 20 armor")
                            attacker.remove_inventory_item('Defense Potion', 1)
                            attacker_turn = False
                    else:
                        print('You do not have any Defense Potions')

                if choice == 'Energy Potion':
                    if choice in attacker._inventory.keys():
                        if attacker._inventory[choice] > 0:
                            attacker_init_energy += 20
                            print("You gained 20 Energy")
                            attacker.remove_inventory_item('Energy Potion', 1)
                            attacker_turn = False
                    else:
                        print('You do not have any Energy Potions')

                if choice == 'Strength Potion':
                    if choice in attacker._inventory.keys():
                        if attacker._inventory[choice] > 0:
                            attacker_init_strength += 30
                            print("You gained 30 strength")
                            attacker.remove_inventory_item('Strength Potion', 1)
                            attacker_turn = False
                    else:
                        print('You do not have any Strength Potions')

        else:
            target_choice = str(random.randint(1, 2))
            if target_choice == '1':
                attack_power = target.attack(attacker)
                print("%s did " % target._name + str(attack_power) + " damage to you")
                attacker_turn = True

            elif target_choice == '2':
                target_init_defense += target._fight_defense
                print("%s gained " % target._name + str(target._fight_defense) + " armor")
                attacker_turn = True

    if target._fight_health <= 0:
        attacker.add_to_inventory(target._inventory)
        print()
        print("You Defeated %s" % target._name)
        sleep(2)
        print("You recieved %s's inventory" % target._name)
        sleep(2)
        attacker.add_experience_points()
        if attacker.check_level() == True:
            attacker.increase_experience_ceiling()
        attacker.update_experience_to_go()
        sleep(0.3)
        attacker.playerinfo()
    elif attacker._fight_health <= 0:

        print()
        print("You have been defeated by %s" % target._name)

    target._fight_defense = target_init_defense
    target._fight_health = target_init_health
    attacker._fight_health = attacker_init_health
    attacker._fight_defense = attacker_init_defense

