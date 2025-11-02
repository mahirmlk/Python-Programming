# Indexing in python

# String indexing
s = "Python"
print("s =", s)
print("s[0] ->", s[0])      
print("s[1] ->", s[1])     
print("s[-1] ->", s[-1])    
print("s[-2] ->", s[-2])   
print("last char using len:", s[len(s)-1]) 

# List indexing
lst = [10, 20, 30, 40, 50]
print("\nlst =", lst)
print("lst[0] ->", lst[0])   
print("lst[2] ->", lst[2])   
print("lst[-1] ->", lst[-1]) 
print("lst[-3] ->", lst[-3])  


# Out-of-range index handling
try:
    print("\ns[100] ->", s[100])
except IndexError as e:
    print("IndexError (example):", e)

