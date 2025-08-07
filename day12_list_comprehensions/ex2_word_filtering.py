"""
Day 12, Example 2: Word Filtering

Purpose: Filter and process words using list comprehensions.
We use list comprehensions to select and transform words based on criteria.

Expected output when run:
Original words: ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
Long words: ['banana', 'cherry', 'elderberry']
Uppercase words: ['APPLE', 'BANANA', 'CHERRY', 'DATE', 'ELDERBERRY', 'FIG', 'GRAPE']
Short words capitalized: ['DATE', 'FIG']
Words with 'e': ['apple', 'cherry', 'elderberry', 'grape']
Reversed long words: ['ananab', 'yrrehc', 'yrrebredle']
"""

def main():
    """Demonstrate list comprehensions with word filtering and processing."""
    # List of words
    words = ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape']
    
    # Filter words longer than 5 characters
    long_words = [word for word in words if len(word) > 5]
    
    # Convert all words to uppercase
    uppercase_words = [word.upper() for word in words]
    
    # Filter short words (<= 4 characters) and capitalize them
    short_words_cap = [word.upper() for word in words if len(word) <= 4]
    
    # Filter words containing the letter 'e'
    words_with_e = [word for word in words if 'e' in word]
    
    # Get long words and reverse them
    reversed_long_words = [word[::-1] for word in words if len(word) > 5]
    
    # Display the results
    print("Original words:", words)
    print("Long words:", long_words)
    print("Uppercase words:", uppercase_words)
    print("Short words capitalized:", short_words_cap)
    print("Words with 'e':", words_with_e)
    print("Reversed long words:", reversed_long_words)


if __name__ == "__main__":
    main()
