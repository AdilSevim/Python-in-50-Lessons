"""
Day 17, Module: Contact Manager

Purpose: Provide contact management functions using JSON for storage.
This module contains functions for managing contacts with JSON serialization.
"""

import json
from typing import List, Dict, Optional

def save_contacts(contacts: List[Dict[str, str]], filename: str) -> None:
    """Save contacts to a JSON file.
    
    Args:
        contacts: List of contact dictionaries
        filename: Name of the file to save to
    """
    with open(filename, "w") as file:
        json.dump(contacts, file, indent=2)


def load_contacts(filename: str) -> List[Dict[str, str]]:
    """Load contacts from a JSON file.
    
    Args:
        filename: Name of the file to load from
    
    Returns:
        List of contact dictionaries
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def add_contact(contacts: List[Dict[str, str]], name: str, phone: str) -> None:
    """Add a new contact to the list.
    
    Args:
        contacts: List of contact dictionaries
        name: Contact's name
        phone: Contact's phone number
    """
    contacts.append({"name": name, "phone": phone})


def find_contact(contacts: List[Dict[str, str]], name: str) -> Optional[Dict[str, str]]:
    """Find a contact by name.
    
    Args:
        contacts: List of contact dictionaries
        name: Name to search for
    
    Returns:
        Contact dictionary if found, None otherwise
    """
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None
