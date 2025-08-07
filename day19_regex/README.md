# Day 19: Regular Expressions

## Today's Focus
- Understanding regular expressions (regex) patterns
- Using the re module to search, match, and manipulate text

**Today we learn about regular expressions!** Regex helps us search and manipulate text patterns.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    import re
    text = "Contact: john@example.com or call 123-456-7890"
    email = re.search(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
    phone = re.search(r'\b\d{3}-\d{3}-\d{4}\b', text)
    print("Email found:", email.group() if email else "None")
    print("Phone found:", phone.group() if phone else "None")

main()
```

## Step-by-step Guide

1. **What are regular expressions?**
   - Patterns for matching text
   - Powerful tool for text processing
   - Used for validation, search, and replacement

2. **Common regex patterns**
   - `.` : Any character except newline
   - `\d`: Any digit (0-9)
   - `\w`: Any word character (letters, digits, underscore)
   - `\s`: Any whitespace character
   - `*` : Zero or more occurrences
   - `+` : One or more occurrences
   - `?` : Zero or one occurrence
   - `[]`: Character set
   - `()` : Grouping

3. **Using the re module**
   - `re.search()`: Find first match
   - `re.findall()`: Find all matches
   - `re.sub()`: Replace matches
   - `re.match()`: Match at beginning of string

## Common Mistakes & Fixes

❌ Forgetting to escape special characters
✅ Fix: Use raw strings (r"pattern") or escape with backslashes

❌ Using `match()` instead of `search()` when you need to find anywhere in string
✅ Fix: Use `search()` for finding anywhere in string; `match()` only checks beginning

❌ Not using raw strings for patterns with backslashes
✅ Fix: Use raw strings like r"\d+" instead of "\\d+"

## Mini Quiz

1. What does `\d+` match?
2. How do you find all occurrences of a pattern in a string?
3. What's the difference between `re.match()` and `re.search()`?

<details>
<summary>Answers</summary>

1. One or more digits
2. `re.findall(pattern, string)`
3. `match()` only checks the beginning; `search()` checks the entire string
</details>

## Homework Brief

Create a text validator that checks email addresses and phone numbers using regex.
Use regular expressions to validate common text patterns.

## Stretch Goal (Optional)

Add more complex validation patterns like URLs or postal codes.

---

Run the examples:
```bash
python ex1_regex_basics.py
python ex2_regex_groups.py
python homework_text_validator.py
```

Expected outputs:
- ex1_regex_basics.py: Demonstrates basic regex patterns and searching
- ex2_regex_groups.py: Shows how to use groups to extract specific parts of matches
- homework_text_validator.py: Implements a text validator using regex patterns
