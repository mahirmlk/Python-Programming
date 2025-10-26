# Basic print examples
print("Hello World")  
print(18) 
print(True) 
print(3.14)

# Print multiple items
print("Name:", "Mahir", "Age:", 25)

# Using sep parameter
print("Python", "is", "awesome", sep="-")  
print("Date", "24", "08", "2025", sep="/")  
print("Hello", "World", sep="***")  
print( "Hello", "World", sep=" ") 

# Using end parameter 
print("Hello", end="!") 
print("World") 

print("One", end=" ")
print("Two", end=" ")
print("Three") 

# Combining sep and end
print("Python", "Java", "C++", sep=" | ", end="\n")
print("programming languages ")

# Print with formatting
name = "Mahir"
age = 25
print(f"Name: {name}, Age: {age}")  # f-string
print("Name: {}, Age: {}".format(name, age)) 

# Print empty lines
print()  # Prints a blank line
print("\n")  # Prints two blank lines

# Print special characters
print("This\tis\ttabbed")  
print("Line 1\nLine 2") 
print("He said, \"Hello!\"") 
print('It\'s a beautiful day!') 

# Print with different number systems
number = 42
print(f"Decimal: {number}")
print(f"Binary: {bin(number)}")
print(f"Octal: {oct(number)}")
print(f"Hexadecimal: {hex(number)}")



