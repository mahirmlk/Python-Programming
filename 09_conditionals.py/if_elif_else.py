# If-Elif-Else Statement 
# Grade classification example
marks = 85

# Multiple conditions checked in order
if marks >= 90:
    print("Grade: A+")               # Won't execute
elif marks >= 80:
    print("Grade: A")                # This will execute
    print("Excellent performance!")
elif marks >= 70:
    print("Grade: B")                # Won't execute (already found match)
elif marks >= 60:
    print("Grade: C")                # Won't execute
else:
    print("Grade: F")                # Won't execute
    print("Need improvement")

# Traffic light example
light_color = "yellow"

if light_color == "red":
    print("Stop!")
elif light_color == "yellow":
    print("Caution - prepare to stop")  # This will execute
elif light_color == "green":
    print("Go!")
else:
    print("Invalid light color")

# Age category example
age = 25

if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 60:
    print("Adult")                   # This will execute
else:
    print("Senior")
