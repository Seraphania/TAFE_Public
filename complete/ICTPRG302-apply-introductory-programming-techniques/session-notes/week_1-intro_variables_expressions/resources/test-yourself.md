## Test yourself
Here is some code that should start to make sense. Do you know what it does? If you do, you are doing well! Check your answers by running this code in an interactive python >>> shell. 

```python
# Takes a users input of their mood, and incorporates it into a print statement.
mood = input("How are you feeling today?  ")
print("It sounds like your mood is", mood)
```

Consider: why did we assign the user input to a variable?
 - Because it can then be recalled later (in this case in the print statement)

```python
x = 5
x = x + 15
print(x)
# what is the value of x? - 20
```

Here's a tougher one from the lecture:
```python
x = 2
x = 3.5 * x * ( 1 - x )
print(x)
# what is the value of x? - -7
print(type(x))
# what is the type of x? float
# remember, anticipate before you execute
```