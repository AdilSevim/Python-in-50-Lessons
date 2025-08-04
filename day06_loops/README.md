# Day 6: Loops

## Today's Focus
- Repeating code with `for` and `while` loops
- Using loops to solve problems efficiently

**Today we learn how to repeat code!** Loops help us avoid writing the same code multiple times.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    for i in range(5):
        print("Hello", i)

main()
```

## Step-by-step Guide

1. **What are loops?**
   - Code that repeats until a condition is met
   - `for` loops repeat a specific number of times
   - `while` loops repeat while a condition is true

2. **For loops**
   - `for variable in range(number):` repeats 'number' times
   - `range(5)` creates numbers 0, 1, 2, 3, 4
   - The variable (like `i`) changes each time through the loop

3. **While loops**
   - `while condition:` repeats as long as condition is true
   - Must be careful to avoid infinite loops
   - Usually need to change something in the loop to eventually stop it

## Common Mistakes & Fixes

❌ Infinite loops with `while`
✅ Fix: Make sure the condition will eventually become false

❌ Off-by-one errors with `range()`
✅ Fix: Remember `range(5)` is 0,1,2,3,4 (not 1,2,3,4,5)

❌ Forgetting the colon `:` after `for` or `while`
✅ Fix: Always add a colon at the end of loop statements

## Mini Quiz

1. How many times does `for i in range(3):` repeat?
2. What is the difference between `for` and `while` loops?
3. What happens if the condition in a `while` loop never becomes false?

<details>
<summary>Answers</summary>

1. 3 times (i = 0, 1, 2)
2. `for` repeats a specific number of times; `while` repeats while a condition is true
3. Infinite loop - the program runs forever
</details>

## Homework Brief

Create a multiplication table generator that prints the multiplication table for a given number.
Use loops to generate and display all multiplication facts from 1 to 10.

## Stretch Goal (Optional)

Create a multiplication table that shows tables for multiple numbers (e.g., tables 1 through 5).

---

Run the examples:
```bash
python ex1_fizzbuzz.py
python ex2_guessing_game.py
python homework_multiplication_table.py
```

Expected outputs:
- ex1_fizzbuzz.py: Prints numbers 1-20 with FizzBuzz rules
- ex2_guessing_game.py: Interactive number guessing game
- homework_multiplication_table.py: Multiplication table for a user-specified number
