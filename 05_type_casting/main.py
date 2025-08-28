# Typecasting in Python: Converting Data Types
# Typecasting, also known as type conversion, is the process of converting a variable from one data type to another.
# Python has several built-in functions for this purpose, such as int(), float(), str(), list(), tuple(), etc.

# ----------------------------------------------------------------
# 1. Converting to Integers: int()
# ----------------------------------------------------------------

# From float to integer
# When a float is converted to an integer, the decimal part is truncated (removed).
float_number = 15.7
integer_from_float = int(float_number)
print(f"Float {float_number} to integer: {integer_from_float}")  # Output: 15

# From string to integer
# The string must contain a valid integer representation.
string_number = "123"
integer_from_string = int(string_number)
print(f"String '{string_number}' to integer: {integer_from_string}")  # Output: 123

# From boolean to integer
# True is converted to 1, and False is converted to 0.
bool_true = True
integer_from_bool = int(bool_true)
print(f"Boolean {bool_true} to integer: {integer_from_bool}")  # Output: 1


# ----------------------------------------------------------------
# 2. Converting to Floats: float()
# ----------------------------------------------------------------

# From integer to float
# An integer is converted to a float by adding a decimal point and a zero.
integer_number = 10
float_from_integer = float(integer_number)
print(f"Integer {integer_number} to float: {float_from_integer}")  # Output: 10.0

# From string to float
# The string must contain a valid float or integer representation.
string_float = "3.14"
float_from_string = float(string_float)
print(f"String '{string_float}' to float: {float_from_string}")  # Output: 3.14


# ----------------------------------------------------------------
# 3. Converting to Strings: str()
# ----------------------------------------------------------------

# From integer to string
# The integer is converted into its string representation.
num_to_str = 456
string_from_int = str(num_to_str)
print(f"Integer {num_to_str} to string: '{string_from_int}'")  # Output: '456'

# From float to string
# The float is converted into its string representation.
float_to_str = 9.81
string_from_float = str(float_to_str)
print(f"Float {float_to_str} to string: '{string_from_float}'")  # Output: '9.81'


# ----------------------------------------------------------------
# 4. Converting to Booleans: bool()
# ----------------------------------------------------------------

# In Python, certain values are considered "falsy" and will convert to False.
# All other values are "truthy" and will convert to True.
# Falsy values include: 0, 0.0, '', [], (), {}, None, False

# From integer to boolean
# Zero (0) becomes False, and any non-zero integer becomes True.
zero_int = 0
bool_from_zero = bool(zero_int)
print(f"Integer {zero_int} to boolean: {bool_from_zero}")  # Output: False

non_zero_int = -5
bool_from_non_zero = bool(non_zero_int)
print(f"Integer {non_zero_int} to boolean: {bool_from_non_zero}")  # Output: True


# ----------------------------------------------------------------
# 5. Converting Sequence Types
# ----------------------------------------------------------------

# From list to tuple
# Converts a list into an immutable tuple.
my_list = [1, 2, 3, 'a']
tuple_from_list = tuple(my_list)
print(f"List {my_list} to tuple: {tuple_from_list}")  # Output: (1, 2, 3, 'a')

# From tuple to list
# Converts a tuple into a mutable list.
my_tuple = (4, 5, 6, 'b')
list_from_tuple = list(my_tuple)
print(f"Tuple {my_tuple} to list: {list_from_tuple}")  # Output: [4, 5, 6, 'b']
