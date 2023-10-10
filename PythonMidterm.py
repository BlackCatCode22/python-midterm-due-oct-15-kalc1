# PythonMidterm.py
#
# Name: Kevin Alcocer
# Date: 09/29/23
# Class: CIT 95

import datetime     #This is used 
#******* Start of Classes********
class Animal:
    # A counter to keep track of the number of animals we have.    
    animal_count = 00
    
    def __init__(self, name, age, birthday, sex, season_born, color, weight, location, country, Hyena, Lion, Bear, Tiger, ID, habitat):
        self.name = ''
        self.age = ''
        self.birthday = ''
        self.sex = ''
        self.season_born = ''
        self.color = ''
        self.weight = ''
        self.location = ''
        self.country = ''
        self.Hyena = False
        self.Lion = False 
        self.Bear = False 
        self.Tiger = False
        self.ID = '' # def genUniqueAnimalID(): 
        self.habitat = '' # def genZooHabitat():
        
        Animal.animal_count += 1
    
class Hyena(Animal):
    # A counter to keep track of the number of Hyenas
    hyena_count = 00
    
    def __init__(self, name, age, sex, season_born, color, weight, location, country, Hyena, Lion, Bear, Tiger, ID, habitat):
        super().__init__(name, age, sex, season_born, color, weight, location, country)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Hyena'

class Tiger(Animal):
    # A counter to keep track of the number of Tigers
    tiger_count = 00
        
    def __init__(self, name, age, sex, season_born, color, weight, location, country, Hyena, Lion, Bear, Tiger, ID, habitat):
        super().__init__(name, age, sex, season_born, color, weight, location, country)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Tiger'

class Lion(Animal):
    # A counter to keep track of the number of Lions
    lion_count = 00
    
    def __init__(self, name, age, sex, season_born, color, weight, location, country, Hyena, Lion, Bear, Tiger, ID, habitat):
        super().__init__(name, age, sex, season_born, color, weight, location, country)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Lion'

class Bear(Animal):
    # A counter to keep track of the number of Bears
    bear_count = 00
    
    def __init__(self, name, age, sex, season_born, color, weight, location, country, Hyena, Lion, Bear, Tiger, ID, habitat):
        super().__init__(name, age, sex, season_born, color, weight, location, country)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Bear'
#*******End of Classes**********


arrivingAnimalstxt = open('c:\\Users\\kalco\\Coding Projects\\Python\\python-midterm-due-oct-15-kalc1\\arrivingAnimals.txt', 'r')
read_arriving = arrivingAnimalstxt.readlines()

arrivingAnimals_list = []               # Turns the content in arrivingAnimals.txt into a list, splits into seperate elements by ',', 
for animal in read_arriving: 
    append_animal = animal.strip().split(',')
    arrivingAnimals_list.append(append_animal)

#arrivingAnimals_list[0][4:6] = [''.join(arrivingAnimals_list[0][4:6])]
# print(arrivingAnimals_list)

new_element_0 = []
for list in arrivingAnimals_list:
    update_list = list[0].split()
    new_element_0.append(update_list)
    
print(new_element_0)
 
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
# print(name_list)

# Create 4 lists of names: 
Hyena_Names = []
Lion_Names = []
Bear_Names = []
Tiger_Names = []
for element in name_list:
    if element == 'Hyena Names:':
        Hyena_Names.append(name_list[name_list.index(element)+1])
    if element == 'Lion Names:':
        Lion_Names.append(name_list[name_list.index(element)+1])
    if element == 'Bear Names:':
        Bear_Names.append(name_list[name_list.index(element)+1])  
    if element == 'Tiger Names:':
        Tiger_Names.append(name_list[name_list.index(element)+1])      
# print(Hyena_Names)                           
# print(Lion_Names)
# print(Bear_Names)
# print(Tiger_Names)

# https://www.youtube.com/watch?v=JeznW_7DlB0 38:48 uses f-strings to output attributes. Might be useful for above functions ^^^
# lists within dictionaries within a list: https://www.youtube.com/watch?v=6x8oN6FtpLo
# To-Do with the name_list: seperate each of the animal names into 4 different lists. Put those 4 lists into 1 dictionary. Use 'Hyena Names:' as the key(s) for the dictionary for the corresponding animals. 
# - move 4 functions I need to define into the parent Animal Class
# - "Do i need to create 1 list with all the animal names? Or 4 different lists with animal names. Probably 4 different lists....
# - Maybe define the different attributes by either string, bool, or int. Place empty placeholders for now (i.e. "" for str, 0 for int, false/true for Bool)
# - Idea: Create booleans for the classes that signify which animal they are.
#             for example: Animal class, Hyena = False, Lion = False, Bear = False, Tiger = False
#             but the child class turns the corresponding Bool True
#             You can then use those booleans to direct how your functions will act
#information hiding: The object-oriented programming principle to only allow the object to have access to the underlying details of the object and hide the data and internal workings from entities outside of it.
# "Methods are typically used to change the state of an object."