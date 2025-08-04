# Day 9: Dictionaries

## Today's Focus
- Storing key-value pairs with dictionaries
- Accessing and manipulating dictionary data

**Today we learn about dictionaries!** Dictionaries let us store data with meaningful keys instead of just numbers.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    student = {"name": "Alice", "age": 20, "grade": "A"}
    print("Student name:", student["name"])
    print("All info:", student)

main()
```

## Step-by-step Guide

1. **What are dictionaries?**
   - Collections of key-value pairs in curly braces `{key: value}`
   - Keys are unique identifiers (usually strings)
   - Values can be any type of data

2. **Creating and accessing**
   - Create: `my_dict = {"key1": "value1", "key2": "value2"}`
   - Access: `my_dict["key1"]` gets the value associated with "key1"
   - Add: `my_dict["new_key"] = "new_value"` adds a new key-value pair

3. **Working with dictionaries**
   - Check if key exists: `if "key" in my_dict:`
   - Get all keys: `my_dict.keys()`
   - Get all values: `my_dict.values()`
   - Loop through keys: `for key in my_dict:`
   - Loop through key-value pairs: `for key, value in my_dict.items():`

## Common Mistakes & Fixes

❌ `KeyError: 'key'` when accessing a non-existent key
✅ Fix: Check if key exists first, or use `my_dict.get("key", default_value)`

❌ Confusing keys and values
✅ Fix: Remember keys are the identifiers, values are the data

❌ Forgetting curly braces `{}` for dictionaries
✅ Fix: Use curly braces `{}` for dictionaries, square brackets `[]` for lists

## Mini Quiz

1. How do you access the value associated with the key "name" in a dictionary called `person`?
2. How do you add a new key-value pair to a dictionary?
3. What happens if you try to access a key that doesn't exist in a dictionary?

<details>
<summary>Answers</summary>

1. `person["name"]`
2. `person["new_key"] = "new_value"`
3. A `KeyError` is raised
</details>

## Homework Brief

Create a simple inventory management system that tracks product quantities and prices.
Use dictionaries to store product information and update inventory levels.

## Stretch Goal (Optional)

Add functionality to calculate the total value of inventory (quantity × price for each product).

---

Run the examples:
```bash
python ex1_student_grades.py
python ex2_word_count.py
python homework_inventory.py
```

Expected outputs:
- ex1_student_grades.py: Manages student grades using a dictionary
- ex2_word_count.py: Counts word occurrences in a text using a dictionary
- homework_inventory.py: Tracks product quantities and prices in an inventory system
