
# Python Syntax Explanation


# print displays output to the screen.
# Comments start with # and are ignored by Python.

print("Hello, world!")  # This is a comment
print("You can print", "multiple", "things", 123)

# VARIABLES AND BASIC TYPES
# Python figures out the type automatically (dynamic typing).
name = "tyson"         # string (text)
age = 20              # int (whole number)
height = 5.69         # float (decimal)
is_student = True     # bool
nothing = None        # special "no value"

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student?", is_student)
print("Nothing:", nothing)



# INPUT (commented to avoid blocking when you run this) 
# input() reads a line of text from the user and returns a string.
# Uncomment these lines to try:
# user_name = input("Your name: ")
# user_age = int(input("Your age: "))  # convert to integer
# print(f"Hello {user_name}, next year you'll be {user_age + 1}")

# OPERATORS AND EXPRESSIONS

# Math: + - * / // % **    Compare: == != < <= > >=    Logic: and or not
print("5 + 3 =", 5 + 3)
print("10 / 3 =", 10 / 3)   # float division
print("10 // 3 =", 10 // 3) # floor division
print("2 ** 3 =", 2 ** 3)   # exponentiation
print("5 % 2 =", 5 % 2)     # modulus (remainder)
print("3 > 2 and 2 > 1:", 3 > 2 and 2 > 1)
print("not (3 < 2):", not (3 < 2))



# IF / ELIF / ELSE 
score = 78
if score >= 90:
    grade = "A"
elif score >= 75:
    grade = "B"
else:
    grade = "C or below"
print("Grade:", grade)

# LISTS (ORDERED COLLECTIONS) 
nums = [10, 20, 30]
print("First number:", nums[0])  # indexing starts at 0
nums.append(40)                   # add to end
print("All numbers:", nums)
print("Length:", len(nums))       # number of items



# Indentation Rules:
# INDENTATION DEFINES BLOCKS 
# Indentation (spaces at the start) defines code blocks. Use 4 spaces.
if age >= 18:
    print("Adult (inside if-block)")
else:
    print("Minor")

# - Use 4 spaces for each block level (not tabs).
# - A colon (:) starts a block; the next line must be indented.
# - All lines in the same block must have the SAME indentation.


# if/else block
x = 7
if x > 5:              # colon starts a block
    print("x > 5")     # 4 spaces = inside the if-block
else:
    print("x <= 5")    # aligned with the 'if' block's body

print("if/else") # no indent = outside the block



# Common mistakes to avoid (EXAMPLES ONLY; do not uncomment)
# 1) Missing indentation after colon -> IndentationError
if True:
    print("must be indented")

# 2) Inconsistent indentation (mixing tabs and spaces) -> IndentationError
if True:
     print("4 spaces")
     print("a tab")  # don't mix!

print("End")
