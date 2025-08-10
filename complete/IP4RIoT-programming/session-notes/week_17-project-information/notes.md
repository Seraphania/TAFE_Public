# Contents
- [Contents](#contents)
- [Week 16/Session 17 - Project information](#week-16session-17---project-information)
  - [Notes](#notes)
    - [TDD - Test Driven Development](#tdd---test-driven-development)
    - [TearDown](#teardown)
    - [Working with files](#working-with-files)
    - [JSON in Python](#json-in-python)
    - [Classmethods](#classmethods)
  - [Tasks for today](#tasks-for-today)
  - [Resources](#resources)
  - [Activities](#activities)


# Week 16/Session 17 - Project information
3/6/2025  

[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_35877_1&content_id=_3663755_1)  
[Raf's Lecture materials](https://github.com/NM-TAFE/civ-ipriot-in-class-demos/tree/2025/s1/raf)

## Notes

### TDD - Test Driven Development
Essentially writing tests before writing code. It is useful for ensuring that code works and helps avoid not testing what should be tested. The drawback is that it assumes that everything that needs to be coded is established before the code is written, when often a lot of thinking happens while coding.

Rather that using a pure TDD approach; when a bug is encountered, a test should be written that fails because of the bug, then fix the bug so the test passes.  


### TearDown
When testing, tests should always run under the same conditions, however by necessity some tests may change conditions, for example: 
```python
      def test_log_file_created(self):
         new_carpark = Carpark(location="Moondalup", capacity=100, log_file=log_file)
         self.assertTrue(Path("log/test_log.txt").exists())
```
This test creates a new path and file each time it is run, changing the condition if the test is run again.  

The `tearDown()` method will run after each test, just as `setUp()` will run before each test.
```python
      def tearDown(self):
         Path("log/test_log.txt").unlink(missing_ok=True) # unlink ~= delete
```

### Working with files
if working with files, import pathlib not os.path `from pathlib import Path`. pathlib is a library for  handling file paths regardless of the operating system, it is far more robust across different operating systems than `os.sys`.

Pathlib can also be used to create directories, though it is a good idea to resolve the path name after the directory is created (not before)
```python
                ...
                 log_file=Path("log/log.txt"), # relative to the working directory
                 ...
        self.log_file.parent.mkdir(parents=True, exist_ok=True) 
        self.log_file.touch(exist_ok=True)
        self.log_file = log_file.resolve()
```

### JSON in Python
JSON is Javascript object notation, it is how objects are stored in javascript. It is a useful way to save structured information to a file; such as the configuration of a carpark.  

Historically information was sent between webpages using XML (C# still uses XML), as javascript became more widespread, instead of converting all JS objects to XML it was decided to send them as text in JSON format.  

JSON syntax is very similar to Python dictionaries with a few minor differences:
* true and false are lower case
* null is the same as None  

See [JavaScript Object Notation (JSON)](https://www.json.org/json-en.html) for detail.  

Railroad diagrams are cool:
- Anything ON the line is required.  
- Anything BELOW the line is optional.
- Anything ABOVE the line is a default.  

In python it is easy to convert a dictionary to JSON, or JSON to a dictionary:
```python
import json
from pathlib import Path

file_path = Path("file.json")

a_dictionary = {"location": "location",
                    "capacity": "capacity",
                    "log_file": "log_file"} 
with open(file_path, "w") as file:
    json.dump(a_dictionary, file) # converts to json object (in this case output to a file)

string =  json.dumps(a_dictionary) # json.dumps() converts the whole thing to a string (does not output to file)
print(string)
```
`json.load`/`json.loads` do the same but in reverse.

### Classmethods
class methods are for creating instances, they are specified using the `@classmethod` decorator.
Both `@classmethod` and `@staticmethod` are methods where we don't need to pass self, they are specified using the `@classmethod` or `@staticmethod` decorator. Static methods are used wne we want to create methods that don't refer to or call an instance of the class.  

Class methods are used for passing an instance of the class like `self` is a very strong convention when passing an instance `cls` is a very strong convention when passing a class:
```python
@classmethod
def from_config(cls):
  return cls(...)
```

* When neither a class or an instance of a class are needed, a static method should be used.  
* When a class is needed, but not an instance of it, a class method should be used.
Class methods are generally preferred as they are more explicit - because the class is passed.







## Tasks for today





look into automation + python - devops, OS's Git, github.



## Resources
fun links from raf:  
https://www.youtube.com/watch?v=uNjxe8ShM-8  
https://github.com/cdchoy/ppcc


## Activities
have a look at projects
https://github.com/borisbabic/browser_cookie3  
