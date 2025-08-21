## Exercises
# 1. Create a class `Shape` with an abstract method `area`. Create two subclasses `Circle` and `Rectangle` that inherit from `Shape`. Implement the `area` method for each subclass.
from abc import ABC, abstractmethod
from math import pi

class Shape():
    def __init__(self, colour):
        self.colour = colour # if set will ovveride unless specified in subclass __init__

    @abstractmethod
    def area(self):
        ...

class Circle(Shape):
    def __init__(self, radius, colour):
        super().__init__(colour)
        self.colour = "pink" # Overrides super
        self.radius = radius

    def area(self):
        area = pi * (self.radius ** 2)
        return area

class Rectangle(Shape):
    def __init__(self, length, width, colour="yellow"): # sets default colour to yellow inless specified
        super().__init__(colour)
        self.length = length
        self.width = width

    def area(self):
        area = self.length * self.width
        return area
    
c = Circle(3, "green")
print(f"{c.colour} Circle area: {c.area()}")

r = Rectangle(5, 3)
print(f"{r.colour} Rectangle Area: {r.area()}")

r2 = Rectangle(4, 2, colour="Blue")
print(f"{r2.colour} Rectangle Area: {r2.area()}")

# Output:
# pink Circle area: 28.274333882308138
# yellow Rectangle Area: 15
# Blue Rectangle Area: 8

# 2. Create a `BankAccount` class with private attributes for `account_number` and `balance`. Implement methods to `deposit`, `withdraw`, and view the current `balance`.
class BankAccount():
    def __init__(self, account_number):
        self._account_number = account_number
        self._balance = 0

    def deposit(self, value):
        if value <=0:
            print("Deposit amount must be positive")
        self._balance += value

    def withdraw(self, value):
        if value <=0:
            print(" Withdrawal amount must be positive")
        elif self._balance - value <= 0:
            print("Insufficient Funds")
        self._balance -= value

    def view_balance(self):
        print(f"Current balance for {self._account_number} is ${self._balance}")

account = BankAccount(12345)
print(f"Welcme to PyBank!\nNew acocunt created. Account number is {account._account_number}")
activity = "y"
while True:
    if activity == 'y':
        print("would you like to\n[1] Make a Deposit\n[2] Make a Withdrawal\n[3] View Current Balance")
        task = input("Please enter 1, 2 or 3: ")
        if task == '1':
            account.deposit(int(input("Enter deposit amount: ")))
            activity = input("Would you like to continue? y/n: ")
        elif task == '2':
            account.withdraw(int(input("Enter withdrawal amount: ")))
            activity = input("Would you like to continue? y/n: ")
        elif task == '3':
            account.view_balance()
            activity = input("Would you like to continue? y/n: ")
    else:
        print("Thank you for using PyBank Services")
        exit()