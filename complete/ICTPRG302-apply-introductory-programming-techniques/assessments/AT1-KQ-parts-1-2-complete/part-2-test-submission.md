# AT1-KQ Part 2 Test Submisson

[link](https://blackboard.northmetrotafe.wa.edu.au/webapps/assessment/review/review.jsp?attempt_id=_9937949_1&course_id=_41920_1&content_id=_4703841_1&outcome_id=_7949508_1&outcome_definition_id=_2117976_1)

Contents:
- [AT1-KQ Part 2 Test Submisson](#at1-kq-part-2-test-submisson)
  - [Instructions](#instructions)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3)
    - [Question 4](#question-4)
    - [Question 5](#question-5)
    - [Question 6](#question-6)
    - [Question 7](#question-7)
    - [Question 8](#question-8)
    - [Question 9](#question-9)
    - [Question 10](#question-10)

___

## Instructions 	
If you use any form of generative AI (ChatGPT, Gemini, MS CoPilot etc) to help you answer Questions, then you must:
 * Phrase the answers in **YOUR** own words, **NOT** the **AI's**. Failure to comply will result in evidence of academic misconduct.

**Remember:** Lecturers have the right to ask you to explain your answers to ### Questions face-to-face and monitor assessments.

___
### Question 1
Needs Marking  
Unmarked 	

**How do you define a function in Python? Provide an example of code to support your answer.**  
Selected Answer: 	
```python
# functions are defined with the `def`, followed by the function name, input parameters or argumnents (in parentheses) and a colon.

def greet_user(user):
    print(f"Hello {user}! ")

greet_user(input("Please enter your name: "))
```
Response Feedback: 	[None Given]  

___
### Question 2
Needs Marking  
Unmarked 

**Arrange these words to correctly define and call a function.**
* print
* ("Good morning!")
* def
* greeting
* ()
* \# Output: Good, morning!   
  
Selected Answer: 	
```python
def greeting():
    print("Good morning!")

greeting()
# Output: Good, morning! 
```
Response Feedback: 	[None Given]

___
### Question 3
Needs Marking  
Unmarked 	

**How can you convert a string to all uppercase in Python?**  
Provide an example using the words Good Morning.   
Selected Answer: 	
```python
greeting = "Good Morning"

print(greeting.upper())
```
Response Feedback: 	[None Given]

___
### Question 4
Needs Marking  
Unmarked 	

**How can you find the *length* of a list?**  
Provide an example of code ***using 3 units in your course.***  
Selected Answer: 	
```python
units = [
    "ICTPRG302 - Apply introductory programming techniques - ICT30120 ICT40120",
    "Cluster - IP4RIoT - ICT40120 (Programming)",
    "ICTSAS432 - Identify and resolve client ICT problems - Software"
]

print(len(units))

# Output: 3
```
Response Feedback: 	[None Given]

___
### Question 5
Needs Marking  
Unmarked 	

**How do you add an item to a list in Python?**  
Provide an example using the word Cheetah to a list of 5 African animals.  
Selected Answer: 	
```python
african_animals = ["Caracal", "Leopard", "African Wildcat", "Lion", "Serval"]
african_animals.append("Cheetah")
print(african_animals)

# Output: ['Caracal', 'Leopard', 'African Wildcat', 'Lion', 'Serval', 'Cheetah']
```
Response Feedback: 	[None Given]

___
### Question 6
Needs Marking  
Unmarked 	

**How can you check if an item exists in a list?**  
Provide an example using the code from the previous question, by checking the list for the word Meerkat.    
Selected Answer: 	
```python
african_animals = ["Caracal", "Leopard", "African Wildcat", "Lion", "Serval"]
african_animals.append("Cheetah")
african_animals.index("Meerkat")
#Output: ValueError: 'Meerkat' is not in list
```
Response Feedback: 	[None Given]

___
### Question 7
Needs Marking  
Unmarked 	

**What is a dictionary in Python?**  
How is it different from a list?  
Selected Answer: 	
```
Like lists, dictionaries are a type of collection which can contain different types, and even sub-collections.

However unlike lists and tuples, dictionaries don't have indexes for each element, but instead keys and values. This makes them an unordered collection
```
Response Feedback: 	[None Given]

___
### Question 8
Needs Marking  
Unmarked 	

**Given the dictionary: student = {'name': 'John', 'age': 17, 'courses': ['Networking', 'Cyber Security', 'Information Technology']}, how would you access the value associated with the key 'courses'?**  
Provide an example of your code  
Selected Answer: 	
```python
student = {'name': 'John', 'age': 17, 'courses': ['Networking', 'Cyber Security', 'Information Technology']}
student['courses']

# Output: ['Networking', 'Cyber Security', 'Information Technology']
```
Response Feedback: 	[None Given]

___
### Question 9
Needs Marking  
Unmarked 	

 	

**How do you read the contents of a file in Python?**  
Provide an example of your code incorporating the following words:
* \# Open the file in read mode.
* python-variables.txt
* contents

Selected Answer: 
```python
# Open the file in read mode.
contents = open("python-variables.txt" ,"r")
```
Response Feedback: 	[None Given]

___
### Question 10
Needs Marking  
Unmarked 	

**Match each characteristic or example with either "List" or "Tuple".**  
| Question                                                  | Selected Match    |
|-----------------------------------------------------------|-------------------|
| Mutable (can be changed)                                  | a. List           |
| Immutable (cannot be changed)                             | b. Tuple          |
| Defined using square brackets []                          | c. List           |
| Defined using parentheses ()                              | d. Tuple          |
| Example: ['apple', 'banana', 'cherry']                    | e. List           |
| Example: ('apple', 'banana', 'cherry')                    | f. Tuple          |
| Can add items using append() method                       | g. List           |
| Cannot add items after creation                           | h. Tuple          |
| Supports item assignment (e.g., `my_list[0] = 'orange'`)  | i. List           |
| Does not support item assignment.                         | j. Tuple          |


Selected Answer: 	

| All Answer Choices |
|--------------------|
| a. List            |
| b. Tuple           |
| c. List            |
| d. Tuple           |
| e. List            |
| f. Tuple           |
| g. List            |
| h. Tuple           |
| i. List            |
| j. Tuple           |


Response Feedback: 	Well done! You have matched all the characteristics correctly!