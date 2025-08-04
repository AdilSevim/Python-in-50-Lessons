"""
Day 3, Homework: Net Salary Calculator

Purpose: Calculate net salary after deducting taxes and insurance.
We use variables to store salary components and perform calculations.

Expected output when run:
Enter your gross salary: [user types number]
Gross Salary: [amount]
Taxes (20%): [amount]
Insurance (5%): [amount]
Net Salary: [amount]
"""

# Get gross salary from the user
gross_input = input("Enter your gross salary: ")
gross_salary = float(gross_input)

# Define deduction rates
tax_rate = 0.20      # 20% tax
insurance_rate = 0.05  # 5% insurance

# Calculate deductions
taxes = gross_salary * tax_rate
insurance = gross_salary * insurance_rate

# Calculate net salary
net_salary = gross_salary - taxes - insurance

# Display the salary breakdown
print("Gross Salary:", gross_salary)
print("Taxes (20%):", taxes)
print("Insurance (5%):", insurance)
print("Net Salary:", net_salary)
