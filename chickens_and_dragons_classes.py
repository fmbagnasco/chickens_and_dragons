#setup of the Hero class

import random

from time import *

#text unroll function

def text_unroll(text):
    string = str(text)
    for letter in string:
        print(letter, end = "")
        sleep(0.02)

class Hero:

    #basic class attributes

    race_attributes = {
        "Resilience": 0,
        "Strength": 0,
        "Agility": 0
    }

    clas_attributes = {
        "Sword": 0,
        "Axe": 0,
        "Mace": 0,
        "Light armour": 0,
        "Heavy armour": 0
    }

    inventory = {
        "Small health": 0,
        "Large health": 0,
        "Weapon": "",
        "Helmet": "",
        "Cuirass": "",
        "Boots": ""
    }

    hp = 0
    max_hp = 0

    #race and class defined in the constructor

    def __init__(self, name, race, clas):
        self.race = race
        self.clas = clas
        self.name = name

        #different classes and races defined here

        if race == "Human":
            self.race_attributes["Resilience"] = 4
            self.race_attributes["Strength"] = 3
            self.race_attributes["Agility"] = 3
        elif race == "Orc":
            self.race_attributes["Resilience"] = 4
            self.race_attributes["Strength"] = 5
            self.race_attributes["Agility"] = 1
        elif race == "Elf":
            self.race_attributes["Resilience"] = 3
            self.race_attributes["Strength"] = 2
            self.race_attributes["Agility"] = 5

        if clas == "Barbarian":
            self.clas_attributes["Sword"] = 1
            self.clas_attributes["Axe"] = 5
            self.clas_attributes["Mace"] = 3
            self.clas_attributes["Light armour"] = 3
            self.clas_attributes["Heavy armour"] = 3
            self.inventory["Weapon"] = Weapon("Hatchet")
        elif clas == "Paladin":
            self.clas_attributes["Sword"] = 3
            self.clas_attributes["Axe"] = 1
            self.clas_attributes["Mace"] = 5
            self.clas_attributes["Light armour"] = 1
            self.clas_attributes["Heavy armour"] = 5
            self.inventory["Weapon"] = Weapon("Club")
        elif clas == "Scout":
            self.clas_attributes["Sword"] = 5
            self.clas_attributes["Axe"] = 3
            self.clas_attributes["Mace"] = 1
            self.clas_attributes["Light armour"] = 4
            self.clas_attributes["Heavy armour"] = 2
            self.inventory["Weapon"] = Weapon("Short sword")

        #hero HP

        self.hp = (self.race_attributes["Resilience"] + self.race_attributes["Strength"]) * 10
        self.max_hp = (self.race_attributes["Resilience"] + self.race_attributes["Strength"]) * 10

    def __repr__(self):
        return self.name + " the " + self.race + " " + self.clas

    #movement function

    def movement(self, hero, level):
        monster = 0
        monster_chances = random.randint(1, 100)

        if level == 0:

            if monster_chances < 61:
                monster = Monster("Chicken Scout")
            elif monster_chances < 91:
                monster = Monster("Dragon Fighter")
            elif monster_chances < 96:
                monster = Monster("Chicken Overlord")
            elif monster_chances <= 100:
                monster = Monster("Dragon Master")

        if level == 1:

            if monster_chances < 16:
                monster = Monster("Chicken Scout")
            elif monster_chances < 31:
                monster = Monster("Dragon Fighter")
            elif monster_chances < 81:
                monster = Monster("Chicken Overlord")
            elif monster_chances <= 100:
                monster = Monster("Dragon Master")
        
        text_unroll("\nLooks like you have encountered a monster!")
        text_unroll("\nA dreadful {} stands in your way!".format(monster.name))
        fight(hero, monster)


    #inventory check function

    def inventory_check(self, item):
        if isinstance(item, Weapon):
            text_unroll("\nYour current weapon is {}".format(self.inventory["Weapon"]))
            text_unroll("\nDo you want substitute it for the new weapon instead? y/n\n")
            user_answer = input()
            if user_answer == "y":
                self.inventory["Weapon"] = item
                text_unroll("\nCongratuation! Your new weapon is a {}".format(item))
            if user_answer == "n":
                text_unroll("\nYou decided to keep your old weapon instead.\nMay it continue to serve you well.")
        elif isinstance(item, Armor):

            if self.inventory[item.armor_stats["Part"]] == "":
                text_unroll("\nYou have no {}!".format(item.armor_stats["Part"]))
                self.inventory[item.armor_stats["Part"]] = item
                text_unroll("\nYou wear your brand new {}!".format(item))
            else:
                text_unroll("\nYour current {} is a {}.".format(item.armor_stats["Part"], self.inventory[item.armor_stats["Part"]]))
                text_unroll("\nDo you want to substitute it? y/n\n")
                user_answer = input()
                if user_answer == "y":
                    self.inventory[item.armor_stats["Part"]] = item
                    text_unroll("\nYou wear your brand new {}!".format(item))
                elif user_answer == "n":
                    text_unroll("\nYou keep your current {}.".format(item.armor_stats["Part"]))

        elif isinstance(item, Potion):
            if item.name == "Small health potion":
                self.inventory["Small health"] += 1
                text_unroll("\nYou now have {} small health potions.".format(self.inventory["Small health"]))
            elif item.name == "Large health potion":
                self.inventory["Large health"] += 1
                text_unroll("\nYou now have {} large health potions.".format(self.inventory["Large health"]))

    #inventory inquiry function

    def inventory_inquiry(self):
        cont = True

        while cont == True:
        
            text_unroll("\n What would you like to know?\nWrite 'w' for your current weapon,\n'b' for your boots,\n'c' for your cuirass,\n and 'h' for your helmet")
            text_unroll("\nYou can also write 'p' if you want to know\nhow many potions you still have.\n")
            answer = input()

            if answer == "w":
                text_unroll("\nYour current weapon is: {}".format(self.inventory["Weapon"]))
            elif answer == "b":
                if self.inventory["Boots"] == "":
                    text_unroll("\nYou currently have no boots!\nKill monsters for a chance to get some.")
                else:
                    text_unroll("\nYour current boots are: {}".format(self.inventory["Boots"]))
            elif answer == "c":
                if self.inventory["Cuirass"] == "":
                    text_unroll("\nYou currently have no cuirass!\nKill monsters for a chance to get one.")
                else:
                    text_unroll("\nYour current cuirass is: {}".format(self.inventory["Cuirass"]))
            elif answer == "h":
                if self.inventory["Helmet"] == "":
                    text_unroll("\nYou currently have no helmet!\nKill monsters for a chance to get one.")
                else:
                    text_unroll("\nYour current helmet is: {}".format(self.inventory["Helmet"]))
            elif answer == "p":
                if self.inventory["Small health"] == 0 and self.inventory["Large health"] == 0:
                    text_unroll("\nYou currently have no health potions!\nKill monsters for a chance to get some.")
                else:
                    text_unroll("\nYou have: {} small health potions.".format(self.inventory["Small health"]))
                    text_unroll("\nand {} large health potions.".format(self.inventory["Large health"]))
            
            text_unroll("\nWould you like to check anything else? y/n\n")
            answer = input()

            if answer == "y":
                continue
            elif answer == "n":
                cont = False

    #attack function

    def attack(self, monster):

        proficiency = 0

        if self.inventory["Weapon"].weapon_stats["Type"] == "Sword":
            proficiency = self.clas_attributes["Sword"]
        if self.inventory["Weapon"].weapon_stats["Type"] == "Axe":
            proficiency = self.clas_attributes["Axe"]
        if self.inventory["Weapon"].weapon_stats["Type"] == "Mace":
            proficiency = self.clas_attributes["Mace"]

        attack_damage = ((proficiency * 2) + (self.race_attributes["Strength"] * 2) + self.inventory["Weapon"].weapon_stats["Damage"]) / 2

        attack_coefficient = ((proficiency * 2) + (self.race_attributes["Agility"] * 2) + self.inventory["Weapon"].weapon_stats["Speed"]) / 2

        chances = (attack_coefficient * 25) / monster.monster_attributes["Defence"]

        if random.randint(1, 100) < chances:
            return attack_damage
        else:
            return 0

    #flee function

    def flee(self):
        text_unroll("\nYou run away from the fight!")

    #defence function

    def defence(self, monster):

        armour_coefficient = 0

        #calculate armour-coefficient based on inventory

        if self.inventory["Helmet"] != "":
            if self.inventory["Helmet"].armor_stats["Type"] == "Light":
                armour_coefficient += self.inventory["Helmet"].armor_stats["Protection"] * self.clas_attributes["Light armour"]
            if self.inventory["Helmet"].armor_stats["Type"] == "Heavy":
                armour_coefficient += self.inventory["Helmet"].armor_stats["Protection"] * self.clas_attributes["Heavy armour"]
        if self.inventory["Cuirass"] != "":
            if self.inventory["Cuirass"].armor_stats["Type"] == "Light":
                armour_coefficient += self.inventory["Cuirass"].armor_stats["Protection"] * self.clas_attributes["Light armour"]
            if self.inventory["Cuirass"].armor_stats["Type"] == "Heavy":
                armour_coefficient += self.inventory["Cuirass"].armor_stats["Protection"] * self.clas_attributes["Heavy armour"]
        if self.inventory["Boots"] != "":
            if self.inventory["Boots"].armor_stats["Type"] == "Light":
                armour_coefficient += self.inventory["Boots"].armor_stats["Protection"] * self.clas_attributes["Light armour"]
            if self.inventory["Boots"].armor_stats["Type"] == "Heavy":
                armour_coefficient += self.inventory["Boots"].armor_stats["Protection"] * self.clas_attributes["Heavy armour"]

        armour_coefficient /= 2
        
        defence_coefficient = (armour_coefficient + self.race_attributes["Agility"]) / 2

        #chances and result

        chances = (100 * monster.monster_attributes["Defence"]) / (defence_coefficient * 2.75)

        new_hp = self.hp - monster.monster_attributes["Attack damage"]

        if random.randint(1, 100) < chances:
            text_unroll("\nYou got hit!")
            text_unroll("\nThe monster dealt {} damage!".format(round(monster.monster_attributes["Attack damage"], 2)))
            text_unroll("\nYou have {} hp!".format(round(new_hp, 2)))
            self.hp = new_hp
        else:
            text_unroll("\nThe monster missed you!")

    #take potion function

    def take_potion(self):
        text_unroll("You have {} health points out of {}".format(self.hp, self.max_hp))
        if self.inventory["Small health"] != 0 and self.inventory["Large health"] != 0:
            text_unroll("\nDo you wanna take a small\nor a large health potion?")
            text_unroll("\nWrite 'small' or 'large'.\n")
            answer = input()
            if answer == "small":
                if self.hp <= self.max_hp - 20:
                    self.hp += 20
                else:
                    self.hp = self.max_hp
                self.inventory["Small health"] -= 1
                text_unroll("\nThe potions gives you your streagth back!")
                text_unroll("You now have {} health points".format(self.hp))
                text_unroll("\nYou still have {} small health potions.".format(self.inventory["Small health"]))
            if answer == "large":
                self.hp += 50
                if self.hp <= self.max_hp - 50:
                    self.hp += 50
                else:
                    self.hp = self.max_hp
                self.inventory["Large health"] -= 1
                text_unroll("\nThe potions gives you your streagth back!")
                text_unroll("\nYou now have {} health points".format(self.hp))
                text_unroll("\nYou still have {} large health potions.".format(self.inventory["Large health"]))
        elif self.inventory["Small health"] != 0 and self.inventory["Large health"] == 0:
            text_unroll("\nYou only have small health potions.\nYou take one!")
            self.hp += 20
            if self.hp <= self.max_hp - 20:
                    self.hp += 20
            else:
                self.hp = self.max_hp
            self.inventory["Small health"] -= 1
            text_unroll("\nThe potions gives you your streagth back!")
            text_unroll("\nYou now have {} health points".format(self.hp))
            text_unroll("\nYou still have {} small health potions.".format(self.inventory["Small health"]))
        elif self.inventory["Large health"] != 0 and self.inventory["Small health"] == 0:
            text_unroll("\nYou only have large health potions.\nYou take one!")
            self.hp += 50
            if self.hp <= self.max_hp - 50:
                    self.hp += 50
            else:
                self.hp = self.max_hp
            self.inventory["Large health"] -= 1
            text_unroll("\nThe potions gives you your streagth back!")
            text_unroll("You now have {} health points".format(self.hp))
            text_unroll("\nYou still have {} large health potions.".format(self.inventory["Large health"]))
        elif self.inventory["Large health"] == 0 and self.inventory["Small health"] == 0:
            text_unroll("\nYou do not have health potions!")

    #end of combat function

    def end_of_combat(self, monster):
        text_unroll("\nThe monster dropped a {}!".format(monster.dropped_item))

        self.inventory_check(monster.dropped_item)

