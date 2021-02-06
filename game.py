# game.py

#Enter UserName
User_Name=input("Hello, Please enter a User Name: ")

# introduction
print(f"Welcome {User_Name} to my Rock-Paper-Scissors game...")


# Asking user for an Input
user_choice=input("Please choose either 'rock', 'paper', or 'scissors': ").lower()



#Stop the program and check if the user choice is invalid
options=['rock', 'paper', 'scissors']
if user_choice not in options:
    print("OOPS, please choose an exact option and try again")
    exit ()

#computer makes selection
import random
computer_choice=random.choice(options)

# Play the game out, displaying the user and computer choice
print("Rock, Paper, Scissors, Shoot!")
print(f"You chose: {user_choice}")
print(f"The computer chose: {computer_choice}")





# Name a Winner
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


#Message, If there was an issue
else:
    print("OOPS SOMETHING WENT WRONG")






