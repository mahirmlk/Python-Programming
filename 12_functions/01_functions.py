# Python Functions

# 1. DEFINING A SIMPLE FUNCTION
def say_hello():
    """A simple function that prints a message"""
    print("Hello from the function!")

# Calling the function
say_hello()
print()

# 2. FUNCTION WITH RETURN VALUE
def get_greeting():
    """A function that returns a value"""
    return "Hello, World!"

# Store the returned value
message = get_greeting()
print(f"Returned message: {message}")
print()

# 3. FUNCTION THAT PERFORMS CALCULATIONS
def calculate_area():
    """Calculate area of a rectangle with fixed dimensions"""
    length = 10
    width = 5
    area = length * width
    return area

result = calculate_area()
print(f"Area of rectangle: {result}")
print()

# 4. FUNCTION WITH LOCAL VARIABLES
def process_data():
    """Function demonstrating local variables"""
    number1 = 15
    number2 = 25
    total = number1 + number2
    average = total / 2
    return average

avg = process_data()
print(f"Average: {avg}")
print()

# 5. MULTIPLE FUNCTIONS WORKING TOGETHER
def get_square():
    """Returns square of 7"""
    return 7 * 7

def get_cube():
    """Returns cube of 3"""
    return 3 * 3 * 3

def combine_results():
    """Combines results from other functions"""
    square = get_square()
    cube = get_cube()
    return square + cube

final_result = combine_results()
print(f"Square of 7: {get_square()}")
print(f"Cube of 3: {get_cube()}")
print(f"Combined result: {final_result}")
print()

# 6. FUNCTION THAT CALLS ITSELF 
def display_info():
    """Function that calls other functions to display info"""
    title = get_title()
    content = get_content()
    print(f"{title}")
    print(f"{content}")

def get_title():
    return "=== REPORT ==="

def get_content():
    return "This is the content of the report."

display_info()
print()

