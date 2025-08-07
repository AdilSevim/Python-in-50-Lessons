# Day 17: Working with JSON Data

## Today's Focus
- Understanding JSON (JavaScript Object Notation) format
- Using the json module to parse and generate JSON data

**Today we learn to work with JSON data!** JSON is a popular format for storing and exchanging data.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    import json
    data = {"name": "Alice", "age": 30}
    json_string = json.dumps(data)
    print("JSON string:", json_string)
    parsed = json.loads(json_string)
    print("Parsed data:", parsed)

main()
```

## Step-by-step Guide

1. **What is JSON?**
   - Lightweight data interchange format
   - Easy for humans to read and write
   - Easy for machines to parse and generate
   - Used widely in web APIs and configuration files

2. **JSON syntax**
   - Objects: `{"key": "value"}` (like Python dictionaries)
   - Arrays: `[1, 2, 3]` (like Python lists)
   - Data types: strings, numbers, booleans, null, objects, arrays
   - Strings must be in double quotes

3. **Working with JSON in Python**
   - `json.dumps()`: Convert Python object to JSON string
   - `json.loads()`: Parse JSON string to Python object
   - `json.dump()`: Write Python object to JSON file
   - `json.load()`: Read JSON data from file to Python object

## Common Mistakes & Fixes

❌ Forgetting to import the json module
✅ Fix: Add `import json` at the top of your file

❌ Trying to parse invalid JSON strings
✅ Fix: Ensure JSON strings are properly formatted with double quotes

❌ Not handling JSON parsing errors
✅ Fix: Use try/except blocks to catch `json.JSONDecodeError`

## Mini Quiz

1. How do you convert a Python dictionary to a JSON string?
2. How do you parse a JSON string back to a Python object?
3. What's the difference between `json.dump()` and `json.dumps()`?

<details>
<summary>Answers</summary>

1. `json.dumps(dictionary)`
2. `json.loads(json_string)`
3. `json.dump()` writes to a file; `json.dumps()` returns a string
</details>

## Homework Brief

Create a simple contact manager that stores contacts in JSON format.
Use JSON to save and load contact information to and from files.

## Stretch Goal (Optional)

Add functionality to search contacts by name and update existing contacts.

---

Run the examples:
```bash
python ex1_json_basics.py
python ex2_json_files.py
python homework_contact_manager.py
```

Expected outputs:
- ex1_json_basics.py: Demonstrates converting between Python objects and JSON strings
- ex2_json_files.py: Shows reading from and writing to JSON files
- homework_contact_manager.py: Implements a contact manager using JSON for storage
