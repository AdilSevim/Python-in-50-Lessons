"""
Day 4, Example 2: Pass/Fail with Logical Operators

Purpose: Determine if a student passes based on grade and attendance.
We use logical operators to combine multiple conditions.

Expected output when run:
Enter your grade (0-100): [user types number]
Enter your attendance percentage (0-100): [user types number]
Passed: True/False
"""

# Get student information
grade_input = input("Enter your grade (0-100): ")
attendance_input = input("Enter your attendance percentage (0-100): ")

# Convert to numbers
grade = float(grade_input)
attendance = float(attendance_input)

# Determine pass/fail criteria
# Pass if grade >= 60 AND attendance >= 75
min_grade = 60
min_attendance = 75

passed = grade >= min_grade and attendance >= min_attendance

# Display the result
print("Passed:", passed)
