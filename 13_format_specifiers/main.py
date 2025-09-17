# format_specifiers in python

apples = 42
pi = 3.14159
discount = 0.256
temperature = 23.6789
order_number = 4

# Integer formatting
print(f"I have {apples:d} apples.")
print(f"Locker number in binary: {apples:b}")

# Float Formatting
print(f"Pi rounded to 2 decimals: {pi:.2f}")
print(f"Discount: {discount:.2%}")

# Alignment and Width
print(f"Product | {'Price':>10}")
print(f"Apple   | {50:>10}")
print(f"Banana  | {5:>10}")

# Padding 
print(f"Order Number: {order_number:05d}")
print(f"Title: {'Invoice':-^20}")

