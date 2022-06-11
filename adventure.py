# TODO:
# FIXME:

weapons = ["sword", "axe", "spear"]

health = 100
while health != 0:
    first_name = input("What is your first name? ")
    if first_name != "":
        print(f"Is it a pleasure to meet you {first_name}")
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
