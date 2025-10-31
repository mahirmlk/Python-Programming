# Membership Operators Demo
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]

# in operator - returns True if value exists in sequence
print("'apple' in fruits:", 'apple' in fruits)  
print("'grape' in fruits:", 'grape' in fruits) 
print("3 in numbers:", 3 in numbers)  

# not in operator - returns True if value does not exist in sequence
print("'grape' not in fruits:", 'grape' not in fruits)  
print("'apple' not in fruits:", 'apple' not in fruits) 

# Works with strings too
text = "Hello World"
print("'Hello' in text:", 'Hello' in text)  
print("'Python' not in text:", 'Python' not in text)  

# Practical example with membership operators
user_input = "banana"
if user_input in fruits:
    print(f"{user_input} is available in the fruit list.")
else:
    print(f"{user_input} is not available in the fruit list.")

    