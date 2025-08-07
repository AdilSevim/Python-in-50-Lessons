"""
Day 11, Homework: Robust Calculator

Purpose: Create a calculator that handles various input errors gracefully.
We use exception handling to manage invalid inputs, division by zero, and other errors.

Expected output when run:
Basic Calculator
Enter first number: [user input]
Enter operator (+, -, *, /): [user input]
Enter second number: [user input]
Result: [calculated result]

OR error messages for invalid inputs, division by zero, etc.
"""

def get_number(prompt):
    """Safely get a number from user input.
    
    Args:
        prompt: Message to display to user
    
    Returns:
        A valid number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def calculate(num1, operator, num2):
    """Perform calculation with error handling.
    
    Args:
        num1: First number
        operator: Mathematical operator (+, -, *, /)
        num2: Second number
    
    Returns:
        Result of the calculation
    
    Raises:
        ValueError: For invalid operator
        ZeroDivisionError: For division by zero
    """
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero!")
        return num1 / num2
    else:
        raise ValueError(f"Invalid operator: {operator}")


def main():
    """Run the robust calculator."""
    print("Basic Calculator")
    
    try:
        # Get inputs from user
        num1 = get_number("Enter first number: ")
        operator = input("Enter operator (+, -, *, /): ")
        num2 = get_number("Enter second number: ")
        
        # Perform calculation
        result = calculate(num1, operator, num2)
        
        # Display result
        print(f"Result: {result}")
        
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
