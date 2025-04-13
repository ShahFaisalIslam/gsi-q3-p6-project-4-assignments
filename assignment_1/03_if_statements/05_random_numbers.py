# Random numbers
# Print 10 random numbers in the range 1-100

N_NUMBERS : int = 10
MIN_NUMBER : int = 1
MAX_NUMBER : int = 100

from random import randint

def main():
    for _ in range(N_NUMBERS):
        print(randint(MIN_NUMBER,MAX_NUMBER),end=" ")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()