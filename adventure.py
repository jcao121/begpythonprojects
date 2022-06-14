from time import sleep
from random import randint

weapons = ["sword", "axe", "spear"]
game_state = ""
health = 100
while game_state != "over":
    first_name = input("What is your first name? ").capitalize()
    if first_name != "":
        print(
            f"Is it a pleasure to meet you {first_name}, My name is Gandolf The Grey, Let's get you out of The Shire. "
        )
    else:
        continue
    sleep(1)
    playing = input("Do you want to go on an adventure? Enter Yes or No: ").lower()[0]
    if playing == "y":
        print(
            "If we are going on an adventure we need a weapon in case something goes wrong, would you like a Sword, Axe or Spear?"
        )
        sleep(1)
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
        break
    sleep(1)
    print("You pack your things and follow Gandolf")
    sleep(1)
    print("After half a day of traveling you and Gandolf run into Smaug The Dragon!")
    sleep(1)
    smaughp = 25
    while smaughp > 0:
        fight_response = input("What do you DO? Enter: Fight or Run? ").lower()
        if fight_response == "fight":
            attack = randint(0, 10)
            smaugattack = randint(0, 8)
            print(f"You attacked Smaug and it did {attack} damage")
            smaughp -= attack
            if attack >= smaughp and smaughp <= 0:
                smaughp = +0
                print(f"Smaug has {smaughp} HP left")
                print(
                    "You have defeated Smaug The Dragon!, you beg Gandolf to take you back to The Shire and your adventure ends here..."
                )
                game_state = "over"
                break
            else:
                print(f"Smaug has {smaughp} HP left")
                print(f"Smaug retaliates and hits you for {smaugattack} damage")
                health -= smaugattack
                print(f"You have {health} amount of HP left")
        elif fight_response == "run":
            game_state = "over"
            print(
                "You tried to flee and smaug burned you with his flame breath, YOU DIED!"
            )
            break
