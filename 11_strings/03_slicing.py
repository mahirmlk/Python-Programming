# Basic string slicing 
text = "Hello, World!"
print(text[2:5])  

# Examples of slicing with different parameters
sentence = "The quick brown"
second_word = sentence[4:9]   
third_word = sentence[10:15]  
print(second_word)  
print(third_word)   


# Slicing from start or to end
s = "Hello, World!"

# From start to position 5 (exclusive)
print(s[:5])    

# From position 7 to end
print(s[7:])   

# Entire string
print(s[:])    

#Negative indexing with slicing

b = "Hello, World!"
# From position -5 to -2 (exclusive)
print(b[-5:-2])  

# List slicing example

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get elements from index 2 to end
print(a[2:])    

# Get elements from start to index 3 (exclusive)
print(a[:3])    

# Get all elements
print(a[:])    





