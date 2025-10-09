import random

# PYTHON RANDOM NUMBERS

print("Random float (0.0-1.0):")
print(random.random())

print("\nRandom integer (1-6):")
print(random.randint(1, 6))

print("\nRandom float (15.0-30.0):")
print(random.uniform(15.0, 30.0))

print("\nRandom choice from list:")
fruits = ["apple", "banana", "cherry", "date"]
print(random.choice(fruits))

print("\nRandom sample (3 unique items):")
print(random.sample(fruits, k=3))

print("\nShuffle list:")
deck = ["A", "K", "Q", "J", "10"]
random.shuffle(deck)
print(deck)

print("\nWeighted random choice:")
items = ["Common", "Rare", "Epic"]
weights = [70, 25, 5]
print(random.choices(items, weights=weights, k=1)[0])

print("\nRandom password:")
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
print(''.join(random.choices(chars, k=12)))

print("\nCoin flips (10 times):")
flips = [random.choice(["H", "T"]) for _ in range(10)]
print(flips)