#setup of the Monster class

class Monster:

    #basic class attributes

    monster_attributes = {"HP": 0, "Attack damage": 0, "Defence": 0, "Type": ""}        #dict or single separate ints?

    #constructor

    def __init__(self, name):
        self.name = name

        #calculate drop rates

        dropped_item = 0

        drop_calculator_1 = random.randint(1, 10)
        drop_calculator_2 = random.randint(1, 9)
        drop_calculator_3 = random.randint(1, 100)

        if drop_calculator_1 < 4:
            if drop_calculator_2 < 4:
                if drop_calculator_3 < 51:
                    dropped_item = Weapon("Short sword")
                elif drop_calculator_3 < 86:
                    dropped_item = Weapon("Long sword")
                else:
                    dropped_item = Weapon("Claymore")
            elif drop_calculator_2 < 7:
                if drop_calculator_3 < 51:
                    dropped_item = Weapon("Hatchet")
                elif drop_calculator_3 < 86:
                    dropped_item = Weapon("Battle Axe")
                else:
                    dropped_item = Weapon("Two-handed axe")
            else:
                if drop_calculator_3 < 51:
                    dropped_item = Weapon("Club")
                elif drop_calculator_3 < 86:
                    dropped_item = Weapon("War mace")
                else:
                    dropped_item = Weapon("War hammer")
        elif drop_calculator_1 < 7:
            if drop_calculator_2 < 6:
                if drop_calculator_3 < 34:
                    dropped_item = Armor("Light helmet")
                elif drop_calculator_3 < 67:
                    dropped_item = Armor("Light cuirass")
                else:
                    dropped_item = Armor("Light boots")
            else:
                if drop_calculator_3 < 34:
                    dropped_item = Armor("Heavy helmet")
                elif drop_calculator_3 < 67:
                    dropped_item = Armor("Heavy cuirass")
                else:
                    dropped_item = Armor("Heavy boots")
        else:
            if drop_calculator_3 < 76:
                dropped_item = Potion("Small health potion")
            else:
                dropped_item = Potion("Large health potion")


        #just like for the Hero class

        if name == "Chicken Scout":
            self.monster_attributes["HP"] = 10
            self.monster_attributes["Attack damage"] = 7
            self.monster_attributes["Defence"] = 1
            self.monster_attributes["Type"] = "Minion"
            self.dropped_item = dropped_item
        elif name == "Dragon Fighter":
            self.monster_attributes["HP"] = 15
            self.monster_attributes["Attack damage"] = 7
            self.monster_attributes["Defence"] = 2
            self.monster_attributes["Type"] = "Minion"
            self.dropped_item = dropped_item
        elif name == "Chicken Overlord":
            self.monster_attributes["HP"] = 40
            self.monster_attributes["Attack damage"] = 15
            self.monster_attributes["Defence"] = 4
            self.monster_attributes["Type"] = "Boss"
            self.dropped_item = dropped_item
        elif name == "Dragon Master":
            self.monster_attributes["HP"] = 60
            self.monster_attributes["Attack damage"] = 25
            self.monster_attributes["Defence"] = 5
            self.monster_attributes["Type"] = "Boss"
            self.dropped_item = dropped_item
        elif name == "Chickenator the Soulless King of Dragons":
            self.monster_attributes["HP"] = 100
            self.monster_attributes["Attack damage"] = 40
            self.monster_attributes["Defence"] = 10
            self.monster_attributes["Type"] = "Final boss"
            self.dropped_item = dropped_item

