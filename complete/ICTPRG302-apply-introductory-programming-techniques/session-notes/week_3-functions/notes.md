# Contents
- [Contents](#contents)
- [Week 3/Session 5 - Functions (and revisiting loops)](#week-3session-5---functions-and-revisiting-loops)
    - [For loops](#for-loops)
    - [Functions](#functions)
  - [Resources](#resources)
  - [Activities](#activities)


# Week 3/Session 5 - Functions (and revisiting loops)
In this session, we're going to explore the world of Python Functions.  
Functions are a fundamental building block in programming, allowing us to write reusable and organised code. You'll learn how to define and call functions and return values.  

**This session will provide you with the skills and knowledge required to:**  
* 2.1 Apply basic language syntax rules: Understand the syntax for defining and using functions in Python.
* 2.4 Use program library functions: Utilise built-in Python functions and libraries to enhance your programs.
* 4.1 Develop algorithms using sequence, selection, and iteration constructs: Integrate functions into your algorithms to create efficient and maintainable code.

By the end of this session, you'll be able to create your own functions to simplify complex tasks and improve the readability of your code.  

**Session 5 Overview**  
At the end of this session, you should be able to:  
* Define and understand functions
* Understand the difference between parameters and arguments
* Discover the purpose of return values
* Identify void functions (functions that do not return a value)
* Identify fruitful functions (functions that return a value)

***Pycharm is good***


build in stages
While loops are indefinate (unless specified)

### For loops
Definate loops are for statements (for loops), they self-limit

```python
for interation_variable in some_iterable:
    print("something")
    print("another thing")
```

```python
greeting = "Hello World"

for interation_variable in greeting:
    print("something")
    print("another thing")
```
```python
greeting = "Hello World"
length = 0
for characters in greeting:
    length += 1
    print(character)
    print(length)
```

```python
greeting = "Hello World"
length = 0
for characters in greeting:
    length += 1
    print(characters)
    print(length)
```

continue and break both work in for loops  
`time.sleep(1)` is fun  

range has increment (and decrement)  
`for i in range (10,1, -2)`  

For loops are much quicker for doing something a specific number of times.

co-ord look into (ASCII/ANSI - windows) or unicode?

### Functions
Functions are the last element of control flow
* sequence
* selection (if)
* iterables
* functions (modular)

void and fruitful.

next: write our own functions (def)  
return is really important in functions. substitues entire call with what you want (otherwaise none).  

return doesn't have a certain type - it's good idea to specfy one.

## Resources
***Functions***  
[Lecture Slides](./resources/ICTPRG302-Functions-S5.pdf)  
[Further reading: Python Functions](https://www.w3schools.com/python/python_functions.asp) 

## Activities
***Functions***  
[Activity 1: Build a Simple Calculator](./activities/calculator.md)  
[Activity 1: Complete](./activities/calculator.py)  

*Although not required by the course, consider revisiting week 2's [fox, chicken and corn](../week_2-selection-comparison-loops/activivties/fox-chicken-corn-riddle.md) riddle and coding a full solution with functions*