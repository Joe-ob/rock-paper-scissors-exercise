# game.py

import os
from dotenv import load_dotenv
load_dotenv ()
USER_NAME = os.getenv("USER_NAME", default="Player One")

# introduction, including the user's input name
print(f"Welcome, {USER_NAME}, to my Rock-Paper-Scissors game...")


# Asking user for an Input
user_choice=input("Please choose either 'rock', 'paper', or 'scissors': ").lower()



#Validation, Stop the program and check if the user choice is valid
# If user selections is not within options, message prints and exits code
options=['rock', 'paper', 'scissors']
if user_choice not in options:
    print("OOPS, please try again and choose one of the options listed above")
    exit ()

#using random function to allow computer to make selection
# Limiting selections to variables in options
import random
computer_choice=random.choice(options)


# Play the game out, displaying the user and computer choice
print("Rock, Paper, Scissors, Shoot!")
print(f"You chose: {user_choice}")
print(f"The computer chose: {computer_choice}")




# Using if function to Name a Winner 
# by comparing User selection and computer selection
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








