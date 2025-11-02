# F-strings (formatted string literals) 

# Basic f-string with variables
name = "Mahir"
age = 25
print(f"Name: {name}, Age: {age}") 

# Expressions in f-strings
x = 10
y = 20
print(f"Sum of {x} and {y} is {x + y}")  

# Formatting numbers
price = 49.95
quantity = 3
print(f"Price: ${price:.2f}") 
print(f"Total: ${price * quantity:.2f}")  

# Date formatting
from datetime import datetime
today = datetime.now()
print(f"Date: {today:%Y-%m-%d}")  
print(f"Time: {today:%H:%M}")  

# Boolean expressions
is_valid = True
print(f"Status: {'Yes' if is_valid else 'No'}")  

# Padding and alignment
name = "Kai"
score = 90
print(f"Name: {name:<10} Score: {score:>3}")  

# Dictionary values in f-strings
person = {"name": "Charlie", "age": 30}
print(f"Person: {person['name']} is {person['age']} years old")