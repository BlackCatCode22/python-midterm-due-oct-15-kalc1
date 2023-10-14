# PythonMidterm.py
#
# Name: Kevin Alcocer
# Date: 09/29/23
# Class: CIT 95

from datetime import date    # This is used for genBirthDay()
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
        self.ID = ID 
        self.habitat = habitat 
        
        Animal.animal_count += 1  
    
class Hyena(Animal):
    # A counter to keep track of the number of Hyenas
    hyena_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived) 
    
        Hyena.hyena_count += 1

class Tiger(Animal):
    # A counter to keep track of the number of Tigers
    tiger_count = 0
        
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
         
        Tiger.tiger_count += 1

class Lion(Animal):
    # A counter to keep track of the number of Lions
    lion_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
         
        Lion.lion_count += 1

class Bear(Animal):
    # A counter to keep track of the number of Bears
    bear_count = 0
    
    def __init__(self, name='', age='', birthday='', sex='', season_born='', color='', weight='', origin='', ID='', habitat='', arrived=''):
        super().__init__(name, age, birthday, sex, season_born, color, weight, origin, ID, habitat, arrived)
         
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

# Create 4 lists of names seperated by animal taken from name_list above: 
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
#print(len(Hyena_Names[0].split(',')))
# print(Lion_Names)
# print(Bear_Names)
# print(Tiger_Names)

#####  These define the functions that will go into our genZooHabitat for-loop ######
def genUniqueAnimalID(habitat):
    """Calculates a unique ID to uniquely identify each animal in the zoo."""
    if habitat == 'hyena':
        uniqueID = "Hy0" + str(Hyena.hyena_count +1)
        return uniqueID
    elif habitat == 'tiger':
        uniqueID = "Ti0" + str(Tiger.tiger_count +1)
        return uniqueID        
    elif habitat == 'lion':
        uniqueID = "Li0" + str(Lion.lion_count +1)
        return uniqueID
    elif habitat == 'bear':
        uniqueID = "Be0" + str(Bear.bear_count +1)
        return uniqueID
    else:
	    print("UniqueAnimalID function error")
     
def genAnimalName(habitat, i):
    """Create an animal name based on input from a community fundraiser (animalNames.txt)"""
    if habitat == 'hyena':
        name = Hyena_Names[0].split(',')[i].strip()
        return name  
    if habitat == 'tiger':
        name = Tiger_Names[0].split(',')[i].strip()
        return name  
    if habitat == 'lion':
        name = Lion_Names[0].split(',')[i].strip()
        return name  
    if habitat == 'bear':
        name = Bear_Names[0].split(',')[i].strip()
        return name  
    else:
        print("AnimalName function error")

