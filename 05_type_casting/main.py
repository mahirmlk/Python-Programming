# Typecasting in Python means converting one data type to another.

# Integer to float
num_int = 10
num_float = float(num_int)  # Converts integer to float
print("Integer to float:", num_float)  # Output: 10.0

# Float to integer
num_float2 = 15.7
num_int2 = int(num_float2)  # Converts float to integer (truncates decimal part)
print("Float to integer:", num_int2)  # Output: 15

# String to integer
str_num = "123"
int_num = int(str_num)  # Converts string to integer
print("String to integer:", int_num)  # Output: 123

# Integer to string
num = 456
str_num2 = str(num)  # Converts integer to string
print("Integer to string:", str_num2)  # Output: '456'

# String to float
str_float = "3.14"
float_num = float(str_float)  # Converts string to float
print("String to float:", float_num)  # Output: 3.14

# Float to string
float_num2 = 9.81
str_float2 = str(float_num2)  # Converts float to string
print("Float to string:", str_float2)  # Output: '9.81'

# Boolean to integer
bool_val = True
int_bool = int(bool_val)  # True becomes 1, False becomes 0
print("Boolean to integer:", int_bool)  # Output: 1

# Integer to boolean
num3 = 0
bool_num = bool(num3)  # 0 becomes False, any non-zero becomes True
print("Integer to boolean:", bool_num)  # Output: False

# List to tuple
list1 = [1, 2, 3]
tuple1 = tuple(list1)  # Converts list to tuple
print("List to tuple:", tuple1)  # Output: (1, 2, 3)

# Tuple to list
tuple2 = (4, 5, 6)
list2 = list(tuple2)  # Converts tuple to list
print("Tuple to list:", list2)  # Output: [4, 5, 6]