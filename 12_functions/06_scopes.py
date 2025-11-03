# Global Scope: Variables defined at the top level of your program
# Local Scope: Variables defined inside a function

# Enclosing Scope: Variables in outer functions (for nested functions)

x = "global"

def test_scope():
    x = "local"        # This creates a new local variable
    print(f"Inside function: {x}")

test_scope()           
print(f"Outside function: {x}")  

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
        print(local_var)      
        print(outer_var)      
        print(global_var)     
    
    inner_function()
    print(outer_var)       
    # print(local_var)        

def another_function():
    print(global_var)        
    # print(outer_var)       

# Test the functions
outer_function()
another_function()