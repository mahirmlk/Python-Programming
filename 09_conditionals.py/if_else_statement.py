# If-Else Statement 
# Variable for demonstration
number = -5

# If-else provides two paths of execution
if number > 0:
    print("The number is positive")    # Won't execute
else:
    print("The number is not positive")  # This will execute

# Another example with user input simulation
balance = 500
withdrawal = 600

if withdrawal <= balance:
    print("Withdrawal successful")
    print(f"Remaining balance: {balance - withdrawal}")
else:
    print("Insufficient funds")       # This will execute
    print(f"Current balance: {balance}")

# Boolean condition example
is_weekend = True

if is_weekend:
    print("Time to relax!")          # This will execute
else:
    print("Time to work!")
