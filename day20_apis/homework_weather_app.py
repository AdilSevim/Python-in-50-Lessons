"""
Day 20, Homework: Weather App

Purpose: Create a simple weather app that fetches data from a weather API.
We use HTTP requests to get weather information for a given location.

Expected output when run:
Weather App
Enter a city name: [user input]
[Weather information for the city or error message]
"""

import weather_api


def display_weather(city: str, weather_data: dict) -> None:
    """Display weather information.
    
    Args:
        city: The city name
        weather_data: The weather data dictionary
    """
    print(f"\nWeather in {city}:")
    print(f"Temperature: {weather_data['temperature']}°C")
    print(f"Description: {weather_data['description']}")
    print(f"Humidity: {weather_data['humidity']}%")
    print(f"Wind Speed: {weather_data['wind_speed']} km/h")

def main():
    """Run the weather app program."""
    print("Weather App")
    
    while True:
        city = input("Enter a city name (or 'quit' to exit): ")
        
        if city.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Get weather data
        weather_data = weather_api.get_weather(city)
        
        if weather_data:
            display_weather(city, weather_data)
        else:
            print(f"Could not find weather data for {city}")


if __name__ == "__main__":
    main()
