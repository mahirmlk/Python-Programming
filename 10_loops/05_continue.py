# continue in a loop
for i in range(1, 11):
    if i % 2 == 0:
        # Skip even numbers and continue with next iteration
        continue
    print("Odd i =", i)  # prints 1, 3, 5, 7, 9

print("Loop finished.")