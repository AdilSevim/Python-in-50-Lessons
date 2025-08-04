"""
Day 6, Homework: Multiplication Table

Purpose: Generate a multiplication table for a user-specified number.
We use a loop to repeat multiplication and display the results.

Expected output when run:
Enter a number: [user types number]
[number] x 1 = [result]
[number] x 2 = [result]
...
[number] x 10 = [result]
"""

def main():
    """Generate and display a multiplication table."""
    # Get the number from the user
    number_input = input("Enter a number: ")
    number = int(number_input)
    
    # Generate the multiplication table from 1 to 10
    print(f"Multiplication table for {number}:")
    
    for i in range(1, 11):  # range(1, 11) gives us 1 to 10
        result = number * i
        print(f"{number} x {i} = {result}")


if __name__ == "__main__":
    main()
