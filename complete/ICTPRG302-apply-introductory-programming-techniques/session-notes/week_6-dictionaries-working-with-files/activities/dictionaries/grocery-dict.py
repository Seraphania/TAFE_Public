
## Slide 12 Grocery Activity
# create an empty dictionary called groceries
groceries = {}

while True: # create a loop to use until we break out by pressing enter
    buy = input("Enter Product & Quantity: ").lower() # lowercase grocery items will will be the key
    if buy == '': # if the user presses enter break out
        break
    items = buy.split() # split the entered grocery name and value
    key = items[0] # get the product name and apply as the key
    try:
        value = int(items[1]) # the quantity must be stored as an integer.
    except: # if no quantity or quantity is not a number, display an error message
        print("Please enter a quantity with your order")
        break ## This could be better - let the user try again
    if key in groceries:  
        groceries[key] = groceries[key] + value # add the key and the value to the dictionary
    else:
        groceries[key] = value  # add the key and the value to the dictionary 

print('')
print(f"{'Item'.ljust(30, " ")}| Quantity") # print out the groceries
for key, value in groceries.items():
    print(f"{key.ljust(30, ".")}| {value}")