from random import randint

playing = input("Do you want to play a guess game? ").lower()[0]
if playing == "y":
    print("Let's Game!")
elif playing == "n":
    print("Okay Bye!")
    quit()
else:
    print("You did not enter yes or no")
    quit()

attempts = 0
number = randint(1, 10)
while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == number:
        print(
            f"You guessed correctly it was {number} and it took you {attempts} attempts"
        )
        break
    elif guess < number:
        attempts += 1
        print("YOU GUESSED LOWER TRY AGAIN")
    elif guess > 10:
        attempts += 1
        print("You guessed a number higher then 10... Try again..")
    else:
        attempts += 1
        print("YOU GUESSED HIGHER TRY AGAIN")
