
import RSPF as SELECTION

print("Welcome to Rock, Paper, Scissors with ELO Rating System!")
print("Rate yourself and try to improve your ELO rating by winning games.\n")

# Initialize count to track the number of games the user plays
count = 1
user_rating = SELECTION.user_rating()
computer_rating = SELECTION.computer_rating()
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
  
    
    # Play  a round to determine the winner
    result = SELECTION.win_move(user_move, computer_move)

    user_rating, computer_rating = SELECTION.update_ratings(user_rating, computer_rating, result)
    # Display updated ratings
    print(f"Updated Ratings:\nUser: {user_rating}\nComputer: {computer_rating}\n")

    # Ask the player if they want to play another round.
   

    # If the user does not choose y  the game will terminate
    if SELECTION.play_again() != "y":
        print(f"Game over. You played {count - 1} times.")
        break  # the loop will break ending the game
    else:
        print(f"Another round of play, game number {count}.\n")


