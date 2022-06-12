# TODO: uppercase first letter of first_name, figure out how the attack system will work, attack needs to keep changing
# FIXME: smaughp drops to negative, i want it to end as soon as its 0, need to find a way, need to dummy proof program also and add sleep to make it more of a dialoge
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
    sleep(1)
    playing = input("Do you want to go on an adventure? ").lower()[0]

    if playing == "y":
        print(
            "If we are going on an adventure we need a weapon in case something goes wrong, would you like a Sword, Axe or Spear?"
        )
        weapon = input("Choose your WEAPON: ").lower()
        while weapon not in weapons:
            weapon = input(
                "You did not enter one of options as a weapon... Try again: "
            ).lower()
        if weapon in weapons:
            print(f"You chose a {weapon}! Let's head out on our adventure!")
    elif playing == "n":
        print("Alright see you later coward!")
        quit()
    else:
        print("You did not enter yes or no")

    print("You pack your things and follow Gandolf")
    sleep(1)
    print("After half a day of traveling you and Gandolf run into Smaug The Dragon!")
    sleep(1)

    fight_response = input("What do you DO? Enter: Fight or Run? ").lower()
    if fight_response == "fight":
        smaughp = 25
        while smaughp > 0:
            attack = randint(0, 10)
            smaugattack = randint(0, 8)
            attacksmaug = print(f"You attacked Smaug and it did {attack} damage")
            smaughp -= attack
            print(f"Smaug has {smaughp} HP left")
            print(f"Smaug retaliates and hits you for {smaugattack} damage")
            health -= smaugattack
            print(f"You have {health} amount of HP left")

            fight_or_flight = input(
                "Do you want to keep attacking or try to flee? "
            ).lower()
            if fight_or_flight == "attack" and smaughp > 0:
                continue
            elif fight_or_flight == "flee":
                health += 0
                print(
                    "You tried to flee and Smaug burned you with his flame breath and you die."
                )
            else:
                print(
                    "You have defeated SMAUG, you beg Gandolf to take you back to The Shire and your adventure ends here..."
                )
    break
