# Day 12: List Comprehensions

## Today's Focus
- Creating lists concisely with list comprehensions
- Understanding and using conditional list comprehensions

**Today we learn a more concise way to work with lists!** List comprehensions let us create lists in a single line.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    # Traditional way
    squares1 = []
    for i in range(5):
        squares1.append(i**2)
    
    # List comprehension way
    squares2 = [i**2 for i in range(5)]
    
    print("Traditional:", squares1)
    print("Comprehension:", squares2)

main()
```

## Step-by-step Guide

1. **What are list comprehensions?**
   - A concise way to create lists
   - Often more readable and faster than loops
   - Follows the pattern: `[expression for item in iterable]`

2. **Basic syntax**
   - `[expression for item in iterable]`
   - Example: `[x*2 for x in [1, 2, 3]]` creates `[2, 4, 6]`
   - The expression is applied to each item in the iterable

3. **Conditional list comprehensions**
   - `[expression for item in iterable if condition]`
   - Example: `[x for x in [1, 2, 3, 4] if x % 2 == 0]` creates `[2, 4]`
   - Only items that meet the condition are included

## Common Mistakes & Fixes

❌ Making comprehensions too complex and hard to read
✅ Fix: Use regular loops for complex logic; reserve comprehensions for simple cases

❌ Forgetting that comprehensions create new lists
✅ Fix: Remember they don't modify existing lists; assign the result to a variable

❌ Trying to do too much in the expression part
✅ Fix: Keep expressions simple; move complex logic to functions

## Mini Quiz

1. How would you create a list of squares of numbers 1-5 using a list comprehension?
2. How do you filter items in a list comprehension?
3. When should you use a regular loop instead of a list comprehension?

<details>
<summary>Answers</summary>

1. `[i**2 for i in range(1, 6)]`
2. Add an `if` condition: `[item for item in iterable if condition]`
3. When the logic is complex or when readability would be compromised
</details>

## Homework Brief

Create a program that processes text to find and format specific words using list comprehensions.
Use list comprehensions to filter and transform words based on various criteria.

## Stretch Goal (Optional)

Implement nested list comprehensions to process a list of sentences (list of lists of words).

---

Run the examples:
```bash
python ex1_number_transformations.py
python ex2_word_filtering.py
python homework_text_processor.py
```

Expected outputs:
- ex1_number_transformations.py: Creates lists of numbers with transformations using comprehensions
- ex2_word_filtering.py: Filters and processes words using list comprehensions
- homework_text_processor.py: Processes text to find and format specific words using comprehensions
