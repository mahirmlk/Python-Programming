count = 0  # Global variable

def increment():
    global count  
    count = count + 1
    print(f"Count inside function: {count}")

def reset():
    global count
    count = 0
    print("Count reset to 0")

# Test the functions
print(f"Initial count: {count}")  
increment()                      
increment()                      
print(f"Count outside: {count}")  
reset()                          
print(f"Final count: {count}")   

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
print(new_var) 

# When not to use global keyword

message = "Hello"

def read_only():
    # No 'global' needed - just reading the variable
    print(message) 

def local_variable():
    message = "Local message"  
    print(message)  

read_only()        
local_variable()  
print(message)    