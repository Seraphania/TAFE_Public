## Activity 1: String Magic

# **Objective:**  
# Write a program to perform basic operations on a string.  

# **Instructions:**
# 1. Create a string variable 
# 2. Ask user to input their name (Enter your name:)
# 3. Concatenation: Combine the string (user_name) with another string (how are you?)
# 4. Change Case: Convert the string (user_name) to uppercase.

# **Task:**  
# Run the code to see the output. 

# Ask the user to input their name (string)
user_name = input("Please enter your name: ")

## Perform string operations
# Concatenation
print(f"Hello {user_name}")
print(f"how are you today {user_name}?")

# Changing Case
print(f"Uppercase: {user_name.upper()}")

# **Example Output:**  

# Enter your name: Alex
# Concatentaion: Hello Alex, how are you?
# Uppercase: ALEX

# **Discussion question:**   
# 1. What would happen if you removed the spaces in the concatenation line? Try it and observe the result.  
#     *There would be no space between the greeting and the username.*
