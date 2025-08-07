# Day 20: Working with APIs

## Today's Focus
- Understanding Application Programming Interfaces (APIs)
- Using the requests module to make HTTP requests

**Today we learn to work with APIs!** APIs allow our programs to communicate with web services.

## Warm-up
Try this in your Python interpreter (requires internet connection):
```python
# Note: This is for demonstration only - we'll use a mock example in our scripts
# import requests
# response = requests.get('https://api.github.com/users/octocat')
# data = response.json()
# print("Username:", data['login'])
# print("Name:", data['name'])
```

## Step-by-step Guide

1. **What are APIs?**
   - Application Programming Interfaces
   - Allow different software systems to communicate
   - Provide access to web services and data
   - Return data in formats like JSON

2. **HTTP methods**
   - `GET`: Retrieve data
   - `POST`: Send data to create something
   - `PUT`: Update existing data
   - `DELETE`: Remove data

3. **Using the requests module**
   - `requests.get(url)`: Make a GET request
   - `response.json()`: Parse JSON response
   - `response.status_code`: Check request success
   - `response.text`: Get raw response text

## Common Mistakes & Fixes

❌ Forgetting to install the requests module
✅ Fix: Run `pip install requests` or add to requirements.txt

❌ Not checking response status codes
✅ Fix: Always check `response.status_code == 200` for success

❌ Not handling network errors
✅ Fix: Use try/except blocks to catch `requests.RequestException`

## Mini Quiz

1. What does HTTP stand for?
2. Which HTTP method is used to retrieve data?
3. How do you parse JSON data from an API response?

<details>
<summary>Answers</summary>

1. HyperText Transfer Protocol
2. GET
3. `response.json()`
</details>

## Homework Brief

Create a simple weather app that fetches data from a weather API.
Use HTTP requests to get weather information for a given location.

## Stretch Goal (Optional)

Add error handling for network issues and invalid locations.

---

Run the examples:
```bash
python ex1_api_basics.py
python ex2_api_error_handling.py
python homework_weather_app.py
```

Expected outputs:
- ex1_api_basics.py: Demonstrates basic API requests and JSON parsing
- ex2_api_error_handling.py: Shows how to handle API errors and exceptions
- homework_weather_app.py: Implements a simple weather app using a mock API
