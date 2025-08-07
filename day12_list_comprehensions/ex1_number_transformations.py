"""
Day 12, Example 1: Number Transformations

Purpose: Create lists of numbers with transformations using list comprehensions.
We use list comprehensions to generate lists more concisely than with loops.

Expected output when run:
Numbers 1-10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Squares: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
Even numbers: [2, 4, 6, 8, 10]
Even squares: [4, 16, 36, 64, 100]
Cubes of odd numbers: [1, 27, 125, 343, 729]
"""

def main():
    """Demonstrate various list comprehensions with numbers."""
    # Traditional way to create a list of numbers 1-10
    numbers = []
    for i in range(1, 11):
        numbers.append(i)
    
    # List comprehension way (much shorter!)
    numbers_comp = [i for i in range(1, 11)]
    
    # Create a list of squares
    squares = [i**2 for i in range(1, 11)]
    
    # Create a list of even numbers
    evens = [i for i in range(1, 11) if i % 2 == 0]
    
    # Create a list of squares of even numbers
    even_squares = [i**2 for i in range(1, 11) if i % 2 == 0]
    
    # Create a list of cubes of odd numbers
    odd_cubes = [i**3 for i in range(1, 11) if i % 2 != 0]
    
    # Display the results
    print("Numbers 1-10:", numbers_comp)
    print("Squares:", squares)
    print("Even numbers:", evens)
    print("Even squares:", even_squares)
    print("Cubes of odd numbers:", odd_cubes)


if __name__ == "__main__":
    main()
