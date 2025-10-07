# 2D Collections in Python

# Creating a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original matrix:")
print(matrix)

print()
for row in matrix:
    print(row)


# Accessing elements

print("Element at row 0, col 1:", matrix[0][1])
print("Element at row 2, col 2:", matrix[2][2])


# Creating empty 2D list

rows, cols = 3, 4
empty_matrix = [[0 for j in range(cols)] for i in range(rows)]

for row in empty_matrix:
    print(row)


# Modifying elements
matrix[0][0] = 100
matrix[1][1] = 200

for row in matrix:
    print(row)


# Iterating through all elements

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(f"[{i}][{j}] = {matrix[i][j]}")


# Simple way to iterate

for row in matrix:
    for element in row:
        print(element, end=" ")
    print()


# Common operations

# 1. Getting a Row 
first_row = matrix[0]
print("First row:", first_row)


# 2. Getting a Column
second_col = [row[1] for row in matrix]
print("Second column:", second_col)


# Practical example: Players Scores

runs = [
    [85, 90, 78],
    [92, 88, 95],
    [70, 85, 80]
]

players = ["Virat", "Rahul", "Jaiswal"]
Innings = ["Perth", "MCG", "Oval"]

print("Scored runs:")
for i, player in enumerate(players):
    print(f"{player}: {runs[i]}")

print("\nAverage per player:")
for i, player in enumerate(players):
    avg = sum(runs[i]) / len(runs[i])
    print(f"{player}: {avg:.2f}")

print("\nAverage per Innings:")
for j, Inning in enumerate(Innings):
    Innings_grades = [runs[i][j] for i in range(len(runs))]
    avg = sum(Innings_grades) / len(Innings_grades)
    print(f"{Inning}: {avg:.2f}")


# 2D list with mixed data

data = [
    ["John", 25, "Engineer"],
    ["Sarah", 30, "Doctor"],
    ["Mike", 28, "Teacher"]
]

for person in data:
    name, age, job = person
    print(f"{name} is {age} years old and works as a {job}")