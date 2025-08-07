"""
Day 13, Module: Temperature Converter

Purpose: Provide temperature conversion functions.
This module contains functions for converting between temperature units.
"""

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit.
    
    Args:
        celsius: Temperature in Celsius
    
    Returns:
        Temperature in Fahrenheit
    """
    return (celsius * 9/5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius.
    
    Args:
        fahrenheit: Temperature in Fahrenheit
    
    Returns:
        Temperature in Celsius
    """
    return (fahrenheit - 32) * 5/9


def celsius_to_kelvin(celsius):
    """Convert Celsius to Kelvin.
    
    Args:
        celsius: Temperature in Celsius
    
    Returns:
        Temperature in Kelvin
    """
    return celsius + 273.15
