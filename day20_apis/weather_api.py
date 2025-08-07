"""
Day 20, Module: Weather API

Purpose: Provide weather data functions using a mock API.
This module contains functions for getting weather information.
"""

from typing import Dict, Optional

# Mock weather data
MOCK_WEATHER_DATA = {
    "New York": {
        "temperature": 22,
        "description": "Partly cloudy",
        "humidity": 65,
        "wind_speed": 10
    },
    "London": {
        "temperature": 18,
        "description": "Rainy",
        "humidity": 80,
        "wind_speed": 15
    },
    "Tokyo": {
        "temperature": 28,
        "description": "Sunny",
        "humidity": 50,
        "wind_speed": 5
    }
}

class MockWeatherResponse:
    """Mock response class to simulate weather API responses."""
    def __init__(self, status_code: int, json_data: Optional[Dict] = None):
        self.status_code = status_code
        self._json_data = json_data or {}
    
    def json(self):
        """Return JSON data."""
        return self._json_data

def mock_get_weather(city: str) -> MockWeatherResponse:
    """Mock function to simulate getting weather data.
    
    Args:
        city: The city to get weather for
    
    Returns:
        Mock weather response
    """
    # In a real application, this would be:
    # response = requests.get(f"https://api.weather.com/data/{city}")
    # return response
    
    if city in MOCK_WEATHER_DATA:
        return MockWeatherResponse(200, MOCK_WEATHER_DATA[city])
    else:
        return MockWeatherResponse(404, {"error": "City not found"})

def get_weather(city: str) -> Optional[Dict]:
    """Get weather information for a city.
    
    Args:
        city: The city to get weather for
    
    Returns:
        Weather data dictionary if successful, None otherwise
    """
    try:
        response = mock_get_weather(city)
        
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except Exception:
        return None
