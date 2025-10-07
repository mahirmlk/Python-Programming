# Tuples - Immutable ordered collections of items

# Empty tuple
empty = ()

# Tuple with elements
numbers = (10, 20, 30, 40)

# Mixed data types
mixed = (1, "hello", 3.5, True)

# Single element tuple — MUST have a comma
single = (5,)
print(type(single))   # <class 'tuple'>

# Without comma → not a tuple
not_tuple = (5)
print(type(not_tuple))  # <class 'int'>

# Tuple from a list
tuple_from_list = tuple([1, 2, 3])
print(tuple_from_list)

# Nested tuple
nested = ((1, 2), (3, 4), (5, 6))

# Accessing Elements

print(numbers[0])      # First element
print(numbers[-1])     # Last element
print(nested[1][0])    # 3

# Slicing Tuples

letters = ('a', 'b', 'c', 'd', 'e')
print(letters[1:4])   # ('b', 'c', 'd')
print(letters[:3])    # ('a', 'b', 'c')
print(letters[::2])   # ('a', 'c', 'e')

# Tuple Operations

A = (1, 2, 3)
B = (4, 5, 6)

print(A + B)       # Concatenation → (1, 2, 3, 4, 5, 6)
print(A * 2)       # Repetition → (1, 2, 3, 1, 2, 3)
print(len(A))      # Length → 3
print(3 in A)      # Membership → True

# Unpacking Tuples

person = ("John", 25, "Engineer")
name, age, job = person
print(name, age, job)

# Built-in Functions & Methods

nums = (10, 20, 30, 20, 40)

print(nums.count(20))   # 2
print(nums.index(30))   # 2
print(max(nums))        # 40
print(min(nums))        # 10
print(sum(nums))        # 120
print(sorted(nums))     # [10, 20, 20, 30, 40]

"""

Tuples are immutable — once created, they cannot be changed (no append, remove, etc.).

Ordered — elements maintain their position.

Allow duplicates.

"""


