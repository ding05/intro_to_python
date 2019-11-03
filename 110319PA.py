""" Extra Practice """

def too_easy(message):
    print(message)

def full_name(given_name, surname, surname_first):
    if surname_first == True:
        return str(surname) + ', ' + str(given_name)
    else:
        return str(given_name) + ' ' + str(surname)

def bmi_risk(bmi, age):
    if bmi < 22 and age < 45:
        return 'Low'
    if bmi >= 22 and age >= 45:
        return 'High'
    else:
        return 'Medium'

def print_nums(numbers):
    for i in range(0, len(numbers)):
        print(str(i) + ': ' + str(numbers[i]))

def sum_over_threshold(nums, threshold):
    asum = 0
    for num in nums:
        if num >= threshold:
            asum += num
    return asum

def concat_with_length(string_list, length):
    temp = []
    for string in string_list:
        if len(string) == length:
            temp.append(string)
    temp = ''.join(temp)
    return temp

def weighted_sum(values, weights):
    temp = 0
    for i in range(0, len(values)):
        temp += values[i] * weights[i]
    return temp

def reachable(station_list):
    temp = []
    for tup in station_list:
        if tup[1] <= 100:
            temp.append(tup)
    return temp

def program():
    strings = input('Enter some numbers: ')
    temp = strings.split(' ')
    asum = 0
    for word in temp:
        if word != '':
            asum += int(word)
    print('Total = ' + str(asum))
program()

'asdsad'
import os
def readlines():
    'sad'
    filename = input("Filename? ")
    if os.path.exists(filename):
        infile = open(filename)
        lines = infile.readlines()
        infile.close()
    return lines
def getfor(lines):
    'fewa'
    num_for = 0
    for line in lines:
        if line.strip().startswith('for'):
            num_for += 1
    return num_for
def getwhile(lines):
    'sadgfa'
    num_while = 0
    for line in lines:
        if line.strip().startswith('while'):
            num_while += 1
    return num_while
LINES = readlines()
print("Lines starting with for:", getfor(LINES))
print("Lines starting with while:", getwhile(LINES))

def blat(nums, value):
    """Does something weird"""
    stuff = []
    i = 0
    while i < len(nums):
        if nums[i] % value == 0:
            stuff.append(nums[i] // value)
        else:
            stuff.append(nums[i])
        i += 1
    return stuff

def program():
    test = 0
    while test == 0:
        string = input('Full name? ')
        strings = string.split(' ')
        temp = []
        for string in strings:
            if string != '':
                temp.append(string)
        if len(temp) == 2:
            count = 0
            for string in temp:
                if string.isalpha() == True:
                    count += 1
                    if count == 2:
                        test = 1
                else:
                    print('Invalid input - try again')
        else:
            print('Invalid input - try again')      
    first = temp[0][0].upper() + temp[0][1:].lower()
    last = temp[1][0].upper() + temp[1][1:].lower()
    print('Hi ' + first)
    print('Your surname is ' + last)
program()

def blatter2(nums, value):
    """Does something weirder"""
    stuff = []
    i = 0
    while i < len(nums):
        if nums[i] != value:
            if nums[i] % value == 0:
                stuff.append(nums[i] // value)
            else:
                stuff.append(nums[i])
            i += 1
        else:
            i = len(nums)
    print(stuff)

def print_totals(filename):
    infile = open(filename)
    data = infile.readlines()
    for dat in data:
        strings = dat.split(',')
        for string in strings:
            name = strings[0].rstrip()
            num = 0
            for i in range(1, len(strings)):
                num += float(strings[i])
            num = round(num, 1)
        print(name + ': ' + str(num))

def print_content(strings):
    start = 0
    end = 0
    i = 0
    while i < len(strings):
        if strings[i].startswith('START'):
            start = i
            end = 1
        if strings[i].startswith('END') and end == 1:
            end = i
            i = len(strings)
        i += 1
    for i in range(start + 1, end):
        print(strings[i])

def read_dictionary(filename):
    infile = open(filename)
    data = infile.readlines()
    temp = []
    for dat in data:
        strings = dat.split(':')
        temp.append((strings[0], float(strings[1])))
    temp = sorted(temp)
    keys = []
    values = []
    for tem in temp:
        keys.append(tem[0])
        values.append(tem[1])
    dictionary = dict(zip(keys, values))
    return dictionary

def censor(words, patterns):
    for pattern in patterns:
        pattern = list(pattern)        
        countnoques = 0       
        for i in range(0, len(pattern)):          
            if pattern[i] != '?':
                countnoques += 1        
        for j in range(0, len(words)):
            words[j] = list(words[j])
            if len(pattern) == len(words[j]):
                count = 0
                for i in range(0, len(pattern)):
                    if pattern[i].lower() == words[j][i].lower():
                        count += 1
                if count == countnoques:
                    words[j] = '####'   
            words[j] = ''.join(words[j])

def print_all_sales(sales_dict):
    sales = []
    for keys, values in sales_dict.items():
        sales.append([keys, values])    
    sales = sorted(sales)
    for i in range(0, len(sales)):
        temp = []
        print('Branch: ' + sales[i][0])
        for j in range(0, len(sales[i][1])):
            temp.append((sales[i][1][j][1], sales[i][1][j][0]))
            temp = sorted(temp)
        for k in range(0, len(temp)):
            print(str(temp[k][0]).rjust(8) + ' ' + temp[k][1])
        print()

class Bug:
    def __init__(self, name, height, legs, has_wings=False):
        self.name = name
        self.height = height
        self.legs = legs
        self.has_wings = has_wings
    def __str__(self):
        self.height = round(self.height, 1)
        self.height = '{0:.1f}'.format(self.height)
        if self.has_wings == True:
            return (self.name + ' (' + self.height + ' mm) with ' +
                    str(self.legs) + ' legs and wings')
        else:
            return (self.name + ' (' + self.height + ' mm) with ' +
                    str(self.legs) + ' legs and no wings')
    def grow(self, amount):
        self.height += amount
        return self.height

class Whatsit:
    def __init__(self, name, weight, sounds=[]):
        self.name = name
        self.weight = weight
        self.sounds = sounds
    def __str__(self):
        sounds = ' '.join(self.sounds)
        weight = '{0:.1f}'.format(self.weight)
        return self.name + ' (' + weight + ' kg) ' + sounds
    def fatter_by(self, amount):
        self.weight += amount
        return self.weight
    def teach(self, string):
        self.sounds.append(string)
        return self.sounds
    def unteach(self, string):
        if string in self.sounds:
            self.sounds.remove(string)
        else:
            print("Error: " + self.name + " can't " + string)

def plot_bar_chart(counts):
    temp = []
    for keys, values in counts.items():
        temp.append(values)
    maximum = max(temp)
    letter = ' '
    for i in range(1, maximum + 1):
        expression = ''
        for j in range(0, len(temp)):
            if temp[j] + i - maximum <= 0:
                letter = ' '
            else:
                letter = '*'
            expression += letter
        print(expression)
