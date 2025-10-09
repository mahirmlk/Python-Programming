"""
File reading with error handling to prevent crashes.
Common errors: FileNotFoundError, PermissionError
"""

# Read entire file
try:
    with open("test.txt", "r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not found!")

# Read line by line
try:
    with open("test.txt", "r") as f:
        for line in f:
            print(line)
except FileNotFoundError:
    print("File not found!")

# Read all lines into list
try:
    with open("test.txt", "r") as f:
        lines = f.readlines()
        print(lines)
except FileNotFoundError:
    print("File not found!")

# Simple function to read file safely
def read_file(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

result = read_file("test.txt")
print(result)

# Check if file exists first
import os

if os.path.exists("test.txt"):
    with open("test.txt", "r") as f:
        print(f.read())
else:
    print("File doesn't exist")

# Handle multiple errors
try:
    with open("test.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("No permission to read")
except Exception as e:
    print(f"Something went wrong: {e}")

# Read numbers from file
def read_numbers(filename):
    try:
        with open(filename, "r") as f:
            numbers = []
            for line in f:
                numbers.append(int(line.strip()))
            return numbers
    except FileNotFoundError:
        print("File not found")
        return []
    except ValueError:
        print("File contains invalid numbers")
        return []

nums = read_numbers("numbers.txt")
print(nums)