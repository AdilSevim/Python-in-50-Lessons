"""
Day 4, Homework: BMI Category Calculator

Purpose: Determine BMI category based on Body Mass Index value.
We use comparison operators to categorize BMI values.

Expected output when run:
Enter your weight in kg: [user types number]
Enter your height in meters: [user types number]
Your BMI is: [calculated BMI]
Category: [Underweight/Normal/Overweight/Obese]
"""

# Get user's weight and height
weight_input = input("Enter your weight in kg: ")
height_input = input("Enter your height in meters: ")

# Convert to numbers
weight = float(weight_input)
height = float(height_input)

# Calculate BMI
# Formula: BMI = weight / (height^2)
bmi = weight / (height ** 2)

# Determine BMI category
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"

# Display the results
print("Your BMI is:", round(bmi, 2))
print("Category:", category)
