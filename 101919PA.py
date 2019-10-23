def make_person(id_num, name, weight, height, age):
    ''' Create and return a dictionary with keys id_num, name, weight, 
    height and age '''
    person = {'id_num': id_num,
            'name': name,
            'weight': weight,
            'height': height,
            'age': age,
            'num_steps': 0,
            'first_date_recorded': None,
            'last_date_recorded': None}
    return person

def bmi(person):
    ''' Return the floating point body-mass-index using the formula 
    bmi = weight / height ^2 '''
    person_bmi = person['weight'] / (person['height'] ** 2)
    return person_bmi

def add_steps(person, date, steps):
    ''' Update the given person dictionary by incrementing the num_steps value
    by the given number of steps '''
    if person['first_date_recorded'] == None:
        person['first_date_recorded'] = date
    if person['last_date_recorded'] == None:
        person['last_date_recorded'] = date
    if date < str(person['first_date_recorded']):
        person['first_date_recorded'] = date
    if date > str(person['last_date_recorded']):
        person['last_date_recorded'] = date
    person['num_steps'] += steps

def print_person(person):
    ''' Print the given person in a format like the following '''
    print('----------------------------------------')
    print(str(person['id_num']) + ' - ' + person['name'])
    print(str('{:.2f}'.format(person['weight'])) + ' kgs, '
          + str('{:.2f}'.format(person['height'])) + ' m, '
          + str(person['age']) + ' years')
    print('BMI = ' + str('{:.2f}'.format(bmi(person))))
    print('Total steps = ' + str(person['num_steps']))
    print('First date recorded = ' + str(person['first_date_recorded']))
    print('Last date recorded = ' + str(person['last_date_recorded']))
    print('----------------------------------------')

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
    person = make_person(id_num, name, weight, height, age)
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
        add_steps(person, date, steps)

def read_people_from_file(filename):
    ''' Take a filename and returns a list of person dictionaries '''
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