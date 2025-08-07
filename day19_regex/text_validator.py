"""
Day 19, Module: Text Validator

Purpose: Provide text validation functions using regular expressions.
This module contains functions for validating common text patterns.
"""

import re
from typing import Tuple, Optional

def validate_email(email: str) -> bool:
    """Validate an email address format.
    
    Args:
        email: The email address to validate
    
    Returns:
        True if valid, False otherwise
    """
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'
    return bool(re.match(pattern, email))


def validate_phone(phone: str) -> bool:
    """Validate a US phone number format.
    
    Args:
        phone: The phone number to validate
    
    Returns:
        True if valid, False otherwise
    """
    # Accept formats like: 123-456-7890, (123) 456-7890, 123.456.7890
    pattern = r'^\(?\d{3}\)?[-.]?\d{3}[-.]?\d{4}$'
    return bool(re.match(pattern, phone))


def extract_email_parts(email: str) -> Optional[Tuple[str, str, str]]:
    """Extract username, domain, and extension from an email.
    
    Args:
        email: The email address to parse
    
    Returns:
        Tuple of (username, domain, extension) if valid, None otherwise
    """
    pattern = r'^([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+)\.([A-Z|a-z]{2,})$'
    match = re.match(pattern, email)
    if match:
        return match.groups()
    return None
