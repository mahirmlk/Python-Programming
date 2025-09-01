# Python Functions - Arguments and Parameters

# 1. SINGLE PARAMETER
print("1. Single Parameter:")
def greet(name):
    """Function with one parameter"""
    return f"Hello, {name}!"

# Calling with argument
print(greet("Mahir"))
print(greet("Harry"))
print()

# 2. MULTIPLE PARAMETERS
print("2. Multiple Parameters:")
def add_numbers(x, y):
    """Function with two parameters"""
    result = x + y
    return f"{x} + {y} = {result}"

def create_sentence(subject, verb, object):
    """Function with three parameters"""
    return f"{subject} {verb} {object}."

print(add_numbers(5, 3))
print(add_numbers(10, 15))
print(create_sentence("The cat", "chased", "the mouse"))
print(create_sentence("Students", "study", "programming"))
print()

# 3. DEFAULT PARAMETERS
print("3. Default Parameters:")
def greet_with_title(name, title="Mr./Ms."):
    """Function with default parameter"""
    return f"Hello, {title} {name}!"

def calculate_power(base, exponent=2):
    """Function with default exponent"""
    result = base ** exponent
    return f"{base}^{exponent} = {result}"

# Using default values
print(greet_with_title("Smith"))
print(calculate_power(5))

# Overriding default values
print(greet_with_title("Johnson", "Dr."))
print(calculate_power(3, 4))
print()

# 4. POSITIONAL vs KEYWORD ARGUMENTS
print("4. Positional vs Keyword Arguments:")
def describe_pet(name, animal_type, age):
    """Function to demonstrate different argument styles"""
    return f"{name} is a {age}-year-old {animal_type}"

# Positional arguments (order matters)
print("Positional:", describe_pet("charlie", "dog", 3))

# Keyword arguments (order doesn't matter)
print("Keyword:", describe_pet(age=2, name="Peter", animal_type="cat"))

# Mixed (positional first, then keyword)
print("Mixed:", describe_pet("Andy", age=4, animal_type="parrot"))
print()

# 5. VARIABLE-LENGTH ARGUMENTS (*args)
print("5. Variable-length Arguments (*args):")
def sum_numbers(*numbers):
    """Function that accepts any number of arguments"""
    total = sum(numbers)
    return f"Sum of {numbers} = {total}"

def find_maximum(*values):
    """Find maximum among any number of values"""
    if values:
        return f"Maximum of {values} = {max(values)}"
    return "No values provided"

print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40, 50))
print(find_maximum(5, 2, 8, 1, 9))
print(find_maximum(100))
print()

# 6. KEYWORD VARIABLE ARGUMENTS (**kwargs)
print("6. Keyword Variable Arguments (**kwargs):")
def create_profile(**details):
    """Create profile from keyword arguments"""
    profile = "Profile Details:\n"
    for key, value in details.items():
        profile += f"  {key.capitalize()}: {value}\n"
    return profile

def calculate_total(base_price, **extras):
    """Calculate total with additional costs"""
    total = base_price
    print(f"Base price: ${base_price}")
    for item, cost in extras.items():
        print(f"  {item}: ${cost}")
        total += cost
    return f"Total: ${total}"

print(create_profile(name="John", age=30, city="New York", job="Engineer"))
print(calculate_total(100, shipping=15, tax=8, insurance=5))
print()

# 7. COMBINING ALL PARAMETER TYPES
print("7. Combining All Parameter Types:")
def process_order(customer_name, *items, discount=0, **customer_info):
    """Function combining all parameter types"""
    print(f"Processing order for: {customer_name}")
    print(f"Items: {', '.join(items)}")
    print(f"Discount: {discount}%")
    print("Customer Info:")
    for key, value in customer_info.items():
        print(f"  {key}: {value}")
    return "Order processed successfully!"

result = process_order(
    "Alice Johnson",           # positional argument
    "laptop", "mouse", "keyboard",  # *args
    discount=10,               # keyword argument
    email="alice@email.com",   # **kwargs
    phone="555-1234",
    address="123 Main St"
)
print(result)
print()

