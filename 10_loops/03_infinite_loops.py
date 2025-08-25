# Example of infinite loops in Python
# Safe version: an 'infinite' loop that breaks after a few iterations

count = 0
print("Example: safe demo (stops after 5 iterations)")
while True:
    count += 1
    print("count =", count)
    time.sleep(0.5)
    if count >= 5:
        print("Breaking to avoid real infinite loop in demo.")
        break


# Notes:
# - True infinite loops are useful for servers, daemons, and event loops.
# - Always provide a clean shutdown mechanism (signal handling or break conditions).
# - To stop an infinite loop running in terminal, use Ctrl+C (KeyboardInterrupt) on