"""
Day 5, Example 1: Letter Grade

Purpose: Convert a numeric grade to a letter grade using conditionals.
We use if/elif/else statements to determine the letter grade.

Expected output when run:
Enter your numeric grade (0-100): [user types number]
Your letter grade is: [A/B/C/D/F]
"""
"""Convert numeric grade to letter grade."""
# Get the numeric grade from the user
grade_input = input("Enter your numeric grade (0-100): ")
grade = float(grade_input)
    
    # Determine the letter grade
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
    
# Display the result
print("Your letter grade is:", letter)