#setup of the weapon class

class Weapon:
    
    #basic class attributes

    weapon_stats = {"Type": "", "Damage": 0, "Speed": 0}

    #constructor

    def __init__(self, name):
        self.name = name

        #define types

        if name == "Short sword":
            self.weapon_stats["Type"] = "Sword"
            self.weapon_stats["Damage"] = 4
            self.weapon_stats["Speed"] = 5
        elif name == "Long sword":
            self.weapon_stats["Type"] = "Sword"
            self.weapon_stats["Damage"] = 6
            self.weapon_stats["Speed"] = 4
        elif name == "Claymore":
            self.weapon_stats["Type"] = "Sword"
            self.weapon_stats["Damage"] = 10
            self.weapon_stats["Speed"] = 2
        elif name == "Hatchet":
            self.weapon_stats["Type"] = "Axe"
            self.weapon_stats["Damage"] = 4
            self.weapon_stats["Speed"] = 5
        elif name == "Battle axe":
            self.weapon_stats["Type"] = "Axe"
            self.weapon_stats["Damage"] = 8
            self.weapon_stats["Speed"] = 3
        elif name == "Two-handed axe":
            self.weapon_stats["Type"] = "Axe"
            self.weapon_stats["Damage"] = 10
            self.weapon_stats["Speed"] = 2
        elif name == "Club":
            self.weapon_stats["Type"] = "Mace"
            self.weapon_stats["Damage"] = 6
            self.weapon_stats["Speed"] = 4
        elif name == "War mace":
            self.weapon_stats["Type"] = "Mace"
            self.weapon_stats["Damage"] = 8
            self.weapon_stats["Speed"] = 3
        elif name == "War hammer":
            self.weapon_stats["Type"] = "Mace"
            self.weapon_stats["Damage"] = 10
            self.weapon_stats["Speed"] = 2

    def __repr__(self):
        return self.name

