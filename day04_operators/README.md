# Day 4: Operators

## Today's Focus
- Using comparison operators (==, !=, <, >, etc.)
- Combining conditions with logical operators (and, or, not)

**Just operators and basic logic today!** Still no functions yet.

## Warm-up
Try this in your Python interpreter:
```python
age = 20
print(age >= 18)  # True
print(age < 18)   # False
```

## Step-by-step Guide

1. **Comparison Operators**
   - `==` equal to
   - `!=` not equal to
   - `<` less than
   - `>` greater than
   - `<=` less than or equal to
   - `>=` greater than or equal to

2. **Logical Operators**
   - `and` both conditions must be true
   - `or` at least one condition must be true
   - `not` reverses the result

3. **Using Operators in Practice**
   - Combine comparisons: `age >= 18 and age <= 65`
   - Store results in variables: `is_adult = age >= 18`

## Common Mistakes & Fixes

❌ Using `=` instead of `==` for comparison
✅ Fix: Use `==` for comparison, `=` for assignment

❌ Forgetting that `and` requires both conditions to be true
✅ Fix: Use `or` if only one condition needs to be true

❌ Confusing `<=` and `<`
✅ Fix: `<=` means "less than OR equal", `<` means "strictly less than"

## Mini Quiz

1. What does `5 > 3` evaluate to?
2. What does `5 == 3` evaluate to?
3. What does `True and False` evaluate to?

<details>
<summary>Answers</summary>

1. True
2. False
3. False
</details>

## Homework Brief

Create a BMI (Body Mass Index) category calculator that determines if someone is underweight, normal, overweight, or obese based on their BMI value.
Use comparison operators to check which category the BMI falls into.

## Stretch Goal (Optional)

Add more detailed categories (e.g., severely underweight, moderately obese) or include health recommendations for each category.

---

Run the examples:
```bash
python ex1_comparison_table.py
python ex2_pass_fail.py
python homework_bmi_category.py
```

Expected outputs:
- ex1_comparison_table.py: Shows results of various comparison operations
- ex2_pass_fail.py: Determines pass/fail based on grade and attendance
- homework_bmi_category.py: Categorizes BMI values into health categories
