# Simple one-line docstrings
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

def say_hello(name):
    """Say hello to a person."""
    return f"Hello, {name}!"

def is_even(number):
    """Check if a number is even."""
    return number % 2 == 0

# Multi-line docstrings with basic info
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Takes length and width, returns the area.
    """
    return length * width

def find_max(numbers):
    """
    Find the largest number in a list.
    
    Takes a list of numbers.
    Returns the biggest number.
    """
    return max(numbers)

# Slightly more detailed docstrings

def divide_numbers(a, b):
    """
    Divide two numbers.
    
    a: first number
    b: second number (cannot be zero)
    
    Returns: result of a divided by b
    """
    if b == 0:
        return "Cannot divide by zero!"
    return a / b

# Simple class docstring
class Dog:
    """A simple dog class."""
    
    def __init__(self, name):
        """Create a new dog with a name."""
        self.name = name
    
    def bark(self):
        """Make the dog bark."""
        return f"{self.name} says Woof!"
    
    def sit(self):
        """Make the dog sit."""
        return f"{self.name} is sitting."

