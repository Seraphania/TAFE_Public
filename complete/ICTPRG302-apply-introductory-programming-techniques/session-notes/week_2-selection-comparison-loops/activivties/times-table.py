## Activity 1: Learn Your Times Tables
# **Objective:**  
# Create a program that asks the user for a number and then shows its multiplication table using loops.  

# **Instructions:**  
# 1. Ask the user to input a number (integer). `Use the input()` function in Python to get user input.
# 2. Use a **for loop** to iterate through numbers 1 to 10.
# 3. Inside the loop, multiply the user-provided number by the current loop number and print the result.

# **Use the following in your code:**
# * user_number
# * int
# * input
# * number
# * for
# * in
# * range
# * print
# * *
# * =

# Ask the user for a numebr
user_number = int(input("Which times table would you like to see? (Please enter a numebr): "))
print(f"The {user_number} times table is:")
for i in range(1, 11):
    print(f"{user_number} x {i} = {user_number*i}")

exit = input("Press any key to exit")
# **Example Output:**
# ```
# Enter a number: 6
# 6 x 1 = 6
# 6 x 2 = 12 
# 6 x 3 = 18 
# 6 x 4 = 24 
# 6 x 5 = 30 
# 6 x 6 = 36 
# 6 x 7 = 42 
# 6 x 8 = 48 
# 6 x 9 = 54 
# 6 x 10 = 60
# ```

# **Discussion question:**  
# Why is a loop useful in programming?
# Looping can repeat actions for a set number of times, removing the need to repeat code (and reducing chances to make errors.)

