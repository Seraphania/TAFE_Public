# AT1-KQ Part 2 Test Submisson

[link](https://blackboard.northmetrotafe.wa.edu.au/webapps/assessment/take/launch.jsp?course_assessment_id=_152712_1&course_id=_41920_1&content_id=_4707342_1&step=null)

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

___

## Instructions 	
In real-world scenarios, client briefings might not provide all the necessary information you need to assist you with developing an application.

If you don't fully understand the project requirements, asking for clarification is important.

Listen and/or watch the video and think about what questions you need to ask to recieve the answers that will help you.

**Here are some indicators to help you:**
* When the information provided is vague or ambiguous, seek more details.
* If you find yourself making assumptions about what the other person means, it's better to ask.
* When you feel that some details are missing, ask for more information.
* For complex information, it's helpful to break down the information and ask questions to ensure you understand each part.
* When you need to confirm your understanding, restate what you've heard and ask if it's correct.

***Note:***  
* To clarify the task, ask appropriate questions, specific to what was mentioned in the video.
* Avoid generic questions such as ‘When do you need it done by?”.
* Each question must relate to specific information in the video. Start with "You mentioned in the video...."
* Questions must focus on what the application needs to do, relating to design specifications, programming standards and guidelines.
* In formulating the questions, ensure that the responses assist you in determining scope, timeline, or priorities.

**Instructions**  
1. Locate the video "Project Client Brief".
2. Watch the video in its entirety.
3. Formulate three questions that you would ask the client or the senior developer as a follow up to better understand the application requirements.
4. Write your questions in the spaces provided below.

___
### Question 1
Complete

**Clarifying Question 1. Your assessor must be able to determine what aspect of the brief you are responding to. Please include what part of the brief led to the question. For example: "You mentioned in the video..."**  

Selected Answer: 	
```
As you suggested I went to check out wordle, great game!
It has been argued that part of the appeal is that all users played with the same word each day, and could therefore share and compete with eachother
(as per this article in psychology today:  https://www.psychologytoday.com/us/blog/psychology-tomorrow/202201/why-is-wordle-so-popular.)

Is this something you are looking to implement? Are there any other aspects of the original wordle that you feel are particularly important to include, or any you would like to change, for example would you like to change the number of guesses?
```
Response Feedback: 	[Fantastic question!]  
___
### Question 2
Complete

**Clarifying Question 2. Your assessor must be able to determine what aspect of the brief you are responding to. Please include what part of the brief led to the question. For example: "You mentioned in the video..."**   
  
Selected Answer: 	
```
You mentioned during our briefing that we are building a clone of the game that (for now), works in a CLI environment; Can you be more specific about which platforms you would like this to work on? and does the company have a preferred language that this is to be programmed in?
Also related; the original version of the game is web-based, and relies on coloured tiles to give hints, how would you like that represented in a text-based environment?
```
Response Feedback: 	[You're hired!]

___
### Question 3
Complete 	

**Clarifying Question 1. Your assessor must be able to determine what aspect of the brief you are responding to. Please include what part of the brief led to the question. For example: "You mentioned in the video..."**  

Selected Answer: 	
```
You mentioned you would like a prototype ASAP, could you give me an idea of your ideal timeframe, including major milestones?
```
Response Feedback: 	[Amazing!]

___
### Question 4
Complete

**In your own words, summarise "What is Wordle" and the project requirements.**  

Selected Answer: 	
```
### What is Wordle
Wordle is a free online puzzle game where each user is given 6 chances to guess a 5-letter word based on clues. 
In the case of NYT-Wordle, the clues are based the tiles (each letter) being coloured:  
Green tile: The letter is in the word and in the correct spot.
Yellow tile: The letter is contained in the word, but not in the correct spot
Grey tile: The letter is not in the word at any spot.

Part of the game's appeal is that the game is restarted once per day, with all players attempting the same word.

### Client Requirements
* build a prototype of a clone of wordle (under guidance) in CLI to better understand the game logic, and the algorithms and how to interact with it.
* This lets the company decide if they want to to devlop their own unique take on the game.
* Ensure I validate the requirements with CEO Raf, as well as Senior Developer Raf.
* Prioritise and Track my own tasks

### Project Mission
* Understand how Wordle works (go play it) - NYT Version
* Ask any clarifying questions (Senior dev Raf will reply)
* Begin working with Senior Dev Raf to come up with the prototype ASAP. - Focus on game logic and playability, don't worry about how it looks ATM.
```
Response Feedback: 	[None Given]

___
### Question 5
Complete 	

During the video briefing, the developer provided an overview of the resources (files) available to assist you in successfully completing the project.  
Please list the names of these files along with a brief description for each.  
The first file has been provided as an example:  
**1. all_words.txt:** A list of all valid words that can be entered, I need to use this list to check that a guess is valid before providing clues.  

Selected Answer: 	
```
1. all_words.txt: A list of all valid words that can be entered, I need to use this list to check that a guess is valid before providing clues.

2. target_words.txt: A list of common words that from which the tatrget word ('word of the day') will be chosen.
```
Response Feedback: 	[None Given]

___
### Question 6
Complete	

1. Ask your Senior Developer your questions to confirm the requirements of the project.
2. Listen carefully to their answers and ask further questions to clarify their answers.
3. Ensure that you fully understand the requirements and the desired outcomes.  
4. Document the responses including any additional information gathered from your Senior Developer’s in the space provided below each of your questions.   

Selected Answer: 	
```
**Question 1:** My questions were a little bit out of scope for now, however "keep it simple" does sort of answer that, and for now just copy the game as it is in the original NYT version.

**Question 2:** To be written in python following PEP 8 standards - this should be pretty much OS agnostic. Use symbols to represent the correctness of guesses for now, don't worry about colour or anything else; the goal is to make the instructions clear and the game playable (with case insensitivity) and number of tries remaining.

**Question 3:** 7 weeks to complete the project, client/developer review meeting will be in a few weeks.

**Additional:**
Documentation must be included: At least one docstring at the top of the program, include comments only where they are useful and choose good variable names.

START
  |
  v
HELP MESSAGE
(how to play)
  |
  v
GET TARGET WORD
(from target_words.txt)
  |
  v
PROMPT FOR GUESS <-----------------------------   <-----------------------------
                                               |                                |
                             Provide different messages for why invalid         |
IS GUESS VALID                Invalid does not count aginst guess count         |
(length, syntax,                               |                                |
in valid-words.txt?)---> NO -------------------                                 |
 |                                                                              |
yes                                                                   increment guess count by 1
 |                                                                              |        
 v                                                                              |
SCORE GUESS-------------->INCORRECT-------> [ATTEMPTS > MAX ATTEMPTS?]----NO----
 |                                                        |                        
CORRECT!                                                 yes
(print a nice win message)                                |
                                                          v
                                                Print a nice loss message
                                            Include what the winning word was
```
Response Feedback: 	[None Given]

___
### Question 7
Complete

In the section below, confirm that you have located and identified each of the files you listed above.  
Use this format:  
>I < your name > have been able to locate and access each of the files on < date >.

Selected Answer: 	
```
I have been able to locate and access each of the files on 27/3/2024.
```
Response Feedback: 	[None Given]