"""
Day 2, Example 2: Average of Three Numbers

Purpose: Calculate the average of three numbers entered by the user.
We use input() three times and print() to show the average.

Expected output when run:
Enter first number: [user types number]
Enter second number: [user types number]
Enter third number: [user types number]
The average is: [calculated average]
"""

# Get three numbers from the user
num1_input = input("Enter first number: ")
num2_input = input("Enter second number: ")
num3_input = input("Enter third number: ")

# Convert text inputs to numbers
num1 = float(num1_input)
num2 = float(num2_input)
num3 = float(num3_input)

# Calculate the average
average = (num1 + num2 + num3) / 3

# Display the result
print("The average is:", average)
