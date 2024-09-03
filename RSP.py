# Importing the random module to generate random choices for the computer
import random

print(" Play the game by choosing Rock, Scissors or Paper ")

# Initialize count to track the number of games the user plays
count = 1

# Loop to allow the game to be played multiple times
while True:
    # Adding the number of times the user played
    count += 1
    # List of choice a computer will pick on
    select = ["Rock", "Scissors", "Paper"]
    opponent = random.choice(select)

    # Getting user input and capitalizing it for consistency
    user = input('What is your move? ').capitalize()

    # Check for a tie condition
    if user == opponent:
        print("It's a tie!\n")

    # Check if user chose Rock
    elif user == "Rock":
        if opponent == "Scissors":
            print("Rock smashes scissors!\n\t You win!!!\n")
        else:
            print("Rock covers paper!\n\t You lost!!!\n")

    # Check if user chose Scissors
    elif user == "Scissors":
        if opponent == "Paper":
            print("Scissors cuts paper!\n\t You win!!!\n")
        else:
            print("paper covers Rock!\n\t You lost!!!\n")

    # Check if user chose paper
    elif user == "Paper":
        if opponent == "Rock":
            print("Paper covers Rock!\n\t You win!!!\n")
        else:
            print("Rock smashes Scissors!\n\t You lost!!!\n")

    # If input from user is invalid
    else:
        print("Invalid choice\n")

    # Ask the user if they want to continue playing the game.
    play = input("Do you want to play again? (Y/N): ").lower()

    # If the user does not choose y  the game will terminate
    if play != "y":
        print(f"Game over. You played {count-1} times.")
        break # the loop will break ending the game
    else:
        print(f"Another round of play, game number {count}.\n")

