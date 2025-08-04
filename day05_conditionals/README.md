# Day 5: Conditionals

## Today's Focus
- Making decisions with `if`, `elif`, and `else`
- Introducing the `main()` function pattern

**Today we start using functions!** We'll learn the `main()` pattern that we'll use from now on.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    age = 20
    if age >= 18:
        print("You are an adult")
    else:
        print("You are a minor")

main()
```

## Step-by-step Guide

1. **What are conditionals?**
   - Code that runs only when certain conditions are met
   - `if` checks a condition
   - `elif` (else if) checks another condition
   - `else` runs when no conditions are met

2. **The `main()` function**
   - A special function that contains our main program logic
   - We call it at the bottom with `if __name__ == "__main__": main()`
   - This is the standard way to structure Python programs

3. **Using conditionals**
   - Indent the code that should run conditionally
   - Use colons `:` after `if`, `elif`, and `else`
   - Python uses indentation to group code blocks

## Common Mistakes & Fixes

❌ Forgetting the colon `:` after `if`, `elif`, or `else`
✅ Fix: Always add a colon at the end of these statements

❌ Inconsistent indentation
✅ Fix: Use 4 spaces for each indentation level (or tab, but be consistent)

❌ Using `=` instead of `==` in conditions
✅ Fix: Use `==` for comparison, `=` for assignment

## Mini Quiz

1. What does `elif` stand for?
2. What is the purpose of `if __name__ == "__main__": main()`?
3. What happens if none of the `if` or `elif` conditions are true and there's no `else`?

<details>
<summary>Answers</summary>

1. "else if" - checks another condition
2. It ensures main() runs when the script is executed directly
3. Nothing happens - the conditional block is skipped
</details>

## Homework Brief

Create a progressive tax calculator that applies different tax rates based on income brackets.
Use conditionals to determine which tax rate applies to different portions of income.

## Stretch Goal (Optional)

Add more tax brackets or implement a system where multiple brackets apply to different portions of income.

---

Run the examples:
```bash
python ex1_letter_grade.py
python ex2_leap_year.py
python homework_progressive_tax.py
```

Expected outputs:
- ex1_letter_grade.py: Converts numeric grade to letter grade
- ex2_leap_year.py: Determines if a year is a leap year
- homework_progressive_tax.py: Calculates tax based on income brackets
