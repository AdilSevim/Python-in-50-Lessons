"""
Day 19, Example 1: Regex Basics

Purpose: Demonstrate basic regex patterns and searching.
We use the re module to find patterns in text.

Expected output when run:
Text: Call 123-456-7890 or email john@example.com
Phone found: 123-456-7890
Email found: john@example.com
All digits: ['123', '456', '7890']
Words starting with 'e': ['email', 'example']
Replaced text: Call XXX-XXX-XXXX or email XXX@XXXX.XXX
"""

import re

def main():
    """Demonstrate basic regex operations."""
    # Sample text
    text = "Call 123-456-7890 or email john@example.com"
    print("Text:", text)
    
    # Find phone number pattern (XXX-XXX-XXXX)
    phone_pattern = r'\b\d{3}-\d{3}-\d{4}\b'
    phone_match = re.search(phone_pattern, text)
    if phone_match:
        print("Phone found:", phone_match.group())
    
    # Find email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_match = re.search(email_pattern, text)
    if email_match:
        print("Email found:", email_match.group())
    
    # Find all digits
    digit_matches = re.findall(r'\d+', text)
    print("All digits:", digit_matches)
    
    # Find words starting with 'e'
    e_words = re.findall(r'\be\w*', text)
    print("Words starting with 'e':", e_words)
    
    # Replace sensitive information
    replaced_text = re.sub(r'\b\d{3}-\d{3}-\d{4}\b', 'XXX-XXX-XXXX', text)
    replaced_text = re.sub(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', 'XXX@XXXX.XXX', replaced_text)
    print("Replaced text:", replaced_text)


if __name__ == "__main__":
    main()
