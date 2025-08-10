# ### Activity 1: Shopping list
# **Objective:** Write a program to create and update a shopping list.  

# **Instructions:**
# 1. Start by creating a list with some initial items.
# 2. Add an Item to the List and prompt the user to add an item to the list.
# 3. Prompt the user to remove an item from the list. Hint: Use a `while` loop to ensure the item exists in the list before removing it.
# 4. Run the Program by combining all the steps into a single program and run it to see how it works.

# **Include:**
# * print() -
# * .title() -
# * .append -
# * input() -
# * while -
# * if -
# * not in -
# * else -
# * break -


# **Task:**   
# Run the code to see the output and test the program by adding and removing different items to see how it behaves. Happy coding! 😊  

# 1. Start by creating a list with some initial items.
shopping_list = ['Bread', 'Milk', 'Eggs', 'Vegemite']
print(f"Shopping List:\n{shopping_list}")

# 2. Add an Item to the List and prompt the user to add an item to the list.
shopping_list.append('Potatoes')
print(f"Updated Shopping List:\n{shopping_list}")

user_item = input("Can you think of another item to add to the list? ")
shopping_list.append(user_item.title())
print(f"User Updated Shopping List:\n{shopping_list}")

# 3. Prompt the user to remove an item from the list. Hint: Use a `while` loop to ensure the item exists in the list before removing it.

remove_item = input("Is there any item you would like to remove from the list?: ")

while True:
    if remove_item.title() not in shopping_list:   
        remove_item = input("Please choose an item that is already on the list: ")
    else:
        shopping_list.remove(remove_item.title())
        print(f"Shopping List with {remove_item.title()} removed:\n{shopping_list}")
        break

# **Output 1:**
# ```
# ['Bread', 'Milk', 'Eggs', 'Vegemite']
# Can you think of another item to add to the list?
# ```
 
# **Output 2:**
# ```
# Can you think of another item to add to the list? ham
# ['Bread', 'Milk', 'Eggs', 'Vegemite', 'Ham']
# Is there any item you would like to remove from the list?
# ```

# **Output 3:**
# ```
# Is there any item you would like to remove from the list? milk
# ['Bread', 'Eggs', 'Vegemite', 'Ham']
# ```

# **Discussion question:**   
# How does the use of the while loop in this program ensure that the item to be removed is actually in the list before attempting to remove it? Can you think of any other ways to handle this situation in Python?

## The while loop allows the check to happen as many times as needed until the user enters an item actually on the list. This could be part of a validator function that is called when needed

## A try except block could be used, although they are better suited to system error handling.

