"""Guess a number between 1 and 10."""

## Activity 2: Guess the Magic Number
# Objective:  
# Write a program that allows the user to guess a magic number. The program will provide feedback on whether the guess is too high, too low, or correct.  

import random
magic_number = random.randint(1, 10)
guess = int(input("What number between 1 and 10 am I thinking of? "))

if guess == magic_number:
    print(f"Great guess! The number is {magic_number}!")
elif guess < magic_number:
    print(f"Sorry {guess} is too low! the number was {magic_number}.")
else:
    print(f"Sorry {guess} is too high! the number was {magic_number}.")

input("Press any key to exit: ")

# **Discussion question:**  
# 1. How do the selection statements (if, elif, else) and comparison operators (==, <, >) help in guiding the user towards guessing the correct number? 
# They can be used to select different outputs relevant to the user depending on the user's input.
