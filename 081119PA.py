def cubes(data):
    ''' Return a list of the cubes '''
    result = []
    for num in data:
        result.append(num ** 3)
    return result

def tuplinator(string):
    ''' Return a tuple consisting of three types of strings '''
    double = str(string+string)
    triple = str(string+string+string)
    result = (string, double, triple)
    return result

def furthest(data):
    ''' Return the last element of the list '''
    return data[-1]

def concatenate(strings):
    ''' Return a single string formed by concatenating all the strings '''
    result = ''
    for string in strings:
        result = result + string
    return result

def long_enough(strings, min_length):
    ''' Return a list of all strings with length greater than the minimum '''
    result = []
    for string in strings:
        if len(string) >= min_length:
            result.append(string)
    return result

def vertical_strings(string):
    ''' Return each letter for the times equal to length '''
    length = len(string)
    for letter in string:
        print(letter * length)