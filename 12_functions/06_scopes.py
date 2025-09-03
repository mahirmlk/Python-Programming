# Global Scope: Variables defined at the top level of your program
# Local Scope: Variables defined inside a function
# Enclosing Scope: Variables in outer functions (for nested functions)

x = "global"

def test_scope():
    x = "local"        # This creates a new local variable
    print(f"Inside function: {x}")

test_scope()           # Output: Inside function: local
print(f"Outside function: {x}")  # Output: Outside function: global

# Another Example

# Global scope
global_var = "I'm global!"

def outer_function():
    # Enclosing scope (local to outer_function)
    outer_var = "I'm in the outer function!"
    
    def inner_function():
        # Local scope (local to inner_function)
        local_var = "I'm local to inner function!"
        
        # Accessing variables from different scopes
        print(local_var)      # Local scope
        print(outer_var)      # Enclosing scope
        print(global_var)     # Global scope
    
    inner_function()
    print(outer_var)          # Can access its own local variable
    # print(local_var)        # Error! Can't access inner function's local variable

def another_function():
    print(global_var)         # Can access global variable
    # print(outer_var)        # Error! Can't access other function's local variable

# Test the functions
outer_function()
another_function()