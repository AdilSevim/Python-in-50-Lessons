# Day 1: Python Setup & Hello World

## Today's Focus
- Writing your first Python program
- Using the `print()` function to display text

**Just print statements today!** No functions, no variables, no complex syntax. We're taking tiny steps.

## Warm-up
Try this in your Python interpreter:
```python
print("Hello, world!")
```

## Step-by-step Guide

1. **Create your first Python file**
   - Open your text editor
   - Type: `print("Hello, world!")`
   - Save as `ex1_hello_prints.py`

2. **Run your program**
   - Open terminal/command prompt
   - Navigate to the file location
   - Type: `python ex1_hello_prints.py`

3. **See the magic happen!**
   - You should see: `Hello, world!`

## Common Mistakes & Fixes

❌ `SyntaxError: Missing parentheses in call to 'print'`
✅ Fix: Use `print("text")` not `print "text"`

❌ `FileNotFoundError`
✅ Fix: Make sure you're in the correct directory

❌ `SyntaxError: EOL while scanning string literal`
✅ Fix: Make sure quotes match: `"text"` or `'text'`

## Mini Quiz

1. What does `print()` do?
2. How do you run a Python file named `my_script.py`?
3. What happens if you forget the closing quote in `print("Hello)`?

<details>
<summary>Answers</summary>

1. Displays text on the screen
2. `python my_script.py`
3. You get a SyntaxError
</details>

## Homework Brief

Create an ASCII art poster using multiple `print()` statements. Include your name and a fun message!

## Stretch Goal (Optional)

Add emojis to your poster (if your terminal supports them) or try creating shapes with characters like `*`, `-`, `|`.

---

Run the examples:
```bash
python ex1_hello_prints.py
python ex2_print_variations.py
python homework_ascii_poster.py
```

Expected outputs:
- ex1_hello_prints.py: Displays three greeting messages
- ex2_print_variations.py: Shows different ways to use print
- homework_ascii_poster.py: Your custom ASCII art poster
