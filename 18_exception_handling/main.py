"""
Exception handling prevents program crashes from errors.
try: Code that might cause error
except: Handle the error
else: Runs if no error
finally: Always runs (cleanup)
"""

# Basic try-except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Multiple exceptions
try:
    num = int("abc")
except ValueError:
    print("Invalid number format")
except TypeError:
    print("Type error occurred")

# Catching any exception
try:
    x = [1, 2, 3][10]
except Exception as e:
    print(f"Error: {e}")

# try-except-else-finally
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found")
else:
    print("File opened successfully")
finally:
    print("Cleanup completed")

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation error: {e}")

# Custom exceptions
class InsufficientFundsError(Exception):
    pass

class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Not enough funds")
        self.balance -= amount
        return self.balance

account = BankAccount(100)
try:
    account.withdraw(150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")

# Practical example - safe division
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    except TypeError:
        return "Invalid input types"

print(safe_divide(10, 2))
print(safe_divide(10, 0))
print(safe_divide(10, "a"))

