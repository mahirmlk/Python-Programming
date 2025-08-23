# Python Typecasting Demo
# Typecasting (Type Conversion) is the process of converting one data type to another

print("=" * 50)
print("PYTHON TYPECASTING DEMONSTRATION")
print("=" * 50)

# 1. IMPLICIT TYPECASTING (Automatic)
print("\n1. IMPLICIT TYPECASTING (Automatic)")
print("-" * 40)

# Python automatically converts smaller types to larger types
int_num = 5
float_num = 3.14
result = int_num + float_num  # int + float = float
print(f"int({int_num}) + float({float_num}) = {result} (type: {type(result)})")

# 2. EXPLICIT TYPECASTING (Manual)
print("\n2. EXPLICIT TYPECASTING (Manual)")
print("-" * 40)

# Converting to int
print("\n--- Converting to int ---")
float_val = 3.14
string_num = "42"
bool_val = True

int_from_float = int(float_val)
int_from_string = int(string_num)
int_from_bool = int(bool_val)

print(f"int({float_val}) = {int_from_float}")
print(f"int('{string_num}') = {int_from_string}")
print(f"int({bool_val}) = {int_from_bool}")

# Converting to float
print("\n--- Converting to float ---")
int_val = 7
string_float = "3.14"
string_int = "42"

float_from_int = float(int_val)
float_from_string = float(string_float)
float_from_string_int = float(string_int)

print(f"float({int_val}) = {float_from_int}")
print(f"float('{string_float}') = {float_from_string}")
print(f"float('{string_int}') = {float_from_string_int}")

# Converting to string
print("\n--- Converting to string ---")
number = 42
decimal = 3.14159
boolean = True
none_val = None

string_from_int = str(number)
string_from_float = str(decimal)
string_from_bool = str(boolean)
string_from_none = str(none_val)

print(f"str({number}) = '{string_from_int}'")
print(f"str({decimal}) = '{string_from_float}'")
print(f"str({boolean}) = '{string_from_bool}'")
print(f"str({none_val}) = '{string_from_none}'")

# Converting to boolean
print("\n--- Converting to boolean ---")
zero = 0
one = 1
empty_string = ""
non_empty_string = "Hello"
zero_float = 0.0
none_value = None

bool_from_zero = bool(zero)
bool_from_one = bool(one)
bool_from_empty = bool(empty_string)
bool_from_non_empty = bool(non_empty_string)
bool_from_zero_float = bool(zero_float)
bool_from_none = bool(none_value)

print(f"bool({zero}) = {bool_from_zero}")
print(f"bool({one}) = {bool_from_one}")
print(f"bool('{empty_string}') = {bool_from_empty}")
print(f"bool('{non_empty_string}') = {bool_from_non_empty}")
print(f"bool({zero_float}) = {bool_from_zero_float}")
print(f"bool({none_value}) = {bool_from_none}")

# 3. COMPLEX TYPECASTING SCENARIOS
print("\n3. COMPLEX TYPECASTING SCENARIOS")
print("-" * 40)

# List to other types
print("\n--- List conversions ---")
my_list = [1, 2, 3, 4, 5]
list_to_string = str(my_list)
list_to_tuple = tuple(my_list)
list_to_set = set(my_list)

print(f"Original list: {my_list}")
print(f"str({my_list}) = {list_to_string}")
print(f"tuple({my_list}) = {list_to_tuple}")
print(f"set({my_list}) = {list_to_set}")

# String to list/tuple
print("\n--- String to sequence ---")
text = "Hello"
string_to_list = list(text)
string_to_tuple = tuple(text)

print(f"Original string: '{text}'")
print(f"list('{text}') = {string_to_list}")
print(f"tuple('{text}') = {string_to_tuple}")

# 4. COMMON TYPECASTING FUNCTIONS
print("\n4. COMMON TYPECASTING FUNCTIONS")
print("-" * 40)

# chr() and ord() for character conversion
print("\n--- Character conversions ---")
ascii_num = 65
char = chr(ascii_num)
char_to_ascii = ord('A')

print(f"chr({ascii_num}) = '{char}'")
print(f"ord('A') = {char_to_ascii}")

# bin(), oct(), hex() for number base conversion
print("\n--- Number base conversions ---")
decimal_num = 42
binary = bin(decimal_num)
octal = oct(decimal_num)
hexadecimal = hex(decimal_num)

print(f"Decimal: {decimal_num}")
print(f"Binary: {binary}")
print(f"Octal: {octal}")
print(f"Hexadecimal: {hexadecimal}")

# 5. ERROR HANDLING IN TYPECASTING
print("\n5. ERROR HANDLING IN TYPECASTING")
print("-" * 40)

# Safe typecasting with error handling
def safe_int_conversion(value):
    try:
        return int(value)
    except (ValueError, TypeError):
        return f"Cannot convert '{value}' to int"

def safe_float_conversion(value):
    try:
        return float(value)
    except (ValueError, TypeError):
        return f"Cannot convert '{value}' to float"

# Test cases
test_values = ["123", "3.14", "abc", "", "12.34", None]

print("\n--- Safe int conversion ---")
for value in test_values:
    result = safe_int_conversion(value)
    print(f"int('{value}') = {result}")

print("\n--- Safe float conversion ---")
for value in test_values:
    result = safe_float_conversion(value)
    print(f"float('{value}') = {result}")

# 6. PRACTICAL EXAMPLES
print("\n6. PRACTICAL EXAMPLES")
print("-" * 40)

# User input processing
print("\n--- User input processing ---")
# Simulating user input (normally you'd use input())
user_age = "25"
user_height = "5.8"
user_name = "John"

# Convert string inputs to appropriate types
age_int = int(user_age)
height_float = float(user_height)

print(f"User: {user_name}, Age: {age_int} (type: {type(age_int)})")
print(f"User: {user_name}, Height: {height_float} (type: {type(height_float)})")

# Mathematical operations
print("\n--- Mathematical operations ---")
string_num1 = "10"
string_num2 = "5"

# Convert strings to numbers for calculation
num1 = int(string_num1)
num2 = int(string_num2)

sum_result = num1 + num2
product = num1 * num2

print(f"'{string_num1}' + '{string_num2}' = {num1} + {num2} = {sum_result}")
print(f"'{string_num1}' * '{string_num2}' = {num1} * {num2} = {product}")

# 7. TYPE CHECKING
print("\n7. TYPE CHECKING")
print("-" * 40)

# Using isinstance() to check types
def demonstrate_type_checking():
    values = [42, 3.14, "Hello", True, [1, 2, 3], None]
    
    for value in values:
        if isinstance(value, int):
            print(f"{value} is an integer")
        elif isinstance(value, float):
            print(f"{value} is a float")
        elif isinstance(value, str):
            print(f"{value} is a string")
        elif isinstance(value, bool):
            print(f"{value} is a boolean")
        elif isinstance(value, list):
            print(f"{value} is a list")
        elif value is None:
            print(f"{value} is None")

demonstrate_type_checking()

print("\n" + "=" * 50)
print("TYPECASTING DEMO COMPLETE!")
print("=" * 50)
