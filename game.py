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
computer_choice=["Rock", "Paper", "Scissors"]
print(f"The computer chose: {random.choice(computer_choice)}")



exit()










#Naming a Winner
print("Rock, Paper, Scissors, Shoot!")
print("-------------------")
print("Oh, the computer won. It's ok.")
print("-------------------")

#Goodbye
print("Thanks for playing. Please play again!")