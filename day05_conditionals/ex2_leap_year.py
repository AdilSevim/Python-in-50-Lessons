"""
Day 5, Example 2: Leap Year

Purpose: Determine if a year is a leap year using conditionals.
We use if/elif/else statements with logical operators to check leap year rules.

Expected output when run:
Enter a year: [user types number]
[year] is a leap year: True/False
"""

def is_leap_year(year):
    """Determine if a year is a leap year.
    
    Args:
        year: The year to check
    
    Returns:
        True if leap year, False otherwise
    """
    # Leap year rules:
    # 1. Divisible by 4
    # 2. If divisible by 100, must also be divisible by 400
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def main():
    """Get year from user and check if it's a leap year."""
    # Get the year from the user
    year_input = input("Enter a year: ")
    year = int(year_input)
    
    # Check if it's a leap year
    leap = is_leap_year(year)
    
    # Display the result
    print(year, "is a leap year:", leap)


if __name__ == "__main__":
    main()
