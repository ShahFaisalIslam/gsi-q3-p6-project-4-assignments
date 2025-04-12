# Get First Element
# Create a function that takes list as argument, and prints first element

# Function that takes list as argument, and prints first element
def get_first_element(input_list : list):
    return input_list[0]

def main():
    input_list : list = []
    # Prompt the user to generate a list by entering one item at a time
    print("Generate a list by entering one item at a time")

    while True:
        user_input : str = input("Enter item(enter nothing to stop): ")
        if not user_input:
            break
        input_list.append(user_input)

    print(f"First element: {get_first_element(input_list)}")

if __name__ == '__main__':
    main()