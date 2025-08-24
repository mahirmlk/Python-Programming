# Identity Operators in Python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# is operator - returns True if both variables point to same object
print("list1 is list2:", list1 is list2)  # Output: False (different objects)
print("list1 is list3:", list1 is list3)  # Output: True (same object)

# is not operator - returns True if variables point to different objects
print("list1 is not list2:", list1 is not list2)  # Output: True
print("list1 is not list3:", list1 is not list3)  # Output: False

# Note: == checks value equality, is checks object identity
print("list1 == list2:", list1 == list2)  # Output: True (same values)
print("list1 == list3:", list1 == list3)  # Output: True (same values)
# Commonly used in scenarios where object identity matters, like singletons.
