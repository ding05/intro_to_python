def lossy_fuse(list_1, list_2):
    '''  Return a new list containing all the elements of list 1 except the
    last followed by all the elements of list 2 except the first '''
    temp = []
    for i in range(0, len(list_1) - 1):
        temp.append(list_1[i])
    for j in range(1, len(list_2)):
        temp.append(list_2[j])
    return temp
        
def should_shutdown(battery_level, time_on):
    ''' Return true or false according to the two factors '''
    if time_on < 60 and battery_level < 4.7:
        return 1 > 0
    elif time_on >= 60 and battery_level < 4.8:
        return 1 > 0
    else:
        return 1 < 0

def print_wedge(size):
    ''' Print a wedge of asterisks of a given size '''
    star = '*' * size
    while size > 0:
        print(star)
        size = size - 1
        star = '*' * size

def num_doublings(initial_population, final_population):
    ''' Count how many doublings '''
    i = 0
    while initial_population < final_population:
        i = i + 1
        initial_population = initial_population * 2
    return i

def sum_numbers_in_file(filename):
    ''' Read the numbers and return the sum '''
    infile = open(filename)
    data = infile.readlines()
    data = map(int, data)
    data_sum = sum(data)
    return data_sum

def max_num_in_file(filename):
    ''' Return the largest integer '''
    infile = open(filename)
    data = infile.readlines()
    data = map(int, data)
    data_max = max(data)
    return data_max

def print_numbered_lines(filename):
    ''' Print out all the lines of the file with the line number '''
    infile = open(filename)
    data = infile.readlines()
    for i in range(0, len(data)):
        print(str(i + 1) + ':', data[i].rstrip())

def print_reversed(filename):
    ''' Print out the lines from the file in reversed order '''
    infile = open(filename)
    data = infile.readlines()
    for i in range(len(data) - 1, -1, -1):
        print(data[i].rstrip())

def print_daily_totals(filename):
    ''' Print out the date and the total amount of rainfall '''
    infile = open(filename)
    data = infile.readlines()
    for i in range(0, len(data)):
        item = data[i]
        string = item.split(',')
        date = string[0]
        string[-1] = string[-1].rstrip()
        amount = string[1: ]
        amount = map(float, amount)
        total = sum(amount)
        print(date, '=', '{0:.2f}'.format(total))

def file_size(filename):
    ''' Return the count of letters '''
    infile = open(filename)
    data = infile.readlines()
    total = 0
    for i in range(0, len(data)):
        total = total + len(data[i])
    return total

def generate_daily_totals(input_filename, output_filename):
    ''' Generate a new file with the date and the total amount of rainfall '''
    infile = open(input_filename)
    outfile = open(output_filename, 'w')
    data = infile.readlines()
    for i in range(0, len(data)):
        item = data[i]
        string = item.split(',')
        date = string[0]
        string[-1] = string[-1].rstrip()
        amount = string[1: ]
        amount = map(float, amount)
        total = sum(amount)
        outfile.write(date + ' = ' + '{0:.2f}'.format(total) + '\n')

def write_reversed_file(input_filename, output_filename):
    ''' Generate a new file with the lines from the file in reversed order '''
    infile = open(input_filename)
    outfile = open(output_filename, 'w')
    data = infile.readlines()
    for i in range(len(data) - 1, -1, -1):
        invdata = data[i].rstrip()
        outfile.write(invdata + '\n')