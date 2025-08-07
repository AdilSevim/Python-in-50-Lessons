# Day 14: Classes and Objects

## Today's Focus
- Understanding object-oriented programming concepts
- Creating classes and instantiating objects

**Today we learn about classes and objects!** Classes are blueprints for creating objects with attributes and methods.

## Warm-up
Try this in your Python interpreter:
```python
class Dog:
    def __init__(self, name):
        self.name = name
    
    def bark(self):
        return f"{self.name} says woof!"

def main():
    my_dog = Dog("Buddy")
    print(my_dog.bark())

main()
```

## Step-by-step Guide

1. **What are classes and objects?**
   - Class: A blueprint or template for creating objects
   - Object: An instance of a class with actual data
   - Classes define attributes (data) and methods (functions)

2. **Creating classes**
   - Use `class ClassName:` to define a class
   - `__init__` method initializes object attributes
   - `self` refers to the specific instance of the class
   - Define methods to give objects behaviors

3. **Using classes**
   - Create objects: `object_name = ClassName(arguments)`
   - Access attributes: `object_name.attribute`
   - Call methods: `object_name.method()`

## Common Mistakes & Fixes

❌ Forgetting `self` as the first parameter in methods
✅ Fix: Always include `self` as the first parameter in class methods

❌ Confusing classes with objects
✅ Fix: Remember classes are templates; objects are instances of those templates

❌ Not using `__init__` for initialization
✅ Fix: Use `__init__` to set up initial state when creating objects

## Mini Quiz

1. What is the difference between a class and an object?
2. What is the purpose of the `__init__` method?
3. What does `self` refer to in a class method?

<details>
<summary>Answers</summary>

1. A class is a blueprint; an object is an instance of that blueprint
2. It initializes the object's attributes when it's created
3. It refers to the specific instance of the class
</details>

## Homework Brief

Create a simple bank account class with deposit, withdrawal, and balance checking methods.
Use classes to model a bank account with appropriate attributes and behaviors.

## Stretch Goal (Optional)

Add transaction history tracking to the bank account class.

---

Run the examples:
```bash
python ex1_person_class.py
python ex2_rectangle_class.py
python homework_bank_account.py
```

Expected outputs:
- ex1_person_class.py: Creates and uses a Person class with attributes and methods
- ex2_rectangle_class.py: Creates and uses a Rectangle class with area and perimeter methods
- homework_bank_account.py: Implements a BankAccount class with deposit and withdrawal methods
