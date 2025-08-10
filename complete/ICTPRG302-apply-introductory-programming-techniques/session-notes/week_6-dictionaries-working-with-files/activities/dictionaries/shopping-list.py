# ### Activity 1: Shopping list
# **Objective:** Create a dictionary to represent a shopping list, practice adding, accessing, and modifying key-value pairs.  

# **Instructions:**  
# 1. Start by creating a dictionary.
# 2. Add five grocery items with their quantities (see items and quantities below).
# 3. Access the quantity of the apple and print it.
# 4. Update the quantity of an existing item (milk).
# 5. Remove an item from the dictionary (bananas).
# 6. Run the Program by combining all the steps into a single program and run it to see how it works.

# **Include:**  
# * {}
# * []
# * print()
# * apples, Qty: 4
# * bananas, Qty: 6
# * milk, Qty: 2
# * bread, Qty: 1
# * eggs, Qty: 12

def print_dict(dictionar):
    print("SHOPPING LIST:")
    for key, value in dictionar.items():
        print(key.strip(), value)

shopping_list = {
    'apples': 4,
    'bananas': 6,
    'milk': 2,
    'bread': 1,
    'eggs': 12,
    }

print(f"There are {shopping_list['apples']} apples in the shopping list")

shopping_list['milk'] = 3
print(f"There are {shopping_list['milk']} milk in the shopping list")

del(shopping_list['bananas'])

print_dict(shopping_list)


# **Task:**  
# Run the code to see the output and test the program by adding and removing different items to see how it behaves. Happy coding! 😊

# **Output:**
# ```
# Quantity of apples: 4
# Updated quantity of milk: 3
# Shopping list after removing bananas: ('apples': 4, 'milk': 3, 'bread': 1 'eggs': 12)
# ```

# **Discussion question:**   
# Think of other scenarios where dictionaries could be applied.
# For storing referenceable data where having access to a key or value is important. Because they can contain many types of data, they can be useful for holding and manipulating data.

