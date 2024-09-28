import sys
import random
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3


def play_game():
    while True:
        print(" ")
        player_choice = input(
            "Enter... \n 1 for Rock,\n 2 for Paper, \n 3 for Scissors: \n\n"
        )

        try:
            player = int(player_choice)
            if 1 <= player <= 3:
                break  # Exit the loop if the input is valid
            else:
                print("Invalid input! You need to enter 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number!")

    computer_choice = random.choice("123")
    computer = int(computer_choice)

    print("Player Choice " + str(RPS(player)).replace("RPS.", "") + ".")
    print("Computer Choice " + str(RPS(computer)).replace("RPS.", "") + ".")

    if player == 1 and computer == 3:
        print("You win")
    elif player == 2 and computer == 1:
        print("You win")
    elif player == 3 and computer == 2:
        print("You win")
    elif player == computer:
        print("Draw")
    else:
        print("Python win")


while True:
    play_game()
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break
