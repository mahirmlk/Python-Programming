# Logical Operators in Python
p = True
q = False

# AND (and) - returns True only if both conditions are True
print("p and q:", p and q)  
print("p and p:", p and p)  
print("q and q:", q and q)   
print("q and p:", q and p)  
print("True and True:", True and True)  # 

# OR (or) - returns True if at least one condition is True
print("p or q:", p or q)  
print("p or p:", p or p)   
print("q or q:", q or q)   
print("q or p:", q or p)   
print("False or False:", False or False)  # 

# NOT (not) - returns opposite of the condition
print("not p:", not p)  
print("not q:", not q)  

# Practical example with conditions
age = 25
has_license = True

# Using logical operators in conditional statements
if age >= 18 and has_license:
    print("Can drive")  # This will execute
else:
    print("Cannot drive")
