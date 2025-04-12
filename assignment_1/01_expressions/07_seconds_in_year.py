# Seconds in year
# Print nicely how many seconds exist in an year (assuming 365 days per year)

# List of constants
SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60
HOURS_IN_DAY = 24
DAYS_IN_YEAR = 365

def seconds_in_year() -> int:
    return SECONDS_IN_MINUTE * MINUTES_IN_HOUR * HOURS_IN_DAY * DAYS_IN_YEAR

def main():
    print(f"There are {seconds_in_year()} seconds in an year!")

if __name__ == '__main__':
    main()