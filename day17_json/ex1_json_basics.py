"""
Day 17, Example 1: JSON Basics

Purpose: Demonstrate converting between Python objects and JSON strings.
We use the json module to work with JSON data in memory.

Expected output when run:
Python dictionary: {'name': 'Alice', 'age': 30, 'city': 'New York'}
JSON string: {"name": "Alice", "age": 30, "city": "New York"}
Parsed back to Python: {'name': 'Alice', 'age': 30, 'city': 'New York'}
List of numbers: [1, 2, 3, 4, 5]
JSON array: [1, 2, 3, 4, 5]
Parsed back to Python: [1, 2, 3, 4, 5]
"""

import json

def main():
    """Demonstrate JSON basics with strings."""
    # Create a Python dictionary
    person = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    
    print("Python dictionary:", person)
    
    # Convert Python dictionary to JSON string
    json_string = json.dumps(person)
    print("JSON string:", json_string)
    
    # Parse JSON string back to Python object
    parsed_person = json.loads(json_string)
    print("Parsed back to Python:", parsed_person)
    
    # Work with lists
    numbers = [1, 2, 3, 4, 5]
    print("List of numbers:", numbers)
    
    # Convert list to JSON array
    json_array = json.dumps(numbers)
    print("JSON array:", json_array)
    
    # Parse JSON array back to Python list
    parsed_numbers = json.loads(json_array)
    print("Parsed back to Python:", parsed_numbers)


if __name__ == "__main__":
    main()
