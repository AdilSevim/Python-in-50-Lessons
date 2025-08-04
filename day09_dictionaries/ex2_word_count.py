"""
Day 9, Example 2: Word Counter

Purpose: Count word occurrences in a text using a dictionary.
We use a dictionary to store words as keys and their counts as values.

Expected output when run:
Text: "the quick brown fox jumps over the lazy dog the fox"
Word counts: {'the': 3, 'quick': 1, 'brown': 1, 'fox': 2, 'jumps': 1, 'over': 1, 'lazy': 1, 'dog': 1}
"""

def count_words(text):
    """Count occurrences of each word in a text.
    
    Args:
        text: A string of text
    
    Returns:
        A dictionary with words as keys and counts as values
    """
    # Create an empty dictionary for word counts
    word_counts = {}
    
    # Split text into words
    words = text.split()
    
    # Count each word
    for word in words:
        # If word is already in dictionary, increment count
        if word in word_counts:
            word_counts[word] = word_counts[word] + 1
        # If word is not in dictionary, add it with count of 1
        else:
            word_counts[word] = 1
    
    return word_counts


def main():
    """Count words in a sample text."""
    # Sample text
    text = "the quick brown fox jumps over the lazy dog the fox"
    
    # Count words
    counts = count_words(text)
    
    # Display the results
    print("Text:", repr(text))
    print("Word counts:", counts)


if __name__ == "__main__":
    main()
