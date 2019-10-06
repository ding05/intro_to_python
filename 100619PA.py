"""
class Person:
    ''' Define a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: status()
    '''

    def status(self):
        ''' Return the person's status '''
        if self.bmi < 18.5:
            return 'Underweight'
        if self.bmi >= 18.5 and self.bmi < 25:
            return 'Normal'
        if self.bmi >= 25 and self.bmi < 30:
            return 'Overweight'
        if self.bmi >= 30:
            return 'Obese'

    def __init__(self, name, age, weight, height):
        ''' Create a new Person object with the specified name, age, 
        weight and height '''
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.bmi = weight / (height * height)

    def __str__(self):
        ''' Print persons! '''
        temp = '{0} ({1}) has a bmi of {2:.2f}.'
        return temp.format(self.name, self.age, self.bmi)
"""

class Blork:
    ''' Define the Blork class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_horns of type bool    
    '''

    def __init__(self, name, height, has_horns=False, baranges=0):
        ''' Create a new Blork object '''
        self.name = name
        self.height = height
        self.has_horns = has_horns
        self.name_cap = name.upper()
        self.baranges = baranges
    
    def say_hello(self):
        ''' If the Blork has horns, capitalize the letters '''
        if self.has_horns == True:
            print('HI! MY NAME IS ' + self.name_cap + '!')
        else:
            print('Hi! My name is ' + self.name + '!')
    
    def __str__(self):
        ''' Print Blorks! '''
        if self.has_horns == False:
            temp = '{0} is a {1:.2f} m tall blork!'
            return temp.format(self.name, self.height)
        else:
            temp = '{0} is a {1:.2f} m tall horned blork!'
            return temp.format(self.name, self.height)
    
    def collect_baranges(self, add=1):
        ''' Add one barange '''
        self.baranges = self.baranges + add
        return self.baranges
    
    def eat(self):
        ''' Eat all baranges and rise 0.1 meter for each '''
        if self.baranges > 0:
            self.height = self.height + 0.1 * self.baranges
            return self.height
        else:
            print("I don't have any baranges to eat!")
    
    def feast(self):
        ''' Feast 5 baranges and grow a horn or grow 1 meter '''
        if self.baranges >= 5:
            self.baranges = self.baranges - 5
            if self.has_horns == False:
                self.has_horns = True
                return self.has_horns
            else:
                self.height = self.height * 1.5
                return self.height
        else:
            print("I don't have enough baranges to feast!")

class Car:
    ''' Define the Car calss.
    Data attributes: model of type str
                     year of type float
                     speed of type float
    '''
    
    def __init__(self, model, year, speed=0):
        ''' Create a new Car object '''
        self.model = model
        self.year = year
        self.speed = speed
    
    def accelerate(self):
        ''' Add 5 to the speed data '''
        self.speed = self.speed + 5
        return self.speed
    
    def brake(self):
        ''' Substract 5 from the speed data; stop at 0 '''
        self.speed = self.speed - 5
        if self.speed >= 0:
            return self.speed
        else:
            self.speed = 0
            return self.speed
    
    def honk_horn(self):
        ''' Print a sentense '''
        print(self.model + " goes 'beep beep'")

    def __str__(self):
        ''' Print cars! '''
        temp = '{0} ({1}), moving at {2:.0f} km/h.'
        return temp.format(self.model, self.year, self.speed)

class Plonkle:
    ''' Define the Plonkle calss.
    Data attributes: quality of type str
                     name of type str
                     health of type float
    '''
    
    def __init__(self, quality, name, health):
        ''' Create a new Plonkle object '''
        self.quality = quality
        self.name = name
        self.health = health
        if self.health < 0:
            self.health = 0
    
    def __str__(self):
        ''' Print Plonkles! '''
        if self.quality == 'Grooch' or self.quality == 'Throve' or self.quality == 'Plaguelet':
            temp = '{1} ({0}), health = {2:.1f}'
            return temp.format(self.quality, self.name, self.health)
        else:
            return 'Invalid Plonkle quality'
    
    def inflict(self, num=0):
        ''' Substract num from health '''
        self.health = self.health - num
        if self.health >= 0:
            return self.health
        else:
            self.health = 0
            return self.health

class Stuff:
    ''' Define the Stuff calss.
    Data attributes: name of type str
                     height of type int
                     words of type list
    '''
    
    def __init__(self, name, height, words):
        ''' Create a new Plonkle object '''
        self.name = name
        self.height = height
        self.words = words
    
    def taller_by(self, num):
        ''' Increase the height by num '''
        self.height = self.height + num
        return self.height
    
    def study(self, new_words):
        ''' Add new words to the word list '''
        for word in new_words:
            self.words.append(word)
        return self.words
    
    def __str__(self):
        ''' Print Plonkles! '''
        temp = "Hi. I'm {0}. I'm {1} cm tall."
        word = ''
        for i in range(0, len(self.words)):
            word = word + self.words[i] + ', '
        word = word[: -2]
        if word != '':
            temp_1 = '\nWords I know: {0}.'
        else:
            temp_1 = '\nWords I know:'
        return temp.format(self.name, self.height) + temp_1.format(word)

class Person:
    ''' Define a Person class, suitable for use in a hospital context.
    Data attributes: name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
    Methods: status()
    '''

    def __init__(self, name, age, weight, height):
        ''' Create a new Person object with the specified name, age, 
        weight and height '''
        self.name = name
        self.age = int(age)
        self.weight = weight
        self.height = height
        self.bmi = weight / (height * height)
        if self.bmi < 18.5:
            self.status = 'Underweight'
        if self.bmi >= 18.5 and self.bmi < 25:
            self.status = 'Normal'
        if self.bmi >= 25 and self.bmi < 30:
            self.status = 'Overweight'
        if self.bmi >= 30:
            self.status = 'Obese'
        
    def __str__(self):
        ''' Print persons! '''
        temp = '{0} ({1}) has a bmi of {2:.2f}. Their status is {3}.'
        return temp.format(self.name, self.age, self.bmi, self.status)
    
def read_people(csv_filename):
    ''' Read the csv '''
    infile = open(csv_filename)
    data = infile.readlines()
    bods = []
    for item in data:
        string = item.split(',')
        name = str(string[0])
        age = float(string[1])
        weight = float(string[2])
        height = float(string[3])
        bods.append(Person(name, age, weight, height))
    return bods

def filter_people(people, status_string):
    ''' Filter the people based on their status '''
    temp = []
    for bod in people:
        bod_1 = str(bod)
        words = bod_1.split()
        status = words[-1][: -1]
        if status_string == status:
            temp.append(bod)
    return temp