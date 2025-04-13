# Asks the user to type an affirmation till they type it correctly

AFFIRMATION : str = "I am capable of doing anything I put my mind to."

def main():
    while True:
        # Ask the user to provide affirmation
        user_affirmation : str = input("Please type the following affirmation: "
                                       + AFFIRMATION + "\n")
 
        # Stop if affirmation typed correctly
        if user_affirmation == AFFIRMATION:
            print("That's right! :)")
            break

        # Inform about the incorrectness of the affirmation
        print("Hmmm That was not the affirmation.")

if __name__ == '__main__':
    main()