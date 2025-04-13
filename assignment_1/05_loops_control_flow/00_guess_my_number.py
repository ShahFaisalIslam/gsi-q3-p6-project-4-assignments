# Guess my number
# Program initializes a guess, then keeps asking the user till they get it
# right. Also informs how a wrong guess was different from the correct guess

from random import randint

MIN_NUMBER : int = 0
MAX_NUMBER : int = 99

def main():
    # Initialize number
    number : int = randint(MIN_NUMBER,MAX_NUMBER)

    # Keep asking the user till they get it right
    guess : int = int(input(f"I am thinking of a number between {MIN_NUMBER}\
 and {MAX_NUMBER}... Enter a guess: "))
    while True:
        if guess < number:
            print("Your guess is too low")
        elif guess > number:
            print("Your guess is too high")
        else:
            break
        guess = int(input("Enter a new number: "))

    print(f"Congrats! The number was: {number}")
if __name__ == '__main__':
    main()