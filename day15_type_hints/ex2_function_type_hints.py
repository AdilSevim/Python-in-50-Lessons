"""
Day 15, Example 2: Function Type Hints

Purpose: Show type hints for functions with parameters and return values.
We use type hints to specify what types of data functions expect and return.

Expected output when run:
Sum: 15
Product: 50
Full name: John Doe
Word count: 4
"""

# Import typing module for complex type hints
from typing import List


def add_numbers(a: int, b: int) -> int:
    """Add two numbers together.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b


def multiply_numbers(x: float, y: float) -> float:
    """Multiply two numbers together.
    
    Args:
        x: First number
        y: Second number
    
    Returns:
        The product of x and y
    """
    return x * y


def create_full_name(first: str, last: str) -> str:
    """Combine first and last names.
    
    Args:
        first: First name
        last: Last name
    
    Returns:
        Full name as a single string
    """
    return f"{first} {last}"


def count_words(text: str) -> int:
    """Count the number of words in a text.
    
    Args:
        text: The text to analyze
    
    Returns:
        The number of words in the text
    """
    return len(text.split())


def main():
    """Demonstrate function type hints."""
    # Use functions with type hints
    sum_result: int = add_numbers(5, 10)
    print("Sum:", sum_result)
    
    product_result: float = multiply_numbers(5.0, 10.0)
    print("Product:", product_result)
    
    full_name: str = create_full_name("John", "Doe")
    print("Full name:", full_name)
    
    word_count: int = count_words("This is a sample sentence.")
    print("Word count:", word_count)


if __name__ == "__main__":
    main()
