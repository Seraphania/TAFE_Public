## Activity 1: Build a Simple Calculator
# **Objective:**  
# Write a program to create a simple calculator that can perform basic addition and subtraction, using functions.  

# **Instructions:**  
# 1. Define functions for addition and subtraction.
# 2. Create a main function to ask the user for input and call the appropriate function.
def addition(num_1, num_2):
    result = int(num_1) + int(num_2)
    return result

def subtraction(num_1, num_2):
    result = int(num_1) - int(num_2)
    return result

# Main function
def calculator():
    num_1 = int(input("Enter the first number: "))
    num_2 = int(input("Enter the second number: "))
    operator = input("Enter operation (+  or -): ")
    if operator == "+":
        print(f" Result is: {addition(num_1, num_2)}") # This is fine, but...
    elif operator == "-":
        print(f" Result is: {subtraction(num_1, num_2)}") # This is fine, but...
    else:
        print("Invalid Operation")

# For extensibility it is probably preferable to print down here, and even store the result of the calculator() function call in a variable. Not world ending here though.
calculator()
input("Press enter to exit. ")

# **Discussion question:**  
# 1. What would happen if you tried to perform an operation that is not defined in the code (e.g., multiplication)?
# It will print a message "Invalid Operation" - that is covered by my else: statement, however not typing integers will also cause an error, the input should probably be better validated.