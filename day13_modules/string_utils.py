"""
Day 13, Module: String Utilities

Purpose: Provide string-related utility functions.
This module contains functions for common string operations.
"""

def reverse_string(s):
    """Reverse a string.
    
    Args:
        s: The string to reverse
    
    Returns:
        The reversed string
    """
    return s[::-1]


def capitalize_words(s):
    """Capitalize the first letter of each word in a string.
    
    Args:
        s: The string to process
    
    Returns:
        The string with each word capitalized
    """
    return ' '.join(word.capitalize() for word in s.split())


def count_vowels(s):
    """Count the number of vowels in a string.
    
    Args:
        s: The string to process
    
    Returns:
        The number of vowels in the string
    """
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
