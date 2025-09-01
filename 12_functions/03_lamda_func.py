# lambda function syntax

# Example 1: Simple addition
add = lambda x, y: x + y
print(add(5, 3))  # Output: 8

# Example 2: Square a number
square = lambda x: x ** 2
print(square(4))  # Output: 16

# Example 3: Check if number is even
is_even = lambda x: x % 2 == 0
print(is_even(6))  # Output: True
print(is_even(7))  # Output: False

# Example 4: Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# With map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

# With filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

# With sorted()
words = ['apple', 'pie', 'Washington', 'book']
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)  # Output: ['pie', 'book', 'apple', 'Washington']

# Example 5: Lambda with multiple arguments
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  # Output: 24

# Example 6: Lambda with conditional expression
max_of_two = lambda x, y: x if x > y else y
print(max_of_two(10, 5))  # Output: 10