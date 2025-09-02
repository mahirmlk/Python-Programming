
# PYTHON MODULES 


print("PYTHON MODULES \n")
print("=" * 20)


# WHAT IS A MODULE?


"""
A MODULE is simply a Python file (.py) that contains:
- Functions
- Variables  
- Classes
- Code that can be reused

Think of it as a toolbox with useful tools inside!

"""

# CREATING YOUR FIRST MODULE

import my_tools

print("Let's use our custom module:")
print(f"   Greet: {my_tools.greet('Mahir')}")
print(f"   Add: 5 + 3 = {my_tools.add_numbers(5, 3)}")



# HOW TO IMPORT MODULES (4 WAYS)


# WAY 1: Import the whole module
print(" WAY 1: Import the whole module")
import math
print(f"Using math.sqrt(16): {math.sqrt(16)}")
print(f"Using math.pi: {math.pi}")

# WAY 2: Import specific things
print("\n🔧 WAY 2: Import specific things")
from math import sqrt, pi
print(f"Using sqrt(25): {sqrt(25)}")
print(f"Using pi: {pi}")

# WAY 3: Import with a nickname (alias)
print(" WAY 3: Import with a nickname")
import datetime as dt
now = dt.datetime.now()
print(f"Current time: {now.strftime('%H:%M:%S')}")

# WAY 4: Import everything (be careful!)
print(" WAY 4: Import everything (use sparingly)")
from random import *
print(f"Random number 1-10: {randint(1, 10)}")


#  USING BUILT-IN MODULES (PYTHON'S TOOLBOX)

# Math module - Mathematical functions
print(" MATH MODULE:")
import math
print(f"   Square root of 100: {math.sqrt(100)}")
print(f"   2 to the power of 3: {math.pow(2, 3)}")
print(f"   Round down 4.7: {math.floor(4.7)}")

# Random module - Generate random things
print(" RANDOM MODULE:")
import random
print(f"   Random number 1-100: {random.randint(1, 100)}")
print(f"   Random choice: {random.choice(['apple', 'banana', 'cherry'])}")
print(f"   Coin flip: {random.choice(['Heads', 'Tails'])}")

# DateTime module - Work with dates and time
print("\n📅 DATETIME MODULE:")
import datetime
today = datetime.date.today()
print(f"   Today's date: {today}")
print(f"   Current year: {today.year}")
print(f"   Day of week: {today.strftime('%A')}")

# OS module - Interact with your computer
print(" OS MODULE:")
import os
print(f"   Current folder: {os.path.basename(os.getcwd())}")
print(f"   Your username: {os.getenv('USER', os.getenv('USERNAME', 'Unknown'))}")


# CREATING A SIMPLE MODULE (SIMULATION)

print("Let's simulate our own module:")

# This simulates what would be in a separate file
class MyCalculator:
    """A simple calculator"""
    
    def add(self, a, b):
        return a + b
    
    def multiply(self, a, b):
        return a * b
    
    def greet_user(self, name):
        return f"Welcome to calculator, {name}!"

# Simulate importing our module
calc = MyCalculator()
print(f"   Using our calculator: 5 + 3 = {calc.add(5, 3)}")
print(f"   Using our calculator: 4 × 7 = {calc.multiply(4, 7)}")
print(f"   {calc.greet_user('Alice')}")


# PACKAGE STRUCTURE (ORGANIZING MODULES)


"""
A PACKAGE is a folder containing multiple modules:

my_game/                    ← This is a package
    __init__.py            ← Makes it a package (can be empty)
    player.py              ← Module for player functions
    weapons.py             ← Module for weapon functions  
    levels.py              ← Module for level functions

How to use:
    import my_game.player
    from my_game import weapons
    from my_game.levels import create_level
"""


# EXPLORING MODULES 

print("Let's explore what's inside the math module:")

# See what's inside a module
math_stuff = [item for item in dir(math) if not item.startswith('_')]
print(f"   Math module has {len(math_stuff)} things!")
print(f"   First 8 things: {math_stuff[:8]}")

# Get help about a function
print(f"\n   What does sqrt do? {math.sqrt.__doc__}")

# Check module info
print(f"   Module name: {math.__name__}")

# PRACTICAL EXAMPLES

# Example 1: Working with files
print(" Example 1: File operations")
import os
file_count = len([f for f in os.listdir('.') if f.endswith('.py')])
print(f"   Python files in current folder: {file_count}")

# Example 2: Working with JSON data
print(" Example 2: JSON data")
import json
student = {"name": "Emma", "age": 20, "grade": "A"}
json_text = json.dumps(student)
print(f"   Student data as JSON: {json_text}")

# Example 3: Working with time
print(" Example 3: Time calculations")
import time
print("   Waiting 1 second...")
start_time = time.time()
time.sleep(1)  # Wait 1 second
end_time = time.time()
print(f"   Actually waited: {end_time - start_time:.2f} seconds")


# COMMON MISTAKES AND HOW TO AVOID THEM


"""
   DON'T DO THIS:
   from math import *        # Imports everything (confusing)
   
   DO THIS INSTEAD:
   from math import sqrt, pi # Import only what you need
   import math               # Or import the whole module

   DON'T DO THIS:
   import MyModule.py        # Don't include .py
   
   DO THIS INSTEAD:
   import MyModule           # Just the name

   DON'T DO THIS:
   import sys
   import os  
   import math              # Scattered imports
   
   DO THIS INSTEAD:
   import math              # Group imports at the top
   import os
   import sys

"""



# SUMMARY OF KEY POINTS

"""
   IMPORT METHODS:
   import module_name
   from module_name import function_name
   import module_name as nickname
   from module_name import *

   USEFUL BUILT-IN MODULES:
   math      → Mathematical functions
   random    → Random numbers and choices  
   datetime  → Working with dates and time
   os        → Operating system functions
   json      → Working with JSON data
   time      → Time-related functions

   EXPLORING MODULES:
   dir(module)        → See what's inside
   help(function)     → Get help
   module.__name__    → Module name
   function.__doc__   → Function description

   MODULE STRUCTURE:
   Create: Save code in .py file
   Import: Use import statement
   Use: Call functions with module.function()

"""

