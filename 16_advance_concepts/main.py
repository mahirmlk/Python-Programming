"""
Iterables: Objects you can loop over (lists, tuples, strings, dicts, sets, etc.)
Iterators: Objects that produce values one at a time using __next__()
"""

# Basic iterables
print("List:", [1, 2, 3])
print("Tuple:", (1, 2, 3))
print("String:", "abc")
print("Set:", {1, 2, 3})
print("Dict keys:", {"a": 1, "b": 2}.keys())

# Looping over iterables
for x in [10, 20, 30]:
    print(x)

# iter() converts iterable to iterator
nums = [1, 2, 3]
it = iter(nums)
print(next(it))  # 1
print(next(it))  # 2

# range() is an iterable
for i in range(3):
    print(i)

# enumerate() adds index
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")

# zip() combines iterables
names = ["Alice", "Bob"]
ages = [25, 30]
for name, age in zip(names, ages):
    print(f"{name} is {age}")

# List comprehension with iterables
squares = [x**2 for x in range(5)]
print(squares)

# Generator expression (memory efficient)
gen = (x**2 for x in range(5))
print(list(gen))

# Custom iterable class
class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        self.n = self.start
        return self
    
    def __next__(self):
        if self.n <= 0:
            raise StopIteration
        self.n -= 1
        return self.n + 1

for num in Countdown(3):
    print(num)

# any() and all() work with iterables
print(any([False, True, False]))  # True
print(all([True, True, False]))   # False

# sum(), min(), max() with iterables
print(sum([1, 2, 3, 4]))    # 10
print(min([5, 2, 8, 1]))    # 1
print(max([5, 2, 8, 1]))    # 8