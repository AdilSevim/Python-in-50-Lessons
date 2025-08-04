# Day 7: Functions

## Today's Focus
- Creating and using custom functions
- Understanding function parameters and return values

**Today we dive deeper into functions!** We'll learn to create our own functions to organize code.

## Warm-up
Try this in your Python interpreter:
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))
```

## Step-by-step Guide

1. **What are functions?**
   - Reusable blocks of code that perform a specific task
   - Can take inputs (parameters) and return outputs (return values)
   - Help organize code and avoid repetition

2. **Creating functions**
   - Use `def function_name(parameters):` to define a function
   - Indent the code inside the function
   - Use `return` to send a value back

3. **Using functions**
   - Call the function by name: `function_name(arguments)`
   - Pass values to parameters when calling
   - Use the return value if needed: `result = function_name(arg)`

## Common Mistakes & Fixes

❌ Forgetting the colon `:` after the function definition
✅ Fix: Always add a colon at the end of the `def` line

❌ Not returning a value when one is expected
✅ Fix: Use `return` to send back a result

❌ Confusing parameters (in definition) with arguments (when calling)
✅ Fix: Parameters are the variables in the function definition; arguments are the values passed when calling

## Mini Quiz

1. What is the purpose of a function?
2. What does `return` do in a function?
3. What's the difference between a parameter and an argument?

<details>
<summary>Answers</summary>

1. To organize code into reusable blocks that perform a specific task
2. It sends a value back to the code that called the function
3. Parameters are the variables in the function definition; arguments are the values passed when calling
</details>

## Homework Brief

Create a prime number checker and a function to find the next prime number.
Use functions to determine if a number is prime and to find the next prime after a given number.

## Stretch Goal (Optional)

Create a function that generates a list of the first n prime numbers.

---

Run the examples:
```bash
python ex1_factorial.py
python ex2_fibonacci.py
python homework_prime_tools.py
```

Expected outputs:
- ex1_factorial.py: Calculates factorial of a number using iteration
- ex2_fibonacci.py: Calculates Fibonacci number using recursion
- homework_prime_tools.py: Checks if number is prime and finds next prime