# The datetime module is used here to calculate the date of birth for each animal. In order to calculate the year they were born in, the current year was subtracted from the same element used in the genAge() function below.     
def genBirthDay(habitat, i):
    """Calculates a birthday from the information received from the originating zoo. Handles cases where the birth season is unknown."""
    if habitat == 'hyena':
        season_born = arriving_Hyenas[i][1]
        if season_born == ' born in spring':
            birthday = date(date.today().year - int(arriving_Hyenas[i][0][0]), 3, 21)
            return birthday
        elif season_born == ' born in fall':
            birthday =  date(date.today().year - int(arriving_Hyenas[i][0][0]), 9, 21)
            return birthday
        elif season_born == ' born in winter':
            birthday = date(date.today().year - int(arriving_Hyenas[i][0][0]), 12, 21)
            return birthday
        elif season_born == ' born in summer':
            birthday = date(date.today().year - int(arriving_Hyenas[i][0][0]), 6, 21)
            return birthday
        else:
            birthday = date.today().year - int(arriving_Hyenas[i][0][0])
            return ('Year ' + str(birthday))
    if habitat == 'tiger':
        season_born = arriving_Tigers[i][1]
        if season_born == ' born in spring':
            birthday = date(date.today().year - int(arriving_Tigers[i][0][0]), 3, 21)
            return birthday
        elif season_born == ' born in fall':
            birthday =  date(date.today().year - int(arriving_Tigers[i][0][0]), 9, 21)
            return birthday
        elif season_born == ' born in winter':
            birthday = date(date.today().year - int(arriving_Tigers[i][0][0]), 12, 21)
            return birthday
        elif season_born == ' born in summer':
            birthday = date(date.today().year - int(arriving_Tigers[i][0][0]), 6, 21)
            return birthday
        else:
            birthday = date.today().year - int(arriving_Tigers[i][0][0])
            return ('Year ' + str(birthday))
    if habitat == 'lion':
        season_born = arriving_Lions[i][1]
        if season_born == ' born in spring':
            birthday = date(date.today().year - int(arriving_Lions[i][0][0]), 3, 21)
            return birthday
        elif season_born == ' born in fall':
            birthday =  date(date.today().year - int(arriving_Lions[i][0][0]), 9, 21)
            return birthday
        elif season_born == ' born in winter':
            birthday = date(date.today().year - int(arriving_Lions[i][0][0]), 12, 21)
            return birthday
        elif season_born == ' born in summer':
            birthday = date(date.today().year - int(arriving_Lions[i][0][0]), 6, 21)
            return birthday
        else:
            birthday = date.today().year - int(arriving_Lions[i][0][0])
            return ('Year ' + str(birthday))
    if habitat == 'bear':
        season_born = arriving_Bears[i][1]
        if season_born == ' born in spring':
            birthday = date(date.today().year - int(arriving_Bears[i][0][0]), 3, 21)
            return birthday
        elif season_born == ' born in fall':
            birthday =  date(date.today().year - int(arriving_Bears[i][0][0]), 9, 21)
            return birthday
        elif season_born == ' born in winter':
            birthday = date(date.today().year - int(arriving_Bears[i][0][0]), 12, 21)
            return birthday
        elif season_born == ' born in summer':
            birthday = date(date.today().year - int(arriving_Bears[i][0][0]), 6, 21)
            return birthday
        else:
            birthday = date.today().year - int(arriving_Bears[i][0][0])
            return ('Year ' + str(birthday))
    else:
	    print("genBirthday function error")

def genAge(habitat, i):
    if habitat == 'hyena':
            age = str(arriving_Hyenas[i][0][0]) + ' years old'
            return age
    elif habitat == 'tiger':
            age = str(arriving_Tigers[i][0][0]) + ' years old'
            return age
    elif habitat == 'lion':
            age = str(arriving_Lions[i][0][0]) + ' years old'
            return age
    elif habitat == 'bear':
            age = str(arriving_Bears[i][0][0]) + ' years old'
            return age
    else:
        print("genAge function error")

def genColor(habitat, i):
    if habitat == 'hyena':
        color = str(arriving_Hyenas[i][2])
        return color
    if habitat == 'tiger':
        color = str(arriving_Tigers[i][2])
        return color
    if habitat == 'lion':
        color = str(arriving_Lions[i][2])
        return color
    if habitat == 'bear':
        color = str(arriving_Bears[i][2])
        return color
    else:
        print("genColor function error")

def genSex(habitat, i):
    if habitat == 'hyena':
        sex = str(arriving_Hyenas[i][0][3])
        return sex
    if habitat == 'tiger':
        sex = str(arriving_Tigers[i][0][3])
        return sex
    if habitat == 'lion':
        sex = str(arriving_Lions[i][0][3])
        return sex
    if habitat == 'bear':
        sex = str(arriving_Bears[i][0][3])
        return sex
    else:
        print("gensex function error")

def genWeight(habitat, i):
    if habitat == 'hyena':
        weight = str(arriving_Hyenas[i][3])
        return weight
    if habitat == 'tiger':
        weight = str(arriving_Tigers[i][3])
        return weight
    if habitat == 'lion':
        weight = str(arriving_Lions[i][3])
        return weight
    if habitat == 'bear':
        weight = str(arriving_Bears[i][3])
        return weight
    else:
        print("genWeight function error")

