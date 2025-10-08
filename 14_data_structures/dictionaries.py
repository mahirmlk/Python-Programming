# Python Dictionary - A collection of key-value pairs

# 1. Creating a dictionary
student = {
    "name": "Andrew",
    "age": 20,
    "grade": "A",
    "courses": ["Math", "Physics", "Computer Science"]
}

print("Student dictionary:", student)
print()

# 2. Accessing values
print("Student name:", student["name"])
print("Student age:", student["age"])
print()

# 3. Adding new items
student["email"] = "alice@example.com"
print("After adding email:", student)
print()

# 4. Updating values
student["age"] = 21
print("After updating age:", student)
print()

# 5. Removing items
del student["grade"]
print("After removing grade:", student)
print()

# 6. Checking if key exists
if "name" in student:
    print("Name exists in dictionary")
print()

# 7. Getting all keys and values
print("All keys:", list(student.keys()))
print("All values:", list(student.values()))
print()

# 8. Looping through dictionary
print("Looping through key-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")
print()

# 9. Using get() method (safer way to access)
email = student.get("email", "No email found")
phone = student.get("phone", "No phone found")
print("Email:", email)
print("Phone:", phone)
print()

# 10. Creating an empty dictionary and adding items
inventory = {}
inventory["apples"] = 50
inventory["bananas"] = 30
inventory["oranges"] = 40
print("Inventory:", inventory)