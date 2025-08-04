"""
Day 3, Example 1: Price with VAT and Discount

Purpose: Calculate final price after adding VAT and applying discount.
We use variables to store prices and perform calculations.

Expected output when run:
Original price: 100.0
Price with VAT: 120.0
Final price after discount: 108.0
"""

# Store the original price
original_price = 100.0

# Calculate price with VAT (20%)
vat_rate = 0.20
price_with_vat = original_price + (original_price * vat_rate)

# Apply discount (10%)
discount_rate = 0.10
final_price = price_with_vat - (price_with_vat * discount_rate)

# Display the results
print("Original price:", original_price)
print("Price with VAT:", price_with_vat)
print("Final price after discount:", final_price)
