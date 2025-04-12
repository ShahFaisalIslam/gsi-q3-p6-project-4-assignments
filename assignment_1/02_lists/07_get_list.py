# Get List
# Prompt the user to generate a list and then print the list


def main():
    input_list : list = []
    # Prompt the user to generate a list by entering one item at a time
    print("Generate a list by entering one item at a time")

    while True:
        user_input : str = input("Enter item(enter nothing to stop): ")
        if not user_input:
            break
        input_list.append(user_input)

    print(f"Here's the list: {input_list}")

if __name__ == '__main__':
    main()