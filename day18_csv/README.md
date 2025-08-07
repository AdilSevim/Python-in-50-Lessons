# Day 18: Working with CSV Files

## Today's Focus
- Understanding CSV (Comma-Separated Values) format
- Using the csv module to read and write CSV files

**Today we learn to work with CSV files!** CSV is a simple format for storing tabular data.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    import csv
    data = [['Name', 'Age'], ['Alice', '30'], ['Bob', '25']]
    with open('sample.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
    print("CSV file created!")

main()
```

## Step-by-step Guide

1. **What is CSV?**
   - Comma-Separated Values format
   - Simple way to store tabular data
   - Widely used for data exchange between applications
   - Can be opened in spreadsheet programs like Excel

2. **CSV module basics**
   - `csv.reader()`: Read data from CSV files
   - `csv.writer()`: Write data to CSV files
   - `csv.DictReader()`: Read CSV as dictionaries (first row as keys)
   - `csv.DictWriter()`: Write CSV from dictionaries

3. **Working with CSV files**
   - Always open CSV files with `newline=''` parameter
   - Use `with` statement for proper file handling
   - Handle different delimiters if needed
   - Be aware of encoding issues with special characters

## Common Mistakes & Fixes

❌ Forgetting `newline=''` when opening CSV files for writing
✅ Fix: Always use `newline=''` to avoid extra blank lines

❌ Not using `with` statement for file handling
✅ Fix: Use `with` statement to ensure files are properly closed

❌ Not handling different delimiters
✅ Fix: Specify delimiter parameter when needed (e.g., `delimiter=';'`)

## Mini Quiz

1. How do you create a CSV writer object?
2. What's the difference between `csv.reader()` and `csv.DictReader()`?
3. Why should you use `newline=''` when opening CSV files for writing?

<details>
<summary>Answers</summary>

1. `csv.writer(file)`
2. `csv.reader()` returns lists; `csv.DictReader()` returns dictionaries
3. To prevent extra blank lines in the CSV file
</details>

## Homework Brief

Create a simple grade book that stores student grades in CSV format.
Use CSV files to save and load student grade information.

## Stretch Goal (Optional)

Add functionality to calculate averages and find top-performing students.

---

Run the examples:
```bash
python ex1_csv_basics.py
python ex2_csv_dicts.py
python homework_grade_book.py
```

Expected outputs:
- ex1_csv_basics.py: Demonstrates basic CSV reading and writing with lists
- ex2_csv_dicts.py: Shows CSV reading and writing with dictionaries
- homework_grade_book.py: Implements a grade book using CSV for storage
