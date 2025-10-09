"""
File writing modes:
'w' - Write (overwrites existing file)
'a' - Append (adds to end of file)
'x' - Create new (fails if file exists)
"""

# Write to file (overwrites if exists)
file = open("output.txt", "w")
file.write("Hello World\n")
file.write("Python is great")
file.close()

# Better way - automatically closes file
with open("output.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")

# Write multiple lines at once
lines = ["Apple\n", "Banana\n", "Cherry\n"]
with open("fruits.txt", "w") as f:
    f.writelines(lines)

# Append to existing file
with open("output.txt", "a") as f:
    f.write("Line 3\n")
    f.write("Line 4\n")

# Write numbers
with open("numbers.txt", "w") as f:
    for i in range(1, 6):
        f.write(f"{i}\n")

# Write dictionary data
data = {"name": "Alice", "age": 25, "city": "Delhi"}
with open("user.txt", "w") as f:
    for key, value in data.items():
        f.write(f"{key}: {value}\n")

# Create file only if it doesn't exist
try:
    with open("new_file.txt", "x") as f:
        f.write("This is a new file")
except FileExistsError:
    print("File already exists")

# Write CSV format
with open("students.csv", "w") as f:
    f.write("Name,Age,Grade\n")
    f.write("John,20,A\n")
    f.write("Emma,22,B\n")

# Write using print function
with open("output.txt", "w") as f:
    print("Hello", file=f)
    print("World", file=f)

# Safe file writing function
def write_to_file(filename, content):
    try:
        with open(filename, "w") as f:
            f.write(content)
        return "Success"
    except Exception as e:
        return f"Error: {e}"

result = write_to_file("example.txt", "Sample content")
print(result)