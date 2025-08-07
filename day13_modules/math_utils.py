"""
Day 13, Module: Math Utilities

Purpose: Provide math-related utility functions.
This module contains functions for common mathematical operations.
"""

import math

def calculate_area_of_circle(radius):
    """Calculate the area of a circle given its radius.
    
    Args:
        radius: The radius of the circle
    
    Returns:
        The area of the circle
    """
    return math.pi * radius ** 2


def calculate_hypotenuse(a, b):
    """Calculate the hypotenuse of a right triangle.
    
    Args:
        a: Length of one side
        b: Length of the other side
    
    Returns:
        The length of the hypotenuse
    """
    return math.sqrt(a ** 2 + b ** 2)


def is_perfect_square(n):
    """Check if a number is a perfect square.
    
    Args:
        n: The number to check
    
    Returns:
        True if n is a perfect square, False otherwise
    """
    if n < 0:
        return False
    root = math.sqrt(n)
    return root == int(root)
