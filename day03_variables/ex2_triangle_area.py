"""
Day 3, Example 2: Triangle Area

Purpose: Calculate the area of a triangle using base and height.
We use variables to store the dimensions and perform the calculation.

Expected output when run:
Enter the base of the triangle: [user types number]
Enter the height of the triangle: [user types number]
The area of the triangle is: [calculated area]
"""

# Get triangle dimensions from the user
base_input = input("Enter the base of the triangle: ")
height_input = input("Enter the height of the triangle: ")

# Convert text inputs to numbers
base = float(base_input)
height = float(height_input)

# Calculate the area of the triangle
# Formula: area = 0.5 * base * height
area = 0.5 * base * height

# Display the result
print("The area of the triangle is:", area)
