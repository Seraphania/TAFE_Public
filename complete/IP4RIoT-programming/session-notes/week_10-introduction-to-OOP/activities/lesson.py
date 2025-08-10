## Create a class:
class Cat:
    pass

## Check the type of 'cat' class
print(type(Cat))
# <class 'type'> ... need to instantiate the class

## Call the class to get an instance of that class
cat = Cat() 
print(type(cat))
# <class '__main__.Cat'>

## Add attributes to an instance:
cat.name = 'Lenny'
cat.age = 3

## Access attributes using the '.' operator:
print(cat.name)
print(cat.age)
# Lenny
# 3

cat2 = Cat()
cat2.bark = "Woof, Woof" # Oh no! A barking cat
## print(cat2.name) # Oops forgot to set the name!
# AttributeError: 'Cat' object has no attribute 'name'

## Add attributes to the cat class:
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

## Example:
class Cat:
    def meow(self):
        print("Meow!")

my_cat = Cat()
my_cat.meow()  # Python internally calls Cat.meow(my_cat)

# in fact you can do exactly that, and the two are equivalent:
Cat.meow(my_cat)

#cat = Cat('Whiskers', 3)
#print(cat.name)
#print(cat.age)

# cat2 = Cat('Kenny') # Error! We must pass the age

## Define Method:
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says "Meow"')

cat = Cat('Lenny', 3)
cat.meow()



## 1. Add a coat color attribute to the Cat class. Instantiate a Cat instance and print the name, age, and coat_color attributes.
class Cat:
    def __init__(self, name, age, coat):
        self.name = name
        self.age = age
        self.coat = coat

    def meow(self):
        print(f'{self.name} says "Meow"')

    def purr(self):
        print(f'{cat.name} purrs...')

    def meet(self, other):
        if isinstance(other, Cat):
            print(f'{self.name} purrs at {other.name}')
        else:
            print(f'{self.name} hisses at {other.name}')

cat = Cat('Lenny', 3, 'Black')
print(f"The cat's name is {cat.name}, he is {cat.age} years old, and a coat that is {cat.coat} ")

## 2. Add a purr method to the Cat class that prints <name> purrs. Call the purr method on the Cat instance.
cat.purr()

## 3. Define a class Dog that has a name and an age attribute. Instantiate a Dog instance and print the name and age attributes.
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def bark(self):
        print(f'{dog.name} barks...')

    def meet(self, other):
        if isinstance(other, Dog):
            print(f'{self.name} wags their tail at {other.name}')
        else:
            print(f'{self.name} barks at {other.name}')

dog = Dog('Goldie', 4)
print(f"The dog''s name is {dog.name} and she is {dog.age} years old")

## 4. Add a bark method to the Dog class that prints <name> barks. Call the bark method on the Dog instance.
dog.bark()

### Challenge exercise
## 1. Define a method in both the Cat and Dog class called "meet" when a cat gets passed a cat or a dog it will "hisses at <other's name>".
cat1 = Cat('Tex', 3, 'Orange')
cat.meet(dog)
cat.meet(cat1)

## 2. When a dog gets passed a cat it will bark but when passed a dog it will wag its tail.
dog1 = Dog('Luna', 5)
dog.meet(cat1)
dog.meet(dog1)