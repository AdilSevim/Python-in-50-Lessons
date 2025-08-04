"""
Day 10, Homework: Simple Diary Application

Purpose: Create a diary that saves entries to a file and can read them back.
We use file handling to store diary entries with dates and retrieve them.

Expected output when run:
(First creates diary.txt if it doesn't exist)
Diary Entries:
No entries found.

Adding new entry...
Diary Entries:
2023-01-01: Today I learned about file handling in Python. It's really useful!
"""

import datetime

def load_diary(filename):
    """Load diary entries from a file.
    
    Args:
        filename: Name of the file to load from
    
    Returns:
        A list of diary entries
    """
    try:
        with open(filename, "r") as f:
            # Read all lines and remove newline characters
            entries = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        # If file doesn't exist, return empty list
        entries = []
    
    return entries


def save_diary_entry(filename, entry):
    """Save a diary entry to a file.
    
    Args:
        filename: Name of the file to save to
        entry: Diary entry to save
    """
    with open(filename, "a") as f:  # Use append mode to add to existing entries
        f.write(entry + "\n")


def display_diary(entries):
    """Display all diary entries.
    
    Args:
        entries: List of diary entries
    """
    if not entries:
        print("No entries found.")
    else:
        print("Diary Entries:")
        for entry in entries:
            print(entry)


def main():
    """Run the simple diary application."""
    filename = "diary.txt"
    
    # Load existing diary entries
    print("Loading diary...")
    diary_entries = load_diary(filename)
    
    # Display current diary
    display_diary(diary_entries)
    
    # Add a new entry
    print("\nAdding new entry...")
    # Get current date
    today = datetime.date.today().strftime("%Y-%m-%d")
    # Create sample entry
    new_entry = f"{today}: Today I learned about file handling in Python. It's really useful!"
    save_diary_entry(filename, new_entry)
    
    # Load and display updated diary
    diary_entries = load_diary(filename)
    display_diary(diary_entries)


if __name__ == "__main__":
    main()
