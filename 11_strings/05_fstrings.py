# F-strings (formatted string literals) 
# F-strings start with f" and can include expressions inside { }

# Basic f-string with variables
name = "Mahir"
age = 25
print(f"Name: {name}, Age: {age}")  # Name: Mahir, Age: 25

# Expressions in f-strings
x = 10
y = 20
print(f"Sum of {x} and {y} is {x + y}")  # Sum of 10 and 20 is 30

# Formatting numbers
price = 49.95
quantity = 3
print(f"Price: ${price:.2f}")  # Price: $49.95
print(f"Total: ${price * quantity:.2f}")  # Total: $149.85

# Date formatting
from datetime import datetime
today = datetime.now()
print(f"Date: {today:%Y-%m-%d}")  # Date: 2025-08-30
print(f"Time: {today:%H:%M}")  # Time: 14:30

# Boolean expressions
is_valid = True
print(f"Status: {'Yes' if is_valid else 'No'}")  # Status: Yes

# Padding and alignment
name = "Kai"
score = 90
print(f"Name: {name:<10} Score: {score:>3}")  # Name: Bob        Score:  95

# Dictionary values in f-strings
person = {"name": "Charlie", "age": 30}
print(f"Person: {person['name']} is {person['age']} years old")