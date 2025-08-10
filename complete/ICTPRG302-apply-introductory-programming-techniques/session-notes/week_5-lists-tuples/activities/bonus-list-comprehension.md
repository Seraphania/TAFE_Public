## BONUS: List Comprehension
>The following optional exercises are not assessable in this unit, but they will let you feel like a Python master and for the IoT students, you will need to understand list comprehension for some of the exercises.

**Did you say you want more?**

Our journey with py4e ended with a mysterious bit of syntax:  
```python
sorted([(v,k) for k,v in d.items()])
```

*What is it? What does it mean? And should you care?*  

Answer: list comprehension; Python is awesome; and yes!  

This is one of the most powerful aspects of Python and it combines compactness with readability (when used correctly) and allows us to flatten nesting (that's good). If you go beyond beginner Python, you will start to see this construct all the time. It can be a bit intimidating at first, but it is an indispensable part of pythonisting.  

The best tutorial I can recommend for it is here:  

[Generators & Comprehension Expressions — Python Like You Mean It](https://www.pythonlikeyoumeanit.com/Module2_EssentialsOfPython/Generators_and_Comprehensions.html)  

Make sure to complete the callouts labelled **"Reading Comprehension"**; answers are at the end. 

## Reading Comprehension Excercises

### Reading Comprehension: Using ``range``:
Using range in a for-loop, print the numbers 10-1, in sequence.

### Reading Comprehension: Writing a Generator Comprehension:
Using a generator comprehension, define a generator for the series:  
`(0, 2).. (1, 3).. (2, 4).. (4, 6).. (5, 7)`  
*Note that (3, 5) is not in the series.*
Iterate over the generator and print its contents to verify your solution.

### Reading Comprehension: Using Generator Comprehensions on the Fly:
In a single line, compute the sum of all of the odd-numbers in 0-100.

### Reading Comprehension: List Comprehensions:
Use a list comprehension to create a list that contains the string “hello” 100 times.

### Reading Comprehension: Fancier List Comprehensions:
Use the inline if-else statement (discussed earlier in this module), along with a list comprehension, to create the list:
```
['hello',
 'goodbye',
 'hello',
 'goodbye',
 'hello',
 'goodbye',
 'hello',
 'goodbye',
 'hello',
 'goodbye']
```

### Reading Comprehension: Tuple Comprehensions:
Use a tuple-comprehension to extract comma-separated numbers from a string, converting them into a tuple of floats. I.e. `"3.2,2.4,99.8"` should become `(3.2, 2.4, 99.8)`. You will want to use the built-in string function `str.split`.

### Reading Comprehension: Translating a For-Loop:
Replicate the functionality of the the following code by writing a list comprehension.
```python
# skip all non-lowercased letters (including punctuation)
# append 1 if lowercase letter is equal to "o"
# append 0 if lowercase letter is not "o"
out = []
for i in "Hello. How Are You?":
    if i.islower():
        out.append(1 if i == "o" else 0)
```

### Reading Comprehension: Memory Efficiency:
Is there any difference in performance between the following expressions?
```python
# feeding `sum` a generator comprehension
sum(1/n for n in range(1, 101))
```

```python
# feeding `sum` a list comprehension
sum([1/n for n in range(1, 101)])
```
Is one expression preferable over the other? Why?
