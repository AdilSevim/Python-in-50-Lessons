# Day 11: Exception Handling

## Today's Focus
- Handling errors gracefully with try/except blocks
- Understanding different types of exceptions

**Today we learn to handle errors!** We'll make our programs more robust by catching and handling exceptions.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    try:
        number = int(input("Enter a number: "))
        print("You entered:", number)
    except ValueError:
        print("That's not a valid number!")

main()
```

## Step-by-step Guide

1. **What are exceptions?**
   - Errors that occur during program execution
   - Examples: `ValueError`, `FileNotFoundError`, `ZeroDivisionError`
   - Without handling, they crash the program

2. **Handling exceptions**
   - `try:` block contains code that might cause an error
   - `except ExceptionType:` block handles specific errors
   - `except:` block (without type) handles any error
   - `else:` block runs if no exceptions occur
   - `finally:` block always runs, regardless of exceptions

3. **Common exception types**
   - `ValueError`: Wrong value type (e.g., int("abc"))
   - `FileNotFoundError`: File doesn't exist
   - `ZeroDivisionError`: Division by zero
   - `IndexError`: Invalid list index
   - `KeyError`: Invalid dictionary key

## Common Mistakes & Fixes

❌ Catching all exceptions with bare `except:`
✅ Fix: Catch specific exceptions to avoid hiding unexpected errors

❌ Forgetting that code after an unhandled exception doesn't run
✅ Fix: Use try/except to handle exceptions and continue execution

❌ Handling exceptions but not fixing the underlying issue
✅ Fix: Either fix the problem or provide meaningful feedback to the user

## Mini Quiz

1. What is the purpose of a try/except block?
2. What's the difference between `except:` and `except ValueError:`?
3. When does the `finally:` block execute?

<details>
<summary>Answers</summary>

1. To catch and handle errors so the program doesn't crash
2. `except:` catches all exceptions; `except ValueError:` catches only ValueError exceptions
3. The `finally:` block always executes, whether an exception occurred or not
</details>

## Homework Brief

Create a robust calculator that handles various input errors gracefully.
Use exception handling to manage invalid inputs, division by zero, and other errors.

## Stretch Goal (Optional)

Add functionality to save calculation history to a file, handling file I/O exceptions.

---

Run the examples:
```bash
python ex1_safe_number_input.py
python ex2_safe_file_reader.py
python homework_robust_calculator.py
```

Expected outputs:
- ex1_safe_number_input.py: Safely gets numbers from user input
- ex2_safe_file_reader.py: Safely reads files with error handling
- homework_robust_calculator.py: Calculator that handles various errors gracefully
