# `pass` is a no-op (does nothing). Use it as a placeholder

# when a block is required syntactically but you have no code yet.

# 1) placeholder in a function
def todo_function():
    pass  # implementation will be added later

print("todo_function() returns:", todo_function())  # prints: None

# 2) placeholder in a class
class EmptyClass:
    pass  # class body empty for now

print("EmptyClass:", EmptyClass)

# 3) used in loops or conditionals (does nothing for that case)
for i in range(3):
    if i == 1:
        pass  # intentionally skip handling for i == 1
    else:
        print("i =", i)  # prints i = 0 and i = 2

# 4) empty loop body (valid but no action taken)
for _ in range(2):
    pass
print("Finished empty loop")