#setup of the armor class

class Armor:

    #basic class attributes

    armor_stats = {"Type": "", "Part": "", "Protection": 0}

    #constructor

    def __init__(self, name):
        self.name = name

        #define types

        if name == "Light helmet":
            self.armor_stats["Type"] = "Light"
            self.armor_stats["Part"] = "Helmet"
            self.armor_stats["Protection"] = 1
        elif name == "Light cuirass":
            self.armor_stats["Type"] = "Light"
            self.armor_stats["Part"] = "Cuirass"
            self.armor_stats["Protection"] = 3
        elif name == "Light boots":
            self.armor_stats["Type"] = "Light"
            self.armor_stats["Part"] = "Boots"
            self.armor_stats["Protection"] = 1
        elif name == "Heavy helmet":
            self.armor_stats["Type"] = "Heavy"
            self.armor_stats["Part"] = "Helmet"
            self.armor_stats["Protection"] = 2
        elif name == "Heavy cuirass":
            self.armor_stats["Type"] = "Heavy"
            self.armor_stats["Part"] = "Cuirass"
            self.armor_stats["Protection"] = 5
        elif name == "Heavy boots":
            self.armor_stats["Type"] = "Heavy"
            self.armor_stats["Part"] = "Boots"
            self.armor_stats["Protection"] = 2

    def __repr__(self):
        return self.name

