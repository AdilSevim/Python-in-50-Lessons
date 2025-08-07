"""
Day 15, Example 1: Basic Type Hints

Purpose: Demonstrate basic type hints for variables and simple functions.
We add type hints to improve code readability and catch potential errors.

Expected output when run:
Name: Alice
Age: 30
Height: 5.5
Is student: True
Greeting: Hello, Alice!
"""

# Type hints for variables
def main():
    """Demonstrate basic type hints."""
    # Variable type hints
    name: str = "Alice"
    age: int = 30
    height: float = 5.5
    is_student: bool = True
    
    # Display variables
    print("Name:", name)
    print("Age:", age)
    print("Height:", height)
    print("Is student:", is_student)
    
    # Function with type hints
    def greet(person_name: str) -> str:
        """Create a greeting message.
        
        Args:
            person_name: The name of the person to greet
        
        Returns:
            A greeting message
        """
        return f"Hello, {person_name}!"
    
    # Use the function
    greeting: str = greet(name)
    print("Greeting:", greeting)


if __name__ == "__main__":
    main()
