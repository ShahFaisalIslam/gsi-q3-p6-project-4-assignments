# Print first twenty even numbers, starting from 0

def main():
    i : int = 0
    while i < 20:
        print(i * 2,end=" ")
        i += 1

if __name__ == '__main__':
    main()