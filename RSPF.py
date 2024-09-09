import random

# Function to get the computer rating
def computer_rating():
    return random.randint(1,10)

# Function to get the user rating by input from user
def user_rating():
    while True:
        try:
            user_rate = int(input ( "Rate yourself in a scale of 1 to 10 on game skill: "))
            if 1<= user_rate <=10:
                return user_rate

            else: 
                print("Rate between 1 and 10.")
        except valueError:
            print("Invalid input. Please enter a valid input.")

# Function to calculate updated ELO ratings
def update_ratings(user_rating, computer_rating, result):
    """
    Updates ELO ratings based on game result.
    ELO adjustment factor is arbitrarily set to 32.
    """
    K = 32  # K-factor, a constant to control how much ratings change

    # Calculate the expected scores for both players
    expected_user_score = 1 / (1 + 10 ** ((computer_rating - user_rating) / 400))
    expected_computer_score = 1 / (1 + 10 ** ((user_rating - computer_rating) / 400))

    # Update ratings based on the game outcome
    if result == 'user_win':
        user_rating += K * (1 - expected_user_score)
        computer_rating += K * (0 - expected_computer_score)
    elif result == 'computer_win':
        user_rating += K * (0 - expected_user_score)
        computer_rating += K * (1 - expected_computer_score)
    elif result == 'tie':
        user_rating += K * (0.5 - expected_user_score)
        computer_rating += K * (0.5 - expected_computer_score)

    # Return updated ratings
    return round(user_rating), round(computer_rating)

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


# Function to determine who wins the game by comparing the moves
def win_move(user_move, computer_move):
    # Check for a tie condition
    if user_move == computer_move:
              
        print("It's a tie!\n")
        return 'tie'

    # Win and lose conditionsfor the user
    if (user_move == "Rock" and computer_move=="Scissors" ) or\
       (user_move == "Scissors" and computer_move=="Paper") or\
       (user_move == "Paper" and computer_move=="Rock"  ):
       print(f"You win! {user_move} beats {computer_move}")
       return "user_win"
    else:
        print(f"You loose!{computer_move}beats {user_move}.n\ ")
        return "computer_win"      


# Function to ask to continue to play.
def play_again():
    # Ask the user if they want to continue playing the game.
    play = input("Do you want to play again? (Y/N): ").lower()
    return play
