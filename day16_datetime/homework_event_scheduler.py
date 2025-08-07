"""
Day 16, Homework: Event Scheduler Program

Purpose: Create a simple event scheduler that tracks events with dates and times.
We use datetime objects to store and manipulate event schedules.

Expected output when run:
Event Scheduler
Enter event details:
Event name: Team Meeting
Event date (YYYY-MM-DD): 2023-06-20
Event time (HH:MM): 14:30
Event scheduled: Team Meeting on 2023-06-20 at 14:30
Event is in the future: True
"""

import event_scheduler
from datetime import datetime

def main():
    """Run the event scheduler program."""
    print("Event Scheduler")
    print("Enter event details:")
    
    # Get event details from user
    name = input("Event name: ")
    date_str = input("Event date (YYYY-MM-DD): ")
    time_str = input("Event time (HH:MM): ")
    
    # Parse the date and time
    datetime_str = f"{date_str} {time_str}"
    event_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")
    
    # Schedule the event
    event = event_scheduler.schedule_event(name, event_datetime)
    
    # Display the event
    print("Event scheduled:", end=" ")
    event_scheduler.display_event(event)
    
    # Check if event is in the future
    is_future = event_scheduler.is_future_event(event)
    print("Event is in the future:", is_future)


if __name__ == "__main__":
    main()
