# Basic of for-loop in Python

# 1) Simple iteration over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  

# 2) Using range() to iterate numeric sequences
for i in range(5):     
    print(i)

for i in range(1, 6):  
    print(i)

# 3) range() with step
for i in range(0, 10, 2):  
    print(i)

# 4) enumerate() gives index and value (useful when you need position)
players = ["Rahul", "Jaiswal", "Virat"]
for playing_eleven, name in enumerate(players, start=1):
    print(playing_eleven, name) 

# 5) Iterating over a string (character by character)
for ch in "hello":
    print(ch)
    


