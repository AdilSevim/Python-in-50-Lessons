"""
Day 13, Example 1: Using Math Utilities Module

Purpose: Demonstrate using a custom math utility module.
We import and use functions from our own math_utils module.

Expected output when run:
Area of circle with radius 5: 78.54
Hypotenuse of triangle with sides 3 and 4: 5.0
Is 16 a perfect square? True
Is 15 a perfect square? False
"""

# Import our custom math utilities module
import math_utils


def main():
    """Demonstrate using the math_utils module."""
    # Calculate area of a circle
    radius = 5
    area = math_utils.calculate_area_of_circle(radius)
    print(f"Area of circle with radius {radius}: {area:.2f}")
    
    # Calculate hypotenuse of a right triangle
    side_a, side_b = 3, 4
    hypotenuse = math_utils.calculate_hypotenuse(side_a, side_b)
    print(f"Hypotenuse of triangle with sides {side_a} and {side_b}: {hypotenuse}")
    
    # Check if numbers are perfect squares
    num1, num2 = 16, 15
    is_square1 = math_utils.is_perfect_square(num1)
    is_square2 = math_utils.is_perfect_square(num2)
    print(f"Is {num1} a perfect square? {is_square1}")
    print(f"Is {num2} a perfect square? {is_square2}")


if __name__ == "__main__":
    main()
