# -----------------------------------------------
# Variables in Python: rules and examples
# -----------------------------------------------

print("\n=== What is a variable? ===")
# A variable is a named reference to a value (data) stored in memory.
# You create it by assigning with = (single equals).
language = "Python"
version = 3.13
print("language:", language)
print("version:", version)

print("\n=== Naming rules (syntactic rules) ===")
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

print("\n=== Assignment and dynamic typing ===")
# Python is dynamically typed: a variable can point to values of different types at different times.
x = 10            # int
print("x =", x, "(int)")
x = "ten"         # now a string
print("x =", x, "(str)")
x = 10.0          # now a float
print("x =", x, "(float)")

print("\n=== Multiple assignment ===")
# You can assign multiple variables in one line:
a, b = 1, 2
print("a:", a, "b:", b)


print("\n=== Descriptive names (best practice) ===")
# Prefer clear, descriptive names over single letters (except for short loops, math, etc.)
total_amount = 299.99
item_count = 3
average_price = total_amount / item_count
print("average_price:", average_price)

print("\n=== Naming styles (conventions, not enforced by Python) ===")
# snake_case: preferred for variables and functions (per PEP 8 style guide)
first_name = "Asha"

# UPPER_CASE: common for constants (convention only)
MAX_USERS = 100

# camelCase / PascalCase are used in some codebases, but snake_case is the Pythonic default
camelCaseExample = "allowed_but_not_typical"
PascalCaseExample = "also_allowed"

print("first_name:", first_name, "| MAX_USERS:", MAX_USERS)

print("\n=== Keywords caution ===")
# If a name conflicts with a keyword, add a trailing underscore or pick a better name:
# class = "Business"         # INVALID (keyword)
class_ = "Business"           # OK (but better to choose something like passenger_class)
passenger_class = "Business"  # clearer

print("class_:", class_, "| passenger_class:", passenger_class)

print("\n=== Constants (by convention) ===")
# Python doesn’t enforce constants, but use uppercase to signal “don’t reassign”
TAX_RATE = 0.18
print("TAX_RATE:", TAX_RATE)


print("\n=== Unicode names (valid but use with care) ===")
# Python allows many Unicode letters in names; use this only when it improves clarity in your domain.
π = 3.14159    # valid
α = 2
print("π:", π, "| α:", α)

print("\n=== Good vs bad naming examples ===")
# Good (descriptive, readable):
current_temperature_c = 26
items_in_cart = 5

# Bad (too vague or hard to read):
# data = 26
# numberofgraduates = 200  # hard to parse; prefer number_of_graduates

print("current_temperature_c:", current_temperature_c, "| items_in_cart:", items_in_cart)

print("\n=== Quick do/don’t summary (as comments) ===")
# DO:
# - Use snake_case for variable names: user_count, total_price
# - Start names with a letter or underscore
# - Make names descriptive: start_time, last_name, max_retries
# - Use UPPER_CASE for constants: DEFAULT_PORT, API_URL
#
# DON’T:
# - Start with digits: 1st_item
# - Use spaces or special symbols: my var, price$, user-name
# - Shadow keywords: for, class, def, None, True, False
# - Use overly vague names: data, value, temp (unless context is obvious)

print("\nAll variable rule demos complete.")
