from time import sleep
import random


def fight(attacker, target):

    target_init_defense = target._fight_defense
    target_init_health = target._fight_health

    attacker_init_defense = attacker._fight_defense
    attacker_init_health = attacker._fight_health


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
            attacker_choice = input("Your Move: 1 for Attack 2 for Defend: ")
            print()
            if attacker_choice == '1':
                attack_power = attacker.attack(target)
                print("You did " + str(attack_power) + " damage to %s" % target._name)
                attacker_turn = False

            elif attacker_choice == '2':
                attacker_init_health += attacker_init_defense
                print("You gained " + str(attacker_init_defense) + " armor")
                attacker_turn = False
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
