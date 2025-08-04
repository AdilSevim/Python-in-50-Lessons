"""
Day 8, Example 2: Min, Max, and Average Calculator

Purpose: Find the minimum, maximum, and average of a list of numbers.
We use a list to store multiple values and calculate statistics.

Expected output when run:
Numbers: [15, 22, 8, 35, 12, 28]
Minimum: 8
Maximum: 35
Average: 20.0
"""

def calculate_stats(numbers):
    """Calculate minimum, maximum, and average of a list of numbers.
    
    Args:
        numbers: A list of numbers
    
    Returns:
        A tuple containing (min, max, average)
    """
    # Find minimum and maximum
    min_value = min(numbers)
    max_value = max(numbers)
    
    # Calculate average
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(numbers)
    
    return (min_value, max_value, average)


def main():
    """Calculate statistics for a list of numbers."""
    # List of numbers
    numbers = [15, 22, 8, 35, 12, 28]
    
    # Calculate statistics
    min_val, max_val, avg = calculate_stats(numbers)
    
    # Display the results
    print("Numbers:", numbers)
    print("Minimum:", min_val)
    print("Maximum:", max_val)
    print("Average:", avg)


if __name__ == "__main__":
    main()
