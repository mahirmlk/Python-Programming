# 1. Newline (\n) - Moves to the next line
print("Line 1\nLine 2\nLine 3")  # Prints three lines

# 2. Tab (\t) - Adds horizontal tab spacing
print("Name:\tJohn\nAge:\t25")  # Aligns text with tabs

# 3. Backslash (\\) - Prints literal backslash
print("File path: C:\\Users\\Documents")  # Prints: File path: C:\Users\Documents

# 4. Single quote (\') - Prints single quote in string
print('what a beautiful day')  # Prints: what a beautiful day

# 5. Double quote (\") - Prints double quote in string
print("He said \"Hello!\"")  # Prints: He said "Hello!"

# 6. Carriage return (\r) - Returns to start of line
print("Hello\rWorld")  # Prints: World (overwrites Hello)

# 7. Backspace (\b) - Removes one character before it
print("Hello\bWorld")  # Prints: HellWorld

# 8. Form feed (\f) - Page break
print("Page 1\fPage 2")  # Creates a form feed break

# 9. Octal value (\ooo)
print("\110\145\154\154\157")  # Prints: Hello (in octal)

# 10. Hex value (\xhh)
print("\x48\x65\x6c\x6c\x6f")  # Prints: Hello (in hexadecimal)

# Combining multiple escape sequences
print("Row 1\tColumn 1\nRow 2\tColumn 2")

# Raw strings (ignore escape sequences)
print(r"This \n will \t print exactly \\ as is")

# Common use cases
print("Shopping List:\n\t1. Apples\n\t2. Bananas\n\t3. Oranges")  # Formatted list
print("\"Python\" is a \\ programming \\ language")  # Using quotes and backslashes
print("C:\\new_folder\\test.txt")  # File path example