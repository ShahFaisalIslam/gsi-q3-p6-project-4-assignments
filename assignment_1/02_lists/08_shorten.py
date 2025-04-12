# Shorten a list
# Shortens a list by removing from the end till the list is MAX_LENGTH items
# long.

MAX_LENGTH : int = 3

def shorten(lst: list):
    if len(lst) <= MAX_LENGTH:
        return
    while len(lst) > MAX_LENGTH:
        print(lst.pop())

def main():
    input_list : list = []
    # Prompt the user to generate a list by entering one item at a time
    print("Generate a list by entering one item at a time")

    while True:
        user_input : str = input("Enter item(enter nothing to stop): ")
        if not user_input:
            break
        input_list.append(user_input)

    print(f"List: {input_list}")
    shorten(input_list)
    print(f"Shortened list: {input_list}")
if __name__ == '__main__':
    main()
