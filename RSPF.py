
import random


# Function to get the computer choice

def computer_choice():
    # List of choice a computer will pick on
    select = ["Rock", "Scissors", "Paper"]
    opponent = random.choice(select)
    return opponent


# Function to get players choice
def user_choice():
    # Getting user input and capitalizing it for consistency
    user = input('What is your move? ').capitalize()
    return user


def play_RSP(user_choice, computer_choice):
    # Check for a tie condition
    if user_choice == computer_choice:
        print("It's a tie!\n")

    # Check if user chose Rock
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("Rock smashes scissors!\n\t You win!!!\n")
        else:
            print("Rock covers paper!\n\t You lost!!!\n")

    # Check if user chose Scissors
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("Scissors cuts paper!\n\t You win!!!\n")
        else:
            print("paper covers Rock!\n\t You lost!!!\n")

    # Check if user chose paper
    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("Paper covers Rock!\n\t You win!!!\n")
        else:
            print("Rock smashes Scissors!\n\t You lost!!!\n")

    # If input from user is invalid
    else:
        print("Invalid choice\n")

#functio to ask
def play_again ():
    # Ask the user if they want to continue playing the game.
    play = input("Do you want to play again? (Y/N): ").lower()
    return play


