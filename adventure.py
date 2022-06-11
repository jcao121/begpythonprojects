health = 100
weapons = ["Sword", "Mace", "Spear"]
playing = input("Do you want to go on an adventure? ").lower()[0]
if playing == "y":
    print(weapons)
    input("Choose your WEAPON")
elif playing == "n":
    print("Alright see you later coward!")
