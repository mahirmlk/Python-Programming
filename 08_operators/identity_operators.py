# Identity Operators in Python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

# is operator - returns True if both variables point to same object
print("list1 is list2:", list1 is list2)  
print("list1 is list3:", list1 is list3)  

# is not operator - returns True if variables point to different objects
print("list1 is not list2:", list1 is not list2)  
print("list1 is not list3:", list1 is not list3)  

# Note: == checks value equality, is checks object identity
print("list1 == list2:", list1 == list2)  
print("list1 == list3:", list1 == list3)  
