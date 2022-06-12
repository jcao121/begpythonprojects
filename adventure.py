# TODO: uppercase first letter of first_name, figure out how the attack system will work, attack needs to keep changing
# FIXME:
from time import sleep
from random import randint

weapons = ["sword", "axe", "spear"]

health = 100
while health != 0:
    first_name = input("What is your first name? ")
    if first_name != "":
        print(
            f"Is it a pleasure to meet you {first_name}, My name is Gandolf The Grey, Let's get you out of The Shire. "
        )
    else:
        continue
    playing = input("Do you want to go on an adventure? ").lower()[0]

    if playing == "y":
        print(
            "If we are going on an adventure we need a weapon in case something goes wrong, would you like a Sword, Axe or Spear?"
        )
        weapon = input("Choose your WEAPON: ").lower()
        while weapon not in weapons:
            weapon = input(
                "You did not enter one of options as a weapon... Try again: "
            )
        if weapon in weapons:
            print(f"You chose a {weapon}! Let's head out on our adventure!")
    elif playing == "n":
        print("Alright see you later coward!")
        quit()
    else:
        print("You did not enter yes or no")
    print("You pack your things and follow Gandolf")
    sleep(1)
    print("After half a day of traveling you and Gandolf run into a pack of Wargs")
    sleep(1)
    fight_response = input("What do you DO? Enter: Fight or Run? ").lower()
    wargs = 25
    attack = randint(0,10)
    if fight_response == "fight":
        while wargs > 0:




