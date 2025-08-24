# Taking string input from the user

name = input("Enter your name: ")
print(f"Hello, {name}!")

# Taking numeric input
# Note: input() always returns string, so we need to convert it
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print(f"Age: {age} years")
print(f"Height: {height} meters")

# Multiple inputs on one line (split by space)
x, y = input("Enter two numbers separated by space: ").split()
print(f"First number: {x}, Second number: {y}")

# Basic of Input
# input() always returns a string
# Use type conversion functions (int(), float()) for numbers
# Use strip() to remove leading/trailing whitespace

# Input Validation 

# Always validate user input before processing
# Use try-except for type conversion
# Use conditional statements for range checking

# Use map() for applying functions to multiple inputs
a, b = map(int, input("Enter two integers separated by space: ").split())
print(f"Sum: {a + b}")



