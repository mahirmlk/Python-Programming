# Basic string slicing example
text = "Hello, World!"
print(text[2:5])  # Output: "llo" (characters from index 2 to 4)

# Examples of slicing with different parameters

sentence = "The quick brown"
second_word = sentence[4:9]   # Extract "quick"
third_word = sentence[10:15]  # Extract "brown"
print(second_word)  # Output: "quick"
print(third_word)   # Output: "brown"


# Slicing from start or to end
s = "Hello, World!"

# From start to position 5 (exclusive)
print(s[:5])    # Output: "Hello"

# From position 7 to end
print(s[7:])    # Output: "World!"

# Entire string
print(s[:])     # Output: "Hello, World!"

#Negative indexing with slicing

b = "Hello, World!"
# From position -5 to -2 (exclusive)
print(b[-5:-2])  # Output: "orl" (from "o" in "World!" to before "d")

# List slicing example

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to end
print(a[2:])    # Output: [3, 4, 5, 6, 7, 8, 9]

# Get elements from start to index 3 (exclusive)
print(a[:3])    # Output: [1, 2, 3]

# Get all elements
print(a[:])     # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


# Key Points to Remember

# Indexing starts at 0: The first element is at index 0

# End index is exclusive: [2:5] includes indices 2, 3, and 4, but not 5

# Negative indices work backwards: -1 refers to the last element



