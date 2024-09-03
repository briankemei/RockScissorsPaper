import random
import RSPF as selection

print(" Play the game by choosing Rock, Scissors or Paper ")

# Initialize count to track the number of games the user plays
count = 1

# Loop to allow the game to be played multiple times
while True:
    # Adding the number of times the user played
    count += 1

    user_move = selection.user_choice()
    computer_move = selection.computer_choice()

    selection.play_RSP(user_move, computer_move)
    play = selection.play_again()

    # If the user does not choose y  the game will terminate
    if play != "y":
        print(f"Game over. You played {count - 1} times.")
        break  # the loop will break ending the game
    else:
        print(f"Another round of play, game number {count}.\n")


