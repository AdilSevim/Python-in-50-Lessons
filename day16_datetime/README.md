# Day 16: Working with Dates and Times

## Today's Focus
- Using the datetime module to work with dates and times
- Formatting and parsing date/time strings

**Today we learn to work with dates and times!** The datetime module helps us handle temporal data in our programs.

## Warm-up
Try this in your Python interpreter:
```python
def main():
    from datetime import datetime
    now = datetime.now()
    print("Current date and time:", now)
    print("Formatted:", now.strftime("%Y-%m-%d %H:%M:%S"))

main()
```

## Step-by-step Guide

1. **What is the datetime module?**
   - Built-in Python module for working with dates and times
   - Provides classes for manipulating dates, times, and intervals
   - Essential for applications that need temporal data

2. **Key datetime classes**
   - `datetime`: For date and time together
   - `date`: For dates only
   - `time`: For times only
   - `timedelta`: For representing time intervals

3. **Common operations**
   - Create datetime: `datetime.now()` or `datetime(2023, 1, 1, 12, 0)`
   - Format datetime: `dt.strftime("%Y-%m-%d")`
   - Parse datetime: `datetime.strptime("2023-01-01", "%Y-%m-%d")`
   - Calculate differences: `datetime1 - datetime2` gives a timedelta

## Common Mistakes & Fixes

❌ Forgetting to import from the datetime module
✅ Fix: Use `from datetime import datetime, date, time, timedelta`

❌ Confusing month/day order in date strings
✅ Fix: Always specify the format explicitly when parsing dates

❌ Not handling timezone information when needed
✅ Fix: Use timezone-aware datetimes for applications that need timezone support

## Mini Quiz

1. How do you get the current date and time?
2. How do you format a datetime object as a string?
3. How do you calculate the difference between two datetime objects?

<details>
<summary>Answers</summary>

1. `datetime.now()`
2. `dt.strftime(format_string)`
3. Subtract them: `datetime1 - datetime2`
</details>

## Homework Brief

Create a simple event scheduler that tracks events with dates and times.
Use datetime objects to store and manipulate event schedules.

## Stretch Goal (Optional)

Add functionality to calculate time remaining until events and sort events by date.

---

Run the examples:
```bash
python ex1_datetime_basics.py
python ex2_date_calculations.py
python homework_event_scheduler.py
```

Expected outputs:
- ex1_datetime_basics.py: Demonstrates creating, formatting, and parsing datetime objects
- ex2_date_calculations.py: Shows date arithmetic and timedelta usage
- homework_event_scheduler.py: Implements a simple event scheduler with datetime objects
