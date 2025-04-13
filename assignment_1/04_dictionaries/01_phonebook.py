# Implement a phonebook

# Get numbers from the user
def get_user_numbers() -> dict[str,str]:
    phonebook : dict[str,str] = {}
    
    # Prompt the user continually to obtain names and numbers
    while True:
        name : str = input("Enter Name: ")
        if not name:
            break

        number : str = input("Enter Number: ")
        if not number:
            break

        phonebook[name] = number
    
    return phonebook

# Look up for a number by its name
def lookup_number(name: str,phonebook: dict[str,str]):
    if name not in phonebook.keys():
        print(f"{name} not found.")
        return
    
    print(f"{name} : {phonebook[name]}")

def main():

    # Get phone numbers from the user 
    phonebook : dict = get_user_numbers()

    # Continually ask the user to lookup numbers till they provide no name
    while True:
        name : str = input("Enter name to search in phonebook (leave blank to quit): ")
        if not name:
            break

        lookup_number(name,phonebook)

if __name__ == '__main__':
    main()