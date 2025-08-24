# Membership Operators Demo
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

# in operator - returns True if value exists in sequence
print("'apple' in fruits:", 'apple' in fruits)  # Output: True
print("'grape' in fruits:", 'grape' in fruits)  # Output: False
print("3 in numbers:", 3 in numbers)  # Output: True

# not in operator - returns True if value does not exist in sequence
print("'grape' not in fruits:", 'grape' not in fruits)  # Output: True
print("'apple' not in fruits:", 'apple' not in fruits)  # Output: False

# Works with strings too
text = "Hello World"
print("'Hello' in text:", 'Hello' in text)  # Output: True
print("'Python' not in text:", 'Python' not in text)  # Output: True
# Commonly used in membership tests, conditionals, and loops.