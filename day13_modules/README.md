# Day 13: Modules and Imports

## Today's Focus
- Organizing code into separate files (modules)
- Using import statements to access code from other files

**Today we learn to organize our code into modules!** Modules help us keep our code organized and reusable.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    import math
    print("Square root of 16:", math.sqrt(16))
    print("Pi:", math.pi)

main()
```

## Step-by-step Guide

1. **What are modules?**
   - Python files (.py) containing related code
   - Help organize large programs into manageable parts
   - Can be imported and used in other Python files

2. **Creating modules**
   - Create a .py file with functions, variables, or classes
   - Example: `math_utils.py` with math-related functions
   - Can be imported by other files using `import`

3. **Using modules**
   - `import module_name` imports the entire module
   - `from module_name import function_name` imports specific functions
   - `import module_name as alias` imports with a shorter name
   - Access module content with dot notation: `module.function()`

## Common Mistakes & Fixes

❌ Forgetting .py extension when importing
✅ Fix: Import the module name without .py extension

❌ Circular imports (module A imports module B, which imports module A)
✅ Fix: Restructure code to avoid circular dependencies

❌ Importing modules inside functions unnecessarily
✅ Fix: Place imports at the top of the file (standard practice)

## Mini Quiz

1. How do you import the entire `math` module?
2. How do you import just the `sqrt` function from the `math` module?
3. What's the benefit of organizing code into modules?

<details>
<summary>Answers</summary>

1. `import math`
2. `from math import sqrt`
3. Better organization, reusability, and maintainability of code
</details>

## Homework Brief

Create a temperature conversion module and use it in a main program.
Organize temperature conversion functions in a separate module and import them.

## Stretch Goal (Optional)

Create a package (folder with multiple modules) for different types of unit conversions.

---

Run the examples:
```bash
python ex1_math_utils.py
python ex2_string_utils.py
python homework_temp_converter.py
```

Expected outputs:
- ex1_math_utils.py: Demonstrates using custom math utility module
- ex2_string_utils.py: Demonstrates using custom string utility module
- homework_temp_converter.py: Uses a temperature conversion module in a main program
