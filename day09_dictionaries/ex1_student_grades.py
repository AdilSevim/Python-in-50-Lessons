"""
Day 9, Example 1: Student Grades Manager

Purpose: Manage student grades using a dictionary.
We use a dictionary to store student names as keys and their grades as values.

Expected output when run:
Grades: {'Alice': 85, 'Bob': 92, 'Charlie': 78}
Alice's grade: 85
Adding new student...
Grades: {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'Diana': 88}
"""

def main():
    """Manage student grades using a dictionary."""
    # Create a dictionary of student grades
    grades = {"Alice": 85, "Bob": 92, "Charlie": 78}
    
    # Display all grades
    print("Grades:", grades)
    
    # Access a specific student's grade
    print("Alice's grade:", grades["Alice"])
    
    # Add a new student
    print("Adding new student...")
    grades["Diana"] = 88
    
    # Display updated grades
    print("Grades:", grades)


if __name__ == "__main__":
    main()
