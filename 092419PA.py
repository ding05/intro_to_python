def character_set_counts(string_1, string_2, string_3):
    ''' Return a count of the number of distinct characters '''
    string_1 = set(string_1)
    string_2 = set(string_2)
    string_3 = set(string_3)
    inter = string_1 & string_2
    dist = inter - string_3
    return len(dist)

def get_name(name_dict, id_num):
    ''' Return the name associated with the given ID number '''
    if id_num not in name_dict:
        return None
    else:
        for key, value in name_dict.items():
            if key == id_num:
                return value

def find_key(input_dict, value):
    ''' Return the key in the dictionary '''
    if value not in input_dict.values():
        return None
    else:
        for key, value_1 in input_dict.items():
            if value_1 == value:
                return key

def word_counter(input_str):
    ''' Return a dictionary mapping words in input_str to occurrence counts '''
    input_str = input_str.lower()
    strings = input_str.split()
    temp = []
    for word in strings:
        count = 0
        for i in range(0, len(strings)):
            if word == strings[i]:
                count += 1
        tuple_1 = (word, count)
        temp.append(tuple_1)
    dic = {}
    for i in range(0, len(strings)):
        dic[temp[i][0]] = temp[i][1]
    return dic

def produce_dictionary(filename):
    ''' Return a dictionary mapping words in the file to occurrence counts '''
    infile = open(filename)
    data = infile.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].rstrip()
        data[i] = data[i].lower()
    data = list(filter(None, data))
    temp = []
    for word in data:
        count = 0
        for i in range(0, len(data)):
            if word == data[i]:
                count += 1
        tuple_1 = (word, count)
        temp.append(tuple_1)
    dic = {}
    for i in range(0, len(data)):
        dic[temp[i][0]] = temp[i][1]
    return dic

import re

def print_word_counts(filename):
    ''' Print a list mapping words in the file to occurrence counts in an
    alphabetical order '''
    input_file = open(filename, 'r')
    source_string = input_file.read().lower()
    input_file.close()
    words = re.findall('[a-zA-Z]+', source_string)
    words = list(filter(None, words))
    temp = []
    for word in words:
        count = 0
        for i in range(0, len(words)):
            if word == words[i]:
                count += 1
        tuple_1 = (word, count)
        temp.append(tuple_1)
    dic = {}
    for i in range(0, len(words)):
        dic[temp[i][0]] = temp[i][1]
    for key in sorted(dic.keys()):
        print(key + ': ' + str(dic[key]))

def isbn_dictionary(filename):
    ''' Read the data and return a dictionary '''
    try:
        input_file = open(filename)
    except FileNotFoundError:
        print('The file ' + filename + ' was not found.')
        return None    
    infile = open(filename)
    data = infile.readlines()
    for i in range(0, len(data)):
        data[i] = data[i].rstrip()
        data[i] = data[i].split(',')
    dic = {}
    for i in range(0, len(data)):
        dic[data[i][2]] = (data[i][0], data[i][1])
    return dic

def generate_index(words_on_page):
    ''' Return a dictionary that maps from a word to an ordered list of pages
    on which that word appears '''
    words = []
    inverted = {}
    index = int(list(words_on_page.keys())[0]) 
    for i in range(index, index + len(words_on_page)):
        words.append(words_on_page[i])
    words_1 = []
    for i in range(0, len(words)):
        word = []
        for j in range(0, len(words[i])):
            word.append((words[i][j], i + index))
        words_1.append(word)
    words_2 = []
    for i in range(0, len(words)):
        for j in range(0, len(words[i])):
            if words[i][j] not in words_2:
                words_2.append(words[i][j])
    words_2.sort()
    numbers = []
    for i in range(0, len(words_2)):
        number = []
        for j in range(0, len(words_1)):
            for k in range(0, len(words_1[j])):
                if words_2[i] == words_1[j][k][0]:
                    number.append(words_1[j][k][1])
        numbers.append(number)
    for i in range(0, len(words_2)):
        inverted[words_2[i]] = numbers[i]
    return inverted