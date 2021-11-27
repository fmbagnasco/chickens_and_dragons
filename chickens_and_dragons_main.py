from chickens_and_dragons_classes import *

text_unroll("Welcome to Chickens & Dragons,\nthe only game that takes place in the\nwonderfult Chickens & Dragons Universe!")
text_unroll("\nPlease select a race for your hero!\nThe choices are:\n- Human\n- Orc\n- Elf\nMake sure you spell the race correctly!\n")

user_race = input()

text_unroll("\nFantastic! You picked " + user_race + "!")
text_unroll("\nNow it's time to pick your hero class!\nThe different choices are:\n- Barbarian\n- Paladin\n- Scout")
text_unroll("\nThink about this carefully!\nYour class will determine which weapons and armors\nyou will be most proficient in!\n")

user_class = input()

text_unroll("\nGreat! you chose " + user_class + "!")
text_unroll("\nNow, one last thing:\nyour hero needs a name!\nPlese write a name of your choice:\n")

user_name = input()

text_unroll("\nNow that you are all set up with your hero,\nlet's get started!")

user_hero = Hero(user_name, user_race, user_class)

text_unroll("\nThis is your hero:\n")
text_unroll(user_hero)

text_unroll("\nEach class gets a basic weapon to start the game with\nbased on the type of class.\nYour initial weapon is:\n")
text_unroll(user_hero.inventory["Weapon"])

text_unroll("\nLet's start our adventure together!")

game = True

while game == True:

    text_unroll("\nWould you like to travel\nor to check your inventory?")
    text_unroll("\nWrite 't' for travel, or 'i' for inventory.\n")

    answer = input()

    if answer == "i":
        user_hero.inventory_inquiry()
    elif answer == "t":

        distance = 0

        text_unroll("\nWhere do you want to go?\nThese are the options:")
        text_unroll("\n-Chicken Forest, 3 leagues away\n-Dragon Lair, 5 Leagues away\n-Impervious Summit, 8 leagues away")
        text_unroll("\nWrite 'f' for the forest, 'l' for the lair, or 's' for the summit.\n")

        destination = input()

        if destination == "f":
            user_hero.movement(user_hero, 3)
        elif destination == "l":
            user_hero.movement(user_hero, 5)
        elif destination == "s":
            user_hero.movement(user_hero, 8)

    if user_hero.hp <= 0:
        game = False