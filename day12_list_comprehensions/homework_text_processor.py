"""
Day 12, Homework: Text Processor

Purpose: Process text to find and format specific words using list comprehensions.
We use list comprehensions to filter and transform words based on various criteria.

Expected output when run:
Original text: The quick brown fox jumps over the lazy dog. The dog was really lazy!
Word list: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.', 'The', 'dog', 'was', 'really', 'lazy!']
Cleaned words: ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog', 'The', 'dog', 'was', 'really', 'lazy']
Uppercase words: ['THE', 'QUICK', 'BROWN', 'FOX', 'JUMPS', 'OVER', 'THE', 'LAZY', 'DOG', 'THE', 'DOG', 'WAS', 'REALLY', 'LAZY']
Long words: ['quick', 'brown', 'jumps', 'over', 'lazy', 'really']
Words starting with 't' (case insensitive): ['The', 'the', 'The']
"""

def main():
    """Process text using list comprehensions."""
    # Sample text
    text = "The quick brown fox jumps over the lazy dog. The dog was really lazy!"
    
    # Split text into words
    words = text.split()
    
    # Remove punctuation from words
    cleaned_words = [word.strip('.,!?;') for word in words]
    
    # Convert words to uppercase
    uppercase_words = [word.upper() for word in cleaned_words]
    
    # Filter words longer than 4 characters
    long_words = [word for word in cleaned_words if len(word) > 4]
    
    # Filter words starting with 't' (case insensitive)
    t_words = [word for word in cleaned_words if word.lower().startswith('t')]
    
    # Display the results
    print("Original text:", text)
    print("Word list:", words)
    print("Cleaned words:", cleaned_words)
    print("Uppercase words:", uppercase_words)
    print("Long words:", long_words)
    print("Words starting with 't' (case insensitive):", t_words)


if __name__ == "__main__":
    main()
