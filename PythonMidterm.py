# PythonMidterm.py
#
# Name: Kevin Alcocer
# Date: 09/29/23
# Class: CIT 95

#******* Start of Classes: 
# class Animal:
#     def __init__(self, name, age, sex, season_born, color, weight, location, country)
#     self.name = 
#     self.age = 
#     self.sex = 
#     self.season_born = 
#     self.color = 
#     self.weight = 
#     self.location = 
#     self.country = 
    
# class Hyena(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = 
#     self.habitat = (f"Hy"

# class Tiger(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = 
#     self.habitat = (f"Ti"

# class Lion(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = 
#     self.habitat = (f"Li" 

# class Bear(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = 
#     self.habitat = (f"Be"
#*******End of Classes


arrivingAnimalstxt = open('c:\\Users\\kalco\\Coding Projects\\Python\\python-midterm-due-oct-15-kalc1\\arrivingAnimals.txt', 'r')
read_arriving = arrivingAnimalstxt.readlines()

arrivingAnimals_list = []               # Turns the content in arrivingAnimals.txt into a list
for animal in read_arriving: 
    arrivingAnimals_list.append(animal.strip())
print(arrivingAnimals_list)

# def genBirthDay(): 
#   """Calculate a birthday from the information received from the originating zoo. Handle cases where the birth season is unknown."""

# def genUniqueAnimalID(): 
#   """Calculate a unique ID to uniquely identify each animal in your zoo."""

# def genAnimalName(): 
#   """Create an animal name based on input from a community fundraiser (animalNames.txt)."""

# def genZooHabitat(): 
#   """Assign each new animal to a habitat. Each species must have its own habitat."""

# https://www.youtube.com/watch?v=JeznW_7DlB0 38:48 uses f-strings to output attributes. Might be useful for above functions ^^^