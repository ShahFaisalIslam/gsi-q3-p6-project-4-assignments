# Countdown Timer
# Counts down for given time, and then tells the user to go for a run
# Max time is : 99:59

MAX_TIME : int = 5999
from time import sleep,strftime,localtime

def min_sec(time_int : int) -> str:
    time_min : str = time_int // 60
    time_sec : str = time_int % 60
    return f"{time_min:02}:{time_sec:02}"
def main():
    # Obtain time in seconds from user
    time_str : str = input("Enter time in seconds: ")
    time_int : int = int(time_str)

    # Display given time in format of mm:ss
    while time_int:
        print(f"{min_sec(time_int)}",end="\r")
        sleep(1)
        time_int -= 1

    # Tell user to go for a run
    print("Now go for a run!")
if __name__ == '__main__':
    main()
