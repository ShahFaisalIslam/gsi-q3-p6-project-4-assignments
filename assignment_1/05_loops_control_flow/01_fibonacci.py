# Prints fibonacci numbers up to a maximum value
MAX_VALUE : int = 10000

def fibonacci(index : int, prev_terms: list[int]):
    # Case 1: index is less than 2. Same as index
    if index < 2:
        term = index
    # Case 2: index irrelevant, sum of prev terms
    else:
        term = sum(prev_terms)
    # Update the previous terms
    prev_terms.append(term)
    prev_terms.pop(0)
    return term


def main():
    index : int = 0
    term : int = 0
    prev_terms : list[int] = [0,0]
    while True:
        term = fibonacci(index,prev_terms)
        if term > MAX_VALUE:
            break
        print(term,end=" ")
        index += 1

if __name__ == '__main__':
    main()

#fib(0) = 0
#fib(1) = 1
#fib(2) 0 + 1 = 1
#fib(3) 1 + 1 = 2
#fib(3) 1 2 = 3