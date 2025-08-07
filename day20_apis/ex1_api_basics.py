"""
Day 20, Example 1: API Basics

Purpose: Demonstrate basic API requests and JSON parsing.
We use the requests module to make HTTP requests to web APIs.

Expected output when run:
Note: This example uses a mock API for demonstration.
User ID: 1
Username: john_doe
Email: john@example.com
Phone: 123-456-7890
"""

# Mock API response data (simulating what we'd get from a real API)
MOCK_API_DATA = {
    "id": 1,
    "username": "john_doe",
    "email": "john@example.com",
    "phone": "123-456-7890"
}

def mock_get_user(user_id):
    """Mock function to simulate an API request.
    
    Args:
        user_id: The ID of the user to retrieve
    
    Returns:
        Mock user data
    """
    # In a real application, this would be:
    # response = requests.get(f"https://api.example.com/users/{user_id}")
    # return response.json()
    
    # For this example, we return mock data
    if user_id == 1:
        return MOCK_API_DATA
    else:
        return None

def main():
    """Demonstrate basic API usage with mock data."""
    print("Note: This example uses a mock API for demonstration.")
    
    # Get user data from "API"
    user_data = mock_get_user(1)
    
    if user_data:
        # Display user information
        print("User ID:", user_data["id"])
        print("Username:", user_data["username"])
        print("Email:", user_data["email"])
        print("Phone:", user_data["phone"])
    else:
        print("User not found!")


if __name__ == "__main__":
    main()
