def min_number_in_file(filename):
    ''' Return the smallest integer '''
    infile = open(filename)
    data = infile.readlines()
    data = map(int, data)
    data_min = min(data)
    return data_min

def copy_first(data, nuclear):
    ''' Return every letter twice if it's true '''
    temp = []
    if nuclear == True:
        for i in range(0, len(data)):
            temp.append(data[i])
            temp.append(data[i])
    else:
        temp.append(data[0])
        temp.append(data[0])
        for i in range(1, len(data)):
            temp.append(data[i])
    return temp

def funky_file(input_name, output_name):
    ''' Convert the letter into the capitalized '''
    infile = open(input_name)
    outfile = open(output_name, 'w')
    data = infile.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].lstrip()
        data[i] = data[i].upper()
        data[i] = data[i].rstrip()
        outfile.write(data[i] + '\n')
        
def crazy_join(list_1, list_2):
    ''' Join the two lists '''
    temp = []
    for i in range(2, len(list_1)):
        temp.append(list_1[i])
    for j in range(0, len(list_2) - 1):
        temp.append(list_2[j])
    return temp

def sum_numbers_in_file(filename):
    ''' Read all numbers and return the sum '''
    infile = open(filename)
    data = infile.readlines()
    temp = 0
    def is_number(s):
        ''' Test if a string is a number '''
        try:
            float(s)
            return True
        except ValueError:
            return False    
    for i in range(0, len(data)):
        if is_number(data[i]) == True:
            data[i] = int(data[i])
            temp = temp + data[i]
    return temp

def stat_master(filename):
    ''' Return the average, maximum, and minimum '''
    infile = open(filename)
    data = infile.read()
    data = data.split(':')
    data_1 = data
    data = map(float, data)
    min_data = min(data)
    infile = open(filename)
    data = infile.read()
    data = data.split(':')
    data = map(float, data)
    max_data = max(data)
    infile = open(filename)
    data = infile.read()
    data = data.split(':')
    data = map(float, data)
    avg_data = float('{0:.1f}'.format(sum(data) / len(data_1)))
    return (avg_data, max_data, min_data)