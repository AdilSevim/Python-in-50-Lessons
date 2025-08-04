"""
Day 2, Homework: Unit Converter

Purpose: Convert between different units of measurement.
Convert kilometers to miles and Celsius to Fahrenheit using input and print.

Expected output when run:
Enter distance in kilometers: [user types number]
[distance] kilometers is [miles] miles
Enter temperature in Celsius: [user types number]
[temperature] Celsius is [fahrenheit] Fahrenheit
"""

# Convert kilometers to miles
km_input = input("Enter distance in kilometers: ")
km = float(km_input)
miles = km * 0.621371
print(km, "kilometers is", miles, "miles")

# Convert Celsius to Fahrenheit
celsius_input = input("Enter temperature in Celsius: ")
celsius = float(celsius_input)
fahrenheit = (celsius * 9/5) + 32
print(celsius, "Celsius is", fahrenheit, "Fahrenheit")
