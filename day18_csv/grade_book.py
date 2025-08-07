"""
Day 18, Module: Grade Book

Purpose: Provide grade book functions using CSV for storage.
This module contains functions for managing student grades with CSV files.
"""

import csv
from typing import List, Dict

def save_grades(grades: List[Dict[str, str]], filename: str) -> None:
    """Save student grades to a CSV file.
    
    Args:
        grades: List of grade dictionaries
        filename: Name of the file to save to
    """
    with open(filename, "w", newline="") as file:
        fieldnames = ["Name", "Subject", "Grade"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(grades)


def load_grades(filename: str) -> List[Dict[str, str]]:
    """Load student grades from a CSV file.
    
    Args:
        filename: Name of the file to load from
    
    Returns:
        List of grade dictionaries
    """
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except FileNotFoundError:
        return []


def add_grade(grades: List[Dict[str, str]], name: str, subject: str, grade: str) -> None:
    """Add a new grade to the list.
    
    Args:
        grades: List of grade dictionaries
        name: Student's name
        subject: Subject name
        grade: Grade value
    """
    grades.append({"Name": name, "Subject": subject, "Grade": grade})


def find_grades(grades: List[Dict[str, str]], name: str) -> List[Dict[str, str]]:
    """Find all grades for a specific student.
    
    Args:
        grades: List of grade dictionaries
        name: Student's name to search for
    
    Returns:
        List of grade dictionaries for the student
    """
    return [grade for grade in grades if grade["Name"].lower() == name.lower()]
