"""
Day 20, Example 2: API Error Handling

Purpose: Show how to handle API errors and exceptions.
We implement proper error handling for API requests.

Expected output when run:
Note: This example uses a mock API for demonstration.
Success case:
User found: john_doe
Error case:
User not found (404)
Network error case:
Network error occurred
"""

# Mock API response data
MOCK_API_DATA = {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com"
}

class MockResponse:
    """Mock response class to simulate API responses."""
    def __init__(self, status_code, json_data=None):
        self.status_code = status_code
        self._json_data = json_data or {}
    
    def json(self):
        """Return JSON data."""
        return self._json_data

def mock_api_request(endpoint, status_code=200, error_type=None):
    """Mock function to simulate API requests with different responses.
    
    Args:
        endpoint: The API endpoint
        status_code: HTTP status code to return
        error_type: Type of error to simulate
    
    Returns:
        Mock response object
    """
    # Simulate network error
    if error_type == "network":
        raise ConnectionError("Network error")
    
    # Simulate successful response
    if status_code == 200:
        return MockResponse(200, MOCK_API_DATA)
    
    # Simulate not found error
    if status_code == 404:
        return MockResponse(404, {"error": "User not found"})
    
    # Simulate server error
    return MockResponse(500, {"error": "Server error"})

def get_user_safe(user_id):
    """Safely get user data with error handling.
    
    Args:
        user_id: The ID of the user to retrieve
    
    Returns:
        User data if successful, None otherwise
    """
    try:
        # In a real application, this would be:
        # response = requests.get(f"https://api.example.com/users/{user_id}")
        response = mock_api_request(f"/users/{user_id}")
        
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("User not found (404)")
            return None
        else:
            print(f"API error: {response.status_code}")
            return None
    except ConnectionError:
        print("Network error occurred")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    """Demonstrate API error handling with mock data."""
    print("Note: This example uses a mock API for demonstration.")
    
    # Success case
    print("Success case:")
    user_data = get_user_safe(1)
    if user_data:
        print("User found:", user_data["username"])
    
    # Error case (user not found)
    print("Error case:")
    user_data = get_user_safe(999)  # Non-existent user
    
    # Network error case
    print("Network error case:")
    # For this example, we'll simulate a network error directly
    try:
        mock_api_request("/users/1", error_type="network")
    except ConnectionError:
        print("Network error occurred")


if __name__ == "__main__":
    main()
