# Flowing with data structures
# Show that a list, when modified, retains changes because it is mutable

# Adds three copies of given input to list
def add_three_copies(input_list : list,original) -> None:
    for _ in range(3):
        input_list.append(original)

def main():
    message : str = input("Enter a message to copy: ")
    my_list = []
    print(f"List before: {my_list}")
    add_three_copies(my_list,message)
    print(f"List after: {my_list}")


if __name__ == '__main__':
    main()