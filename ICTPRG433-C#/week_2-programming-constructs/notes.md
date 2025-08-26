# Contents
- [Contents](#contents)
- [Week 2/Session 2 - Programming Constructs](#week-2session-2---programming-constructs)
  - [Totally Cool but Unrelated Content ☻](#totally-cool-but-unrelated-content-)
  - [Overview](#overview)
  - [Notes](#notes)
    - [Operators](#operators)
      - [Arithmetic](#arithmetic)
      - [Comparison](#comparison)
      - [Logical](#logical)
      - [Truth Tables](#truth-tables)
      - [Unary/Binary/Ternary](#unarybinaryternary)
    - [Program Constructs](#program-constructs)
    - [Selection Constructs](#selection-constructs)
      - [If Statements](#if-statements)
      - [Switch Statements](#switch-statements)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 2/Session 2 - Programming Constructs
31/7/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/webapps/blackboard/content/listContent.jsp?course_id=_26457_1&content_id=_2687045_1)  
[Class Code](https://github.com/chris-arnold-nmtafe/csharp-sem2-2025)  

## Totally Cool but Unrelated Content ☻
floats in C# are less accurate than decimal:
```cs
decimal accurate = 1.234567891234567M;
float notAccurate = 1.234567891234567f;

Console.WriteLine(accurate); // returns 1.234567891234567
Console.WriteLine(notAccurate); // returns 1.2345679
```

## Overview
Operators and program constructs (selection, iteration and sequence)
Selection - If/Else and Switch/Case

## Notes
### Operators
These are similar to Python.

#### Arithmetic
* `+` is addition, it also works to concatenate strings together. If used with a number and a string the number will be elevated to a string and appended.
  ```cs
  int number1 = 42;
  double number2 = 13.37;
  string message = $"The answer is {number1}, this is {number2}!";
  ```
* `-`, `*`, `/` and  `%`  All work the same as Python.

#### Comparison
The comparison operators `>`, `<`, `==`, `<=`, `>=`, and `!=` are all the same as Python. `=` is  the assignment operator, which is why `==` is used for equals.

Returns for comparisons will be:
 * `-1` Less than
 * `0` Equal to, or
 * `1` Greater than
For example:
```cs
Console.WriteLine("aaa".CompareTo("bbb")); // -1
```
Truthy comparisons will return True/False:
```cs
string string1 = "dog cat";
Console.WriteLine(string1 == "dog"); /// will return False
```

Comparisons will provide a boolean output, these can be used with logical operators such as AND, OR and XOR.  


#### Logical
* `&&` AND
  * `(1==2) && (6<10)`
* `||` OR
  * `(1==2) || (6<10)`
* `!` NOT
  * `!(2==2)`
* `^` XOR
  * Returns false if both statements equate the same. i.e. They must be different to return true:  
    `(2==2) ^ (5 > 2)` -> returns false  
    `(5 % 2) == 1 ^ (6 - 5) == 1` -> returns false

#### Truth Tables
See [Wikipedia](https://en.wikipedia.org/wiki/Truth_table) for more about truth tables.  
Quick truth table reference:  

**AND**
| P       | Q       | P AND Q |
|---------|---------|---------|
| TRUE    | TRUE    | TRUE    |
| TRUE    | FALSE   | FALSE   |
| FALSE   | TRUE    | FALSE   |
| FALSE   | FALSE   | FALSE   |
*And is true if both are true*

**OR**
| P       | Q       | P OR Q  |
|---------|---------|---------|
| TRUE    | TRUE    | TRUE    |
| TRUE    | FALSE   | TRUE    |
| FALSE   | TRUE    | TRUE    |
| FALSE   | FALSE   | FALSE   |
*Or is TRUE if both are TRUE as well*

**XOR**
| P       | Q       | P XOR Q |
|---------|---------|---------|
| TRUE    | TRUE    | FALSE   |
| TRUE    | FALSE   | TRUE    |
| FALSE   | TRUE    | TRUE    |
| FALSE   | FALSE   | FALSE   |
*Exclusive OR, only P or only Q*

**NOT**
| P       | NOT P   |
|---------|---------|
| TRUE    | FALSE   |
| FALSE   | TRUE    |
*Only needs a single operand, basically flips the value*

**NAND:** Take an AND and flip it!

#### Unary/Binary/Ternary
Unary, Binary and Ternary operators refer to the number of arguments.  
* **Unary Operators** are a hangover from C, these are operators that only take one argument. NOT is a unary operator.
  * `++` increment
  * `--` decrement
  * `i++` / `++i` suffix vs prefix
    * Unary operators can be used before or after a variable but they are handled slightly differently:  
      ```cs
      int x = 0;
      Console.WriteLine(++x); // returns 1
      Console.WriteLine(x++); // returns 1 - sends 'x' to Console.WriteLine, THEN increments
      Console.WriteLine(x); // will return 2
      // Same thing with decrement.
      ```
      also; 
      ```cs
      int x = 0;
      Console.WriteLine(x++ + x++); // returns 1
      Console.WriteLine(x); // will return 2
      // Same thing with decrement.
      ```
* **Binary Operators** are typical of comparisons:  
  `argument == argument 2`

* **Ternary Operators** are made up with two characters: `( ? : )`  
  the operators are something that is evaluated, and then what is done in the case of true or false:  
  `true ? "hello" : "goodbye"` 
  Similar to Excel IF statements. Fairly rarely used.

### Program Constructs
Program constructs (as in Python) are Selection, Iteration and Sequence Constructs.
* **Selection** Provides alternative paths by using statements like if and switch.
* **Iteration** Repeats blocks of code; For loops iterate a fixed number of times, While loops iterate a variable number of times. 
* **Sequence** Can change the flow of control when executing. Normally programs execute one line at a time, but it is possible to jump around using keywords like Goto (best avoided - it can cause spaghetti), Continue and Break. When a method is called the logic jumps to the code in that method before returning to the calling program.

### Selection Constructs
Selection constructs include `if/else` and `case/switch` statements.  
**`if/else` and `case/switch`:**
* There are very minor performance increases using switch statements.
* Switch statements may improve readability (unless nesting is used).
* Switch can be used on strings, it looks at the the value of a variable rather than a condition.
* For boolean and compound evaluations `if/else` is preferred, switch is more appropriate for basic comparisons.

#### If Statements
If statements are the best known selection statements; 
```cs
if (x == 0)
{ // Items between {} are the scope. In Python this would be indicated by indentation. In C# indentation/whitespace is ignored (though being consistent is a good idea for readability). This is why line terminators ";" and scopes "{}" are necessary.
Console.WriteLine("x is zero");
x = 1;
Console.WriteLine("x was zero");
if (x==1)
{
  Console.WriteLine("x is now 1");
}
}
else if (x == 1)
{
  Console.WriteLine("x is still 1");
}
else
{
  Console.WriteLine("The joke\'s on you! x was never false.");
}
```
***Note:** Items between {} are the scope. In Python this would be indicated by indentation. In C# indentation/whitespace is ignored (though being consistent is a good idea for readability). This is why line terminators `;` and scopes `{}` are necessary.*  

If statements can be nested, although it is best to avoid deep nesting.  
Compound statements can be constructed using logical operators; `if (x > 10 && x < 28)`. Care should be taken to observe operator precedence:  
`if (x > 10 && x - 10 < 20)` - This may work, but is ambiguous.  
`if ((x > 10) && ((x - 10) < 20))` - This is much clearer.  

#### Switch Statements
C# also has switch statements, which will take a variable and match it against a series of conditions, where the condition matches the code will be executed (since V.3.10 Python has something similar, match/case).
```cs
uint myInt = 50; // Unsigned int, also ulong, ushort, byte, sbyte! (signed byte)

switch(myInt)
{
  case 50:
    Console.WriteLine("The int matches 50.");
    break;
  case 60:
    Console.WriteLine("The int matches 60."); // these can all be very different
    break;
  default: // this is similar to else, if nothing matches, do {thing}. 
    Console.WriteLine("No match was found!");
    break;
}
```
Switch statements can be nested, although it is not recommended.  
`default:` can be placed anywhere in a switch statement, however the bottom is preferred (or the top, be consistent!) halfway through is not good.  
Break is used to exit each case in a switch statement, they are not needed for if statements.

___
## Resources
[Lecture Slides](./resources/Introduction-to-CS-Part-2.pptx)  
[Computer Science Basics: Sequences, Selections, and Loops](https://www.youtube.com/watch?v=eSYeHlwDCNA)
[Additional Reading - Iteration](resources/Iteration-Logic.pdf)  
[Additional Reading - Conditional Logic](resources/Conditional-Logic.pdf)  
[Additional Reading - Program Constructs](resources/Program-Constructs.pdf)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Additional Condition Exercises](https://www.w3resource.com/csharp-exercises/conditional-statement/index.php)  

