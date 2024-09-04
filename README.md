 project is a simple implementation of the classic Rock, Paper, Scissors game, where the player competes against the computer. The game is split into two files: one for functions and one for the main program that controls the game flow.

Project Structure
The project consists of two Python files:

RSPF.py (Functions)

This file contains the core functions that handle the logic of the game:
computer_choice(): Randomly selects a move for the computer (Rock, Paper, or Scissors).
user_choice(): Takes user input and validates the choice.
play_RSP(user_choice, computer_choice): Determines the outcome of the game based on the player's and computer's choices, printing the results accordingly.
RSP.py (Main Program)

This file handles the main game loop and imports the functions from RSPF.py. It controls the flow of the game, allowing players to play multiple rounds and tracking the number of games played. The program prompts the user after each round to see if they would like to play again or quit.
