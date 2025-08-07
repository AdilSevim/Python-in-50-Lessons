"""
Day 18, Homework: Grade Book Program

Purpose: Create a simple grade book that stores student grades in CSV format.
We use CSV files to save and load student grade information.

Expected output when run:
Grade Book
1. Add grade
2. View all grades
3. Find student grades
4. Exit
Choose an option (1-4): [user input]
[Based on user input, appropriate action is taken]
"""

import grade_book


def main():
    """Run the grade book program."""
    filename = "grades.csv"
    grades = grade_book.load_grades(filename)
    
    while True:
        print("\nGrade Book")
        print("1. Add grade")
        print("2. View all grades")
        print("3. Find student grades")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            grade = input("Enter grade: ")
            grade_book.add_grade(grades, name, subject, grade)
            print("Grade added!")
        elif choice == "2":
            if grades:
                print("\nAll Grades:")
                for grade in grades:
                    print(f"- {grade['Name']}: {grade['Subject']} - {grade['Grade']}")
            else:
                print("No grades found.")
        elif choice == "3":
            name = input("Enter student name: ")
            student_grades = grade_book.find_grades(grades, name)
            if student_grades:
                print(f"\n{name}'s Grades:")
                for grade in student_grades:
                    print(f"- {grade['Subject']}: {grade['Grade']}")
            else:
                print("No grades found for this student.")
        elif choice == "4":
            grade_book.save_grades(grades, filename)
            print("Grades saved. Goodbye!")
            break
        else:
            print("Invalid option!")


if __name__ == "__main__":
    main()
