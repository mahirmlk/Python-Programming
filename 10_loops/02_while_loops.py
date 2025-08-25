# Basic of while-loop in Python

# 1) Simple counter loop
i = 0
while i < 5:           # loop runs while condition is True
    print("count:", i) # prints 0,1,2,3,4
    i += 1             # increment to avoid infinite loop

print("---")

# 2) Summing numbers (accumulator pattern)
total = 0
n = 1
while n <= 5:          # sum first 5 natural numbers
    total += n
    n += 1
print("Sum 1..5 =", total)  # prints 15

print("---")


# 3) Using continue and break
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue        # skip even numbers
    if n == 7:
        print("Reached 7, breaking out.")
        break           # exit loop early
    print("Odd number:", n)  # prints 1,3,5 then stops at 7

print("---")

# 4) while-else: else runs only if loop didn't hit break
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("Loop completed without break")

print("---")

