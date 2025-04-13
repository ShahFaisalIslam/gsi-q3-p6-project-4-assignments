# Leap Year
# Tells if year given by user is a leap year or not

# Tell whether a given year is a leap year in the Gregorian calendar
# Following are the criteria:
# * Year must be divisble by 4
# * Year must not be divisible by 100 unless it is divisible by 400
def is_leap_year(year :int) -> bool:
    if year % 400 == 0: # Any year divisible by 400 is a leap year
        return True
    elif year % 100 == 0: # Any other year divisible by 100 is not a leap year
        return False
    elif year % 4 == 0: # Any other year that is divisible by 4 is a leap year
        return True
    else: # All other years are not leap years
        return False

def main():
    # Prompt the user to give an year
    year : int = int(input("Enter an year: "))
    print(f"That's{'' if is_leap_year(year) else ' not'} a leap year!")

if __name__ == '__main__':
    main()