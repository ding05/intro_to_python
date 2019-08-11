def nth_element(data, n):
    ''' Return the nth element of the list '''
    element = data.pop(n)
    return element

def num_words(string):
    ''' Return the word count '''
    string = string.split()
    length = len(string)
    return length

def repeat_last(data):
    ''' returns a new list with the last item appearing twice '''
    data_1 = data[:]
    last_element = data_1[-1]
    data_1.append(last_element)
    return data_1

def concatenate(strings):
    ''' Return a single string formed by concatenating all the strings '''
    words = ''
    for word in strings:
        words += word
    return words

def my_max(data):
    ''' Return the maximum number in the list '''
    max_num = float('-inf')
    for num in data:
        if num > max_num:
            max_num = num
    return max_num

def cubes(data):
    ''' Return a list of the cubes of all those numbers '''
    result = []
    for num in data:
        result.append(num ** 3)
    return result

def abs_nums(numbers):
    ''' Return a list of the absolute values of those numbers '''
    abs_numbers = []
    for num in numbers:
        abs_numbers.append(abs(num))
    return abs_numbers

def lower_case(strings):
    ''' Return a list of those strings converted to lower case '''
    lower_strings = []
    for string in strings:
        lower_strings.append(string.lower())
    return lower_strings

def evens(numbers):
    ''' Return a new list containing just the even elements '''
    even_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers

def long_enough(strings, min_length):
    ''' Return a list with a length greater than or equal to the given '''
    long_strings = []
    for string in strings:
        if len(string) >= min_length:
            long_strings.append(string)
    return long_strings

def top_and_tail(string):
    ''' Return the string with its first and last characters removed '''
    removed_string = string[1:-1]
    return removed_string

def vertical_strings(string):
    ''' Return each letter for the times equal to length '''
    length = len(string)
    for letter in string:
        print(letter * length)

def are_anagrams(word1, word2):
    ''' Return True if the two parameters are anagrams '''
    if word1 == word2:
        return 1 > 2
    else:
        word3 = sorted(word1)
        word4 = sorted(word2)
        return word3 == word4