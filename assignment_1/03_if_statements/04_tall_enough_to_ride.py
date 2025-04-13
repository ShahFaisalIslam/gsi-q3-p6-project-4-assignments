# Tall enough to ride
# Asks the user how they tall they are and then tells them whether they are
# tall enough to ride

MAX_HEIGHT : float = 50

def is_tall_enough(height : float):
    return height >= MAX_HEIGHT

def main():
    # Prompt the user to tell their height
    while True:
        height_input: str = input("How tall are you(do not enter height to stop)?")
        if not height_input:
            break
        height = float(height_input)
        if is_tall_enough(height):
            print("You are tall enough to ride!")
        else:
            print("You are not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()