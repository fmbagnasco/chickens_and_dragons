#setup of the Hero class

class Hero:

    #basic class attributes

    race_attributes = {"Resilience": 0, "Strength": 0, "Agility": 0}
    clas_attributes = {"Sword": 0, "Axe": 0, "Mace": 0, "Light armour": 0, "Heavy armour": 0}
    inventory = {
        "Small health": 0,
        "Large health": 0,
        "Strength": 0,
        "Weapon": False,
        "Helmet": False,
        "Cuirass": False,
        "Boots": False
    }

    #eveything else defined in the constructor

    def __init__(self, name, race, clas):
        self.race = race
        self.clas = clas
        self.name = name

        #different classes and races defined here

        if race == "Human":
            self.race_attributes["Resilence"] = 4
            self.race_attributes["Strength"] = 3
            self.race_attributes["Agility"] = 3
        elif race == "Orc":
            self.race_attributes["Resilence"] = 4
            self.race_attributes["Strength"] = 5
            self.race_attributes["Agility"] = 1
        elif race == "Elf":
            self.race_attributes["Resilence"] = 3
            self.race_attributes["Strength"] = 2
            self.race_attributes["Agility"] = 5

        if clas == "Barbarian":
            self.clas_attributes["Sword"] = 1
            self.clas_attributes["Axe"] = 5
            self.clas_attributes["Mace"] = 3
            self.clas_attributes["Light armour"] = 3
            self.clas_attributes["Heavy armour"] = 3
        elif clas == "Paladin":
            self.clas_attributes["Sword"] = 3
            self.clas_attributes["Axe"] = 1
            self.clas_attributes["Mace"] = 5
            self.clas_attributes["Light armour"] = 1
            self.clas_attributes["Heavy armour"] = 5
        elif clas == "Scout":
            self.clas_attributes["Sword"] = 5
            self.clas_attributes["Axe"] = 3
            self.clas_attributes["Mace"] = 1
            self.clas_attributes["Light armour"] = 4
            self.clas_attributes["Heavy armour"] = 2

    def __repr__(self):
        return self.name + " the " + self.clas

    #inventory function

    def inventory(self, item):
        if isinstance(item, Weapon):
            self.inventory["Weapon"] = item
        elif isinstance(item, Armor):
            if item["Part"] == "Cuirass":
                self.inventory["Cuirass"] = item
            elif item["Part"] == "Boots":
                self.inventory["Boots"] = item
            elif item["Part"] == "Helmet":
                self.inventory["Helmet"] = item
        elif isinstance(item, Potion):
            if item.name == "Small health potion":
                self.inventory["Small health"] += 1
            elif item.name == "Large health potion":
                self.inventory["Large health"] += 1
            elif item.name == "Stremgth potion":
                self.inventory["Strength"] += 1



    
    #attack function

    def attack(damage, speed, monster_agility):
        pass
        

hero_1 = Hero("Thor", "Human", "Barbarian")

print(hero_1.race)
print(hero_1.clas)
print(hero_1.name)
print(hero_1)
print(hero_1.race_attributes["Strength"])
print(hero_1.clas_attributes["Light armour"])

#setup of the Monster class

class Monster:

    #basic class attributes

    monster_attributes = {"HP": 0, "Attack damage": 0, "Defence": 0, "Type": ""}        #dict or single separate ints?

    #constructor

    def __init__(self, name):
        self.name = name

        #just like for the Hero class

        if name == "Chicken Scout":
            self.monster_attributes["HP"] = 10
            self.monster_attributes["Attack damage"] = 7
            self.monster_attributes["Defence"] = 1
            self.monster_attributes["Type"] = "Minion"
        elif name == "Dragon Fighter":
            self.monster_attributes["HP"] = 15
            self.monster_attributes["Attack damage"] = 7
            self.monster_attributes["Defence"] = 2
            self.monster_attributes["Type"] = "Minion"
        elif name == "Chicken Overlord":
            self.monster_attributes["HP"] = 40
            self.monster_attributes["Attack damage"] = 15
            self.monster_attributes["Defence"] = 4
            self.monster_attributes["Type"] = "Boss"
        elif name == "Dragon Master":
            self.monster_attributes["HP"] = 60
            self.monster_attributes["Attack damage"] = 25
            self.monster_attributes["Defence"] = 5
            self.monster_attributes["Type"] = "Boss"
        elif name == "Chickenator the Soulless King of Dragons":
            self.monster_attributes["HP"] = 100
            self.monster_attributes["Attack damage"] = 40
            self.monster_attributes["Defence"] = 10
            self.monster_attributes["Type"] = "Final boss"

monster_1 = Monster("Chicken Scout")

print(monster_1.monster_attributes["HP"])

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
            self.weapon_stats["Damage"] = 2
            self.weapon_stats["Speed"] = 5
        elif name == "Long sword":
            self.weapon_stats["Type"] = "Sword"
            self.weapon_stats["Damage"] = 3
            self.weapon_stats["Speed"] = 4
        elif name == "Claymore":
            self.weapon_stats["Type"] = "Sword"
            self.weapon_stats["Damage"] = 5
            self.weapon_stats["Speed"] = 2
        elif name == "Hatchet":
            self.weapon_stats["Type"] = "Axe"
            self.weapon_stats["Damage"] = 2
            self.weapon_stats["Speed"] = 5
        elif name == "Battle axe":
            self.weapon_stats["Type"] = "Axe"
            self.weapon_stats["Damage"] = 4
            self.weapon_stats["Speed"] = 3
        elif name == "Two-handed axe":
            self.weapon_stats["Type"] = "Axe"
            self.weapon_stats["Damage"] = 5
            self.weapon_stats["Speed"] = 2
        elif name == "Club":
            self.weapon_stats["Type"] = "Mace"
            self.weapon_stats["Damage"] = 3
            self.weapon_stats["Speed"] = 4
        elif name == "War mace":
            self.weapon_stats["Type"] = "Mace"
            self.weapon_stats["Damage"] = 4
            self.weapon_stats["Speed"] = 3
        elif name == "War hammer":
            self.weapon_stats["Type"] = "mace"
            self.weapon_stats["Damage"] = 5
            self.weapon_stats["Speed"] = 2

weapon_1 = Weapon("Short sword")
print(type(weapon_1))

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
        elif name == "Light Boots":
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
        elif name == "Strength potion":
            self.potion_benefits["Strength increase"] = 5
