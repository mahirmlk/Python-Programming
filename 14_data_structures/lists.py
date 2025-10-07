# Lists - ordered, changeable, allows duplicate elements

# Empty list
my_list = []

# List with elements
numbers = [10, 20, 30, 40, 50]
fruits = ["apple", "banana", "cherry"]

# Mixed data types
mixed = [1, "hello", 3.5, True]

# Nested list
nested = [1, [2, 3], [4, 5, 6]]

# Accessing Elements

print(numbers[0])     # First element → 10
print(numbers[-1])    # Last element → 50
print(nested[1][1])   # Access inside nested list → 3

# Modifying Elements

numbers[2] = 35       # Change 30 → 35
print(numbers)        # [10, 20, 35, 40, 50]

# Adding Elements

numbers.append(60)            # Add at end
numbers.insert(1, 15)         # Add at index 1
numbers.extend([70, 80, 90])  # Add multiple elements
print(numbers)

# Removing Elements

numbers.remove(35)    # Remove by value
print(numbers)

popped = numbers.pop()     # Remove last
print(popped)              # 90
print(numbers)

del numbers[0]        # Delete by index
print(numbers)

numbers.clear()        # Empty the list
print(numbers)         # []

# Recreating and Useful Methods

nums = [3, 1, 4, 1, 5, 9, 2]

print(len(nums))         # Count of items
print(nums.count(1))     # Count specific value
print(nums.index(5))     # Index of first 5
nums.sort()              # Sort ascending
print(nums)
nums.reverse()           # Reverse list
print(nums)
nums_copy = nums.copy()  # Copy list
print(nums_copy)

# List Slicing

letters = ['a', 'b', 'c', 'd', 'e']
print(letters[1:4])   # ['b', 'c', 'd']
print(letters[:3])    # ['a', 'b', 'c']
print(letters[::2])   # ['a', 'c', 'e']


# Iterating through a List

for item in letters:
    print(item)

