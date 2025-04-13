# Count numbers
# Count how many times each number occurs in a list
# Use a dictionary to track the count

# Prompt user to give numbers to create a list
def get_user_numbers() -> list[int]:
    numbers : list[int] = []
    while True:
        number : str = input("Enter a number(leave blank to stop): ")
        if not number:
            break
        numbers.append(int(number))

    return numbers

# Count how many times each number appears in the given list
def count_numbers(numbers : list[int]) -> dict:
    count : dict = {}
    for number in numbers:
        if number not in count.keys():
            count[number] = 1
        else:
            count[number] += 1
    
    return count

def main():
    # Get numbers from the user
    numbers : list[int] = get_user_numbers()

    # Count the numbers
    count : dict[int,int] = count_numbers(numbers)

    # Inform the user about each number
    for number in count.keys():
        print(f"{number} appears {count[number]} times.")

if __name__ == '__main__':
    main()