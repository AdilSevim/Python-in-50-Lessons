"""
Day 11, Example 1: Safe Number Input

Purpose: Safely get numbers from user input using exception handling.
We use try/except to handle invalid input gracefully.

Expected output when run:
Please enter a number: [user types valid number]
You entered: [number]

OR

Please enter a number: [user types invalid input]
Invalid input! Please enter a valid number.
Please enter a number: [user types valid number]
You entered: [number]
"""

def get_number():
    """Safely get a number from user input.
    
    Returns:
        A valid number entered by the user
    """
    while True:  # Keep asking until we get a valid number
        try:
            user_input = input("Please enter a number: ")
            number = float(user_input)  # Try to convert to float
            return number
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def main():
    """Get a number from user and display it."""
    number = get_number()
    print("You entered:", number)


if __name__ == "__main__":
    main()
