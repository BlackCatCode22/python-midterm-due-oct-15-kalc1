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
    # self.Hyena = False
    # self.Lion = False 
    # self.Bear = False 
    # self.Tiger = False
    
# class Hyena(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = # def genUniqueAnimalID(): 
#     self.habitat = "Hyena Habitat" def genZooHabitat():

# class Tiger(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = # def genUniqueAnimalID(): 
#     self.habitat = "Tiger Habitat" def genZooHabitat():

# class Lion(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = # def genUniqueAnimalID(): 
#     self.habitat = "Lion Habitat" def genZooHabitat():

# class Bear(Animal):
#     def __init__(self, name, age, sex, season_born, color, weight, location, country, habitat, ID)
#     super().__init__(name, age, sex, season_born, color, weight, location, country)
#     self.ID = # def genUniqueAnimalID(): 
#     self.habitat = "Bear Habitat" def genZooHabitat():
#*******End of Classes


arrivingAnimalstxt = open('c:\\Users\\kalco\\Coding Projects\\Python\\python-midterm-due-oct-15-kalc1\\arrivingAnimals.txt', 'r')
read_arriving = arrivingAnimalstxt.readlines()

arrivingAnimals_list = []               # Turns the content in arrivingAnimals.txt into a list
for animal in read_arriving: 
    arrivingAnimals_list.append(animal.strip())

# Here are 4 seperate lists created by slicing the arrivingAnimals_list. 
arriving_Hyenas =  arrivingAnimals_list[0:4]
arriving_Tigers = arrivingAnimals_list[4:8]
arriving_Lions = arrivingAnimals_list[8:12]
arriving_Bears = arrivingAnimals_list[12:16]
# print(arriving_Hyenas)
# print(arriving_Tigers)
# print(arriving_Lions)
# print(arriving_Bears)

# This block of code takes the data from animalNames.txt and produces a list for each element in the .txt file and also removes the empty '' elements. 
animalNamestxt = open('c:\\Users\\kalco\\Coding Projects\\Python\\python-midterm-due-oct-15-kalc1\\animalNames.txt', 'r')
read_names = animalNamestxt.readlines()
name_list = []
for name in read_names:
    name = name.strip()
    name_list.append(name)

for name in name_list:
    if name == '':
        name_list.pop(name_list.index(''))
print(name_list)

# Create 4 lists of names:
Hyena_Names = []
Lion_Names = []
Bear_Names = []
Tiger_Names = []
for element in name_list:
    if element == 'Hyena Names:':
        Hyena_Names.append(name_list[name_list.index(element)+1])
print(Hyena_Names)                           


# def genUniqueAnimalID(): 
#   """Calculate a unique ID to uniquely identify each animal in your zoo."""

# def genAnimalName(): 
#   """Create an animal name based on input from a community fundraiser (animalNames.txt)."""

# def genBirthDay(): 
#   """Calculate a birthday from the information received from the originating zoo. Handle cases where the birth season is unknown."""

# def genZooHabitat(): 
#   """Assign each new animal to a habitat. Each species must have its own habitat."""

# https://www.youtube.com/watch?v=JeznW_7DlB0 38:48 uses f-strings to output attributes. Might be useful for above functions ^^^
# lists within dictionaries within a list: https://www.youtube.com/watch?v=6x8oN6FtpLo
# To-Do with the name_list: seperate each of the animal names into 4 different lists. Put those 4 lists into 1 dictionary. Use 'Hyena Names:' as the key(s) for the dictionary for the corresponding animals. 