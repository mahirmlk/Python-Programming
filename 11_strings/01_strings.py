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

# --- Common String Methods ---
sentence = "   Python programming is AWESOME!   "

print("--- Common String Methods ---")
# len(): Get the length of the string
print(f"Length of the sentence: {len(sentence)}")

# strip(): Remove leading/trailing whitespace
stripped_sentence = sentence.strip()
print(f"Stripped: '{stripped_sentence}'")

# lower() / upper(): Convert to lowercase or uppercase
print(f"Lowercase: {stripped_sentence.lower()}")
print(f"Uppercase: {stripped_sentence.upper()}")

# capitalize() / title(): Capitalize the first letter or each word
print(f"Capitalized: {stripped_sentence.capitalize()}")
print(f"Title Case: {stripped_sentence.title()}")

# replace(): Replace a substring with another
replaced_sentence = stripped_sentence.replace("AWESOME", "great")
print(f"Replaced: '{replaced_sentence}'")

# split(): Split the string into a list of substrings
words = stripped_sentence.split()
print(f"Split into words: {words}")


# --- Checking for Substrings ---

# Use the 'in' keyword to check if a substring exists.
print("--- Checking for Substrings ---")
contains_python = "python" in stripped_sentence.lower()
print(f"Does the sentence contain 'python'? {contains_python}")

contains_ruby = "ruby" in stripped_sentence.lower()
print(f"Does the sentence contain 'ruby'? {contains_ruby}")
