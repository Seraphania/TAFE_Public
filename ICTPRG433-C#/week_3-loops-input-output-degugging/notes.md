# Contents
- [Contents](#contents)
- [Week 3/Session 3 - Loops, Inputs/Outputs and Debugging](#week-3session-3---loops-inputsoutputs-and-debugging)
  - [Totally Cool but Unrelated Content ☻](#totally-cool-but-unrelated-content-)
  - [Loops](#loops)
    - [While Loop](#while-loop)
    - [Foreach](#foreach)
    - [For Loop](#for-loop)
  - [Input/Output](#inputoutput)
    - [Output](#output)
    - [Input](#input)
  - [Type Conversion](#type-conversion)
    - [Parsing](#parsing)
  - [Debugging](#debugging)
    - [Compile Errors](#compile-errors)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 3/Session 3 - Loops, Inputs/Outputs and Debugging
7/8/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_26457_1/cl/outline)  
[Class Code](https://github.com/chris-arnold-nmtafe/csharp-sem2-2025)  

## Totally Cool but Unrelated Content ☻
* Namespaces are like filesystem folders, they help group things together.
* `using System` a library allowing system level commands, is often utilised to make things work on different operating systems, e.g.:
  ```cs
  Console.WriteLine("Hello, " + System.Environment.Newline + "There"); // Useful if trying to create newlines because windows and *nix based OS's handle line returns differently.
  ```
  Can also system exit (this is a bad idea though).
* putting `@` before a string allows putting line breaks in the string, and they are treated as line breaks.
* Top level statements can be used to input arguments when running a program from the CLI:
  ```cs
  //example.exe / example.cs
  namespace TopLevelExample
  {
    internal class Program
    {
      static void Main(string[] args)
      {
        Console.WriteLine("Hello, World!" + args[0]);
      }
    }
  }
  ```
  If this is run from the CLI as `example hai there!`, the output will be `Hello, World! hai there!"
* 

## Loops
Loops are iteration constructs, there are 3 main types; While, Foreach and For.  
`break;` will break out of the loop when it is encountered, `continue;` will return to the evaluation step.

### While Loop
While loops are very similar to Python
```cs
int i = 0;
int i = 0;
while(i < 3)
{
    Console.WriteLine(++i);
    ++i;
}
```

This can also be written as a do while, this is useful for ensuring that the loop is entered at least once.
```cs

int i = 0;
do 
{
    Console.WriteLine(i);
} while(i < 3);
return; // returns the program to where it was before, should be used after functions.
```

### Foreach
Similar to for in Python
```cs
int[] numbers = new int[3] { 0, 1, 2 };// Array, different from a list, can't be resized (will be covered next week).
foreach(int index in numbers)
{
  Console.WriteLine(index);
}
```

### For Loop
Very different to for in Python; the basic syntax of a for loop is `for ( <initial setup> ; <condition to evaluate> ; <Action at end of loop> ) {...}`
```cs
int[] numbers = new int[3] { 0, 1, 2 };
for (int i=0; i < numbers.Length; i++){
      Console.WriteLine(number[i]);
    }
```

## Input/Output
### Output
To output to the console from a C# console application the `Console.WriteLine()` method is used.  
`Console.WriteLine()` will add a linebreak at the end, `Console.Write()` will not - handy if you want user input on the same line!  
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
Console.WriteLine("My age is:" + myAgeInt);
```

Most of the time a variable must be manually converted to the correct type before evaluation:
```cs
myAgeInt.ToString()
```
another way to do this is the `Convert()` method, it is a good idea to include try catch with this, as it is prone to errors if user input cannot be converted:
```cs
Console.Write("Provide a number: ");
string input=Console.ReadLine();
try 
{
  int num = Convert.ToInt32(input);
}
catch
{
  Console.WriteLine("Houston, we have a problem.");
}
```

This can also be done using Casting:
```cs
(int)myFloat // note the loss of decimal
```
### Parsing
The return value of `Console.ReadLine()` is **always** a string (and case is preserved); converting the input into something more useable such as an integer or a float is *parsing*. Parsing is a function of each type, it is used by calling the `<type>.Parse()` function:
```cs
string input=Console.ReadLine();
int parsedNum=int.Parse(input); // Will also raise errors the same as Convert()...

int number;
bool parsedOK = int.TryParse(input, out number); // Many types have a TryParse method (bool, datetime etc)
if (!parsedOK)
{
  Console.WriteLine("You aint no good");
  return;
}
```
This works for all types that are **not** strings.

## Debugging
### Compile Errors
When compiling and executing code there are often errors that will pop up if there's an issue with the code.  
As C# is compiled most common errors are caught by the compiler. Its important to know how to find the error.

When writing code, it is important to test or validate the program especially with larger more complex applications.  
To do this the program can be paused or stopped using breakpoints, these can be added on the left side of visual studio clicking in the light grey bar just left of the line numbers.

As the program runs it will execute the code until it reaches the line the breakpoint is on.  
It will then stop before that line is executed. As a result, only lines that have statements on them can have a breakpoint.  
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
[Lecture Slides](./resources/Introduction-to-CS-Part-3.pptx)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Additional Exercises](https://www.w3resource.com/csharp-exercises/for-loop/index.php)
