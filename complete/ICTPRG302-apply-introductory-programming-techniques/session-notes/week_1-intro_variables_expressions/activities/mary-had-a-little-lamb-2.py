## Activity 1: Mary Had a Little Lamb (Personalised)

# Get user name and animal
your_name = input("Enter your name: ")
your_animal = input("Enter choice of animal: ")
covering = ""
if your_animal.lower == "sheep":
    covering = "fleece"
else:
    covering = "fur"

print(f"{your_name} had a little {your_animal},\n"
    f"Little {your_animal}, little {your_animal},\n"
    f"{your_name} had a little {your_animal},\n"
    f"Its {covering} was white as snow.\n \n"
    f"And everywhere that {your_name} went,\n"
    f"{your_name} went, {your_name} went,\n"
    f"Everywhere that {your_name} went,\n"
    f"The {your_animal} was sure to go.")

# Clear instructions on the type of input expected helps the user to enter the right information so the program doesn't error (or have to ask again)