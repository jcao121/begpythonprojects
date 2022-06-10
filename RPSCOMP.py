from random import choice
player1_score = 0
comp_score = 0
options = ["rock", "paper", "scissors"]
while player1_score != 3 and comp_score != 3:

    player1 = input("Rock, Paper or Scissors: ").lower()
    if player1 not in options:
        continue
    comp = choice(["Rock", "Paper", "Scissors"]).lower()
    print(f"Computer CHOOSES {comp}")
    if player1 == "rock" and comp == "scissors":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player1 == "paper" and comp == "rock":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player1 == "scissors" and comp == "paper":
        player1_score += 1
        print(f"PLAYER 1 WINS and has {player1_score} point")
    elif player1 == comp:
        print("ITS A TIE! WE GO AGAN")
    else:
        comp_score += 1
        print(f"COMPUTER WON AND HAS {comp_score} point")

