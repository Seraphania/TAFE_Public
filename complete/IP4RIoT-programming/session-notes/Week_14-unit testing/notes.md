# Contents
- [Contents](#contents)
- [Week 14/Session 15 - Class Unit Testing](#week-14session-15---class-unit-testing)
  - [Why Testing is Important](#why-testing-is-important)
    - [What to test](#what-to-test)
    - [Testing methods](#testing-methods)
  - [Unit Testing](#unit-testing)
    - [Organisation](#organisation)
    - [Unit Test Setup in VS Code](#unit-test-setup-in-vs-code)
    - [Writing Unit Tests](#writing-unit-tests)
  - [Resources](#resources)
  - [Activities](#activities)


# Week 14/Session 15 - Class Unit Testing
27/5/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_35877_1&content_id=_3663755_1)

[Raf's Lecture materials](https://github.com/NM-TAFE/civ-ipriot-in-class-demos/tree/2025/s1/raf)

**Objectives**  
* Prepare for writing full applications by learning how to work with folders within your project
* Learn how to develop automated unit tests in Python and why they matter
* Understand organisational requirements for test documentation
* Run automated tests and read and interpret test reports

**Curriculum alignment**  
Aligns with the following elements of ICTPRG430
3. Test the application

**Relevance to industry**  
Unit testing is a fundamental part of writing professional code. Most organizations do not see code as complete until unit tests are written. 

**Relevance to assessment**  
Your final project requires running and developing unit tests
How to use this information
* Follow the lecture slides and recording (if applicable)
* Complete the in-class activities on GitHub: https://github.com/NM-TAFE/civ-ipriot-in-class-demos/blob/main/week15/lesson.md
  * (Online students should try and make an attempt before class)
* Watch the socratica video to further supplement your understanding of how to write unit tests
___

## Why Testing is Important
Testing also known as QA is makings sure what we build is fit for purpose, there are a few ways to approach this: 
* **Functional testing** - the most intutitive, try to use the application, maybe try different inputs to see if it breaks, but basically does it do what it's supposed to, often manuyal but can be automated.
* **Integration Testing** - Seeing that everything works, possibly including deployment.
* **Unit testing** - maybe not most important, but most closely tied to what software *is*

Testing is important because definitions can mask errors - particularly in Python, fewer compile-time checks mean more runtime errors. Python does something called late evaluation. When there are errors the program terminates so we don't necessarily see them - it would be better to see a list of all the problems in our code. Not all bugs raise errors.   

Example bad code from class example:
```py
class Cat:
    def __int__(name, coat):
        self.name = nam
        coat = coat
        oopsy

    def speak(self):
        this_cant_possibly_work()
        self.speak()
        return f"{self.name} with {self.coat} Moos"
```
*Note that despite having obvious problems the code does not initially raise an error, class activity was to fix errors one at a time (after trying to instantiate a cat)*

Initial bugs were hard to find in the code because there is no "contract" for what the Cat class was meant to do. It is good proctice to write tests while coding, as it helps in thinking about the code from the perspective of someone reviewing the code.  
Tests should be simple, this makes them esier to manage.  
If a problem is difficult to test, instead of trying to work out how to test it write simpler code.

```python
class Cat:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat

    def speak(self):
        return f"{self.name} with {self.coat} Moos"
    
    
c = Cat("Tex", "Orange")
response = c.speak()
print(response)

# prints "Tex with Orange Moos"  
```
Just because we got to a point where there were no errors, doens't mean that everything that everything is behaving as it should.

This is why we need to be able to assert that a cerain behaviour should happen, this is done using the `assert` statement followed by an expression that is true or truthy (or false/falsy):
```python
class Cat:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat

    def speak(self):
        return f"{self.name} with {self.coat} Moos"
    
    
c = Cat("Tex", "Orange")
response = c.speak()
print(response)

assert "meow" in response.lower()
# Traceback (most recent call last):
#   File "C:\Users\String\AppData\Local\Temp\temp_1749284634494.py", line 16, in <module>
#     assert "meow" in response.lower()
# AssertionError
```
This allows us to see exactly where in the code something is not behaving properly so we can see errors earlier.

The "Problems" tab in most IDE's can be helpful for basic issues (see the bad code example) but assert statements can be more tailored.

While assert Statements can be useful for quick debugging and testing, but this is not really the most efficient way of testing for large programs, it would be prefereable to have a list of all the erros in the program.

### What to test 
* Create a test for anything that ends up being a bug - if you find a bug, write a test that finds it.  
* Test that any specified requirements are met.  

What not to test:  
* Private methods and attributes - generally.
* Write a public interface or only test what is public.
* Don't test implementation detail, test that output meet expectations.
* If you're writing an application to the test that is not great.

Instead of writing more complicated tests, write better code, for example:
```python
name = input("Name?: ")
print("hello", name)
```
Wile this is one of the easiest programs to write, it is VERY hard to test, the `input` function pauses the program, so it causes the test to hang. It is possible to test by redirecting stdout and other things, but a better option would be to write it so it's testable (this is why the concepts of modularity and unit testing are important):
```python
#greet.py
def get_name(func=input): # pass it the function to be used
  return func("name?: ") # func could be another function used for testing

def greet(name):
  return f'hello, {name}'
```
The `get_name` function will cause a test to hang if used with it's default, but it's easily overridden:
```python
#test_greet.py
from greet import get_name
from greet import greet # could use `from greet import*` but it's jank
import unittest

class TestCase(unittest.TestCase):
  def test_greeting(self):
    self.assertEqual(greet("Jane"), "hello, Jane") # Workds fine

  def test_get_name(self):
    # `get_name()` will fail on it's own because the default is input
    self.assertEqual(get_name(lambda x: "Jane"), "Jane")
```
This can also be used to test them in conjunction with arrange:
```python
#test_greet.py
from greet import get_name
from greet import greet # could use `from greet import*` but it's jank
import unittest

class TestCase(unittest.TestCase):
  def test_greeting(self):
    # arrange
    name = get_name()
    self.assertEqual(greet("Jane"), "hello, Jane") # Workds fine

  def test_get_name(self):
    # `get_name()` will fail on it's own because the default is input
    self.assertEqual(get_name(lambda x: "Jane"), "Jane") # replaces a function (`input()` in this case) with another function
```

Generally in OOP:  
One class per file and one Test Case per object eg cat.py for the cat class test_cat.py or cat_test.py - use only these, one or the other and be consistent.

### Testing methods
Python has 2 built-in methods for testing:
* doctest - Covered in week 8 of ICTPRG302
* unittest - what we will be using, but is less pythonic
Pytest is another framework used for testing, it is probably the most popular, but it is not built-in. 

Unittest framework originated before Java, and is less pythonic than other testing methods(like Pytest), it is widely used in all languages.

## Unit Testing
Unit testing refers to testing *units* of code. Part of the reason OOP focuses on modularity of code is that it makes it easier to test that each discrete unit works as intended. Unit testing is not concerned with how units interact with eachother. It is also used because some components may not have user-facing functionality (for example abstract classes). This allows for better *code coverage* - More code being covered by tests so that we know it works.

Ideally unit testing will be automated (though it can be manual), allowing it to be integrated into a CI/CD workflow:
-> commint change -> run tests -> accept (or decline) change.

Often when unit testing is refered to, people mean automated tests; if you haven't "unit tested" your code, it means you have not written automated tests.

Key Concepts in Unit Testing:
* **Test, TestCase** - A test is an individual thing that is asserted, a TestCase usually consists of mutltiple tests associated with a given unit e.g. can you instantiate a cat? can you make it speak? does the speak method return what it should? All of these are tests in a testcase.
* **Test Runner** - The thing that runs the tests within a testing framework, they do things like handle the errors so that everything can be tested and provide a report.
* **Coverage** - A coverage report will state what lines of code were covered by tests, as a proportion of the total lines of code (not including comment or documentation lines).

Tests should be set up according to the AAA Paradigm:
* **Arrange** - With setUp, tearDown and fixtures
* **Act** - Perform an operation you want to test
* **Assert** - Use a varaiety of assertions you want to check for success or failure.

*Note: Unittests can be run from the command line with the command `python -m unittest discover`*

### Organisation
In IDE's it is common not to just work on files, but on folders and subfolders; good organisation is important programs become more complex, especially where testing is involved.  
A typical project folder setup will look like:
```
Typical folder structure:
project_root/                   # usually also git repo root
│
├── src/                        # Directory for source files
│   ├── cat.py                  # Module for Cat-related functionalities
│   ├── dog.py                  # Module for Dog-related functionalities
│   ├── animal.py               # Common module for general Animal attributes
│
├── tests/                      # Directory for unit test files
│   ├── test_cat.py             # Unit tests for functionalities in cat.py
│   ├── test_dog.py             # Unit tests for functionalities in dog.py
│   ├── test_animal.py          # Unit tests for common functionalities in animal.py
│
├── README.md                   # Project overview and general information
├── requirements.txt            # File to list project dependencies
└── .gitignore                  # Specifies intentionally untracked files to ignore

```
Notes:
1. Keep tests separate from source code
2. Modules still need to be imported into tests
3. The root folder is always treated as the folder the program will run from until a test is run, then it changes to the root of the project
4. The simple solution is an environment variable called PYTHONPATH which is set to equal the src
5. This allows pretending that the source files are in whatever folder we run from

*In VSCode this applies, but only the project folder can be open - open a new workspace with only the "root" folder.*

### Unit Test Setup in VS Code
1. Set up source folders as follows:
    ```
    cat-testing/
    ├── src/
    │   ├── __init__.py
    │   └── bad_cat.py
    ├── tests/
    │   ├── __init__.py
    │   └── test_bad_cat.py
    └── .vscode/
        └── settings.json
    ```
    *If testing a new VS Code window should be opened, and pointed at the root directory - "cat-testing" in the example above.*
2. Create and activate virtual environment:
  From inside cat-testing/: `python -m venv .venv`
3. Activate it:  
  Windows (cmd): `.venv\Scripts\activate`
  PowerShell: `.venv\Scripts\Activate.ps1`
  bash/zsh: `source .venv/bin/activate`
  *if windows has a conniption about security use `Set-ExecutionPolicy RemoteSigned -Scope Process`*
4. Write code and tests
5. Set VSCode to find tests:
    .vscode/settings.json:
    ```json
    {
      "python.testing.unittestEnabled": true,
      "python.testing.pytestEnabled": false,
      "python.testing.unittestArgs": [
        "-v",
        "-s",
        "tests",
        "-p",
        "test*.py"
      ],
      "python.envFile": "${workspaceFolder}/.env",
      "python.analysis.extraPaths": ["./src"]
    }
    ```
    `Ctrl+Shift+P` → Python: Select Interpreter → choose the one inside .venv  
    `Ctrl+Shift+P` → Python: Configure Tests  
      → Select unittest  
      → Choose tests/ as the test folder  
      → Pattern: test*.py  
      in the root folder of the project directory create a file called `.env` and put `PYTHONPATH=./src` in it.

    Then VSCode should automatically run discovery. If it doesn’t, manually run:  
    `Ctrl+Shift+P` → Testing: Refresh Tests  
    Or click the beaker icon on the Activity Bar, top-left of the test pane, and hit refresh.  

6. The VSCode internal test controller sometimes gets out of sync, if so:  
    `Ctrl+Shift+P` → Developer: Reload Window  
    (This restarts the VSCode instance and realigns the test providers.)

### Writing Unit Tests
Assuming we are writing a test for the example class Cat from earlier:
```python
# cat.py
class Cat:
    def __init__(self, name, coat):
        self.name = name
        self.coat = coat

    def speak(self):
        return f"{self.name} with {self.coat} Moos"
```
* The unit test must import the class to be tested
* Also the unittest module must be imported
* Because of unittests Java origins EVERYTHING has to be an object, so the test must be an object (class)
* Naming is strict - must follow normal class conventions.
* Methods (individual tests) must start with `test_`, and names should be descriptive

```python
# test_cat.py
from cat import Cat
import unittest

class TestCat(unittest.TestCase): # inheritance
    def test_create_cat_with_name_and_coat(self): # self is an instance of a TestCat
        self.assertIsInstance(Cat("K", "T"), Cat)
```
Though not strictly required, setUp can be useful as it initiates a test cat so you don't need to to it for every test.
```python
# tests/test_bad_cat.py
from cat import Cat
import unittest

class TestCat(unittest.TestCase): # inheritance
    def setUp(self): # Similar to init, thinks that will run before the rest of the test is performed.
        self.c = Cat("T", "O")

    def test_cat_has_correct_name(self): # self is an instance of a TestCat
        self.assertEqual(self.c.name, "T")

    def test_cat_has_a_coat(self):
        self.assertTrue(hasattr(self.c, "coat"))

    def test_cat_meows_when_it_speaks(self):
        self.assertEqual(self.c.speak(), "meow")

if __name__ == "__main__":
    unittest.main()
```
The code above will work if the files are in the same folder, but if the files are organised into src and tests directories, the import will no longer work. There are two ways to fix this; one is to use `from src.cat import Cat`, though this is not ideal, it is brittle and may not always work.

It is preferable to add the source path to PYTHONPATH environment variable - in the root folder of the project directory create a file called `.env` and put `PYTHONPATH=./src` in it.
___


## Resources
[Lecture Slides](<../week_14-unit testing/resources/ipriot-unittest.pptx>)  

[Video: Socratica on Unit Testing](https://www.youtube.com/watch?v=1Lfv5tUGsn8)  
[Zip: Socratica Source Code](<../week_14-unit testing/resources/testing-overview.zip>)  

*Optional:*

[Zip: File String Num](<../week_14-unit testing/resources/string_num_value.zip>)  
[Geeks for Geeks - Python Unit Testing](https://www.geeksforgeeks.org/unit-testing-python-unittest/)  

[Video: Python TDD Workflow - Unit Testing Code Example for Beginners](https://www.youtube.com/watch?v=ibVSPVz2LAA)

## Activities
[In-class activity](<../week_14-unit testing/activities/class-activities.md>)  

There are activities at the end of the lecture slides based off the socratica video for practice.