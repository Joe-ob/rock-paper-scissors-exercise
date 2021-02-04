# game.py




# introduction
print("------------------")
print("Welcome 'player one' to my Rock-Paper-Scissors game...")
print("-------------------")

# Asking user for an Input
user_choice=input("Please choose either 'rock', 'paper', or 'scissors': ")



# Repeating selection
print(f"You chose: {user_choice}")


#computer makes selection
#options = ['rock,', 'paper', 'scissors']

import random
foo=['rock', 'paper', 'scissors']
computer_choice=random.choice(foo)

print("Rock, Paper, Scissors, Shoot!")
print("-------------------")

print(f"The computer chose: {computer_choice}")
print("-------------------")

if user_choice == 'rock':
    if computer_choice == 'rock':
        print("It's a Tie. Thanks for Playing!")
    elif computer_choice == 'paper':
        print("You Lose. Thanks for Playing!")
    elif computer_choice == 'scissors':
        print("You Win, Thanks for Playing!")
elif user_choice == 'paper':
    if computer_choice == 'paper':
        print("It's a Tie. Thanks for Playing!")
    elif computer_choice == 'scissors':
        print("You Lose. Thanks for Playing!")
    elif computer_choice == 'rock':
        print("You Win, Thanks for Playing!")
elif user_choice == 'scissors':
    if computer_choice == 'scissors':
        print("It's a Tie. Thanks for Playing!")
    elif computer_choice == 'rock':
        print("You Lose. Thanks for Playing!")
    elif computer_choice == 'paper':
        print("You Win, Thanks for Playing!")

else:
    print("OOPS SOMETHING WENT WRONG")






