"""
Day 15, Homework: Text Analyzer Program

Purpose: Use type hints in a text analysis module and its usage.
We add type hints to specify parameter and return types for text processing functions.

Expected output when run:
Analyzing text: The quick brown fox jumps over the lazy dog
Word lengths: [3, 5, 5, 3, 5, 4, 3, 4, 3]
Character counts: {'t': 2, 'h': 2, 'e': 3, ' ': 8, 'q': 1, 'u': 2, 'i': 1, 'c': 1, 'k': 1, 'b': 1, 'r': 2, 'o': 4, 'w': 1, 'n': 1, 'f': 1, 'x': 1, 'j': 1, 'm': 1, 'p': 1, 's': 1, 'v': 1, 'l': 1, 'a': 1, 'z': 1, 'y': 1, 'd': 1, 'g': 1}
Longest word: 'quick' (5 characters)
"""

# Import our custom text analyzer module
import text_analyzer


def main():
    """Run the text analyzer program with type hints."""
    # Sample text to analyze
    sample_text: str = "The quick brown fox jumps over the lazy dog"
    print(f"Analyzing text: {sample_text}")
    
    # Get word lengths
    lengths: List[int] = text_analyzer.get_word_lengths(sample_text)
    print("Word lengths:", lengths)
    
    # Count characters
    char_counts: Dict[str, int] = text_analyzer.count_characters(sample_text)
    print("Character counts:", char_counts)
    
    # Find longest word
    longest: str = text_analyzer.find_longest_word(sample_text)
    print(f"Longest word: '{longest}' ({len(longest)} characters)")


if __name__ == "__main__":
    main()
