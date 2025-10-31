# Arithmetic Operators in Python

a = 15
b = 4

# Addition (+) - adds two numbers
result_add = a + b
print("Addition:", a, "+", b, "=", result_add)  

# Subtraction (-) - subtracts second number from first
result_sub = a - b
print("Subtraction:", a, "-", b, "=", result_sub)  

# Multiplication (*) - multiplies two numbers
result_mul = a * b
print("Multiplication:", a, "*", b, "=", result_mul) 

# Division (/) - divides and returns float result
result_div = a / b
print("Division:", a, "/", b, "=", result_div)  

# Floor Division (//) - divides and rounds down to nearest integer
result_floor = a // b
print("Floor Division:", a, "//", b, "=", result_floor)  

# Modulus (%) - returns remainder after division
result_mod = a % b
print("Modulus:", a, "%", b, "=", result_mod)  

# Exponentiation (**) - raises first number to power of second
result_exp = a ** b
print("Exponentiation:", a, "**", b, "=", result_exp)  

# Demonstrating operator precedence
result_precedence = a + b * 2 
print("Operator Precedence:", a, "+", b, "* 2 =", result_precedence)  

# Using parentheses to change precedence
result_parentheses = (a + b) * 2
print("With Parentheses:", "(", a, "+", b, ") * 2 =", result_parentheses)  


