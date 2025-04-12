# Division
# Ask the user for two numbers, and print the result of dividing the first
# number with the second number, and also the remainder

class Division:
    def calculate(self):
        self.quotient : int = self.dividend // self.divisor
        self.remainder : int = self.dividend % self.divisor

    def __init__(self,dividend : int,divisor: int):
        self.dividend = dividend
        self.divisor = divisor
        self.calculate()    

def main():
    # Prompt the user to enter the two numbers
    num_1 : int = int(input("Please enter an integer to be divided: "))
    num_2 : int = int(input("Please enter an integer to be divide by: "))

    # Calculate the division
    division : Division = Division(num_1,num_2)

    # Display the results
    print(f"The result of division is {division.quotient} with a remainder of\
 {division.remainder}")

if __name__ == '__main__':
    main()