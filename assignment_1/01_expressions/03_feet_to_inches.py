# Feet to inches
# Convert feet to inches

# Each foot is 12 inches. Feet is plural of foot.
def feet_to_inches(feet: float) -> float:
    return feet * 12.0

def main():
    # Ask user for length in feet
    feet: float = float(input("Enter length in feet:"))

    # Display the length in inches
    inches : float = round(feet_to_inches(feet),1)
    print(f"{feet} {'feet' if feet != 1.0 else 'foot'} is {inches} inch{'es' if inches != 1.0 else ''}!")

if __name__ == '__main__':
    main()