# Test 2 Diagnostic Tools Practical: Control Panel

[link](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_13866_1/cl/outline)

Contents:
- [Test 2 Diagnostic Tools Practical: Control Panel](#test-2-diagnostic-tools-practical-control-panel)
  - [Instructions](#instructions)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3)
    - [Question 4](#question-4)
    - [Question 5](#question-5)
    - [Question 6](#question-6)
    - [Question 7](#question-7)


___
## Instructions 	
Attempt all questions in this assessment.

___
### Question 1
Complete  

*What data type would be the most efficient way of storing distances on Earth in Kilo meters?*  

**Selected Answer:**  
 - [ ] TINYINT  
 - [ ] SMALLINT  
 - [x] MEDIUMINT  
 - [ ] INT  
 - [ ] BIGINT  

**Response Feedback:**  
Correct. 

___
### Question 2
Complete  

*What would you use to store the date of birth of customer for a generic business?*  

**Selected Answer:**  
 - [x] DATE  
 - [ ] YEAR  
 - [ ] DATETIME  
 - [ ] TIMESTAMP 

**Response Feedback:**  
Correct. 

___
### Question 3
Complete  

*What would you use to store the date of birth of a baby at a hospital?*  

**Selected Answer:**  
 - [ ] DATE  
 - [ ] YEAR  
 - [x] DATETIME  
 - [ ] TIMESTAMP  

**Response Feedback:**  
Correct. 

___
### Question 4
Complete  

*Which of the following data types would be perfectly safe to store in a CHAR string at all times (as opposed to a VARCHAR string)?*  
Note there are multiple answers. You may also have to research for some of them.

**Selected Answer:**  
 - [x] Number plate  
 - [ ] City or town name  
 - [ ] Book title 
 - [x] Country of origin  
 - [x] Stock ticker symbol  
 - [ ] Name of a medical condition  

**Response Feedback:**  
Correct. 

### Question 5
Complete  

*Give five examples of integer fields that can be unsigned.*  
Hint: Think in terms of what could be stored in an unsigned integer field...

**Selected Answer:**  
1. Age
2. Number of Items in Stock
3. Tax File Number
4. Student Number
5. Film Release Year

(Bonus: Agression in CiV 6 ;P)

**Response Feedback:**  
None Given 

___
### Question 6
Complete  
 
*Research and explain in your own words what error propagation with floating point numbers.*

**Selected Answer:**  
Floating point numbers are stored in a way that saves space (in memory/on disk) at the cost of some precision. They are saved as an approximation, really a percentage within a range. This is accurate enough for most use-cases, but when the numbers are added together or subtracted the inaccuracies are propagated. The compounding of the small inaccuracies can lead to very large inaccuracies when performing multiple addition/subtraction operations.

Source:
https://bertwagner.com/posts/more-wrong-sql-server-math-floating-point-errors/

**Response Feedback:**  
None Given 

___
### Question 7
Complete  

*Do some research and explain, in your own words, why you should generally store telephone numbers as a string, not as a integer.*

**Selected Answer:**  
Phone numbers may have non-integer characters; + for an international number for example, also many phone numbers start with a '0' (or are '000'!), leading zeros are removed from integers. While phone numbers are made up of numbers, they aren't numbers in a mathematical sense, but a "code" represented by digits, it is best to store them as strings not text. This also makes it easier to perform string operations on them, such as prefixing area codes, joining extensions and the like.

Source:

https://stackoverflow.com/questions/23637057/why-is-it-best-to-store-a-telephone-number-as-a-string-vs-integer


**Response Feedback:**  
None Given 