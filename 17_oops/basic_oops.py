"""
OOP (Object-Oriented Programming) organizes code into classes and objects.
Class: Blueprint for creating objects
Object: Instance of a class

"""

# Basic class
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        return f"{self.name} says Woof!"

dog1 = Dog("Buddy", 3)
print(dog1.bark())
print(f"{dog1.name} is {dog1.age} years old")

# Inheritance
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

cat = Cat("Whiskers")
print(cat.speak())

# Class variables vs instance variables
class Car:
    wheels = 4  # Class variable (shared by all)
    
    def __init__(self, brand):
        self.brand = brand  # Instance variable

car1 = Car("Toyota")
car2 = Car("Honda")
print(f"{car1.brand} has {Car.wheels} wheels")

# Encapsulation (private attributes)
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(f"Balance: ${account.get_balance()}")

# Polymorphism
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(4)]
for shape in shapes:
    print(f"Area: {shape.area()}")

# Magic methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} ({self.pages} pages)"
    
    def __len__(self):
        return self.pages

book = Book("Python Guide", 350)
print(book)
print(f"Length: {len(book)}")

