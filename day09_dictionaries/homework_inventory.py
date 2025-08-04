"""
Day 9, Homework: Inventory Management System

Purpose: Track product quantities and prices using a dictionary.
We use a dictionary to store product information and update inventory levels.

Expected output when run:
Initial inventory: {'apples': {'quantity': 50, 'price': 0.5}, 'bananas': {'quantity': 30, 'price': 0.3}}
Adding oranges...
Updated inventory: {'apples': {'quantity': 50, 'price': 0.5}, 'bananas': {'quantity': 30, 'price': 0.3}, 'oranges': {'quantity': 25, 'price': 0.7}}
Selling 10 apples...
Final inventory: {'apples': {'quantity': 40, 'price': 0.5}, 'bananas': {'quantity': 30, 'price': 0.3}, 'oranges': {'quantity': 25, 'price': 0.7}}
"""

def main():
    """Manage inventory using a dictionary."""
    # Create a dictionary of products with quantity and price
    inventory = {
        "apples": {"quantity": 50, "price": 0.5},
        "bananas": {"quantity": 30, "price": 0.3}
    }
    
    # Display initial inventory
    print("Initial inventory:", inventory)
    
    # Add a new product
    print("Adding oranges...")
    inventory["oranges"] = {"quantity": 25, "price": 0.7}
    
    # Display updated inventory
    print("Updated inventory:", inventory)
    
    # Sell some products (decrease quantity)
    print("Selling 10 apples...")
    inventory["apples"]["quantity"] = inventory["apples"]["quantity"] - 10
    
    # Display final inventory
    print("Final inventory:", inventory)


if __name__ == "__main__":
    main()
