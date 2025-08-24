# Basic print examples
print("Hello World")  # Simple string
print(18)  # Number
print(True)  # Boolean
print(3.14)  # Float

# Print multiple items
print("Name:", "Mahir", "Age:", 25)

# Using sep parameter (separator between items)
print("Python", "is", "awesome", sep="-")  # Output: Python-is-awesome
print("Date", "24", "08", "2025", sep="/")  # Output: Date/24/08/2025
print("Hello", "World", sep="***")  # Output: Hello***World
print( "Hello", "World", sep=" ")  # Output: Hello World

# Using end parameter (what to print at the end)
print("Hello", end="!")  # Output: Hello!
print("World")  # Output: World (on new line)

print("One", end=" ")
print("Two", end=" ")
print("Three")  # Output: One Two Three

# Combining sep and end
print("Python", "Java", "C++", sep=" | ", end="\n")
print("programming languages ")  # Output: Python | Java | C++

# Print with formatting
name = "Mahir"
age = 25
print(f"Name: {name}, Age: {age}")  # f-string
print("Name: {}, Age: {}".format(name, age))  # format method

# Print empty lines
print()  # Prints a blank line
print("\n")  # Prints two blank lines

# Print special characters
print("This\tis\ttabbed")  # Using tab
print("Line 1\nLine 2")  # Using newline
print("He said, \"Hello!\"")  # Using double quotes inside string
print('It\'s a beautiful day!')  # Using single quote inside string

# Print with different number systems
number = 42
print(f"Decimal: {number}")
print(f"Binary: {bin(number)}")
print(f"Octal: {oct(number)}")
print(f"Hexadecimal: {hex(number)}")



