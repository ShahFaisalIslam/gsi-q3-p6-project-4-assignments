# Pythagorean Theorem
# Asks user for lengths of the perpendicular sides of a right side triangle
# outputs the third side using the pythagorean theorem

from math import sqrt

# Display a reference triangle
def display_ref_triangle() -> None:
    print(r"""\
Reference:
          C
          |\  
          | \
          |  \
          A---B
""")

class Triangle:
    # Calculate the third side using pythagorean theorem
    def calculate_hypotenuse(self):
        self.hyp = sqrt(self.ab ** 2 + self.bc ** 2)

    def __init__(self, ab: float, bc: float):
        self.ab = ab
        self.bc = bc
        self.calculate_hypotenuse()

def main():
    display_ref_triangle()
    # Prompt user to enter the perpendicular sides
    ab : float = float(input("Enter the length of AB: "))
    ac : float = float(input("Enter the length of AC: "))

    # Print the third side
    triangle : Triangle = Triangle(ab,ac)
    print(f"The length of BC (the hypotenuse) is: {triangle.hyp}")

if __name__ == '__main__':
    main()