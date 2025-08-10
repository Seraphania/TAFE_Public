# Contents
- [Contents](#contents)
- [Week 1/Session 1 \& 2 - Into to Programming and Variables and Expressions](#week-1session-1--2---into-to-programming-and-variables-and-expressions)
  - [Intro to Programming](#intro-to-programming)
    - [Employment Options](#employment-options)
    - [How to learn to program](#how-to-learn-to-program)
  - [Variables and Expressions](#variables-and-expressions)
    - [Exercise:](#exercise)
    - [variables vs literals:](#variables-vs-literals)
    - [pye4e](#pye4e)
  - [Glossary](#glossary)
  - [Resources](#resources)
  - [Activities](#activities)


# Week 1/Session 1 & 2 - Into to Programming and Variables and Expressions

## Intro to Programming
* Programming is hard, long hours and commitment to practice.
  * Can suck if you're not interested
* Always keep learning
  * Is rarely routine, often disruptions
  * Job is to find things that are boring/repetitive and make them easier
* Not great job security
  * Partially because devs are expensive
  * Devs often hired in optimistic times, let go early
  * Perth a little better than average
* Good job availability and income
  * Perth a little worse than average
* Relies on social and communication skills more than expected
  * You have to deal with people still :(
  * Need some (easy) [maths](https://k10outline.scsa.wa.edu.au/home/assessment/snap-shots-choose-a-year/year-10/mathematics)

*Programming can open a lot of doors in interesting industries, gives you a good foundation in logic and reasoning.*

### Employment Options
*Cert IV won't make you job ready... probably*  
Open source participation is really important.  
Build contacts amongst classmates.  
Vendor certifications are well regarded, O'reilly has a lot of good sample tests for these:
  https://www.oreilly.com/member/login/  


### How to learn to program
* Requires consistency, curosity and drive
* More like learning an instrument
* Everything builds on everything else
* Is frustrating
* Everyone learns at a different rate

*Practice writing code in full, don't use autofill.*
____

## Variables and Expressions
An expression is a statement that is evaluated. Expressions may include combinations of values, variables operators and calls to functions.
```python
(3+2) * 5 + 4 / 2
```

### Exercise:  
work out monthly take-home pay:
```python
pay = int(input("What is your gross annual salary?: "))
tax = 0.30
monthly = (pay * tax)/12
print("Your take-home pay is", monthly, "Per month, you really should be paid more for comedy")
```
interactive python (IDLE) doesn't require print statements which is handy.

* `//` is floor division (nearest whole divisor)
* `=` is the assignment operator  
  
evaluate the expression on the right of the = and assign it to the left

Operators in Python behave according to the type  
Anything in quotes is a string, changing types is not called casting?

### variables vs literals:  
`string = 5` : string is a variable  
`10 = 5` : 10 can't be a variable because it is a literal (variable names can't start with a number).

Python does not do well with float precision.
```python
0.1 + 0.1 + 0.1
                   
0.30000000000000004
```

### pye4e
* py4e uses the term constant to refer to literal values: "hello", 42, 42.0, etc. However, for the majority of this course, we will use the more technical definition of constants: a constant is a variable whose value doesn't change and isn't expected to change during the execution of a program whereas the value referenced by a variable will be called a literal. For example, consider the variable PI = 3.141592654 we will refer to the variable "PI" as a constant (it doesn't make sense for us to ever change the value of 𝝅), the value 3.14... as a literal. In the py4e course, you may see "PI" referred to as a variable (which it is) and the value 3.14 as a constant.  Test yourself and review the material here: PY4E - Python for Everybody - VES Reference material: https://books.trinket.io/pfe/02-variables.html  Additional references Learn more about variable names

**Complete AT1 questions 6-10**

## Glossary
* **Assignment:** A statement that assigns a value to a variable.
* **Concatenate:** To join two operands end to end.
* **Comment:** Information in a program that is meant for other programmers (or anyone reading the source code) and has no effect on the execution of the program.
* **Evaluate:** To simplify an expression by performing the operations in order to yield a single value.
* **Expression:**  A combination of variables, operators, and values that represents a single result value.
* **Floating point:** A type that represents numbers with fractional parts.
* **Integer:** A type that represents whole numbers.
* **Keyword:** A reserved word that is used by the compiler to parse a program; you cannot use keywords like if, def, and while as variable names.
* **Mnemonic:** A memory aid. We often give variables mnemonic names to help us remember what is stored in the variable.
* **Modulus operator:** An operator, denoted with a percent sign (%), that works on integers and yields the remainder when one number is divided by another.
* **Operand:** One of the values on which an operator operates.
* **Operator:** A special symbol that represents a simple computation like addition, multiplication, or string concatenation.
* **Rules of precedence:** The set of rules governing the order in which expressions involving multiple operators and operands are evaluated.
* **Statement:** A section of code that represents a command or action. So far, the statements we have seen are assignments and print expression statement.
* **String:** A type that represents sequences of characters.
* **Type:** A category of values. The types we have seen so far are integers (type int), floating-point numbers (type float), and strings (type str).
* **Value:** One of the basic units of data, like a number or string, that a program manipulates.
* **Variable:** A name that refers to a value.

## Resources
***Intro to programming***  
[Lecture Slides](./resources/ICTPRG302-Introduction-to-Programming-S1.pdf)  
[Glossary](./resources/glossary.md)  
[Computer Science Fundamentals - Brilliant (free with signup)](https://brilliant.org/courses/computer-science-algorithms/)  
[Installing Python](https://www.py4e.com/lessons/install)  
[Why Program?](https://www.py4e.com/lessons/intro)  

***Variables and expresions***  
[Lecture Slides](./resources/ICTPRG302-Variables-Expressions-S2.pdf)  
[Python Variables](https://www.w3schools.com/python/python_variables.asp)  
[Python User Input](https://www.w3schools.com/python/python_user_input.asp)  
[PY4E - Variables expressions and statements](https://www.py4e.com/lessons/memory)  
[Test yourself](./resources/test-yourself.md)

## Activities
***Intro to programming***  
[Ceaser Cipher Activity](./activities/ceaser-cipher.md)  
[Ceaser Cipher Complete](./activities/ceaser-cipher.py)  

[Mary Had a LIttle Lamb Activity](./activities/mary-had-a-little-lamb.md)  
[Mary Had a LIttle Lamb Complete](./activities/mary-had-a-little-lamb.py) 


***Variables and expresions***  
[Mary Had a LIttle Lamb Personalised Activity](./activities/mary-had-a-little-lamb-2.md)  
[Mary Had a LIttle Lamb Personalised Complete](./activities/mary-had-a-little-lamb-2.py)  

[Toast Activity](./activities/toast.md)  
[Toast Complete](./activities/toast.py)  
