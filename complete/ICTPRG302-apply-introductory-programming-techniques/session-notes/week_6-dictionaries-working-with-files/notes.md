# Contents
- [Contents](#contents)
- [Week 6/Session 8 \& 9 - Dictionaries and Working With Files](#week-6session-8--9---dictionaries-and-working-with-files)
  - [Dictionaries](#dictionaries)
  - [Working With Files](#working-with-files)
    - [Opening Files](#opening-files)
  - [Raf git comment:](#raf-git-comment)
  - [Assessment intro](#assessment-intro)
  - [Resources](#resources)
  - [Activities](#activities)


# Week 6/Session 8 & 9 - Dictionaries and Working With Files
*Last Python for this term :(*

 Assessment Task 2 (AT2): Project is out now

## Dictionaries
In this session, we are going to learn about selection statements, comparison operators, if, elif and else statements and the different methods used by programmers to test your code.  
This session will provide you with the skills and knowledge required to:  
* 2.2 Create code using language data types, operators and expressions
* 3.1 Apply language syntax in sequence, selection and iteration constructs

Dictionaries are the most useful, versatile and powerful data types (also called hash maps, hash tables and arrays).

Look up by a key (like a word) and look at the definition (value).  

dictionaries have keys and values. Keys must be unique, but they are always strings.

***Evaluate on the right, assign on the left***

## Working With Files
**Introduction**  
In this session, we are going to learn about Python Files, including how to open, read, write and close them.   
This session will provide you with the skills and knowledge required to:
* 2.4 Use program library functions
* 4.3 Code standard sequential access algorithms used in reading and writing text files
* 5.2 Create and conduct simple tests and confirm code meets design specification.

**Overview**  
At the end of this session you should be able to:
* Use Python's built-in functions such as open(), read(), write(), and close() to perform file operations
* Write algorithms that handle sequential access to text files, including reading from and writing to files in a structured manner
* Practice creating and running tests to ensure that your files work correctly to meet specified requirements.

File handling in programming is important, it is how we interact with external data and save persistent results from programs. This session will cover how to read, write, and create files. We'll also take a detour into modules.  

### Opening Files
Basic syntax for opening a file is open, followed by the relative file path and name:
```python
open("./resources/ice_ice_baby.txt")
```
Naturally this will only work if there is a file present and the path is correct. But this on it's won won't be useful for example `print(open("./resources/ice_ice_baby.txt"))` will result in



Searching for things in files is cool and all, but storing entire files in memory is not necessarily the most efficient way to do it.

While a file is open, reading continues from where it left off (a little like pop), files can also be connections to databases and similar, remember the cursor.
`print(file.tell())` shows current position in file. 

strip removes line breaks, print defaults to \n `end=''` will remove them.

Close afterwards is good, avoids unpredictable results, don't want to corrupt data.

with open is better because it auto-closes files once de-dented. (context manager).
get in the habit of using with open as file.

writing is the same but there's a w, will overwrite existing files, does not add line breaks.

## Raf git comment:
The only thing we haven't covered in the course is the use of the built-in enumerate function. I ahmed and ahhd about including it (it's Python bread-and-butter but other program languages do this differently).

The enumerate function works on any collection and returns a tuple of a number and the item and without it things look pretty clunky. Here's print_board without enumerate:

```python
def print_board(board):
    print("  a   b   c")
    for i in range(1, len(board) + 1):
        print(i, end=' ')
        print(' | '.join(board[i - 1]))
```

If you compare it to the original version you can see why we love enumerate:

```python
def print_board(board):
    print("  a   b   c")
    for i, row in enumerate(board, 1):
        print(i, end=' ')
        print(' | '.join(row))
```
See [Class Dictionary](./resources/dictionaries.py) for in-class code.

## Assessment intro
Create a command line version of Wordle

Big gotcha is we are assessed on our ability to follow a process and get feedback - don't just code it... read the assessment requirements first, do it in a more robust way than cert 3.

Don't just ask "what is wordle", can you explain if it needs to run on both windows and mac... follow up on things the CEO has said. 


## Resources
**Dictionaries**  
[Lecture Slides](./resources/ICTPRG302-Dictionaries.pptx)  
[PY4E - Chapter 9 - Dictionaries](https://books.trinket.io/pfe/09-dictionaries.html)   
[Sorting Dictionaries by Value](https://datagy.io/python-sort-a-dictionary-by-values/)  
[Code demonstrated in lecture](./resources/dictionaries.py)  

**Working With Files**  
[Lecture Slides - working with files](./resources/ICTPRG302-ModulesAndFiles.pptx)  
[Shorter Combined Lesson on File Handling](./resources/shorter-combined-files-lesson.pptx)  
[Lecture Slides - working with files updated](./resources/ICTPRG302-S9-Files.pdf)  
[Further reading: Open & Closing Files](https://realpython.com/read-write-files-python/#opening-and-closing-a-file-in-python)    

## Activities
**Dictionaries**  
[Grocery Activity](./activities/dictionaries/grocery-dict.md)  
[Grocery Complete](./activities/dictionaries/grocery-dict.py)

[Activity From Lecture Slides](./activities/dictionaries/name-dict.md)  
[Activity Complete](./activities/dictionaries/name-dict.py)  

[Activity 1: Shopping List](./activities/dictionaries/shopping-list.md)  
[Activity 1: Complete](./activities/dictionaries/shopping-list.py)

[Activity 2: Music Dictionary](./activities/dictionaries/music-dict.md)  
[Activity 2: Complete](./activities/dictionaries/music-dict.py)  

[Raf's Tic Tac Dictionary Exercise](./activities/dictionaries/tictac-dict.md)


**Working With Files**  