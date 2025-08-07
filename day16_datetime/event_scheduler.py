"""
Day 16, Module: Event Scheduler

Purpose: Provide event scheduling functions using datetime objects.
This module contains functions for managing events with dates and times.
"""

from datetime import datetime
from typing import List, Tuple

class Event:
    """A class to represent a scheduled event."""
    
    def __init__(self, name: str, event_datetime: datetime):
        """Initialize an Event object.
        
        Args:
            name: The event name
            event_datetime: The date and time of the event
        """
        self.name = name
        self.datetime = event_datetime
    
    def __str__(self) -> str:
        """Return a string representation of the event."""
        return f"{self.name} on {self.datetime.strftime('%Y-%m-%d at %H:%M')}"


def schedule_event(name: str, event_datetime: datetime) -> Event:
    """Create a new event.
    
    Args:
        name: The event name
        event_datetime: The date and time of the event
    
    Returns:
        A new Event object
    """
    return Event(name, event_datetime)


def display_event(event: Event) -> None:
    """Display an event's details.
    
    Args:
        event: The event to display
    """
    print(event)


def is_future_event(event: Event) -> bool:
    """Check if an event is in the future.
    
    Args:
        event: The event to check
    
    Returns:
        True if the event is in the future, False otherwise
    """
    return event.datetime > datetime.now()
