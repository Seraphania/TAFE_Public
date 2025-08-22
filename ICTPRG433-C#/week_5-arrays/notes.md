# Contents
- [Contents](#contents)
- [Week 5/Session 5 - Data Structures](#week-5session-5---data-structures)
  - [Totally Cool but Unrelated Content ☻](#totally-cool-but-unrelated-content-)
  - [Overview](#overview)
  - [Why Use Data Structures](#why-use-data-structures)
  - [Data Structure Types](#data-structure-types)
  - [Arrays](#arrays)
    - [Creating Arrays](#creating-arrays)
      - [Define](#define)
      - [Initialise](#initialise)
      - [Set Values](#set-values)
    - [Accessing Arrays](#accessing-arrays)
    - [Iterating Through Arrays](#iterating-through-arrays)
  - [Resources](#resources)
  - [Activities](#activities)

# Week 5/Session 5 - Data Structures
21/8/2025  
[Blackboard Lesson Materials](https://blackboard.northmetrotafe.wa.edu.au/ultra/courses/_26457_1/cl/outline)  
[Class Code](https://github.com/chris-arnold-nmtafe/csharp-sem2-2025)  

## Totally Cool but Unrelated Content ☻
* ?? null coalesce if not null, print value, else if null print null: `Console.WriteLine(dafs[i]??'null')`.
* Lambda functions are functions without declarations or namespace, used for one-off tasks. `int[] lengths=Array.ConvertAll<string, int>(catNames, x => x.Length);` the `=>` indicates a lambda function.
* Overloading is calling the same function with different variables to get different results. Creating functions that can be overloaded is done by creating two functions with the same name, but different signatures (the signature is the name plus parameters).

## Overview
Data structures include collections, arrays, and lists.  
Will cover:  
* Why collection are needed
* Different types of data structures
* Arrays
  * Defining a new array
  * Accessing arrays
  * Iterating through arrays

## Why Use Data Structures
When defining only a few variables, they are generally defined individually, however when the number of variables increases defining each individually becomes more difficult; it is both time-consuming and harder to read.

Instead if defining variables individually, data structures or collections are used - in this context they are synonyms, but technically classes are also data structures (but not collections).  These collect similar types together allowing space to  define several values but as one variable. The groups *must always be of the same type*. 

## Data Structure Types
Data structure types include:
* **Arrays** - Statically sized collections, they can be 'resized' but this actually returns a new array, similar to python tuples, but can only contain a single data type.
* **Lists** - Dynamic arrays that automatically resize to accommodate the length of the collection.
* **Linked List** - Similar to a list but with different backend functionality; it's not linear in memory; rather each element points to the next element in the list.
* **Dictionary** - A key value pair, typically the key will be a primitive type and the value will be more complex.
* **Binary Tree** - This is a node-based collection where each node has up to two children. They are efficient for fast lookups because they allow quick filtering, they can reduce **algorithmic complexity**.

List vs linked list is a little like random access vs tape: when accessing data, linked lists are efficient if accessing data sequentially, while lists can access data randomly efficiently.

Linked lists have less overhead when adding/removing items from the middle of the list, where lists are slightly more efficient adding/removing from the end of the list.

## Arrays
Arrays are set sized collections; each element is allocated an equal amount of memory space (like horses being allocated stables). Arrays can have empty elements, but the size of the array (and it's memory allocation) does not change.

Arrays are assigned an index, this always starts at 0. Elements can be accessed by their index.

The `Array.` API has Length; the length of the array or items in it. API's for other collection types instead have Count, which is the same thing.

### Creating Arrays
#### Define
Arrays are defined similarly to regular variables; type, identifier and optionally a value, the difference being the use of `[]` to indicate that it is an array; below are some examples:
```cs
int[] myArray;
double[] myDoubles;
float[] myFloats;
string[] myStrings;
bool[] myBools; 
```
**Note:** all of the objects within a collection must be of the same type!

#### Initialise
Because everything in C# is a class, they need to be defined and then initialised, this is also true for variables. This is done by creating a *new* instance and setting its size:
```cs
int[] myArray = new int[20];
double[] myDoubles = new double[10];
float[] myFloats= new float[10];
string[] myStrings = new string[5];
bool[] myBools = new bool[3];
```

#### Set Values
Arrays can be defined and initialised without setting the values, but all values must be set at the same time - once values are being set, ALL values must be set.
```cs
int[] my Array;
myArray = new int[5] {10. 29. 6. 82. 5}; // This is the full syntax.
```
There is a shorthand for declaring, initialising and setting values for an array:
```cs
int[] my Array = {10, 29, 6, 82, 5}; // shorthand needs all variables
```
`new` is where memory allocation occurs. `gcnew` in C++ sets up memory allocation and garbage collection, this is handled automatically in C#. The shorthand syntax implies the length, it does not need to be explicitly stated when using this form.

If an array is initialised, it can be printed, the default value for the type will be populated if no value is set.  
This can be handy for determining default values for different data types:
```cs
int[] list1= new int[4]; 
for (int i = 0; i < list1.length; ++1)
{Console.WriteLine(list1[i])} // prints 0's array is initialised, values not set, defaults are used. 
```
Defaults:
* all numeric types: 0
* string: null
* bool: false
* classes: null
*Null is not printed in C# CLI output, unlike Python*

### Accessing Arrays
Arrays are accessed using their identifier, the same as with other variables, however elements of arrays can also be accessed and updated using their index:
```cs
int[] my Array = {10, 29, 6, 82, 5};

Console.WriteLine(myArray); // will return the entire array
Console.WriteLine(myArray[2]); // will return the item at index 2 (6)

myArray[2] = 12; // replaces the value 6 in the array with 12
```

This can be combined with other operations like checking for inclusion:
```cs
string[] catNames = ["Panther", "Mushroom", "Tex", "Scratchie", "Lenny", "Kenny", "Jank", "Unwieldy"]
bool included = Array.IndexOf(CatNames, "Tex")>=0;
Console.WriteLine(included); // true
```
using `Array.IndexOF` function allows finding the index of any entry:
```cs
int whereIsScratchie = Array.IndexOf(CatNames, "Scratchie");
Console.WriteLine(whereIsScratchie); // will return 3
```
This can be combined with other operations for example to check for all cat names that end with a 'y':
```cs
bool endsWithAY(string, value); // function to find 'ends with y'
{
  return value.EndsWith("y")
}

int ix=Array.FindIndex<string>(CatNames, endsWithAY); // <string> is possibly redundant here, but makes it type safe
Console.WriteLine(ix); // prints the first result that ends in y

string[] endsInYers= Array.FindAll(catNames, endsWithAY); // create a new array that is a subset of the catNames array.
Console.WriteLine(endsInYers.Length + "results found") // print how many cats have names ending with y
// A loop can hen be used to iterate over the endsInYers array to print each element.
```

### Iterating Through Arrays
Iterating through arrays can be done with a [for loop](../week_3-loops-input-output-degugging/notes.md#for-loop):
```cs
void PrintArray(int[] array)
{
  for (int i = 0; i < array.Length; i++)
  {
    Console.WriteLine(array[i]); // Will print each element of the array
  }
}
```

The same can be achieved with a [foreach loop](../week_3-loops-input-output-degugging/notes.md#foreach):
```cs
foreach (int number in numbers)
{
  Console.WriteLine(number);
}
```
___
## Resources
[Lecture Slides](./resources/Data-Structures.pptx)  

## Activities
[In-class activity](./activities/class-activities.md)  
[Additional Online Activities](https://www.w3resource.com/csharp-exercises/array/index.php)  
