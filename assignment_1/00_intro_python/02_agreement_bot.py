# Agreement Bot
# Asks the user what their favorite animal is, and then always responds with
# 'my favorite animal is also <input>', where <input> is the user's response

def main():
    # Ask the user
    animal : str = input("What is your favorite animal? ")

    # Respond
    print(f"My favorite animal is also {animal}!")

if __name__ == '__main__':
    main()