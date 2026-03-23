# Object Orientated Programming

from pyscript import display, document


# class Section: # Creating the class
    # def __init__ (self, name, numStudents, level, adviser):
        # self.name = name # Attributes
        # self.numStudents = numStudents # Attributes
        # self.level = level # Attributes
        # self.adviser = adviser # Attributes


# Creating an object/instance 
# section1 = Section("Topaz", 24, "10", "ML Cortez")
# section2 = Section("Sapphire", 25, "10", "Ralph De Guzman")


# display(f'{section1.level}-{section1.name} is part of Red Bulldogs', target="output")
# display(f'{section2.level}-{section2.name} is part of Green Hornets', target="output")


# display(section1.name, target="output")
# display(section1.numStudents, target="output")
# display(section1.level, target="output")
# display(section1.adviser, target="output")

# class Cat:
    # def __init__ (self, name, color, owner):
        # self.name = name
        # self.color = color
        # self.owner = owner
        
        
    # def meow(self): # Creating a method
        # display("Meow! "*3, target="output")


# cat1 = Cat("Pia", "Grey", "Calvin")
# display(f'{cat1.name} is a {cat1.color} cat', target="output")
# cat1.meow()


# Creating a child class
# class Persian(Cat):
    # pass


# cat1 = Persian("Honey", "Biege", "Calvin")
# display(f'{cat1.name} is a {cat1.color} Persian cat', target="output")

class petInfo:
        def __init__ (self, name, age, owner):
            self.name = name
            self.age = age
            self.owner = owner
            
class petBreed(petInfo):
    def __init__ (self, breed):
            self.breed = breed
    
def displayInfo(e):
    output = document.getElementById("output")
    output.innerHTML = ""
    
    name = document.getElementById("name").value
    age = document.getElementById("age").value
    breed = document.getElementById("breed").value
    owner = document.getElementById("owner").value
            
    pet1 = petInfo(name, age, owner)
    breed1 = petBreed(breed)
    
    display(f'Name: {pet1.name}', target="output")
    display(f'Age: {pet1.age}', target="output")
    display(f'Breed: {breed1.breed}', target="output")
    display(f'Owner: {pet1.owner}', target="output")
    
        
        