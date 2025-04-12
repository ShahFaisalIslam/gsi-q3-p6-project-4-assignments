# Add Two Numbers
# Take two numbers from the user, add them, and display the result in an
# appropriate message

def main():
    # Prompt the user to enter the first number
    user_input : str = input("Enter the first number: ")

    # Read the input and convert it into an integer
    first_num : int = int(user_input)

    # Prompt the user to enter the second number
    user_input : str = input("Enter the second number: ")

    # Read the input and convert it into an integer
    second_num : int = int(user_input)

    # Calculate the sum of the two numbers
    result : int = first_num + second_num

    # Print the total sum with an appropriate message
    print(f"The sum of {first_num} and {second_num}: {result}")

if __name__ == '__main__':
    main()