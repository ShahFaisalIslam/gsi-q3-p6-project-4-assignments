# Square number
# Obtain a number from the user and print its square

# Calculate square of given number
def square(number: float) -> float:
    return number ** 2

def main():
    # Prompt the user to enter a number
    number : float = float(input("Type a number to see its square: "))
    # Print its square
    print(f"{round(number,1)} squared is {round(square(number),1)}")

if __name__ == '__main__':
    main()