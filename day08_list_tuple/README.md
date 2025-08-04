# Day 8: Lists and Tuples

## Today's Focus
- Storing multiple values in lists and tuples
- Accessing and manipulating list elements

**Today we learn to work with collections of data!** Lists and tuples let us store multiple values together.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    temperatures = [20, 25, 18, 30]
    print("First temperature:", temperatures[0])
    print("All temperatures:", temperatures)

main()
```

## Step-by-step Guide

1. **What are lists and tuples?**
   - Lists: Ordered, changeable collections of values in square brackets `[1, 2, 3]`
   - Tuples: Ordered, unchangeable collections of values in parentheses `(1, 2, 3)`
   - Both can store any type of data (numbers, strings, etc.)

2. **Creating and accessing**
   - Create: `my_list = [1, 2, 3]` or `my_tuple = (1, 2, 3)`
   - Access: `my_list[0]` gets the first element (index starts at 0)
   - Length: `len(my_list)` gives the number of elements

3. **Working with lists**
   - Add: `my_list.append(item)` adds to the end
   - Change: `my_list[0] = new_value` changes an element
   - Loop: `for item in my_list:` processes each element

## Common Mistakes & Fixes

❌ `IndexError: list index out of range`
✅ Fix: Make sure index is less than the length of the list

❌ Trying to change tuple elements
✅ Fix: Use lists if you need to modify elements; tuples are immutable

❌ Forgetting that indexing starts at 0
✅ Fix: First element is at index 0, second at index 1, etc.

## Mini Quiz

1. What's the difference between a list and a tuple?
2. How do you access the third element of a list called `data`?
3. What does `len([1, 2, 3, 4])` return?

<details>
<summary>Answers</summary>

1. Lists are changeable (mutable); tuples are unchangeable (immutable)
2. `data[2]` (remember indexing starts at 0)
3. 4
</details>

## Homework Brief

Create a moving average calculator that computes the average of the last N values in a list.
Use lists to store values and calculate averages over sliding windows.

## Stretch Goal (Optional)

Add functionality to remove outliers before calculating the moving average.

---

Run the examples:
```bash
python ex1_batch_f_to_c.py
python ex2_min_max_avg.py
python homework_moving_average.py
```

Expected outputs:
- ex1_batch_f_to_c.py: Converts a list of Fahrenheit temperatures to Celsius
- ex2_min_max_avg.py: Finds minimum, maximum, and average of a list of numbers
- homework_moving_average.py: Calculates moving average of a list of numbers