def genOrigin(habitat, i):
    if habitat == 'hyena':
        origin = str(arriving_Hyenas[i][4] + ',' + arriving_Hyenas[i][5])
        return origin
    if habitat == 'tiger':
        origin = str(arriving_Tigers[i][4] + ',' + arriving_Tigers[i][5])
        return origin
    if habitat == 'lion':
        origin = str(arriving_Lions[i][4] + ',' + arriving_Lions[i][5])
        return origin
    if habitat == 'bear':
        origin = str(arriving_Bears[i][4] + ',' + arriving_Bears[i][5])
        return origin
    else:
        print("genOrigin function error")

# These for-loops create 4 objects per different animal subclass and adds them to the corresponding animal_objects list.
hyena_habitat = []
tiger_habitat = []
lion_habitat = []
bear_habitat = []

# This function defines a program which creates and adds animal objects to the appropriate habitat. As the animals are added, the appropriate attributes are given using various functions defined above. 
def genzooHabitat(habitat):
    """Assign each new animal to a habitat. Each species must have its own habitat."""
    if habitat == 'hyena':
        for i in range(0,4):
            hyena_habitat.append(Hyena(ID = genUniqueAnimalID(habitat),
                                    age = genAge(habitat, i), 
                                    color = genColor(habitat, i), 
                                    sex = genSex(habitat, i), 
                                    weight = genWeight(habitat, i), 
                                    origin = genOrigin(habitat, i), 
                                    name = genAnimalName(habitat, i),
                                    birthday = genBirthDay(habitat, i)))
    elif habitat == 'tiger':
        for i in range(0,4):
            tiger_habitat.append(Tiger(ID = genUniqueAnimalID(habitat),
                                    age = genAge(habitat, i), 
                                    color = genColor(habitat, i), 
                                    sex = genSex(habitat, i), 
                                    weight = genWeight(habitat, i), 
                                    origin = genOrigin(habitat, i), 
                                    name = genAnimalName(habitat, i),
                                    birthday = genBirthDay(habitat, i)))
    elif habitat == 'lion':
        for i in range(0,4):
            lion_habitat.append(Lion(ID = genUniqueAnimalID(habitat),
                                    age = genAge(habitat, i), 
                                    color = genColor(habitat, i), 
                                    sex = genSex(habitat, i), 
                                    weight = genWeight(habitat, i), 
                                    origin = genOrigin(habitat, i), 
                                    name = genAnimalName(habitat, i),
                                    birthday = genBirthDay(habitat, i)))
    elif habitat == 'bear':
        for i in range(0,4):
            bear_habitat.append(Bear(ID = genUniqueAnimalID(habitat),
                                    age = genAge(habitat, i), 
                                    color = genColor(habitat, i), 
                                    sex = genSex(habitat, i), 
                                    weight = genWeight(habitat, i), 
                                    origin = genOrigin(habitat, i), 
                                    name = genAnimalName(habitat, i),
                                    birthday = genBirthDay(habitat, i)))
    else:
        print("genzooHabitat function error")

# These 4 functions populate our habitats with the arriving Animals
genzooHabitat('hyena')
genzooHabitat('tiger')
genzooHabitat('lion')
genzooHabitat('bear')

# Testing Animal Counters:
# print(Animal.animal_count)
# print(Lion.lion_count)
# print(Hyena.hyena_count)
# print(Bear.bear_count)
# print(Tiger.tiger_count)

# merged_objects combines all 4 animal habitats into one list.
merged_objects = (hyena_habitat+tiger_habitat+lion_habitat+bear_habitat)
# print(merged_objects)

# These print functions serve to test our outputs
print(hyena_habitat[0].birthday)
print(hyena_habitat[1].birthday)
print(hyena_habitat[3].birthday)
print(tiger_habitat[1].birthday)
print(lion_habitat[2].birthday)
print(bear_habitat[3].birthday)

# print(arriving_Hyenas[0][0][0])


Zoo_Animals_Report = open('midtermOutput.txt', 'w') 
Zoo_Animals_Report.close()