"""
Day 14, Example 2: Rectangle Class

Purpose: Create and use a Rectangle class with area and perimeter methods.
We define a class to represent a rectangle with width and height attributes.

Expected output when run:
Rectangle: 5.0 x 3.0
Area: 15.0
Perimeter: 16.0
Square? False
Scaling by 2...
Rectangle: 10.0 x 6.0
Area: 60.0
"""

class Rectangle:
    """A class to represent a rectangle."""
    
    def __init__(self, width, height):
        """Initialize a Rectangle object with width and height.
        
        Args:
            width: The rectangle's width
            height: The rectangle's height
        """
        self.width = width
        self.height = height
    
    def area(self):
        """Calculate and return the rectangle's area."""
        return self.width * self.height
    
    def perimeter(self):
        """Calculate and return the rectangle's perimeter."""
        return 2 * (self.width + self.height)
    
    def is_square(self):
        """Check if the rectangle is a square."""
        return self.width == self.height
    
    def scale(self, factor):
        """Scale the rectangle's dimensions by a factor.
        
        Args:
            factor: The scaling factor
        """
        self.width = self.width * factor
        self.height = self.height * factor
    
    def __str__(self):
        """Return a string representation of the rectangle."""
        return f"Rectangle: {self.width} x {self.height}"


def main():
    """Demonstrate using the Rectangle class."""
    # Create a Rectangle object
    rectangle = Rectangle(5.0, 3.0)
    
    # Display the rectangle
    print(rectangle)
    
    # Calculate and display area and perimeter
    print("Area:", rectangle.area())
    print("Perimeter:", rectangle.perimeter())
    
    # Check if it's a square
    print("Square?", rectangle.is_square())
    
    # Scale the rectangle
    print("Scaling by 2...")
    rectangle.scale(2)
    
    # Display the updated rectangle
    print(rectangle)
    
    # Calculate and display new area
    print("Area:", rectangle.area())


if __name__ == "__main__":
    main()
