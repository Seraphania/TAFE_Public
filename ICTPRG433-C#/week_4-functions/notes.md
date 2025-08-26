# Contents
- [Contents](#contents)
- [Week 4/Session 4 - Functions](#week-4session-4---functions)
  - [Totally Cool but Unrelated Content ☻](#totally-cool-but-unrelated-content-)
  - [Overview](#overview)
    - [Why Use Functions](#why-use-functions)
    - [Defining Functions](#defining-functions)
    - [Scope](#scope)
    - [Function Parameters](#function-parameters)
    - [Return Value/Void](#return-valuevoid)
    - [int.TryParse()](#inttryparse)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 4/Session 4 - Functions
14/8/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_26457_1/cl/outline)  
[Class Code](https://github.com/chris-arnold-nmtafe/csharp-sem2-2025)  

## Totally Cool but Unrelated Content ☻
! has multiple uses:
* It's used as a prefix for a logical not:
  ```cs
  bool isTrue=false;
  isTrue = !isTrue;
  ```
* It can also be used to silence warnings using `Console.Readline()!;` sometimes referred to the null forgiving operator, it says that a thing is not null. `?` will keep the null.
* .dll's are class libraries! - dynamic libraries.
* See recording 2 for info about VS solution vs project setup and public/static/class/OOP stuff.
* One main() per project (not solution).
* Default namespace can be set in VSCode.
* Get and set are "accessor methods"

## Overview
Functions  

### Why Use Functions
Functions allow chunking of repeated code into smaller segments of clear purpose. This allows for reusability for repeated statements. It also improves the ability to extend application and update bugs by minimising the places which must be updated.  

Functions create a layer of Abstraction from the inner complexities of the code; for example it is not necessary to know how a `GetArea()` function works it is just required to return the area.

### Defining Functions
Functions are returned using two parts; **[Void](#return-valuevoid) + Identifier**, followed by parentheses which indicate to the compiler that it is a function, [parameters](#function-parameters) may also be passed in these.  
The code within a function is all enclosed withing curly brackets, everything within these is executed when the function is called.  
for example:
```cs
void MyFunction()
{
  Console.WriteLine("test!");
}
```

### Scope
Scope is important when defining blocks of code, particularly with functions. In functions a scope is a block, or the area within the curly brackets.  
Variable definitions are always declared within their surrounding scope, meaning that they can be accessed anywhere within that scope, including within nested, or internal functions.  

Variables within functions cannot be accessed from outside of the functions scope, even within the outer method or class. This is also true for any block statements such as `if`, `else`, `while` etc.  

The example below demonstrates this; the variable `localString` cannot be accessed by the final `Console.WriteLine()` statement:
```cs
static void Main(string[] args)
{
  string mainString = "hello";

  void ScopeIsImportant()
  {
    string localString = "I'm difficult to find!";
    Console.WriteLine(mainString); // This will work.
  }
  Console.WriteLine(localString); // This will not work!
}
```

### Function Parameters
Functions are often augmented by defining and varying inputs; these are called parameters. These are function defined variables that are that have their value set when the function is called.  
Before they are passed, they must be declared within the function itself. This is done inside the brackets:
```cs
void Print(string myMessage);
{
  Console.WriteLine(myMessage);
}
```
The structure of `<type> <identifier>` remains the same as when defining normal variables, however it should be noted that the variable is not assigned a value when defining the function.  
Multiple parameters may be input, they are separated by `,`. They may also have defaults, having a default is optional, and when a parameter has a default, it is known as an optional parameter. Below is an example of such a function, with the parameter `newLine` having the default value of true:
```cs
void Print(string myMessage, bool newLine=true);
{
  if (newLine)
  {
    Console.WriteLine(myMessage);
  }
  else
  {
    Console.Write(myMessage);
  }
}
```
The function above can then be called with `Print("Hello World!", true);` or simply `Print("Hello World!");`; if a parameter has a default its value does not have to be specified when calling the function.  
Optional parameters/parameters with defaults must be specified after all required parameters.  
When calling a function, only the value, not the type is specified.  

### Return Value/Void
When defining a function, `void` is commonly used; this is the ype of value the function will return, void itself means nothing, or "no type" (Similar to pythons NoneType).  

It is equally possible to have a function return any data type or object. If doing so the keyword `return` must be used as well as the value to be returned.  
for example:
```cs
int GetArea(int length, int width)
{
  return length * width
}
```
Where a function returns a value it's output can be stored when the function is called with `int i = GetArea();`.

### int.TryParse()
Validation of input can be done using `int.TryParse()`. This method takes in two things unlike `int.parse()`. The string and the variable that will become the result of the conversion. The function itself actually returns true or false. This means the whole function an be used to check if the value passed was a valid conversion or not:
```cs
int value;
if(int.TryParse(Console.ReadLine(), out value))
{
  //Success!
  Console.WriteLine("Converted string to: " + value);
}
```

Whats different and unique here is that we pass in the variable we are going to change. Typically value types like `int` copy the value into functions. This passes a reference to the variable and updates that particular instance of the int to be the result of the conversion. The keyword `out` is necessary for this to work.

___
## Resources
[Lecture Slides](./resources/Functions.pptx)  
[Video - How Return works](https://www.youtube.com/watch?v=e46wHUjNDjE)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Additional Activities](./activities/CSharp_Functions_Questions.cs)  
