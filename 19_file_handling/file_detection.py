"""
File detection checks if files/directories exist and their properties.
os.path: Basic file operations
pathlib: Modern, object-oriented approach
"""

import os
from pathlib import Path

file_path = r"C:\Users\DELL\Documents\Python-Programming\19_file_handling\test.txt"

# Does the file exist?
print(os.path.exists(file_path))  # True or False

# Is it a file?
print(os.path.isfile(file_path))  # True if file exists

# Is it a folder?
print(os.path.isdir("my_folder"))  # True if folder exists

# Get file size in bytes
if os.path.exists(file_path):
    print(f"Size: {os.path.getsize(file_path)} bytes")

# Get file name and extension
filename = "report.pdf"
name, extension = os.path.splitext(filename)
print(f"Name: {name}")        # report
print(f"Extension: {extension}")  # .pdf

print("\n--- Modern way using Path ---\n")

# Check if file exists
file = Path("")
print(f"Exists? {file.exists()}")

# Get file info
if file.exists():
    print(f"Is file? {file.is_file()}")
    print(f"Size: {file.stat().st_size} bytes")
    print(f"Name: {file.name}")
    print(f"Extension: {file.suffix}")

# Find all .txt files
for txt in Path(".").glob("*.txt"):
    print(f"Found: {txt.name}")

# Simple function to check files
def check_file(filepath):
    f = Path(filepath)
    if f.is_file():
        return "File exists"
    elif f.is_dir():
        return "This is a folder"
    else:
        return "Not found"

print(check_file(""))
print(check_file("my_folder"))
print(check_file("missing.txt"))