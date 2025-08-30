
# Python String Methods with Examples


# ==========================================
# 1. CASE CONVERSION METHODS
# ==========================================

text = "Hello World Python"

# Convert to uppercase
print("UPPERCASE METHODS:")
print(text.upper())  # HELLO WORLD PYTHON

# Convert to lowercase
print(text.lower())  # hello world python

# Capitalize first letter only
print(text.capitalize())  # Hello world python

# Title case (capitalize each word)
print(text.title())  # Hello World Python

# Swap case
print(text.swapcase())  # hELLO wORLD pYTHON

# Case folding (aggressive lowercase, good for case-insensitive comparison)
text2 = "ß"  # German sharp s
print(text2.casefold())  # ss
print()

# ==========================================
# 2. SEARCHING AND CHECKING METHODS
# ==========================================

sample = "Python Programming is Fun"

print("SEARCHING METHODS:")
# Find substring (returns index or -1 if not found)
print(sample.find("Programming"))  # 7
print(sample.find("Java"))  # -1

# Index (like find but raises ValueError if not found)
print(sample.index("is"))  # 19
# print(sample.index("Java"))  # Would raise ValueError

# rfind and rindex (search from right)
text3 = "apple apple apple"
print(text3.rfind("apple"))  # 12 (last occurrence)
print(text3.rindex("apple"))  # 12

# Count occurrences
print(text3.count("apple"))  # 3
print()

# ==========================================
# 3. BOOLEAN CHECK METHODS
# ==========================================

print("BOOLEAN CHECK METHODS:")

# Check if string starts/ends with substring
filename = "document.pdf"
print(filename.startswith("doc"))  # True
print(filename.endswith(".pdf"))  # True

# Check string composition
print("12345".isdigit())  # True - all digits
print("abc123".isalnum())  # True - alphanumeric
print("abcdef".isalpha())  # True - all alphabetic
print("   ".isspace())  # True - all whitespace
print("Hello".isupper())  # False - not all uppercase
print("hello".islower())  # True - all lowercase
print("Title Case".istitle())  # True - title cased

# Additional checks
print("123.45".isdecimal())  # False (has decimal point)
print("123".isnumeric())  # True
print("hello_world".isidentifier())  # True - valid Python identifier
print("Hello\nWorld".isprintable())  # False (has newline)
print()

# ==========================================
# 4. STRING MODIFICATION METHODS
# ==========================================

print("STRING MODIFICATION:")

# Replace substring
text4 = "I love Java. Java is great!"
print(text4.replace("Java", "Python"))  # I love Python. Python is great!
print(text4.replace("Java", "Python", 1))  # Replace only first occurrence

# Strip whitespace or characters
text5 = "   Hello World   "
print(f"'{text5.strip()}'")  # 'Hello World' - both sides
print(f"'{text5.lstrip()}'")  # 'Hello World   ' - left only
print(f"'{text5.rstrip()}'")  # '   Hello World' - right only

# Strip specific characters
text6 = "***Hello***"
print(text6.strip("*"))  # Hello

# Remove prefix/suffix (Python 3.9+)
url = "https://example.com"
print(url.removeprefix("https://"))  # example.com
print(url.removesuffix(".com"))  # https://example
print()

# ==========================================
# 5. SPLITTING AND JOINING
# ==========================================

print("SPLITTING AND JOINING:")

# Split string into list
sentence = "Python is awesome and powerful"
print(sentence.split())  # ['Python', 'is', 'awesome', 'and', 'powerful']
print(sentence.split("and"))  # ['Python is awesome ', ' powerful']

# Split with max splits
print(sentence.split(" ", 2))  # ['Python', 'is', 'awesome and powerful']

# Split from right
print(sentence.rsplit(" ", 1))  # ['Python is awesome and', 'powerful']

# Split lines
multiline = "Line 1\nLine 2\nLine 3"
print(multiline.splitlines())  # ['Line 1', 'Line 2', 'Line 3']

# Partition (split into 3 parts)
email = "user@example.com"
print(email.partition("@"))  # ('user', '@', 'example.com')
print(email.rpartition("."))  # ('user@example', '.', 'com')

# Join strings
words = ["Python", "is", "fun"]
print(" ".join(words))  # Python is fun
print("-".join(words))  # Python-is-fun
print()
