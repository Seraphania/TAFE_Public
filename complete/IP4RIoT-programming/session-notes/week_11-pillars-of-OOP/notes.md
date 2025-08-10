# Contents
- [Contents](#contents)
- [Week 11/Session 12 - Pillars of OOP](#week-11session-12---pillars-of-oop)
  - [Session Overview](#session-overview)
    - [Summary Card](#summary-card)
  - [Basics](#basics)
  - [The Pillars](#the-pillars)
    - [Preamble](#preamble)
    - [Abstraction](#abstraction)
    - [Polymorphism](#polymorphism)
    - [Inheritance](#inheritance)
    - [Encapsulation](#encapsulation)
  - [Overriding](#overriding)
      - [Note on objects](#note-on-objects)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 11/Session 12 - Pillars of OOP
6/5/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_35877_1&content_id=_3663746_1)

[Raf's Lecture materials](https://github.com/NM-TAFE/civ-ipriot-in-class-demos/tree/2025/s1/raf)

## Session Overview
**Objectives**  
* Review the key principles "pillars" of OOP:
* Encapsulation, Abstraction, Inheritance, and Polymorphism 
* Define their conceptual role and mechanism in Python
* Model fundamental class relationships
* Implement code that employs the pillars in Python

**Curriculum alignment**  
Aligns with the following elements of ICTPRG430
* 2.1 Develop application according to application design and organisational code conventions


**Relevance to industry**  
The four pillars are usually taught as part of the basics of OOP. Historically, some considered them "requirements" for OOP but today we can think of them as guiding principles. Understanding the principles will help you have conversations with peers using industry-appropriate terms as well as write code that that follows core OOP patterns.

**Relevance to assessment**  
The four pillars need to be explicitly discussed in the remaining assessments and are implemented in code samples used in those assessments.  

**How to use this information**  
* Follow the lecture slides and recording if applicable 
* If studying online, it is recommended to attempt the in-class activity before the class, as no time will be given in class for it.


### Summary Card
The following card summarizes the pillars: 
|     Pillar    |        Key Concept       |              General Mechanism             |       Python mechanism                              |
|---------------|--------------------------|--------------------------------------------|-----------------------------------------------------|
| Abstraction   | Interface simplification |       Abstract classes, interfaces         |                  ABC/abstractmethod                 |
| Polymorphism  | Behavioural substitution | Interfaces, duck typing, method overriding | Overriding is all or nothing (no method signatures) |
| Inheritance   |        Code reuse        |            Class hierarchies               |             class Name(Parent1, Parent2)            | 
| Encapsulation |    Information hiding    |     Access modifiers, private fields       |        Single or double underscore prefixes         |
___

"A Pie" is a nice way to remember the words.

## Basics
OOP is basically about **Modularity**, **Reusability**, **Extensibility** and **Maintainability**, as discussed in [week 10](../week_10-introduction-to-OOP/notes.md).  
OOP uses the four pillars to achieve this.  

Languages don't have to follow the pillars perfectly, they are interdependent (meaning sometimes they overlap with eachother). They are more important to keep in mind in statically typed languages.

Staically typed vs dynamically typed: Variable types have to be specified and always retains that type (Static) - eg, java, C++.

Python is Dynamically typed, we can change types on the fly - everything is an object and has a type, but it can be changed.


Python is built around the concepts of OOP, everything in python is an object, and therfore has type. This is useful because once you know how to interact with a type, you can interact with all objects of that type. e.g if you can convert a string to upper case, you can convert all strings to upper case.

**Digression**
* *OOP is probably a solution for problems we don't yet have as students.*
* *Raf recommends learning either python or javascript, and either c# or java, and maybe some C*
* *Browsers are javascript interpreters; javascript is used for the interactivity of websites, html is used for formatting and layout.*
* *Learn more about "frameworks" for example node/react and find out what Rust and Golang are about.*

## The Pillars  
The pillars of OOP overlap heavily and are interdependant. The notes below are not entirely linear!

### Preamble
Example code: bank account:
* What are **attributes** of a bank account? (balance, account name, account number)

```python
class BankAccount:
    balance = 0
    name = ''
    account_number = ''
```
*This code is not syntactically wrong. It's missing an `__init__` method, The code expresses an idea of what attributes bank account has, without implementing anything.*  

*The problem is that it also expresses that all bank accounts should have a balance, and that balance should be 0, all accounts shall have a name, and that name is blank etc. This is stronger than a default, if we change the balance of a bank account that looks like this, it will change the balance for ALL accounts.*

To better express a bank account: 
```python
class BankAccount:
    def __init__(self, name, account_number): # To create a BankAccount, it must have a name and an account number.
        self.name = name
        self.account_number = account_number
        self.balance = 0 # All bank accounts start with a balance of 0

# This is technically a working bank class, accounts can be created, and balances u8pdated:
raf = BankAccount("Raf's Account", "12345")
alex = BankAccount("alex's Account", "12346")

# Deposits
raf.balance += 1000
alex.balance += 100
print("Raf's Balanmce:", raf.balance)
print("alex's Balanmce:", alex.balance)
alex.balance += 42
print("alex's Balanmce:", alex.balance)
```
*Again, while valid, this is not robust, any deletion in the transaction history means that the balance does not reflect reality*  

*There is also the potential to have to make lots of rules: Should we prevent negative balances, what about checking that the balance is valid and not "$$$$". If it is decided that balances aren't allowed to be negative, this could be checked every transaction, but you would have to look though all the code to see where it happened.*

Instead we create methods (*methods are just what functions are called when they are part of a class*) to handle things like updating the balance:
```python
class BankAccount:
    def __init__(self, name, account_number): 
        self.name = name
        self.account_number = account_number
        self.balance = 0

    # encapsulation - protecting a value/state from external updates
    def update_balance(self, value):
        if self.balance + value < 0:
            raise ValueError("Insufficinet Funds")
        self.balance += value

raf = BankAccount("Raf's Account", "12345")
raf.update_balance(1000)
print(raf.balance)
raf.update_balance(-1300)
print(raf.balance)
raf.balance += 1000 # This still works
```
*This is better, but it doesn't stop people updating the balance without using the method*

In OO languages, there are things called access modifiers, they can make things protected or private. In compiled languages, an access modifier would trigger an error if someone tried to update something protected.  

Python does not have access modifiers, instead there is a strong convention:  
`_protected` and `__private`.

This tells anyone working with the code that you *should not* (not *can not*) update that object outside of the class. It doesn't stop it from happening, it is just a warning.  

If using __private it can't be directly accessed by subclasses, however it still can be by referencing the super class. Not relevant for TAFE. See name mangling for more information.  

Trying to restrict or protect how parts of te program are accessed is an example of [encapsulation](#encapsulation).
```python
class BankAccount:
    def __init__(self, name, account_number): 
        self.name = name
        self.account_number = account_number
        self._balance = 0

    # encapsulation - protecting a value/state from external updates
    def update_balance(self, value):
        if self._balance + value < 0:
            raise ValueError("Insufficinet Funds")
        self._balance += value

raf = BankAccount("Raf's Account", "12345")
raf.update_balance(1000)
print(raf._balance)

raf._balance += 1000 # This *still* works!
print(raf._balance)
```
*This is once again better, however it isn't explicit about whether a transaction is a withdrawal or a deposit, users must know what whethere `+` or `-` means withdrawal or deposit.*

Seperate methods for withdrawal and deposit:
```python
class BankAccount:
    def __init__(self, name, account_number): 
        self.name = name
        self.account_number = account_number
        self._balance = 0

    # abstraction exposing functionaliity
    def withdraw(self, value):
        if value <= 0:
            raise ValueError("Amount must be positive")
        if value > self._balance:
            raise ValueError("Insufficient Funds")
        self._balance -= value
        ...

    def deposit(self, value):
        if value <= 0:
            raise ValueError("Amount must be positive")
        self._balance += value
        ...
```
*This approach is more modular and explicit, it makes it easier to re-apply to other account types, for example credit vs debit, both approaches are [encapsualtion](#encapsulation), but the second approach is a better [abstraction](#abstraction)*


### Abstraction  
Abstraction is about exposing the functionaity of something, exposing it as simply as possible. Easy to confuse with [encapsulation](#encapsulation), however abstraction is about hiding the implementation and just exposing the functionality in the simplest way possible. 

For example the "Start" button in newer cars; it doesn't matter what the engine or transmission type is, or the internal mechanics of starting the car, in any car, the button makes the car start, the driver dosn't have to worry about what sort of car it is (electric, combustion etc).

This is not just for ease of use, it can also make things more generalisable - once you know how to press start, you can start any car.

This is not always a good thing, too much abstraction can make it harder to diagnose why something won't work, it is important to choose the correct level of abstraction.

*Think: Abstraction = Simplification*

Using the Animal superclass example from [polymorphism](#polymorphism), in this scenario, there would never be a reason to create an "animal", only objects of type animal (Cat and Dog).  

There is also really no way that an "animal" would speak, a cat might speak, and a dog might speak, but the abstract "animal" does not

All animals should be able to speak, but there is no need to define how, we also don't ever want to instantiate an "Animal":
```python
from abc import ABC, abstractmethod # Abstract base class

class Animal(ABC): #inherits from ABC - is abstract
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0
    
    @abstractmethod # Decorator - lets us know when we stuff up
    def speak(self): # Animals MUST have their own speak method
        ... # all animals can speak, but how does not need to be defined here.

class Cat(Animal): # inheritance
    def speak(self): # polymorphism
        print(f"{self.name} meows")

c = Cat("Tex", "Orange")
c.speak() # This is fine it is also abstraction

a = Animal("WTF", "Monstrous") # Error
a.speak() # Error
# Can't instantiate abstract class Animal without an implementation for abstract method 'speak'
```
*Now we CAN'T instantiate an "Animal", without getting an error, as intended*

Similar to abstract classes are interfaces; an interface is a blueprint for classes. As with abstract classes, an interface cannot be instantiated, and also  can't include implementations of methods.  

In python interfaces aren't strictly defined, so we can have abstract classes with non-abstract methods, however an abstract class with only abstract methods would be considered an interface.

### Polymorphism
Polymorphism is saying the same thing but getting different behaviour.

Using the example of Cat and Dog classes that [inherit](#inheritance) from the Animal class; all animals speak, but they do so differently.
```python
class Animal:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0
    
    def speak(self):
        print(f"I am an animal") # this is the default

class Cat(Animal):
    # polymorphism
    def speak(self):
        print(f"{self.name} meows") # Overriding

class Dog(Animal):
    def speak(self):
        print(f"{self.name} woof woofs")
```
* If a method has the same name as it's parent the bahaviour is [overidden](#overriding), cat will no longer say "I am animal" when they speak*  
* *The animal class is an [abstraction](#abstraction).*

### Inheritance
Inheritance intitally tried to solve the problem of repetition, in the example below, both the classes `Cat` and `Dog` have the same attributes.
```python
class Cat
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0 # Cats start as newborn kittens!

    def meow(self):
        print(f"{self.name} meows") # abstraction

class Dog
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0

    def bark(self):
        print(f"{self.name} woof woofs")
```
*to avoid repetition, we can combine that information into an "Animal" class - this is an example of a (superclass).*

Create an animal class, and then tell Python that Cat and Dog are *types* (classes) of Animal. All animals have a name, age and coat, but only cats meow and only dogs bark - this is inheritance.
```python
class Animal:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0

class Cat(Animal):
    def meow(self):
        print(f"{self.name} roars")

class Dog(Animal):
    def bark(self):
        print(f"{self.name} woof woofs")

# Add a subclass of the subclass Cat
class DomesticCat(Cat):
    def meow(self):
        print(f"{self.name} meows")
```
*Repetition is not in itself a reason to create a superclass, but it is a sign you might want one, the best way to decide is using the **semantic test**: A cat "is a" animal, if the answer is no, then don't use inheritance.*

*The DomesticCat subclass is not preferred, when creating heirarchies, they should be kept shallow*

It is also possible to inherit from multiple classes:
```python
class Pet:
    def show_loyalty(self):
        print("I love you")

class Animal:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0

class Cat(Animal, Pet): # Cats are animals and also pets
    def meow(self):
        print(f"{self.name} roars")

class Dog(Animal): # Dogs are animals but not pets
    def bark(self):
        print(f"{self.name} woof woofs")
```
*This is fine, but a stronger statement would be that all animals speak, but they speak differently see [polymorphism](#polymorphism).*

Inheritance is considered to be largely a bad idea today, it can lead cause 'tight-coupling' - when groups of classes are highly dependent on eachother.

It is preferred to only inherit from [abstract](#abstraction) classes or interfaces. It is only desirable to instantiate children, not parents.

### Encapsulation
Encapsulation is setting boundaries around how things can be modified within a program. In the [banking app](#preamble) above, we isolated how parts of the class can be accessed, and only expose what needs to be exposed. This is simiolar to [abstraction](#abstraction) but is more focused on protection, than making things easy to use.

*Think: Encapsulation = Protection (by hiding)*

## Overriding
In Python overriding is all or nothing, If a method has the same name as its parent the bahaviour is overidden. As in the example from [polymorphism](#polymorphism) A cat will no longer say "I am animal" when they speak. 

Sometimes it is necessary to have a class that does what the parent does, but with some unique attributes or behaviours. For example if a Cat is a Subclass of animal as below (from the example in [abstraction](#abstraction)), and all cats have 9 lives, it must be initialised differently to Animal:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0
    
    @abstractmethod 
    def speak(self):
        ....

class Cat(Animal):
    def __init__(self, coat, name):
        self.lives = 9
        ... # all or nothing
```
*Now it no longer does anything that is in the Animal class `__init__`, so everything from the animal class also has to be re-implemented*

To get around that, we can call the superclass method using the `super()` function. This allows any method from the super class to be called:
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat
        self.age  = 0
    
    @abstractmethod 
    def speak(self):
        ....

class Cat(Animal):
    def __init__(self, coat, name):
        super().__init__(name, coat)
        self.lives = 9
```
*Now the Cat class has all the attributes initialised from the Animal class, as well as it's own unique 'lives' attribute*

It is possible to use `super()` to call ANY method from a parent, but `__init__` is the most common. If things are getting too compliced with `super()` it may be an indication that inheritance shouldn't be used.

#### Note on objects
As discussed previously, EVERYTHING in python is an object, meaning that everything inherits ffrom a class called object. in older versions of Python, that had to be made explicit, so a base class would be declred as `class Animal(object):` that is no longer required, but it may be seen in older code.

## Resources
[Lecture Slides](./resources/ipriot-pillars-of-OO-2.O.pptx)  
[PDF: Pillars of OOP](./resources/Session-6-Pillars-of-OO.pdf)  
[PDF: Object Oriented Python_Chapter2](./resources/ObjectOrientedPython_Chapter2.pdf)  
[Video: Python Object Oriented Programming (OOP) - For Beginners](https://www.youtube.com/watch?v=JeznW_7DlB0)  
[Video: Object Orientated Project](https://www.youtube.com/watch?v=lbXsrHGhBAU)  

## Activities
[In-class activity](./activities/class-activities.md)  
[In-class complete](./activities/class-activities.py) 
[In-class advanced complete](./activities/class-activities-advanced.py) 