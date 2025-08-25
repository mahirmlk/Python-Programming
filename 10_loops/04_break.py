# break in a loop

# Loop numbers 1 to 10, stop when we reach 5
for i in range(1, 11):
    print("i =", i)
    if i == 5:
        print("Reached 5 — breaking out of the loop.")
        break