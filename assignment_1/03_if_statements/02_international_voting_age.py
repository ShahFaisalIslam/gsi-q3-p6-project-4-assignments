# International Voting Age
# Ask user for their age and then inform them whether they can or cannot vote
# in the following fictional countries with their minimum voting ages:
# * Perturksbouipo : 16
# * Stanlau: 25
# * Mayengua: 48

voting_age: dict = {}
voting_age["Peturksbouipo"] = 16
voting_age["Stanlau"] = 25
voting_age["Mayengua"] = 48

def main():
    # Prompt the user for their age
    age : int = int(input("How old are you? "))

    # For each voting age, determine and tell
    for country in voting_age.keys():
        print(f"You {'cannot' if age < voting_age[country] else 'can'} vote in\
 {country} where the voting age is {voting_age[country]}.")
if __name__ == '__main__':
    main()