# PythonMidterm.py
#
# Name: Kevin Alcocer
# Date: 09/29/23
# Class: CIT 95

import datetime     #This is used 
#******* Start of Classes********
class Animal:
    # A counter to keep track of the number of animals we have.    
    animal_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        self.name = name
        self.age = age
        self.birthday = birthday
        self.sex = sex
        self.season_born = season_born
        self.color = color
        self.weight = weight
        self.origin = origin
        self.arrived = arrived
        # self.Hyena = Hyena
        # self.Lion = Lion
        # self.Bear = Bear 
        # self.Tiger = Tiger
        self.ID = ID # def genUniqueAnimalID(): 
        self.habitat = habitat # def genZooHabitat():
        
        Animal.animal_count += 1
    
class Hyena(Animal):
    # A counter to keep track of the number of Hyenas
    hyena_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Hyena'
        Hyena.hyena_count += 1

class Tiger(Animal):
    # A counter to keep track of the number of Tigers
    tiger_count = 0
        
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Tiger'
        Tiger.tiger_count += 1

class Lion(Animal):
    # A counter to keep track of the number of Lions
    lion_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Lion'
        Lion.lion_count += 1

class Bear(Animal):
    # A counter to keep track of the number of Bears
    bear_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
        
    # def genZooHabitat(): 
    #     """Assign each new animal to a habitat. Each species must have its own habitat."""
    #     return self.habitat = 'Bear'
        Bear.bear_count += 1
#*******End of Classes**********


arrivingAnimalstxt = open('c:\\Users\\kalco\\Coding Projects\\Python\\python-midterm-due-oct-15-kalc1\\arrivingAnimals.txt', 'r')
read_arriving = arrivingAnimalstxt.readlines()

arrivingAnimals_list = []               # Turns the content in arrivingAnimals.txt into a list, splits into seperate elements by ',', 
for animal in read_arriving: 
    append_animal = animal.strip().split(',')
    arrivingAnimals_list.append(append_animal)
# print(arrivingAnimals_list)
#arrivingAnimals_list[0][4:6] = [''.join(arrivingAnimals_list[0][4:6])]


new_element_0 = []                      # Splits the first element in each list obtained from arrivingAnimals by spaces. 
for list in arrivingAnimals_list:
    update_list = list[0].split()
    new_element_0.append(update_list)
#print(new_element_0)

# This replaces the newly created lists above with the first item in each list from the original arrivingAnimals_list
for element, new_element in zip(arrivingAnimals_list, new_element_0):
    element[0] = new_element[0:5]
    arrivingAnimals_list.append(element[0])
# print(arrivingAnimals_list[0])
# print(arrivingAnimals_list[0][0])
# print(arrivingAnimals_list[0][0][4])
 
# Here are 4 seperate lists created by slicing the arrivingAnimals_list. 
arriving_Hyenas =  arrivingAnimals_list[0:4]
arriving_Tigers = arrivingAnimals_list[4:8]
arriving_Lions = arrivingAnimals_list[8:12]
arriving_Bears = arrivingAnimals_list[12:16]
# print(arriving_Hyenas)
# print(arriving_Tigers)
# print(arriving_Lions)
#print(arriving_Bears)

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

#  These define the functions that will go into our 
# def genUniqueAnimalID(habitat):
# 	if habitat = hyena:
# 		Hy.ID = "Hy0" + str(hyena_count)
# 	elif habitat = tiger:
# 		Ti.ID = "Ti0" + str(tiger_count)
# 	elif habitat = lion:
# 		Li.ID = "Li0" + str(lion_count)
# 	elif habitat = bear:
# 		Be.ID = "Be0" + str(bear_count)
# 	else:
# 		print("UniqueAnimalID function error")

# def genBirthDay():
# 	arrivingAnimals_list[1] <- modified using datetime.date(year, month, day)
# 	self.birthday
# 	else:
# 		print("genBirthday function error")

# def genAge():
# 	arrivingAnimals_list[0][0][0] + "years old"
# 	self.age
# 	else:
# 		print("genAge function error")

# def genColor():
# 	arrivingAnimals_list[2]
# 	self.color
# 	else:
# 		print("genColor function error")

# def genSex():
# 	arrivingAnimals_list[0][3]
# 	self.sex
# 	else:
# 		print("gensex function error")

# def genWeight():
# 	arrivingAnimals_list[3]
# 	self.weight
# 	else:
# 		print("genWeight function error")

# def genOrigin():
# 	arrivingAnimals_list[4] + arrivingAnimals_list[5]
# 	self.origin
# 	else:
# 		print("genOrigin function error")






# These for-loops create 4 objects per different animal subclass and adds them to the corresponding animal_objects list.
hyena_objects = []
tiger_objects = []
lion_objects = []
bear_objects = []
for i in range(0,4):
    hyena_objects.append(Hyena())
for i in range(0,4):
    tiger_objects.append(Tiger())
for i in range(0,4):
    lion_objects.append(Lion())
for i in range(0,4):
    bear_objects.append(Bear())
merged_objects = (hyena_objects+tiger_objects+lion_objects+bear_objects)
#print(merged_objects)

# This is a skeleton/conceptual format for how the final program should look like:
# def genzooHabitat(habitat):
# 	if habitat = 'hyena':
# 		for i in range(0,4):
# 			Hy = Hyena()
# 			genUniqueAnimalID(habitat)
# 			*insert functions here*
# 			*insert functions here*
# 			*insert functions here*
# 			hyena_objects.append(Hy)
# 	elif habitat = 'tiger':
# 		for i in range(0,4):
# 			Ti = Tiger()
# 			genUniqueAnimalID(habitat)
# 			*insert functions here*
# 			*insert functions here*
# 			*insert functions here*
# 			hyena_objects.append(Ti)
# 	elif habitat = 'lion':
# 		for i in range(0,4):
# 			Li = Lion()
# 			genUniqueAnimalID(habitat)
# 			*insert functions here*
# 			*insert functions here*
# 			*insert functions here*
# 			hyena_objects.append(Li)
# 	elif habitat = 'bear':
# 		for i in range(0,4):
# 			Be = Bear()
# 			genUniqueAnimalID(habitat)
# 			*insert functions here*
# 			*insert functions here*
# 			*insert functions here*
# 			hyena_objects.append(Be)
# 	else:
# 		print("genzooHabitat function error")

# Testing Animal Counters:
# print(Animal.animal_count)
# print(Lion.lion_count)
# print(Hyena.hyena_count)
# print(Bear.bear_count)
# print(Tiger.tiger_count)