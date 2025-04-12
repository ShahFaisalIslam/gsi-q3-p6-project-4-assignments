# E = mc2
# Continually ask user for mass in kilograms, and display the equivalent energy
# in Joules

C : int = 299792458 # metres per second

# Converts mass to energy using the formula e = mc2
def mass_to_energy(mass:float) -> float:
    return mass * (C ** 2)

def main():
    # Implement while loop for continual input
    while True:
        # Ask user for input
        user_input : str = input("Enter kilos of mass(enter nothing to exit): ")

        # Break the loop if empty
        if not user_input:
            break

        mass : float = float(user_input)

        # Print energy
        print(f"""\
e = m * C ^ 2...
m = {mass} kg
C = {C} m/s
{mass_to_energy(mass)} joules of energy!
""")



if __name__ == '__main__':
    main()