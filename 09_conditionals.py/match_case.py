# Match-Case Statement 

# Day of week example
day_number = 3

match day_number:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6 | 7:  
        print("Weekend!")
    case _:  
        print("Invalid day number")

# HTTP status code example
status_code = 404

match status_code:
    case 200:
        print("OK - Success")
    case 404:
        print("Not Found")  
    case 500:
        print("Internal Server Error")
    case code if code >= 400:  
        print("Client/Server Error")
    case _:
        print("Unknown status")

# Grade letter example with conditions
grade = 'B'

match grade:
    case 'A' | 'A+':
        print("Excellent!")
    case 'B' | 'B+':
        print("Good job!")  
    case 'C':
        print("Average")
    case 'D' | 'F':
        print("Needs improvement")
    case _:
        print("Invalid grade")
