
import RSPF as SELECTION

print(" Play the game by choosing Rock, Scissors or Paper ")

# Initialize count to track the number of games the user plays
count = 1

# Loop to allow the game to be played multiple times
while True:
    # Adding the number of times the user played
    count += 1

    try:
        user_move = SELECTION.user_choice()
        computer_move = SELECTION.computer_choice()

    except Exception as e:
        # Catch any unexpected exceptions and inform the user
        print(f"An error occurred: {e}")

        continue  # Continue to the next iteration of the loop to ask for input again
    comp_rate = SELECTION.computer_rating()
    user_rate = SELECTION.user_rating()
    
    # Play  a round to determine the winner
    results = SELECTION.win_move(user_move, computer_move)

    SELECTION.game_Ratings(user_rate,comp_rate,results)

    # Ask the player if they want to play another round.
    play = SELECTION.play_again()

    # If the user does not choose y  the game will terminate
    if play != "y":
        print(f"Game over. You played {count - 1} times.")
        break  # the loop will break ending the game
    else:
        print(f"Another round of play, game number {count}.\n")


