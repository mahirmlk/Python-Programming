# Arithmetic Operators in Python

# Variables for demonstration
a = 15
b = 4

# Addition (+) - adds two numbers
result_add = a + b
print("Addition:", a, "+", b, "=", result_add)  # Output: 19

# Subtraction (-) - subtracts second number from first
result_sub = a - b
print("Subtraction:", a, "-", b, "=", result_sub)  # Output: 11

# Multiplication (*) - multiplies two numbers
result_mul = a * b
print("Multiplication:", a, "*", b, "=", result_mul)  # Output: 60

# Division (/) - divides and returns float result
result_div = a / b
print("Division:", a, "/", b, "=", result_div)  # Output: 3.75

# Floor Division (//) - divides and rounds down to nearest integer
result_floor = a // b
print("Floor Division:", a, "//", b, "=", result_floor)  # Output: 3

# Modulus (%) - returns remainder after division
result_mod = a % b
print("Modulus:", a, "%", b, "=", result_mod)  # Output: 3

# Exponentiation (**) - raises first number to power of second
result_exp = a ** b
print("Exponentiation:", a, "**", b, "=", result_exp)  # Output: 50625

# Demonstrating operator precedence
result_precedence = a + b * 2  # Multiplication has higher precedence than addition
print("Operator Precedence:", a, "+", b, "* 2 =", result_precedence)  # Output: 23

# Using parentheses to change precedence
result_parentheses = (a + b) * 2
print("With Parentheses:", "(", a, "+", b, ") * 2 =", result_parentheses)  # Output: 38

# Note: Python follows standard mathematical precedence rules.

