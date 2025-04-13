# Implementation of rock, papers or scissors game

from random import choice
from enum import Enum

class Choices(Enum):
    ROCK="r"
    PAPER="p"
    SCISSORS="s"

# Choices are simply from rock, paper, and scissors
choices : list = [Choices.ROCK.value,Choices.PAPER.value,Choices.SCISSORS.value]

def is_win(user_guess : str,computer_guess : str) -> bool:
    # User wins in the following situations:
    # * User chose scissor, and computer chose paper
    # * User chose paper, and computer chose rock
    # * User chose rock, and computer chose scissor
    # Since this function is not called when tie, user loses in the rest of the
    # situations
    if user_guess == Choices.ROCK.value and computer_guess == Choices.SCISSORS.value:
        return True
    if user_guess == Choices.PAPER.value and computer_guess == Choices.ROCK.value:
        return True
    if user_guess == Choices.SCISSORS.value and computer_guess == Choices.PAPER.value:
        return True

    return False

def choice_full(choice_abbr : str) -> str:
    if choice_abbr == 'r':
        return 'Rock'
    elif choice_abbr == 'p':
        return 'Paper'
    else:
        return 'Scissors'

def display_choices(user_guess: str,computer_guess: str):
    user_guess_full = choice_full(user_guess)
    computer_guess_full = choice_full(computer_guess)
    print(f"Your guess: {user_guess_full}, Computer guess: {computer_guess_full}")

def main():
    print("Welcome to rock, papers, or scissors game!")

    while True:
        user_guess : str = input("Type r for rock, p for paper, or s for \
scissors: ").lower()
        if user_guess in choices:
            break
        print("Incorrect input, it must be either 'r', 'p', or 's'.")
    computer_guess : str = choice(choices)

    display_choices(user_guess,computer_guess)

    if user_guess == computer_guess:
        print("It's a tie.")
    elif is_win(user_guess=user_guess,computer_guess=computer_guess):
        print("You win!")
    else:
        print("You lose!")
if __name__ == '__main__':
    main()