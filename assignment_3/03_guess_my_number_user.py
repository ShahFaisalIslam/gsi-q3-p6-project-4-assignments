# Guess my number - computer
# Computer asks the user to tell if they guessed a number correctly till they
# get it right


from random import randint

def guess(max : int):
    # Start at a random point
    guess_number : int = randint(1,max)

    # Keep asking the user if the guess is correct, low, or high, till they
    # you it is right
    while True:
        response: str = input(f"Is the guess {guess_number} correct(C), too\
 high(H), or too low(L)?(Enter C,H, or L accordingly) ").lower()
        if response == 'h':
            guess_number -= 1
        elif response == 'l':
            guess_number += 1
        else:
            break
    
    print(f"Yay! I guessed your number {guess_number}\
 right!")

def main():
    print("Keep a number between 1 to 10 in your mind, and let me guess it")
    guess(10)

if __name__ == '__main__':
    main()