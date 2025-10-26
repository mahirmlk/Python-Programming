# A variable is a named reference to a value (data) stored in memory.
# You create it by assigning with =

language = "Python"
version = 3.13
print("language:", language)
print("version:", version)

print("Naming rules")
# 1) Must start with a letter (A–Z or a–z) or underscore (_)
# 2) Cannot start with a digit (0–9)
# 3) Can contain letters, digits, and underscores only (A–Z, a–z, 0–9, _)
# 4) Case-sensitive: name, Name, and NAME are all different
# 5) Cannot be a Python keyword (e.g., if, else, for, class, def, True, None, etc.)

# VALID examples:
user_name = "Mahir"
_age = 20
score2 = 98
PI_APPROX = 3.14  # often used for constants (by convention: UPPER_CASE)

print("user_name:", user_name, "| _age:", _age, "| score2:", score2, "| PI_APPROX:", PI_APPROX)

# INVALID examples):
# 2name = "bad"        # starts with a digit
# first-name = "bad"   # hyphen not allowed
# my name = "bad"      # spaces not allowed
# class = 10           # 'class' is a reserved keyword

# Python is dynamically typed: a variable can point to values of different types at different times.
x = 10            
print("x =", x, "(int)")
x = "ten"         
print("x =", x, "(str)")
x = 10.0          
print("x =", x, "(float)")

# You can assign multiple variables in one line:
a, b = 1, 2
print("a:", a, "b:", b)


print("\n=== Descriptive names (best practice) ===")
# Prefer clear, descriptive names over single letters (except for short loops, math, etc.)
total_amount = 299.99
item_count = 3
average_price = total_amount / item_count
print("average_price:", average_price)

#Naming conventions:
# snake_case: preferred for variables and functions 
first_name = "Asha"

# UPPER_CASE: common for constants
MAX_USERS = 100

# camelCase / PascalCase are used in some codebases, but snake_case is the Pythonic default
camelCaseExample = "allowed_but_not_typical"
PascalCaseExample = "also_allowed"


