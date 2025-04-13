# Guess my number - computer
# Computer asks the user to guess a random number in a range till they get it
# right.


from random import randint

def guess(max : int):
    random_number : int = randint(1,max)
    guess_number : int = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {max}: "))
        if guess_number < random_number:
            print("Guess again, too low")
        elif guess_number > random_number:
            print("Guess again, too high")
        else:
            print(f"Yay, congrats! You have guessed the number {random_number}\
 correctly!")

def main():
    guess(10)

if __name__ == '__main__':
    main()