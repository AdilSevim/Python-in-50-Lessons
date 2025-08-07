"""
Day 15, Module: Text Analyzer

Purpose: Provide text analysis functions with type hints.
This module contains functions for analyzing text with proper type annotations.
"""

from typing import List, Dict


def get_word_lengths(text: str) -> List[int]:
    """Get the length of each word in a text.
    
    Args:
        text: The text to analyze
    
    Returns:
        A list of word lengths
    """
    words: List[str] = text.split()
    lengths: List[int] = []
    for word in words:
        lengths.append(len(word))
    return lengths


def count_characters(text: str) -> Dict[str, int]:
    """Count occurrences of each character in a text.
    
    Args:
        text: The text to analyze
    
    Returns:
        A dictionary with characters as keys and counts as values
    """
    char_counts: Dict[str, int] = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] = char_counts[char] + 1
        else:
            char_counts[char] = 1
    return char_counts


def find_longest_word(text: str) -> str:
    """Find the longest word in a text.
    
    Args:
        text: The text to analyze
    
    Returns:
        The longest word in the text
    """
    words: List[str] = text.split()
    longest: str = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest
