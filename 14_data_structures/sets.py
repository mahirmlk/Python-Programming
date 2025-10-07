# Sets - Unordered, Unindexed, No Duplicates

# Empty set
my_set = set()

# Set with elements
fruits = {"apple", "banana", "cherry"}

# Mixed data types
mixed = {1, "hello", 3.5, True}

# Set from list
nums = set([1, 2, 2, 3, 4, 4, 5])  # duplicates removed automatically
print(nums)   # {1, 2, 3, 4, 5}

# Adding and Removing Elements

fruits.add("orange")           # Add one element
fruits.update(["grape", "mango"])  # Add multiple elements
print(fruits)

fruits.remove("apple")         # Remove item (error if not found)
fruits.discard("pear")         # Remove safely (no error if missing)
popped = fruits.pop()          # Remove random item
print(f"Removed: {popped}")
print(fruits)

fruits.clear()                 # Empty the set
print(fruits)                  # set()

# Set Operations

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(A.union(B))              # {1, 2, 3, 4, 5, 6}
print(A | B)                  

print(A.intersection(B))       # {3, 4}
print(A & B)                  

print(A.difference(B))         # {1, 2}
print(A - B)                   

print(B.difference(A))         # {5, 6}

print(A.symmetric_difference(B))  # {1, 2, 5, 6}
print(A ^ B)                      

# Set Relations

X = {1, 2}
Y = {1, 2, 3, 4}

print(X.issubset(Y))      # True
print(Y.issuperset(X))    # True
print(X.isdisjoint({5, 6}))  # True 

# Copying and Length

Z = {10, 20, 30}
Z_copy = Z.copy()
print(len(Z))
print(Z_copy)

"""
1. Sets are unordered — elements have no fixed position or index.

2. Duplicates are removed automatically.

3. Mutable — you can add or remove elements.

"""