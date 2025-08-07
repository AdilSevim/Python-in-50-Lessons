"""
Day 14, Example 1: Person Class

Purpose: Create and use a Person class with attributes and methods.
We define a class to represent a person with name and age attributes.

Expected output when run:
Person: Alice, Age: 30
Happy Birthday, Alice!
Person: Alice, Age: 31
Introduction: Hi, I'm Alice and I'm 31 years old.
"""

class Person:
    """A class to represent a person."""
    
    def __init__(self, name, age):
        """Initialize a Person object with name and age.
        
        Args:
            name: The person's name
            age: The person's age
        """
        self.name = name
        self.age = age
    
    def birthday(self):
        """Increase the person's age by 1."""
        self.age = self.age + 1
    
    def introduce(self):
        """Return a string introducing the person."""
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    def __str__(self):
        """Return a string representation of the person."""
        return f"Person: {self.name}, Age: {self.age}"


def main():
    """Demonstrate using the Person class."""
    # Create a Person object
    person = Person("Alice", 30)
    
    # Display the person
    print(person)
    
    # Have a birthday
    print(f"Happy Birthday, {person.name}!")
    person.birthday()
    
    # Display the updated person
    print(person)
    
    # Get introduction
    print("Introduction:", person.introduce())


if __name__ == "__main__":
    main()