#setup of the potion class

class Potion:

    #basic attributes

    potion_benefits = {"Health increase": 0, "Strength increase": 0}

    #constructor:

    def __init__(self, name):
        self.name = name

        #define types

        if name == "Small health potion":
            self.potion_benefits["Health increase"] = 20
        elif name == "Large health potion":
            self.potion_benefits["Health increase"] = 50

    def __repr__(self):
        return self.name


def fight(hero, enemy):

    fight = True

    while fight == True:

        text_unroll("\nDo you want to attack, take a potion, or flee?\nWrite 'a' for attack, 'p' for potion, or 'f' to flee from the fight.\n")

        answer = input()

        if answer == "a":
            damage = hero.attack(enemy)
            if damage > 0:
                enemy.monster_attributes["HP"] -= damage
                text_unroll("\nYou attack the monster!")
                text_unroll("\nYou hit the monster!")
                text_unroll("\nYou deal {} damage!".format(round(damage, 2)))

                if enemy.monster_attributes["HP"] > 0:
                    text_unroll("\nThe monster still has {} health points!".format(round(enemy.monster_attributes["HP"], 2)))
                    text_unroll("\nNow the monster attacks you!")
                    hero.defence(enemy)

                elif enemy.monster_attributes["HP"] <= 0:
                    text_unroll("\nYou killed the monster!")
                    hero.end_of_combat(enemy)
                    fight = False
            elif hero.attack(enemy) == 0:
                text_unroll("\nAnd... \nYou miss!")
                text_unroll("\nNow the monster attacks you!")
                hero.defence(enemy)
        elif answer == "f":
            hero.flee()
            fight = False

        elif answer == "p":
            hero.take_potion()
            text_unroll("\nNow the monster attacks you!")
            hero.defence(enemy)

        if hero.hp <= 0:
            text_unroll("\nYou are dead!\nGame over!")
            fight = False

