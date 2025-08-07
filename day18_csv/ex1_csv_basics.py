"""
Day 18, Example 1: CSV Basics

Purpose: Demonstrate basic CSV reading and writing with lists.
We use the csv module to work with comma-separated values files.

Expected output when run:
Writing data to students.csv...
Reading data from students.csv...
['Name', 'Age', 'Grade']
['Alice', '20', '85']
['Bob', '21', '92']
['Charlie', '19', '78']
"""

import csv

def main():
    """Demonstrate basic CSV operations with lists."""
    # Data to save (list of lists)
    student_data = [
        ["Name", "Age", "Grade"],
        ["Alice", "20", "85"],
        ["Bob", "21", "92"],
        ["Charlie", "19", "78"]
    ]
    
    # Write data to a CSV file
    print("Writing data to students.csv...")
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(student_data)
    
    # Read data from a CSV file
    print("Reading data from students.csv...")
    with open("students.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
