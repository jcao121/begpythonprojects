quiz_score = 0
choices = ["A", "B", "C"]
print("What is the correct syntax to print Hello World in Python?"
      " \n A. print('Hello World'): \n B. System.out.println('Hello World') "
      "\n C. print('Hello World') \n D. console.log('Hello World');")

Q1 = input("Choose A,B,C or D: ").upper()

print("What is the syntax for writing comments in Python?"
      "\n A. # \n B. /* \n C. */ \n D. //)")

Q2 = input("Choose A, B or C: ").upper()

print("How do you create a variable with the numeric value 5?"
      "\n A. x = 5 \n B. x = int(5) \n C. Both the other answers are correct")

Q3 = input("Choose A, B or C: ").upper()

print("What is the correct file extension for Python files?"
      " \n A. .py \n B. .pyth"
      "\n C. .pt \n D. .pyt")

Q4 = input("Choose A,B,C or D: ").upper()

print("What is the correct way to create a function in Python?"
      "\n A. def myFunction():" "\n B. function myfunction():" "\n C. create myFunction():")

Q5 = input("Choose A, B or C: ").upper()

if Q1 == "A":
    quiz_score += 20
elif Q1 not in choices:
    print("You did choose one of the options provided for question 1")
else:
    print("You answered question 1 incorrectly")

if Q2 == "A":
    quiz_score += 20
elif Q2 not in choices:
    print("You did choose one of the options provided for question 2")
else:
    print("You answered question 2 incorrectly")

if Q3 == "C":
    quiz_score += 20
elif Q3 not in choices:
    print("You did choose one of the options provided for question 3")
else:
    print("You answered question 3 incorrectly")

if Q4 == "A":
    quiz_score += 20
elif Q4 not in choices:
    print("You did choose one of the options provided for question 4")
else:
    print("You answered question 4 incorrectly")
if Q5 == "A":
    quiz_score += 20
elif Q5 not in choices:
    print("You did choose one of the options provided for question 5")
else:
    print("You answered question 5 incorrectly")

if quiz_score in range(0, 60):
    print("You failed the quiz")
elif quiz_score in range(60, 100):
    print("YOU ARE A PYTHON MASTER YOU PASSED THE QUIZ!")

print(f"Your score is {quiz_score} out of 100")
