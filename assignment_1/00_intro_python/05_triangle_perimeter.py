# Obtain the lengths of each side of a triangle from the user, and then
# calculate and print the perimeter of the triangle

# Triangle class
class Triangle:
    def __init__(self,length_1 : float, length_2: float, length_3: float) -> None:
        self.length_1 = length_1
        self.length_2 = length_2
        self.length_3 = length_3

    # Calculate the perimeter, which is the sum of all lengths of the triangle
    def perimeter(self) -> float:
        return self.length_1 + self.length_2 + self.length_3

def main():
    # Prompt the user to enter the lengths of each side of triangle
    input_1 : float = float(input("What is the length of side 1? "))
    input_2 : float = float(input("What is the length of side 2? "))
    input_3 : float = float(input("What is the length of side 3? "))

    # Create a Triangle instance
    triangle : Triangle = Triangle(input_1,input_2,input_3)

    # Display the perimeter as calculated by the object
    print(f"The perimeter of the triangle is {triangle.perimeter()}")

if __name__ == '__main__':
    main()