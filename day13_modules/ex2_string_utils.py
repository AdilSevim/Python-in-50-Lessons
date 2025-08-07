"""
Day 13, Example 2: Using String Utilities Module

Purpose: Demonstrate using a custom string utility module.
We import and use functions from our own string_utils module.

Expected output when run:
Original text: hello world
Reversed text: dlrow olleh
Capitalized text: Hello World
Vowel count: 3
"""

# Import our custom string utilities module
import string_utils


def main():
    """Demonstrate using the string_utils module."""
    # Original text
    text = "hello world"
    print(f"Original text: {text}")
    
    # Reverse the string
    reversed_text = string_utils.reverse_string(text)
    print(f"Reversed text: {reversed_text}")
    
    # Capitalize words
    capitalized_text = string_utils.capitalize_words(text)
    print(f"Capitalized text: {capitalized_text}")
    
    # Count vowels
    vowel_count = string_utils.count_vowels(text)
    print(f"Vowel count: {vowel_count}")


if __name__ == "__main__":
    main()
