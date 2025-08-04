"""
Day 8, Example 1: Batch Fahrenheit to Celsius Converter

Purpose: Convert a list of Fahrenheit temperatures to Celsius using a loop.
We use a list to store multiple temperature values and process them together.

Expected output when run:
Fahrenheit temperatures: [32, 50, 68, 86, 104]
Celsius temperatures: [0.0, 10.0, 20.0, 30.0, 40.0]
"""

def fahrenheit_to_celsius(f_temp):
    """Convert Fahrenheit temperature to Celsius.
    
    Args:
        f_temp: Temperature in Fahrenheit
    
    Returns:
        Temperature in Celsius
    """
    return (f_temp - 32) * 5/9


def main():
    """Convert a list of Fahrenheit temperatures to Celsius."""
    # List of Fahrenheit temperatures
    fahrenheit_temps = [32, 50, 68, 86, 104]
    
    # Create an empty list for Celsius temperatures
    celsius_temps = []
    
    # Convert each Fahrenheit temperature to Celsius
    for f_temp in fahrenheit_temps:
        c_temp = fahrenheit_to_celsius(f_temp)
        celsius_temps.append(c_temp)
    
    # Display the results
    print("Fahrenheit temperatures:", fahrenheit_temps)
    print("Celsius temperatures:", celsius_temps)


if __name__ == "__main__":
    main()
