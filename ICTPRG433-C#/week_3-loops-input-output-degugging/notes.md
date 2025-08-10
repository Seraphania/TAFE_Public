# Contents
- [Contents](#contents)
- [Week 3/Session 3 - Loops, Inputs/Outputs and Debugging](#week-3session-3---loops-inputsoutputs-and-debugging)
  - [Totally Cool but Unrelated Content ☻](#totally-cool-but-unrelated-content-)
  - [Overview](#overview)
  - [Loops](#loops)
    - [While Loop](#while-loop)
    - [For Loop](#for-loop)
    - [Foreach](#foreach)
  - [Input/Output](#inputoutput)
    - [Output](#output)
    - [Input](#input)
  - [Type Conversion](#type-conversion)
  - [Debugging](#debugging)
    - [Compile Errors](#compile-errors)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 3/Session 3 - Loops, Inputs/Outputs and Debugging
7/8/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_26457_1/cl/outline)  
[Class Code](https://github.com/chris-arnold-nmtafe/csharp-sem2-2025)  

## Totally Cool but Unrelated Content ☻
Namespaces are like filesystem folders, they help group things together.

## Overview
From Blackboard if available

## Loops
Loops are iteration constructs, there are 3 main types:  
### While Loop
```cs
While( true )
{
  ...
}
```

### For Loop
```cs
for ( int i=0; i < myArrayLength; i++){
      Console.WriteLine(myArray[i]);
    }
```

### Foreach
```cs
Foreach(int item in myArray)
{
  ...
}
```

## Input/Output
### Output
To output to the console from a C# console application the `Console.WriteLine()` method is used.  
This method takes inputs inside the Brackets `()` in the form of most primitive data types.
String’s, Int’s, Doubles and bools.  
They can be combined in the form of string concatenation using the + operator:
```cs
Console.WriteLine(“This is my string” + myVariable);
```

*Why is WriteLine a method, but ReadLine is a function?* 
- Not an important distinction yet, strictly speaking they are both methods, and the terms are often used interchangeably.  
Functions that exist in classes are called methods, and EVERYTHING is C# is a class, so technically they are all methods.


### Input
In order to take input, the `Console.ReadLine()` function is used. The program waits for the user to enter text into the console and press return. The result of the input is captured in the form of a string value.  
To capture this we the result of the ReadLine() function is assigned to a variable:
```cs
string userInput = Console.ReadLine();
```

## Type Conversion
As C# is strongly typed it is often necessary to evaluate two variables that might not be in the same format.  
This requires Type Conversion, ie changing the type associated with the value of the variable.

Sometimes the compiler handles it, for example:
```cs
Console.Writeline("My age is:" + myAgeInt);
```

Most of the time a variable must be manually converted to the correct type before evaluation:
```cs
myAgeInt.ToString()
```

This can also be done using Casting:
```cs
(int)myFloat // note the loss of decimal
```

The return value of `Console.ReadLine()` is **always** a string (and case is preserved); converting the input into something more useable such as an integer or a float is *parsing*. Parsing is a function of each type, it is used by calling the `<type>.Parse()` function:
```cs
int.Parse("1") == 1
```
This works for all types that are **not** strings.

## Debugging
### Compile Errors
When compiling and executing code there are often errors that will pop up if there's an issue with the code.  
As C# is compiled most common errors are caught by the compiler. Its important to know how to find the error.

When writing code, it is important to test or validate the program especially with larger more complex applications.  
To do this the program can be paused or stopped using breakpoints, these can be added on the left side of visual studio clicking in the light grey bar just left of the line numbers.

As the program runs it will execute the code until it reaches the line the breakpoint is on.  
It will then stop before that line is executed. As a result, only lines that have statments on them can have a breakpoint.  
When the application runs it will halt and switch back to the IDE showing the current file the breakpoint is in.  

This is powerful because it also allows checking the state of the application such as variables and their values.  
It also allows stepping through the code line by line to follow its execution (while continuing to view the state of various variables).  

When in breakpoint mode, visual studio will change the ribbon to display some controls:
* Continue will return the program to normal execution.
* The three blue arrows are the controls that allow stepping through the application, their functions are as follows from left to right:
  * **Step into** – This arrow allows stepping through the code, while also stepping into any functions that the program comes across to view their sequences.
  * **Step over** – This is the most commonly used. It simply steps over each line in programs execution.
  * **Step Out** – This steps up out of the current code block (the opposite of step into). However this will immediately leave the current code block if it can step up.

___
## Resources
[Lecture Slides](./resources/Introduction%20to%20C#%20-%20Part%203(1).pptx)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Additional Exercises](https://www.w3resource.com/csharp-exercises/for-loop/index.php)
