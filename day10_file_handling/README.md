# Day 10: File Handling

## Today's Focus
- Reading from and writing to files
- Working with file paths and handling file errors

**Today we learn to work with files!** We'll read data from files and write data to files.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    # Write to a file
    with open("sample.txt", "w") as f:
        f.write("Hello, File!")
    
    # Read from a file
    with open("sample.txt", "r") as f:
        content = f.read()
        print(content)

main()
```

## Step-by-step Guide

1. **What is file handling?**
   - Reading data from files stored on your computer
   - Writing data to files for later use
   - Essential for saving and loading program data

2. **Opening files**
   - `open(filename, mode)` opens a file
   - Modes: "r" (read), "w" (write), "a" (append)
   - Always use `with` statement for automatic file closing

3. **Reading and writing**
   - Read: `content = f.read()` reads entire file
   - Read lines: `lines = f.readlines()` reads all lines into a list
   - Write: `f.write(text)` writes text to file
   - Write lines: `f.writelines(list_of_lines)` writes multiple lines

## Common Mistakes & Fixes

❌ Forgetting to close files
✅ Fix: Use `with` statement which automatically closes files

❌ `FileNotFoundError` when file doesn't exist
✅ Fix: Check if file exists or handle the exception

❌ Overwriting files accidentally
✅ Fix: Use "a" (append) mode to add to existing files, not "w" (write)

## Mini Quiz

1. What is the purpose of the `with` statement when working with files?
2. What's the difference between "w" and "a" modes when opening a file?
3. How do you read all lines from a file into a list?

<details>
<summary>Answers</summary>

1. It automatically closes the file when done, even if an error occurs
2. "w" overwrites the file; "a" adds to the end of the file
3. `f.readlines()`
</details>

## Homework Brief

Create a simple diary application that saves entries to a file and can read them back.
Use file handling to store diary entries with dates and retrieve them when requested.

## Stretch Goal (Optional)

Add functionality to search diary entries by date or keyword.

---

Run the examples:
```bash
python ex1_file_stats.py
python ex2_todo_list.py
python homework_diary.py
```

Expected outputs:
- ex1_file_stats.py: Counts lines, words, and characters in a text file
- ex2_todo_list.py: Manages a todo list saved to a file
- homework_diary.py: Simple diary application that saves and loads entries
