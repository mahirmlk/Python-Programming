# Python Syntax andd indentation

message = "Hello, Python!"   # string
count = 3                    # integer
pi = 3.14                    # float
is_ready = True              # boolean

# 2) Printing values
print(message)               # prints: Hello, Python!
print(count, pi, is_ready)   # prints multiple values separated by spaces

# 3) Indentation defines code blocks in Python (use 4 spaces)
if count > 0:                # colon starts a new block
    print("count is positive")   # this line is indented -> inside the if-block
    if count > 2:                # nested block (indent again)
        print("count is greater than 2")
else:
    print("count is not positive")  # would run if condition above is False

# 4) Loops (for) with indentation
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:         # start loop block
    print("Fruit:", fruit)   # indented -> inside the loop
