"""
Day 16, Example 1: DateTime Basics

Purpose: Demonstrate creating, formatting, and parsing datetime objects.
We use the datetime module to work with dates and times.

Expected output when run:
Current datetime: 2023-06-15 14:30:45.123456
Today's date: 2023-06-15
Current time: 14:30:45.123456
Formatted datetime: June 15, 2023 at 02:30 PM
Parsed datetime: 2023-12-25 00:00:00
"""

from datetime import datetime, date, time

def main():
    """Demonstrate datetime basics."""
    # Get current date and time
    now = datetime.now()
    print("Current datetime:", now)
    
    # Get today's date only
    today = date.today()
    print("Today's date:", today)
    
    # Get current time only
    current_time = now.time()
    print("Current time:", current_time)
    
    # Format datetime as a string
    formatted = now.strftime("%B %d, %Y at %I:%M %p")
    print("Formatted datetime:", formatted)
    
    # Parse a string into a datetime object
    date_string = "2023-12-25"
    parsed = datetime.strptime(date_string, "%Y-%m-%d")
    print("Parsed datetime:", parsed)


if __name__ == "__main__":
    main()
