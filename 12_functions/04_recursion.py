# Python Recursion 

# 1. Factorial Example
def factorial(n):
    """Calculate factorial using recursion"""
    # Base case: factorial of 0 or 1 is 1
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")  # Output: 120
print(f"0! = {factorial(0)}")  # Output: 1

# 2. Fibonacci Sequence
def fibonacci(n):
    """Generate nth Fibonacci number"""
    # Base cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(f"F({i}) = {fibonacci(i)}")

# 3. Power Function
def power(base, exp):
    """Calculate base^exp using recursion"""
    # Base case
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    # Recursive case
    return base * power(base, exp - 1)

print(f"2^5 = {power(2, 5)}")  # Output: 32
print(f"3^4 = {power(3, 4)}")  # Output: 81

# 4. Sum of List Elements
def sum_list(lst):
    """Sum all elements in a list recursively"""
    # Base case: empty list
    if not lst:
        return 0
    # Recursive case: first element + sum of rest
    return lst[0] + sum_list(lst[1:])

numbers = [1, 2, 3, 4, 5]
print(f"Sum of {numbers} = {sum_list(numbers)}")  # Output: 15
