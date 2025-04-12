# Double List
# Doubles every number in the given list

def double(numbers : list[int]) -> None:
    index = 0
    for _ in numbers:
        numbers[index] *= 2
        index += 1

def main():
    numbers = [1,2,3,4]
    double(numbers)
    print(numbers)

if __name__ == '__main__':
    main()