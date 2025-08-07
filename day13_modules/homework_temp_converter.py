"""
Day 13, Homework: Temperature Converter Program

Purpose: Use a temperature conversion module in a main program.
We organize temperature conversion functions in a separate module and import them.

Expected output when run:
Temperature Converter
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. Celsius to Kelvin
Enter your choice (1-3): [user input]
Enter temperature: [user input]
[Converted temperature result]
"""

# Import our custom temperature converter module
import temp_converter


def main():
    """Run the temperature converter program."""
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    
    # Get user's choice
    choice = input("Enter your choice (1-3): ")
    
    # Get temperature from user
    temp_input = input("Enter temperature: ")
    temperature = float(temp_input)
    
    # Perform conversion based on choice
    if choice == "1":
        result = temp_converter.celsius_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result:.2f}°F")
    elif choice == "2":
        result = temp_converter.fahrenheit_to_celsius(temperature)
        print(f"{temperature}°F is {result:.2f}°C")
    elif choice == "3":
        result = temp_converter.celsius_to_kelvin(temperature)
        print(f"{temperature}°C is {result:.2f}K")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
