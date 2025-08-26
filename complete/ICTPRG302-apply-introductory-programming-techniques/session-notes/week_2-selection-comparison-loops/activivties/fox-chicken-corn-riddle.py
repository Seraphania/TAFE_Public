"""
The Fox, Chicken and Corn Riddle
Objective:
Help the farmer safely transport the fox, chicken, and corn across the river.

Riddle: 
A farmer needs to cross a river with a fox, a chicken, and a bag of corn. 
The farmer can only take one item at a time. 
If left alone together, the fox will eat the chicken, and the chicken will eat the corn. 
How can the farmer get all three items across the river safely?
"""

bank_1 = []
bank_2 = []

if "chicken" and "fox" in bank_1 or bank_2:
    print("Oh no something's being eaten")
elif "chicken" and "corn" in bank_1 or bank_2:
    print("Oh no something's being eaten!")

    
# * Determine the steps the farmer needs to take to solve the riddle.
# * Draw your process to help you visualise the solution.
# Chicken from bank_1 to bank_2
# Fox from bank_1 to bank_2
# Chicken from bank_2 to bank_1
# Corn from bank_1 to bank_2
# Chicken from bank_1 to bank_2

# **Discussion Question:**  
# 1. How can selection statements help in solving this riddle?  
# Selection statements help to clearly define the logic of a problem, and check if necessary conditions are met.