from time import sleep

# Liftoff
# Counts down from 10 to 1 and then calls off the liftoff of the spaceship!



def main():
    countdown : int = 10
    while countdown > 0:
        print(countdown)
        countdown -= 1
        sleep(1)
    print("Liftoff!")


if __name__ == '__main__':
    main()