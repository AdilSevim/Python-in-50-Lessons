"""
Day 2, Example 1: Age Plus 10

Purpose: Calculate how old someone will be in 10 years.
We use input() to get the current age and print() to show the result.

Expected output when run:
What is your current age? [user types age]
In 10 years, you will be [age+10] years old.
"""

# Get the user's current age
age_input = input("What is your current age? ")

# Convert the text input to a number
current_age = int(age_input)

# Calculate age in 10 years
future_age = current_age + 10

# Display the result
print("In 10 years, you will be", future_age, "years old.")
