"""
Instance method: Needs self, can access instance and class data
Class method: Uses @classmethod, gets cls, can access class data
Static method: Uses @staticmethod, no self/cls, like a regular function

"""

class Employee:
    company = "TechCorp"
    bonus_rate = 0.1
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    # Instance method (accesses instance data)
    def get_salary(self):
        return f"{self.name} earns ${self.salary}"
    
    # Class method (accesses class data, can modify it)
    @classmethod
    def set_bonus_rate(cls, rate):
        cls.bonus_rate = rate
    
    @classmethod
    def from_string(cls, emp_str):
        name, salary = emp_str.split('-')
        return cls(name, int(salary))
    
    # Static method (doesn't need class or instance)
    @staticmethod
    def is_workday(day):
        return day not in ['Saturday', 'Sunday']

# Instance method usage
emp1 = Employee("Alice", 50000)
print(emp1.get_salary())

# Class method usage - alternative constructor
emp2 = Employee.from_string("Bob-60000")
print(emp2.get_salary())

# Class method - modifying class variable
Employee.set_bonus_rate(0.15)
print(f"New bonus rate: {Employee.bonus_rate}")

# Static method usage
print(f"Is Monday workday? {Employee.is_workday('Monday')}")
print(f"Is Sunday workday? {Employee.is_workday('Sunday')}")

# Practical example
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    
    # Class method - alternative constructor
    @classmethod
    def from_string(cls, date_str):
        y, m, d = map(int, date_str.split('-'))
        return cls(y, m, d)
    
    @classmethod
    def today(cls):
        return cls(2025, 10, 9)
    
    # Static method - utility function
    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    
    def display(self):
        return f"{self.year}-{self.month:02d}-{self.day:02d}"

date1 = Date(2024, 12, 25)
print(date1.display())

date2 = Date.from_string("2023-06-15")
print(date2.display())

date3 = Date.today()
print(date3.display())

print(f"Is 2024 leap year? {Date.is_leap_year(2024)}")
print(f"Is 2023 leap year? {Date.is_leap_year(2023)}")