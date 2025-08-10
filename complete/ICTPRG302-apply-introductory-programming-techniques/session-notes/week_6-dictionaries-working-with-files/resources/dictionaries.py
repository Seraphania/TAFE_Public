# create a dictionary of students
#            Name      Student number
students = {'Thomas':  2002,
            'Nic':     2003,
            'Kosta':   2004,
            'Puren':   2009}

# another way to add students:
students['Damon'] = 2010

# prints the students
print(students)

# iterate over the keys (just the names in this case)
for student in students:
    print(student)

# iterate over the values (until we learn a better way):
for student in students:
    print('Key[name]:', student)
    print('Value[num]:', students[student])


# Look up if a key is in a dictionary:
print("Student Checker 3.0")
print("Checks students ")
while True:
    student = input("Provide a student name: ")
    if student == 'quit':
        break
    if student in students:
        print("Student registered")
        print(f"Student number {students[student]}
    else:
        print("Unknown student")

    
# Defining a dictionary
chem = dict()
chem = {}
chem  = {"H": "Heroin",
         "He": "Helium",
         "Li": "Lithium",
         "R": ("Rafium", 42),      
         }

# Dictionary methods
print(chem["H"])
chem["Be"] = "Beryllium" # Adds
print(chem)
chem["He"] = "Halium", 2 # updates, if it exists it will be changed, if it doesn't, it weill be added.


# Getting Values
print(chem["H"]) # Case sensitive
print(chem.get("R", "Don't know too hard")) # Get won't error if a key doesn't exist
chem["hg"] = 42
chem["pb"] = chem["hg"] +2 

print("Au" in chem) # False (Serach, only works for keys, not values)

# to get all vlaues
for item in chem:
    print('key', item, 'value', chem[item])
print("Keys", chem.keys())
print("Keys", chem.values())
print("Keys", chem.items()) # returns tuple with key and value can unpack tuples
for key, value in chem:
    print(key, value)

# Functions are first class objects, cna be treated like any other object - can be keys or values in d dictionaries!