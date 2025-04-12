# Get Last Element
# Create a function that takes list as argument, and prints last element

# Function that takes list as argument, and prints last element
def get_last_element(input_list : list):
    return input_list[-1]

def main():
    input_list : list = []
    # Prompt the user to generate a list by entering one item at a time
    print("Generate a list by entering one item at a time")

    while True:
        user_input : str = input("Enter item(enter nothing to stop): ")
        if not user_input:
            break
        input_list.append(user_input)

    print(f"last element: {get_last_element(input_list)}")

if __name__ == '__main__':
    main()