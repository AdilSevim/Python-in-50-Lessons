"""
Day 17, Example 2: JSON Files

Purpose: Show reading from and writing to JSON files.
We use the json module to save and load data from files.

Expected output when run:
Writing data to data.json...
Reading data from data.json...
Loaded data: {'students': [{'name': 'Alice', 'grade': 85}, {'name': 'Bob', 'grade': 92}], 'class': 'Math 101'}
"""

import json

def main():
    """Demonstrate reading from and writing to JSON files."""
    # Data to save
    class_data = {
        "class": "Math 101",
        "students": [
            {"name": "Alice", "grade": 85},
            {"name": "Bob", "grade": 92}
        ]
    }
    
    # Write data to a JSON file
    print("Writing data to data.json...")
    with open("data.json", "w") as file:
        json.dump(class_data, file, indent=2)
    
    # Read data from a JSON file
    print("Reading data from data.json...")
    with open("data.json", "r") as file:
        loaded_data = json.load(file)
    
    print("Loaded data:", loaded_data)


if __name__ == "__main__":
    main()
