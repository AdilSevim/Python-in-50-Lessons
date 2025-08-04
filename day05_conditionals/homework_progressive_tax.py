"""
Day 5, Homework: Progressive Tax Calculator

Purpose: Calculate tax based on progressive tax brackets.
We use conditionals to apply different tax rates to different income portions.

Expected output when run:
Enter your annual income: [user types number]
Tax owed: [calculated amount]
"""

def calculate_tax(income):
    """Calculate tax based on progressive tax brackets.
    
    Args:
        income: Annual income
    
    Returns:
        Total tax owed
    """
    # Progressive tax brackets (simplified)
    # 10% on income up to $10,000
    # 15% on income from $10,001 to $30,000
    # 25% on income above $30,000
    
    tax = 0.0
    
    if income <= 10000:
        tax = income * 0.10
    elif income <= 30000:
        tax = 10000 * 0.10 + (income - 10000) * 0.15
    else:
        tax = 10000 * 0.10 + 20000 * 0.15 + (income - 30000) * 0.25
    
    return tax


def main():
    """Get income from user and calculate tax."""
    # Get the income from the user
    income_input = input("Enter your annual income: ")
    income = float(income_input)
    
    # Calculate the tax
    tax_owed = calculate_tax(income)
    
    # Display the result
    print("Tax owed:", round(tax_owed, 2))


if __name__ == "__main__":
    main()
