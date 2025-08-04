"""
Day 7, Example 1: Factorial Calculator

Purpose: Calculate the factorial of a number using a function with iteration.
We create a function that takes a number and returns its factorial.

Expected output when run:
Enter a number: [user types number]
The factorial of [number] is [result]
"""

def factorial(n):
    """Calculate the factorial of a number using iteration.
    
    Args:
        n: A non-negative integer
    
    Returns:
        The factorial of n (n!)
    """
    # Factorial of 0 is 1 by definition
    if n == 0:
        return 1
    
    # Calculate factorial using a loop
    result = 1
    for i in range(1, n + 1):
        result = result * i
    
    return result


def main():
    """Get number from user and calculate factorial."""
    # Get the number from the user
    number_input = input("Enter a number: ")
    number = int(number_input)
    
    # Calculate the factorial
    fact = factorial(number)
    
    # Display the result
    print(f"The factorial of {number} is {fact}")


if __name__ == "__main__":
    main()
