# Python String Methods 

# 1. CASE CONVERSION METHODS
text = "Hello World Python"

# Convert to uppercase
print(text.upper())  

# Convert to lowercase
print(text.lower())  

# Capitalize first letter only
print(text.capitalize())  

# Title case (capitalize each word)
print(text.title())  

# Swap case
print(text.swapcase())  

# Case folding (aggressive lowercase, good for case-insensitive comparison)
text2 = "ß"  
print(text2.casefold()) 
print()


# 2. SEARCHING AND CHECKING METHODS
sample = "Python Programming is Fun"

# Find substring (returns index or -1 if not found)
print(sample.find("Programming")) 
print(sample.find("Java"))  

# Index (like find but raises ValueError if not found)
print(sample.index("is"))  

# rfind and rindex (search from right)
text3 = "apple apple apple"
print(text3.rfind("apple"))  
print(text3.rindex("apple"))  

# Count occurrences
print(text3.count("apple")) 
print()


# 3. BOOLEAN CHECK METHODS

# Check if string starts/ends with substring
filename = "document.pdf"
print(filename.startswith("doc"))  
print(filename.endswith(".pdf"))  

# Check string composition
print("12345".isdigit())   
print("abc123".isalnum())   
print("abcdef".isalpha())   
print("   ".isspace())   
print("Hello".isupper())  
print("hello".islower())  
print("Title Case".istitle())   

# Additional checks
print("123.45".isdecimal())  
print("123".isnumeric())  
print("hello_world".isidentifier())   
print("Hello\nWorld".isprintable())  
print()


# 4. STRING MODIFICATION METHODS

# Replace substring
text4 = "I love Java. Java is great!"
print(text4.replace("Java", "Python"))  
print(text4.replace("Java", "Python", 1))  

# Strip whitespace or characters
text5 = "   Hello World   "
print(f"'{text5.strip()}'")  
print(f"'{text5.lstrip()}'")  
print(f"'{text5.rstrip()}'")

# Strip specific characters
text6 = "***Hello***"
print(text6.strip("*")) 

# Remove prefix/suffix (Python 3.9+)
url = "https://example.com"
print(url.removeprefix("https://"))  
print(url.removesuffix(".com"))  
print()


# 5. SPLITTING AND JOINING

# Split string into list
sentence = "Python is awesome and powerful"
print(sentence.split())  
print(sentence.split("and")) 

# Split with max splits
print(sentence.split(" ", 2))  

# Split from right
print(sentence.rsplit(" ", 1))  

# Split lines
multiline = "Line 1\nLine 2\nLine 3"
print(multiline.splitlines())  

# Partition (split into 3 parts)
email = "user@example.com"
print(email.partition("@"))  
print(email.rpartition(".")) 

# Join strings
words = ["Python", "is", "fun"]
print(" ".join(words))  
print("-".join(words))  
print()
