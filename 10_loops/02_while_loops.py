# Basic of while-loop in Python

# 1) Simple counter loop
i = 0
while i < 5:           
    print("count:", i) 
    i += 1             


# 2) Summing numbers (accumulator pattern)
total = 0
n = 1
while n <= 5:         
    total += n
    n += 1
print("Sum 1..5 =", total)  


# 3) Using continue and break
n = 0
while n < 10:
    n += 1
    if n % 2 == 0:
        continue      
    if n == 7:
        print("Reached 7, breaking out.")
        break           
    print("Odd number:", n)  


# 4) while-else: else runs only if loop didn't hit break
x = 0
while x < 3:
    print("x =", x)
    x += 1
else:
    print("Loop completed without break")


