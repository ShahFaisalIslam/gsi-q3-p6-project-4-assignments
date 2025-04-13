# Double it
# Asks the user for a number, and then keeps doubling it till it becomes 100
# or greater
MAX_VALUE : int = 100
def main():
    curr_value : int = int(input("Enter a number: "))
    while curr_value < MAX_VALUE:
        print(f"{curr_value} doubled is {curr_value * 2}")
        curr_value *= 2

if __name__ == '__main__':
    main()