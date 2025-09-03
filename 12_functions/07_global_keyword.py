count = 0  # Global variable

def increment():
    global count  # Tell Python we want to modify the global variable
    count = count + 1
    print(f"Count inside function: {count}")

def reset():
    global count
    count = 0
    print("Count reset to 0")

# Test the functions
print(f"Initial count: {count}")  # 0
increment()                       # Count inside function: 1
increment()                       # Count inside function: 2
print(f"Count outside: {count}")  # 2
reset()                          # Count reset to 0
print(f"Final count: {count}")   # 0

# without global keyword

count = 0  # Global variable

def increment():
    count = count + 1  # Error! Can't modify global variable
    print(count)

# increment()  # This would cause: UnboundLocalError

# multiple global variables

name = "Mahir"
age = 25

def update_person():
    global name, age  # Declare multiple global variables
    name = "Sourabh"
    age = 24

print(f"Before: {name}, {age}")  
update_person()
print(f"After: {name}, {age}")   

# Craeting new global variable

def create_global():
    global new_var  # Create a new global variable
    new_var = "I'm a new global variable!"

create_global()
print(new_var)  # I'm a new global variable!

# When not to use global keyword

message = "Hello"

def read_only():
    # No 'global' needed - just reading the variable
    print(message)  # This works fine

def local_variable():
    message = "Local message"  # This creates a new local variable
    print(message)  # Prints the local version

read_only()        # Hello
local_variable()   # Local message
print(message)     # Hello (global unchanged)