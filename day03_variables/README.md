# Day 3: Variables

## Today's Focus
- Storing values in variables
- Using variables in calculations

**Just variables and basic math today!** Still no functions yet.

## Warm-up
Try this in your Python interpreter:
```python
price = 10
vat = 2
print("Total:", price + vat)
```

## Step-by-step Guide

1. **What is a variable?**
   - A named storage box for values
   - Like a labeled container: `price = 10`
   - Use the name to access the value later

2. **Creating variables**
   - `name = value` (e.g., `age = 25`)
   - Choose descriptive names (e.g., `price`, `tax_rate`)
   - Names can't start with numbers

3. **Using variables in calculations**
   - Use variable names directly in math
   - `total = price + tax`
   - Results can be stored in new variables

## Common Mistakes & Fixes

❌ `NameError: name 'price' is not defined`
✅ Fix: Create the variable before using it

❌ Forgetting to update variables
✅ Fix: Remember variables don't change unless you reassign them

❌ Using invalid names like `1st_item` or `my-price`
✅ Fix: Use letters, numbers, underscores; start with letter/underscore

## Mini Quiz

1. What is a variable?
2. How do you store the value 5 in a variable named `count`?
3. If `x = 10`, what is the value of `x + 5`?

<details>
<summary>Answers</summary>

1. A named storage box for values
2. `count = 5`
3. 15
</details>

## Homework Brief

Create a net salary calculator that takes gross salary and deducts taxes and insurance.
Use variables to store the different values and perform the calculations.

## Stretch Goal (Optional)

Add a bonus calculation that adds a percentage to the gross salary before deductions.

---

Run the examples:
```bash
python ex1_price_vat_discount.py
python ex2_triangle_area.py
python homework_net_salary.py
```

Expected outputs:
- ex1_price_vat_discount.py: Calculates final price after VAT and discount
- ex2_triangle_area.py: Calculates triangle area using base and height
- homework_net_salary.py: Calculates net salary after deductions
