# Indexing in python

# String indexing
s = "Python"
print("s =", s)
print("s[0] ->", s[0])      # 'P' first character
print("s[1] ->", s[1])      # 'y'
print("s[-1] ->", s[-1])    # 'n' last character (negative index)
print("s[-2] ->", s[-2])    # 'o' second last character
print("last char using len:", s[len(s)-1])  # same as s[-1]

# List indexing
lst = [10, 20, 30, 40, 50]
print("\nlst =", lst)
print("lst[0] ->", lst[0])    # 10
print("lst[2] ->", lst[2])    # 30
print("lst[-1] ->", lst[-1])  # 50 (negative index)
print("lst[-3] ->", lst[-3])  # 30 (third from the end)


# Out-of-range index handling
try:
    print("\ns[100] ->", s[100])
except IndexError as e:
    print("IndexError (example):", e)


# - Positive indices start at 0 from the left.
# - Negative indices start at -1 from the right.
# - Use len(seq) when you need the last index programmatically.
