# lambda function syntax

# Example 1: Simple addition
add = lambda x, y: x + y
print(add(5, 3)) 

# Example 2: Square a number
square = lambda x: x ** 2
print(square(4)) 

# Example 3: Check if number is even
is_even = lambda x: x % 2 == 0
print(is_even(6)) 
print(is_even(7))  

# Example 4: Using lambda with built-in functions
numbers = [1, 2, 3, 4, 5]

# With map()
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers) 

# With filter()
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  

# With sorted()
words = ['apple', 'pie', 'Washington', 'book']
sorted_by_length = sorted(words, key=lambda x: len(x))
print(sorted_by_length)  

# Example 5: Lambda with multiple arguments
multiply = lambda a, b, c: a * b * c
print(multiply(2, 3, 4))  

# Example 6: Lambda with conditional expression
max_of_two = lambda x, y: x if x > y else y
print(max_of_two(10, 5))  