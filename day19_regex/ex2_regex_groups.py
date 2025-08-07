"""
Day 19, Example 2: Regex Groups

Purpose: Show how to use groups to extract specific parts of matches.
We use parentheses to create groups in regex patterns.

Expected output when run:
Text: Date: 2023-06-15, Time: 14:30
Year: 2023
Month: 06
Day: 15
Hour: 14
Minute: 30
Swapped date: Date: 15/06/2023
"""

import re

def main():
    """Demonstrate regex groups for extracting parts of matches."""
    # Sample text
    text = "Date: 2023-06-15, Time: 14:30"
    print("Text:", text)
    
    # Extract date components using groups
    date_pattern = r'(\d{4})-(\d{2})-(\d{2})'
    date_match = re.search(date_pattern, text)
    
    if date_match:
        year, month, day = date_match.groups()
        print("Year:", year)
        print("Month:", month)
        print("Day:", day)
    
    # Extract time components using named groups
    time_pattern = r'(?P<hour>\d{2}):(?P<minute>\d{2})'
    time_match = re.search(time_pattern, text)
    
    if time_match:
        hour = time_match.group('hour')
        minute = time_match.group('minute')
        print("Hour:", hour)
        print("Minute:", minute)
    
    # Use groups for replacement with backreferences
    swapped_date = re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3/\2/\1', text)
    print("Swapped date:", swapped_date)


if __name__ == "__main__":
    main()
