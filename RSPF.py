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

#Function to get the final ratings after playing the game
def game_Ratings(user_rating, computer_rating, outcome):
    print("What is the user rating: ", user_rating)
    print("What is the computer rating: ", computer_rating)

    if user_rating > computer_rating:  # User is favored
        if outcome == 'user_choice':
            user_rating += 2
            computer_rating -= 2
        elif outcome == 'tie':
            user_rating -= 1
            computer_rating += 1
        elif outcome == 'computer_choice':
            user_rating -= 3
            computer_rating+= 3

    elif user_rating < computer_rating:  # User is the underdog
        if outcome == 'user_choice':
            user_rating += 3
            computer_rating -= 3
        elif outcome == 0 :
            user_rating += 1
            computer_rating -= 1
        elif outcome == 'computer_choice':
            user_rating -= 2
            computer_rating += 2

    # Print the updated ratings
    print(f"Updated User Rating: {user_rating}")
    print(f"Updated Opponent Rating: {computer_rating}")



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
def win_move(user_choice, computer_choice):
    # Check for a tie condition
    if user_choice == computer_choice:
        
        print("It's a tie!\n")
        return 0

    # Check if user chose Rock
    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            
            print("Rock smashes scissors!\n\t You win!!!\n")
            return user_choice
        else:
            
            print("Rock covers paper!\n\t You lost!!!\n")
            return computer_choice

    # Check if user chose Scissors
    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            
            print("Scissors cuts paper!\n\t You win!!!\n")
            return user_choice
        else:           
            print("paper covers Rock!\n\t You lost!!!\n")
            return computer_choice

    # Check if user chose paper
    elif user_choice == "Paper":
        if computer_choice == "Rock":            
            print("Paper covers Rock!\n\t You win!!!\n")
            return user_choice
        else:            
            print("Rock smashes Scissors!\n\t You lost!!!\n")
            return computer_choice

    # If input from user is invalid
    else:
        print("Invalid choice\n")


# Function to ask to continue to play.
def play_again():
    # Ask the user if they want to continue playing the game.
    play = input("Do you want to play again? (Y/N): ").lower()
    return play
