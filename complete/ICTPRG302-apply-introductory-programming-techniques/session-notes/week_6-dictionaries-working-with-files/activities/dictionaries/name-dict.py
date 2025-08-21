# # Dictionaries - slide 6 & 8

# create an empty dictionary: called names
# create a while loop to use until we break out
# * create an input for the name
# * if the user presses enter break out
# * if the name exists add 1
# * if the name doesnt exist then create the record and add one

# print out the dictionary

names = {}
while True:
    name = input("Name: ")
    if name == "":
        break
    else:
        names[name] = names.get(name, 0) + 1
print(names)

# print the data
names = {"Charlotte": 25,
         "Olivia": 24,
         "Oliver": 17,
         "William": 15,
         "Isla": 10}

print("Print with for loop")
for name in names:
    print(name, names[name])

print("\nprint(list(names))")
print(list(names))
print("\nprint(names.values())")
print(names.values())
print(f"\nprint(names.keys())")
print(names.keys())
print("\nprint(names.items())")
print(names.items())