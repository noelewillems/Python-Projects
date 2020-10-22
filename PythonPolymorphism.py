# Created by Noel Willems for understanding polymorphism in Python.

# Python is polymorphic, in the sense that the child classes have at least the same methods as the parent class. However, these
# individual child methods do different things from each other. If we think about it, Python itself has a lot of polymorphism built in.
# The print() function can take in integers, strings, etc, but depending on the input, it will convert it to a string and print it out.
# Something I found interesting in Python is that you must pass the keyword self to every method in a class. After running into errors,
# I did some research and found this on GeeksForGeeks: "Python decided to do methods in a way that makes the instance to which the method 
# belongs be passed automatically, but not received automatically: the first parameter of methods is the instance the method is called on."
# "self" as a reference to an instance of a class is something that I haven't seen explicitly in other languages yet.

# In regards to private variables, after some research I have come to the conclusion that Python technically doesn't have private 
# variables, but strongly encourages programmers to put the prefix _ before variables they want others to realize as private.
# It's interesting that while this is not a "technical" private variable coded in by the creators of Python, it is a convention (or "syntactic
# sugar") that all self-respecting Python programmers follow.

# In regards to abstract classes, Python does not provide abstract classes by default. The module "ABC" must be added, and the class that
# you wish to be abstract must be declared like this: class Example(ABC). I found this especially interesting - this is basically
# stating that the "abstract" class inherits from a class called ABC that makes it abstract.

zoo = []

class Animal:
    def color(self, color):
        print(color)

class Cow(Animal):
    def color(self, color):
        self.color = color   
    
    def getCol(self):
        print(self.color)  

    def speak(self):
        print("This cow says moo and is ", end="")

class Cat(Animal):
    def color(self, color):
        self.color = color

    def getCol(self):
        print(self.color)    
    
    def speak(self):
        print("This cat says meow and is ", end="")

class Horse(Animal):
    def color(self, color):
        self.color = color   

    def getCol(self):
        print(self.color)  
    
    def speak(self):
        print("This horse says neigh and is ", end="")

cow = Cow()
cow.color("white")
zoo.append(cow)

cat = Cat()
cat.color("calico")
zoo.append(cat)

horse = Horse()
horse.color("dapple gray")
zoo.append(horse)

for i in zoo:
    i.speak()
    i.getCol()
