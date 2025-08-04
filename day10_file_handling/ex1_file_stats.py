"""
Day 10, Example 1: File Statistics

Purpose: Count lines, words, and characters in a text file.
We use file handling to read a file and calculate statistics.

Expected output when run:
(First creates sample.txt with sample content)
File statistics for sample.txt:
Lines: 3
Words: 25
Characters: 124
"""

def create_sample_file():
    """Create a sample text file for demonstration."""
    with open("sample.txt", "w") as f:
        f.write("This is the first line of our sample file.\n")
        f.write("This is the second line with more content.\n")
        f.write("And this is the third and final line.\n")


def count_stats(filename):
    """Count lines, words, and characters in a file.
    
    Args:
        filename: Name of the file to analyze
    
    Returns:
        A tuple containing (lines, words, characters)
    """
    lines = 0
    words = 0
    characters = 0
    
    with open(filename, "r") as f:
        for line in f:
            lines = lines + 1
            words = words + len(line.split())
            characters = characters + len(line)
    
    return (lines, words, characters)


def main():
    """Create a sample file and count its statistics."""
    # Create a sample file
    print("Creating sample.txt...")
    create_sample_file()
    
    # Count statistics
    line_count, word_count, char_count = count_stats("sample.txt")
    
    # Display the results
    print(f"File statistics for sample.txt:")
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")


if __name__ == "__main__":
    main()
