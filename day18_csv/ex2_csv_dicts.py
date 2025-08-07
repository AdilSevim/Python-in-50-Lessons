"""
Day 18, Example 2: CSV with Dictionaries

Purpose: Show CSV reading and writing with dictionaries.
We use the csv module's DictReader and DictWriter classes.

Expected output when run:
Writing data to employees.csv...
Reading data from employees.csv...
{'Name': 'Alice', 'Department': 'Engineering', 'Salary': '75000'}
{'Name': 'Bob', 'Department': 'Marketing', 'Salary': '65000'}
{'Name': 'Charlie', 'Department': 'Sales', 'Salary': '70000'}
"""

import csv

def main():
    """Demonstrate CSV operations with dictionaries."""
    # Data to save (list of dictionaries)
    employee_data = [
        {"Name": "Alice", "Department": "Engineering", "Salary": "75000"},
        {"Name": "Bob", "Department": "Marketing", "Salary": "65000"},
        {"Name": "Charlie", "Department": "Sales", "Salary": "70000"}
    ]
    
    # Write data to a CSV file
    print("Writing data to employees.csv...")
    with open("employees.csv", "w", newline="") as file:
        fieldnames = ["Name", "Department", "Salary"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        # Write header row
        writer.writeheader()
        
        # Write data rows
        writer.writerows(employee_data)
    
    # Read data from a CSV file
    print("Reading data from employees.csv...")
    with open("employees.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


if __name__ == "__main__":
    main()