def travel(hero):
    level = 0

    text_unroll("\nWhere do you want to go?\nYou can choose destinations with mostly minions,\nor destinations with a high chance of encounering a boss:")
    text_unroll("\nWrite 'm' for minions,  or 'b' for bosses.\n")

    difficulty = input()

    if difficulty == "m":
        text_unroll("\nYou chose the less risky option!\nThese are your possible destinations:")
        text_unroll("\n- The Venomous Valley.\n- The Dangerous Dale.\n- The Frightening Forest.\n- The Grotesque Glade.\n- The Ravenous River.")
        text_unroll("\nWrite the corresponding letter,\nv, d, f, g, or r to choose the destination.\n")
        answer = input()
        if answer == "v":
            destination = "The Venomous Valley"
        elif answer == "d":
            destination = "The Dangerous Dale"
        elif answer == "f":
            destination = "The Frightening Forest"
        elif answer == "g":
            destination = "The Grotesque Glade"
        elif answer == "r":
            destination = "The Ravenous River"
        text_unroll("You travel to the {}!".format(destination))
        hero.movement(hero, level)
    elif difficulty == "b":
        level = 1
        text_unroll("\nYou chose risk and likely death!\nThese are your possible destinations:")
        text_unroll("\n- The Sinister Summit.\n- The Gnarled Gorge.\n- The Revolting Ravine.\n- The Daunting Desert.\n- The Vomiting Volcano.")
        text_unroll("\nWrite the corresponding letter,\ns, g, r, d, or v to choose the destination.\n")
        answer = input()
        if answer == "s":
            destination = "The Sinister Summit"
        elif answer == "g":
            destination = "The Gnarled Gorge"
        elif answer == "r":
            destination = "The Revolting Ravine"
        elif answer == "d":
            destination = "The Daunting Desert"
        elif answer == "v":
            destination = "The Vomiting Volcano"
        text_unroll("You travel to the {}!".format(destination))
        hero.movement(hero, level)