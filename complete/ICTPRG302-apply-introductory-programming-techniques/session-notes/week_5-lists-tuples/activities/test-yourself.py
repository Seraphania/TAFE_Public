# ## Test yourself

# ### Q1.
# **What are the three key properties of lists?**
# (hint it is on the lesson overview in the notes)
"""
Lists are an ORDERED collection, and that order is maintained
Lists are MUTABLE - can be modified after creation
Lists are HETEROGENEOUS - they can contain elements of different data types
"""

# ### Q2.
# When you modify a string usually the function returns a new string. For example, `'hello'.upper()` returns 'HELLO', it does not modify the original string.  
# When you modify a list. For example `my_list.sort()` the function returns None but instead simply sorts the original list.  
# **Which of the three properties above explains this apparent inconsistency?**
"""
This is due to the mutability of lists. the sorted() function would retun a new list without modifying the original. The purpose of having two different methods to achieve similar restults is to make the difference between modifying and retuning explicit.
"""  

# ### Q3.
# Given the following list named my_items, predict the result of the following slicing operations (use interactive Python to create the list and check your answers)  

# |    0   |  1   |   2    |  3  |   4    |
# |--------|------|--------|-----|--------|
# | 'Eggs' | 42   | 'Spam' | 2.0 | [4, 0] |

# Predict the output of the following in interactive Python:  
# a. `my_items[0]`  'Eggs'
# b. `my_items[1:3]`  42, 'Spam'
# c. `my_items[1:]`  42, 'Spam', 2.0, [4, 0]
# d. `my_items[:3]`  'Eggs', 42, 'Spam', 2.0
# e. `my_items[4][1]`  0
# f. `my_items[2][1:]`  'pam'
# g. `len(my_items)`  5
# h. `type(my_items[3])`  float
# j. `type(my_items)`  list
# h. `len(my_items[2])`  4

my_items = ['Eggs', 42, 'Spam', 2.0, [4, 0]]

print(my_items[0])
print(my_items[1:3])
print(my_items[1:]) 
print(my_items[:3])
print(my_items[4][1])  
print(my_items[2][1:])  
print(len(my_items))
print(type(my_items[3]))  
print(type(my_items))
print(len(my_items[2]))