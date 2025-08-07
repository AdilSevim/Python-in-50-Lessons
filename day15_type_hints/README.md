# Day 15: Type Hints

## Today's Focus
- Adding type hints to functions and variables
- Improving code readability and catching errors early

**Today we learn about type hints!** Type hints make our code more readable and help catch errors before running.

## Warm-up
Try this in your Python interpreter:
```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def main():
    message: str = greet("Alice")
    print(message)

main()
```

## Step-by-step Guide

1. **What are type hints?**
   - Optional annotations that specify expected data types
   - Don't affect program execution but improve readability
   - Help IDEs provide better autocomplete and error detection

2. **Adding type hints**
   - Function parameters: `def func(param: type)`
   - Return values: `def func() -> return_type:`
   - Variables: `variable: type = value`

3. **Common type hints**
   - Basic types: `int`, `float`, `str`, `bool`
   - Collections: `list`, `dict`, `tuple`
   - Optional values: `Optional[type]` (requires `from typing import Optional`)
   - No return: `-> None`

## Common Mistakes & Fixes

❌ Forgetting to import types from the `typing` module when needed
✅ Fix: Import required types: `from typing import List, Dict, Optional, etc.`

❌ Adding type hints that don't match actual usage
✅ Fix: Ensure hints match the actual data types used

❌ Overcomplicating type hints for simple cases
✅ Fix: Use simple hints for simple cases; complexity when needed

## Mini Quiz

1. How do you specify that a function parameter should be a string?
2. How do you specify that a function returns an integer?
3. What module do you need to import for complex type hints?

<details>
<summary>Answers</summary>

1. `def func(param: str)`
2. `def func() -> int:`
3. `typing` module
</details>

## Homework Brief

Add type hints to a text analysis module and its usage.
Use type hints to specify parameter and return types for text processing functions.

## Stretch Goal (Optional)

Use complex type hints like `List[str]` or `Dict[str, int]` for more precise type specification.

---

Run the examples:
```bash
python ex1_basic_type_hints.py
python ex2_function_type_hints.py
python homework_text_analyzer.py
```

Expected outputs:
- ex1_basic_type_hints.py: Demonstrates basic type hints for variables and simple functions
- ex2_function_type_hints.py: Shows type hints for functions with parameters and return values
- homework_text_analyzer.py: Uses type hints in a text analysis module
