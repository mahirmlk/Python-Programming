# --- String Creation ---

# Strings can be created using single quotes, double quotes, or triple quotes.
simple_string = 'Hello, World!'
another_string = "Python is fun."
multi_line_string = """This is a multi-line string.
It can span across several lines."""

print("--- String Creation ---")
print(simple_string)
print(another_string)
print(multi_line_string)
print("-" * 20)


# --- String Concatenation ---

# You can combine strings using the + operator.
first_name = "KL"
last_name = "Rahul"
full_name = first_name + " " + last_name

print("--- String Concatenation ---")
print(full_name)


# --- String Formatting ---

# f-strings (formatted string literals) are a modern and easy way to format strings.
age = 30
formatted_string = f"{full_name} is {age} years old."

print("--- String Formatting ---")
print(formatted_string)
print("-" * 20)


