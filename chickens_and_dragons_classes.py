class Hero:

    race_attributes = {"Resilience": 0, "Strength": 0, "Agility": 0}
    clas_attributes = {"Sword": 0, "Axe": 0, "Mace": 0, "Light armour": 0, "Heavy armour": 0}
    inventory = {"Small health": 0, "Large health": 0, "Strength": 0}

    race = ""
    clas = ""
    name = ""

    def __init__(self, name, race, clas):
        self.race = race
        self.clas = clas
        self.name = name

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
        return self.name
        

hero_1 = Hero("Thor", "Human", "Barbarian")

print(hero_1.race)
print(hero_1)
print(hero_1.race_attributes["Strength"])
print(hero_1.clas_attributes["Sword"])