# Fahrenheit to Celsius
# Takes temperature from user in fahrenheit, and outputs the temperature
# converted to celsius

# Calculate the temperature in celsius given temperature in fahrenheit
def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5.0 / 9.0

def main():
    # Prompt the user to give temperature in fahrenheit
    fahrenheit : float = float(input("Enter the temperature in fahrenheit: "))
    
    # Convert the temperature to celsius
    celsius = fahrenheit_to_celsius(fahrenheit)

    # Display the converted temperature
    print(f"Temperature: {fahrenheit}F = {round(celsius,2)}C")

if __name__ == '__main__':
    main()