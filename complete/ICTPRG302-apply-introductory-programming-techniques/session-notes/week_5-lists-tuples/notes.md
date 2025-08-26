# Contents
- [Contents](#contents)
- [Week 5/Session 7 - Lists and Tuples](#week-5session-7---lists-and-tuples)
    - [Lists](#lists)
    - [Tuples](#tuples)
  - [Resources](#resources)
  - [Activivites](#activivites)
  - [Glossary](#glossary)

# Week 5/Session 7 - Lists and Tuples
In this session, we're going to explore the versatile and powerful Lists in Python.  

Lists are one of the most commonly used data structures, allowing you to store and manipulate collections of items. You'll learn how to create, access, modify, and iterate over lists, as well as use various list methods and functions.  

**This session will provide you with the skills and knowledge required to:**  
* 2.2 Create code using language data types, operators, and expressions: Understand and use list data types, and apply operators and expressions to manipulate list elements
* 4.2 Create and use data structures: Implement lists to store and manage collections of data effectively
* 4.4 Apply string manipulation: Combine lists with string operations to handle and process text data efficiently.

By the end of this session, you'll be able to work confidently with lists, using them to organise and manipulate data in your Python programs.  

**Session 7 Overview**  
At the end of this session, you should be able to:  
* Understand what lists are and how to create them
* Loop through lists using for loops
* Learn how to access and change elements in a list
* Use methods like `append()`, `insert()`, `remove()`
* Use methods such as `sort()`, `reverse()` and `count()` 

___
### Lists
lists are strings on steroids... a collection of items of any type
 when naming lists, name them plural, then you can use singular for `for`

google list comprehensions vs lists:
List comprehension is building a new list using iteration ```[new_value for item in iterable if condition]``` slicing/stiding searching in a list is NOT list comprehension.

Note: List comprehensions and generator expressions are very similar concepts with the difference being in how they are evaluated:
* a list comprehension will create a list up-front (*eager* evaluation)
* a generator expression will evaluate as it goes

**Example from GPT:**  
**Why Use a Generator + next() Instead of a List?**  
When you don’t need all results, just the first few:
```python
with open('huge_log_file.txt') as f:
    match = next((line for line in f if 'ERROR' in line), None)
    print(match)

# OR:
with open('huge_log_file.txt') as f:
    for line in f:
        if 'ERROR' in line:
            print(line, end='')
```
*Doesn't load the entire file into memory, doesn't can be used for getting just a few results*

VS With list comprehension (bad idea here):
```python
matches = [line for line in open('huge_log_file.txt') if 'ERROR' in line]
print(matches[0])  # Wasteful! Reads the whole file even if the first line matched.
```

find with strings, but index on any sequence (will cause errors, but those are good).
index works well on strings, won't find sub-items, but you can subindex...
```python
students = ["amanda", "tavis"]
print(students [0][0])
```
strings are iummutable, but they can be reassigned.

Lists are mutable however.
```python
students = ["amanda", "tavis"]
students [1] = "grace"
print(students)
```

**list sort**  
will work on items so long as they are the same type.
when changing a mutable object we get none
when changing an immutable obelct you get a copy of the original.

when you assign a mutable item back on itself you get an error.
because it returns none.

sorted returns a sorted copy.

this is why copy (alias/clone from my weird notes, sort of)

append adds only one item, extend adds multiple.

pop is fun. Works through, but also removes (and returns).


Usually, when we program, we don't want to do stuff to just one thing but to a bunch of things.  Often, it makes sense to put those things into a single collection. Python offers us multiple types of collections but the workhorse of them all is the list. Lists are:  
* Mutable: meaning you can add, remove, and change items in a list.
* Heterogenous: meaning you can store values of different types in a single list
(you can even store lists in lists (and then lists in those lists (and lists in those lists (you get the point!))))
* Ordered: Believe it or not, even though this is the easiest word, it is actually the hardest concept. Every item in a list is in a designated position within the list and it will stay in that position unless you move it. List 'positions' or indexes start at 0 for the first item and continue until (len - 1) of the list.


### Tuples 
don't have brackets
they are pretty jank.
can't do loads of stuff

" Python is a language for consenting adults" XD
Why would you want a tuple: 
Wrong: 
* performance - quicker to lookup - it's not always, and if you care that much there are better choices, you're probably not using python.
* 
* 

Right:
they express a different idea than lists, if you want to know all students, but don't want current status. - More like parameters.
Unpacking!
```python
name = "Rafael", "Avigad", 25
first, last, age = name
print(last)
```

github gist.. one file solution
can make it secret, but can still share the link.
gist.github.com/rafrafavi/e7b12d1acc80ed01c4a75eaec4ae0792

## Resources
***Lists***  
[Lecture Slides](./resources/ICTPRG302-S7-Lists.pdf)  
[Video: Python Lists Tutorial](https://www.youtube.com/watch?v=ohCDWZgNIU0)  

***Tuples***  
[Lecture Slides](./resources/ICTPRG302-Tuples.pptx)  
[PY4E - Chapter 10 - Tuples](https://books.trinket.io/pfe/09-dictionaries.html)  

## Activivites
***Lists***  
[List Revision Activity from Raf](activities/list-revision.md)  
[List Revision Complete](activities/list-revision.py)  

[Test Yourself Activity](./activities/test-yourself.md)  
[Test Yourself Complete](./activities/test-yourself.py)

[Activity1: Shopping List](./activities/shopping-list.md)  
[Activity1: Complete](./activities/shopping-list.py)  

[Bonus - List Comprehension](./activities/bonus-list-comprehension.md)  
[Bonus - Complete](./activities/bonus-list-comprehension.py) 
___

## Glossary
* **List** A dynamic data structure that holds items under one name. The items can be of varying data types.
* **Sense HAT** Hardware that attaches to the top of a Raspberry Pi computer and allows you to write programs that collect data from sensors. The Sense HAT also has an LED matrix for displaying output.
* **Pixel** A single element of an image on a computer screen.
* **Sensor** A tool that collects data.
* **Sense HAT emulator** A digital representation of the physical Sense HAT device.
* **LED matrix** A group of LEDs placed in a grid structure. 
