# Dice Simulator
# Simulates rolling two dice, three times. Prints the result of each roll

from random import randint
MAX_SIDE : int = 6
class Die:
    def __init__(self):
        self.position = randint(1,MAX_SIDE)

    # Roll the die
    def roll(self) -> None:
        self.position = randint(1,MAX_SIDE)

def roll_dice(die_1 : Die,die_2: Die):
    # Roll the dice
    die_1.roll()
    die_2.roll()

    # Print the results of roll
    print(f"Roll:\n die_1={die_1.position} die_2={die_2.position} sum={die_1.position + die_2.position}")

def main():
    # Two dice
    die_1 : Die = Die()
    die_2 : Die = Die()

    # Print initial positions
    print(f"Initial positions:\n die_1={die_1.position} , die_2={die_2.position}")

    # Roll the dice thrice
    roll_dice(die_1,die_2)
    roll_dice(die_1,die_2)
    roll_dice(die_1,die_2)

    # Print final positions
    print(f"Final positions:\n die_1={die_1.position} , die_2={die_2.position}")
    pass

if __name__ == '__main__':
    main()