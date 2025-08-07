"""
Day 14, Homework: Bank Account Class

Purpose: Implement a BankAccount class with deposit and withdrawal methods.
We use classes to model a bank account with appropriate attributes and behaviors.

Expected output when run:
Account created for John with balance: $100.00
Depositing $50...
New balance: $150.00
Withdrawing $30...
New balance: $120.00
Attempting to withdraw $200...
Insufficient funds!
Final balance: $120.00
"""

class BankAccount:
    """A class to represent a bank account."""
    
    def __init__(self, owner, initial_balance=0):
        """Initialize a BankAccount object.
        
        Args:
            owner: The account owner's name
            initial_balance: The starting balance (default 0)
        """
        self.owner = owner
        self.balance = initial_balance
    
    def deposit(self, amount):
        """Deposit money into the account.
        
        Args:
            amount: The amount to deposit
        
        Returns:
            The new balance
        """
        if amount > 0:
            self.balance = self.balance + amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw money from the account.
        
        Args:
            amount: The amount to withdraw
        
        Returns:
            The new balance, or None if insufficient funds
        """
        if amount > 0 and amount <= self.balance:
            self.balance = self.balance - amount
            return self.balance
        else:
            return None
    
    def get_balance(self):
        """Get the current account balance."""
        return self.balance
    
    def __str__(self):
        """Return a string representation of the account."""
        return f"Account for {self.owner}, Balance: ${self.balance:.2f}"


def main():
    """Demonstrate using the BankAccount class."""
    # Create a bank account
    account = BankAccount("John", 100.0)
    print("Account created for John with balance: $100.00")
    
    # Deposit money
    print("Depositing $50...")
    account.deposit(50)
    print(f"New balance: ${account.get_balance():.2f}")
    
    # Withdraw money
    print("Withdrawing $30...")
    account.withdraw(30)
    print(f"New balance: ${account.get_balance():.2f}")
    
    # Try to withdraw more than the balance
    print("Attempting to withdraw $200...")
    result = account.withdraw(200)
    if result is None:
        print("Insufficient funds!")
    
    # Display final balance
    print(f"Final balance: ${account.get_balance():.2f}")


if __name__ == "__main__":
    main()
