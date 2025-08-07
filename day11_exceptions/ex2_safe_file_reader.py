"""
Day 11, Example 2: Safe File Reader

Purpose: Safely read files with error handling.
We use try/except to handle file-related errors gracefully.

Expected output when run:
(First creates sample.txt with content)
Reading sample.txt:
This is a sample file.
File reading completed.

Reading non_existent.txt:
Error: File 'non_existent.txt' not found.
File reading completed.
"""

def create_sample_file():
    """Create a sample text file for demonstration."""
    with open("sample.txt", "w") as f:
        f.write("This is a sample file.\n")


def read_file_safely(filename):
    """Safely read a file with error handling.
    
    Args:
        filename: Name of the file to read
    """
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def main():
    """Demonstrate safe file reading with error handling."""
    # Create a sample file
    print("Creating sample.txt...")
    create_sample_file()
    
    # Try to read an existing file
    print("Reading sample.txt:")
    read_file_safely("sample.txt")
    print("File reading completed.\n")
    
    # Try to read a non-existent file
    print("Reading non_existent.txt:")
    read_file_safely("non_existent.txt")
    print("File reading completed.")


if __name__ == "__main__":
    main()
