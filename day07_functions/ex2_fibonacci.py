"""
Day 7, Example 2: Fibonacci Calculator

Purpose: Calculate the nth Fibonacci number using a recursive function.
We create a function that calls itself to solve smaller versions of the same problem.

Expected output when run:
Enter a position in the Fibonacci sequence: [user types number]
The Fibonacci number at position [number] is [result]
"""

def fibonacci(n):
    """Calculate the nth Fibonacci number using recursion.
    
    Args:
        n: Position in the Fibonacci sequence (0-indexed)
    
    Returns:
        The nth Fibonacci number
    """
    # Base cases: F(0) = 0, F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # Recursive case: F(n) = F(n-1) + F(n-2)
        return fibonacci(n - 1) + fibonacci(n - 2)


def main():
    """Get position from user and calculate Fibonacci number."""
    # Get the position from the user
    position_input = input("Enter a position in the Fibonacci sequence: ")
    position = int(position_input)
    
    # Calculate the Fibonacci number
    fib_number = fibonacci(position)
    
    # Display the result
    print(f"The Fibonacci number at position {position} is {fib_number}")


if __name__ == "__main__":
    main()
