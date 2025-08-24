# Logical Operators in Python
p = True
q = False

# AND (and) - returns True only if both conditions are True
print("p and q:", p and q)  # Output: False
print("p and p:", p and p)  # Output: True
print("q and q:", q and q)  # Output: False
print("q and p:", q and p)  # Output: False
print("True and True:", True and True)  # Output: True

# OR (or) - returns True if at least one condition is True
print("p or q:", p or q)  # Output: True
print("p or p:", p or p)  # Output: True
print("q or q:", q or q)  # Output: False
print("q or p:", q or p)  # Output: True
print("False or False:", False or False)  # Output: False

# NOT (not) - returns opposite of the condition
print("not p:", not p)  # Output: False
print("not q:", not q)  # Output: True

# Practical example with conditions
age = 25
has_license = True

# Using logical operators in conditional statements
if age >= 18 and has_license:
    print("Can drive")  # This will execute
else:
    print("Cannot drive")
