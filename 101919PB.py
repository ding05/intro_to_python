'''
Program to process the person data and the step data of Zen industries
Author: D
Date: 10/19/2019
'''


import os


def get_valid_filename():
    ''' Ask for a filename until one is given '''
    
    filename = input('Input file name? ')
    
    while os.path.isfile(filename) == False:
        print('File does not exist.')
        filename = input('Input file name? ')
        
    return filename


def extract_person(lines, start_index=0):
    ''' Take a list of lines and returns a person dictionary based on
    the data starting at a given index '''
    
    id_temp = lines[start_index + 1].split(':')
    id_num = int(id_temp[1])
    
    name_temp = lines[start_index + 2].split(':')
    name = str(name_temp[1])
    
    weight_temp = lines[start_index + 3].split(':')
    weight = float(weight_temp[1])
    
    height_temp = lines[start_index + 4].split(':')
    height = float(height_temp[1])
    
    age_temp = lines[start_index + 5].split(':')
    age = int(age_temp[1])
    
    person = Person(id_num, name, weight, height, age)
    
    return person


def process_steps(person, lines, index):
    ''' Take a person dictionary, a list of lines from a file (with trailing
    newline characters stripped) and the index into that list of the
    <begin step data> line for the given person '''
    
    end = 0
    for i in range(index, len(lines)):
        if lines[i].startswith('<end step data>') and end == 0:
            end = i

    for i in range(index + 1, end):
        day_temp = lines[i].split(':')
        date = str(day_temp[0])
        step_temp = day_temp[1].split(',')
        step_temp = list(map(int, step_temp))
        steps = sum(step_temp)
        person.add_steps(date, steps)


def read_people_from_file(filename):
    ''' Take a filename and return a list of person dictionaries '''
    infile = open(filename)
    lines = infile.readlines()
    lines = [item.strip() for item in lines]
    people = []
    
    for i in range(0, len(lines)):
        if lines[i].startswith('<begin person data>'):
            person = extract_person(lines, i)
        if lines[i].startswith('<begin step data>'):
            process_steps(person, lines, i)
            people.append(person)

    return people


def calculate_bmi(people):
    ''' Return the max, min and mean body-mass indexes of the group '''
    
    bmi_temp = []
    for person in people:
        person_bmi = Person.bmi(person)
        bmi_temp.append(person_bmi)

    min_bmi = str('{:.2f}'.format(min(bmi_temp)))
    mean_bmi = str('{:.2f}'.format(sum(bmi_temp) / len(bmi_temp)))
    max_bmi = str('{:.2f}'.format(max(bmi_temp)))
    
    return min_bmi, mean_bmi, max_bmi


def sort_people(people):
    ''' Sort the people based on their step counts '''

    people_temp = []
    for person in people:
        person_temp = (person.id_num, person.name, person.num_steps)
        people_temp.append(person_temp)
   
    people_temp.sort(key=lambda tup: tup[2])

    return people_temp


class Person:
    ''' Define a Person class, suitable for use in Zen data.
    Data attributes: id_num of type int
                     name of type str
                     age of type int
                     weight (kg) of type float
                     height (metres) of type float
                     num_steps of type int
                     first_date_recorded of type str
                     last_date_recorded of type str
    Methods: bmi(), add_steps()
    '''


    def __init__(self, id_num, name, weight, height, age):
        ''' Initialise the self object in much the same way as the make_person
        initialised the person dictionary '''

        self.id_num = int(id_num)
        self.name = str(name)
        self.weight = float(weight)
        self.height = float(height)
        self.age = int(age)
        self.num_steps = 0
        self.first_date_recorded = None
        self.last_date_recorded = None
        person_bmi = 0


    def bmi(self):
        ''' Return the person's body-mass index '''

        person_bmi = self.weight / (self.height ** 2)
        return person_bmi


    def add_steps(self, date, num_steps):
        ''' Update the given person dictionary by incrementing the num_steps
        value by the given number of steps '''

        if self.first_date_recorded == None:
            self.first_date_recorded = date
        if self.last_date_recorded == None:
            self.last_date_recorded = date
        if date < str(self.first_date_recorded):
            self.first_date_recorded = date
        if date > str(self.last_date_recorded):
            self.last_date_recorded = date

        self.num_steps += num_steps


    def __str__(self):
        ''' Print the given person in a format like the following '''
        
        string = '----------------------------------------\n'
        string += str(self.id_num) + ' - ' + self.name + '\n'
        string += str('{:.2f}'.format(self.weight)) + ' kgs, '
        string += str('{:.2f}'.format(self.height)) + ' m, '
        string += str(self.age) + ' years\n'
        string += 'BMI = ' + str('{:.2f}'.format(self.weight / (self.height ** 2))) + '\n'
        string += 'Total steps = ' + str(self.num_steps) + '\n'
        string += 'First date recorded = ' + str(self.first_date_recorded) + '\n'
        string += 'Last date recorded = ' + str(self.last_date_recorded) + '\n'
        string += '----------------------------------------'
        
        return string


    def __repr__(self):
        ''' Return a string in the following format '''
        
        string = 'Person(' + str(self.id_num) + ", '" + self.name + "', "
        string += str('{:.2f}'.format(self.weight)) + ', '
        string += str('{:.2f}'.format(self.height)) + ', ' + str(self.age) + ')'
        
        return string


def main():
    ''' Main function containing all the functions above '''
    
    filename = get_valid_filename()
    people = read_people_from_file(filename)
    num_people = len(people)
    min_bmi, mean_bmi, max_bmi = calculate_bmi(people)
    people_sorted = sort_people(people)
    
    print('Number of people loaded: ' + str(num_people))
    print()
    print('Minimum BMI = ' + min_bmi)
    print('Average BMI = ' + mean_bmi)
    print('Maximum BMI = ' + max_bmi)
    print()
    print('Total steps summary:')
    for person in people_sorted:
        print('{:<8}{:20} {:8}'.format(person[0], person[1], person[2]))


main()