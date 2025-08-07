"""
Day 16, Example 2: Date Calculations

Purpose: Show date arithmetic and timedelta usage.
We use datetime objects to perform calculations with dates and times.

Expected output when run:
Birthday: 2023-03-15
Today: 2023-06-15
Days until birthday: 90 days, 0:00:00
Days since birthday: 90 days, 0:00:00
One week from now: 2023-06-22
One hour ago: 2023-06-15 13:30:45.123456
"""

from datetime import datetime, timedelta

def main():
    """Demonstrate date calculations with timedelta."""
    # Create specific dates
    birthday = datetime(2023, 3, 15)
    print("Birthday:", birthday.date())
    
    # Get current date
    today = datetime.now()
    print("Today:", today.date())
    
    # Calculate difference between dates
    days_until = birthday.replace(year=today.year + 1) - today
    print("Days until birthday:", days_until)
    
    # Calculate days since birthday this year
    birthday_this_year = birthday.replace(year=today.year)
    if birthday_this_year <= today:
        days_since = today - birthday_this_year
    else:
        days_since = birthday_this_year - today
    print("Days since birthday:", days_since)
    
    # Add time to current datetime
    one_week = timedelta(weeks=1)
    future_date = today + one_week
    print("One week from now:", future_date.date())
    
    # Subtract time from current datetime
    one_hour = timedelta(hours=1)
    past_time = today - one_hour
    print("One hour ago:", past_time)


if __name__ == "__main__":
    main()
