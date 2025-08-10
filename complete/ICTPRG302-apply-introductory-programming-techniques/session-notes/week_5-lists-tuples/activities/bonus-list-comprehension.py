#### BONUS: List Comprehension
### Reading Comprehension Excercises



## Reading Comprehension: Using ``range``:
# Using range in a for-loop, print the numbers 10-1, in sequence.
for i in range(10, 0, -1):
    print(i)

## Reading Comprehension: Writing a Generator Comprehension:
# Using a generator comprehension, define a generator for the series:  
# `(0, 2).. (1, 3).. (2, 4).. (4, 6).. (5, 7)`  
# *Note that (3, 5) is NOT in the series.*
# Iterate over the generator and print its contents to verify your solution.
gen = ((i, i+2) for i in range(6) if i != 3)
for item in gen:
    print(item)

## Reading Comprehension: Using Generator Comprehensions on the Fly:
# In a single line, compute the sum of all of the odd-numbers in 0-100.
print(f"{sum(i for i in range(101) if i%2 != 0)}")

## Reading Comprehension: List Comprehensions:
# Use a list comprehension to create a list that contains the string “hello” 100 times.
hello_100 = [[''.join(str(i)) + '. hello'] for i in range(101)]
print(hello_100)

# ### Reading Comprehension: Fancier List Comprehensions:
# Use the inline if-else statement (discussed earlier in this module), along with a list comprehension, to create the list:
# ```
# ['hello',
#  'goodbye',
#  'hello',
#  'goodbye',
#  'hello',
#  'goodbye',
#  'hello',
#  'goodbye',
#  'hello',
#  'goodbye']
# ```

greet = [('hello' if i%2 == 0 else 'goodbye') for i in range(10)]
print(greet)

## Reading Comprehension: Tuple Comprehensions:
# Use a tuple-comprehension to extract comma-separated numbers from a string, converting them into a tuple of floats. I.e. `"3.2,2.4,99.8"` should become `(3.2, 2.4, 99.8)`. You will want to use the built-in string function `str.split`.
string = "3.2,2.4,99.8"
print(f"{tuple(float (i) for i in string.split(','))}")

## Reading Comprehension: Translating a For-Loop:
# Replicate the functionality of the the following code by writing a list comprehension.
# ```python
# # skip all non-lowercased letters (including punctuation)
# # append 1 if lowercase letter is equal to "o"
# # append 0 if lowercase letter is not "o"
# out = []
# for i in "Hello. How Are You?":
#     if i.islower():
#         out.append(1 if i == "o" else 0)
# ```
out = [(1 if i == 'o' else 0) for i in "Hello. How Are You?" if i.islower()]
print(out)

## Reading Comprehension: Memory Efficiency:
# Is there any difference in performance between the following expressions?
# ```python
# # feeding `sum` a generator comprehension
# sum(1/n for n in range(1, 101))
# ```

# ```python
# # feeding `sum` a list comprehension
# sum([1/n for n in range(1, 101)])
# ```
# Is one expression preferable over the other? Why?
'''
The generator expression would be preferable. The list comprehension requires all the items in the list to be calculated and kept in memory until the end of the list, then summed. Whereas in the generator  expression each element can be calculated, added to the sum, and then discarded. This becomes more relevant for larger data sets.
'''
