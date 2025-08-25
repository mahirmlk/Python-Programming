# Match-Case Statement (Available in Python 3.10+)
# Day of week example
day_number = 3

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")  # This will execute
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:  # Multiple values in one case
        print("Weekend!")
    case _:  # Default case (like else)
        print("Invalid day number")

# HTTP status code example
status_code = 404

match status_code:
    case 200:
        print("OK - Success")
    case 404:
        print("Not Found")  # This will execute
    case 500:
        print("Internal Server Error")
    case code if code >= 400:  # Guard condition
        print("Client/Server Error")
    case _:
        print("Unknown status")

# Grade letter example with conditions
grade = 'B'

match grade:
    case 'A' | 'A+':
        print("Excellent!")
    case 'B' | 'B+':
        print("Good job!")  # This will execute
    case 'C':
        print("Average")
    case 'D' | 'F':
        print("Needs improvement")
    case _:
        print("Invalid grade")
