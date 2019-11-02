""" A 3-Hour Exam Practice (21 of 23 questions done) """

def print_sum(num1, num2):
    print(str(num1+num2))

def full_name(given_name, surname, use_upper_case):
    if use_upper_case == True:
        given_name = given_name.upper()
        surname = surname.upper()
    full = given_name + ' ' + surname
    return full

def is_ok(test_value, low, high):
    tempa = 0
    tempb = 0
    if test_value >= low:
        tempa = 1
    if test_value <= high:
        tempb = 1
    if tempa == 1 and tempb == 1:
        return True
    else:
        return False

def print_string_lengths(strings):
    for string in strings:
        print(string + ': ' + str(len(string)))

def first_chars(strings):
    temp = ''
    for string in strings:
        temp += string[0]
    return temp

def discount(num_plants, has_card):
    disc = 0
    if num_plants >= 10 and num_plants < 50:
        disc += 10
    if num_plants >= 50:
        disc += 20
    if has_card == True:
        disc += 10
    return disc

def is_square():
    temp = input('Side length? ')
    square = float(temp) ** 2
    square = str('{:.2f}'.format(square))
    print('Square area = ' + square)
is_square()

def sign_counters(nums):
    nega = 0
    zero = 0
    posi = 0
    for num in nums:
        if num > 0:
            posi += 1
        if num == 0:
            zero += 1
        if num < 0:
            nega += 1
    return (nega, zero, posi)

"""I'm a silly program"""
def main():
    """I'm a main function that's too long"""
    silly1 = input("Type something: ").split()
    for i in range(0, len(silly1)):
        if silly1[i].isalpha():
            silly1[i] = silly1[i][len(silly1[i])//2:] + silly1[i][0:len(silly1[i])//2]
        else:
            silly1[i] = str(0.5 * float(silly1[i]))
    print(','.join(silly1))
main()

def print_square(inner_size, border_width):
    line = inner_size + border_width * 2
    for i in range(0, border_width):
        print('o' * line)
    for i in range(0, inner_size):
        print('o' * border_width + '+' * inner_size + 'o' * border_width)
    for i in range(0, border_width):
        print('o' * line)

def print_list(strings):
    """Print the strings, one per line, preceded by a line number"""
    num = 0
    while num < len(strings):
        s = strings[num]
        print('{} {}'.format(num + 1, s))
        num += 1
        
mumble([3, 5, 1, 1, 1, 3, 1], 2, 7)

def print_summary(filename):
    infile = open(filename)
    data = infile.readlines()
    for temp in data:
        string = temp.split(':')
        before = string[0].rstrip()
        string1 = string[1].split(',')
        suma = 0
        for item in string1:
            suma += float(item.rstrip())
        avg = suma / len(string1)
        print(before + ': ' + str(round(avg, 1)))

def aprogram():
    line1 = input('Enter a line: ')
    while line1.startswith('GO') == False:
        line1 = input('Enter a line: ')
    line2 = input('Next: ')
    count = 0
    while line2.startswith('STOP') == False:
        line2 = input('Next: ')
        count += 1
    print('Counted ' + str(count) + ' lines')
aprogram()

def get_number(person, mobiles):
    if person not in mobiles:
        return 'Unknown'
    else:
        for key, value in mobiles.items():
            if key == person:
                return value
            
def word_zapper(words, allowed_chars, start_index=0):
    for j in range(start_index, len(words)):
        count = 0
        for i in range(0, len(words[j])):
            if words[j][i] in allowed_chars:
                count += 1
        if count == len(words[j]):
            words[j] = words[j]
        else:
            words[j] = ''

def valid_ints(strings):
    integers = []
    for string in strings:
        try:
            integer = int(string)
            if integer not in integers:
                integers.append(integer)
        except ValueError:
            pass
    return integers

def sorted_common_chars(strings):
    letters = []
    for string in strings:
        for i in range(0, len(string)):
            count = 0
            for stringb in strings:
                if string[i] in stringb:
                    count += 1
                    letter = string[i]
            if count == len(strings) and letter not in letters:
                letters.append(letter)
    sorta = ''.join(sorted(letters))
    return sorta

def area_dict(phone_nums):
    dic = {}
    keys = []
    values = []
    for key, value in phone_nums.items():
        keys.append(key)
        values.append(value.split(' ')[0])
    new_values = []
    for i in range(0, len(keys)):
        if values[i] not in new_values:
            new_values.append(values[i])
    tuples = []
    for i in range(0, len(keys)):
        tuples.append((keys[i], values[i]))  
    temp = []
    for i in range(0, len(new_values)):
        temp.append([])
    new_tuples = temp
    for i in range(0, len(new_tuples)):
        new_tuples[i] = []
    for i in range(0, len(tuples)):
        for j in range(0, len(new_values)):
            if tuples[i][1] == new_values[j]:
                new_tuples[j].append(tuples[i][0])
    for i in range(0, len(new_tuples)):
        new_tuples[i] = sorted(new_tuples[i])
    for i in range(0, len(new_tuples)):
        dic = dict(zip(new_values, new_tuples))
    return dic

class Gingle:
    def __init__(self, name, num_legs, weight):
        self.name = name
        self.num_legs = num_legs
        self.weight = weight
    def __str__(self):
        self.weight = str('{:.2f}'.format(self.weight))
        self.num_legs = str(self.num_legs)
        return "Gingle('" + self.name + "', " + self.num_legs + ', ' + self.weight + ')'
    def can_run(self):
        if float(self.num_legs) >= 2:
            return True
        else:
            return False

def print_crosswords(across, down):
    letters = []
    for i in range(0, len(across)):
        for j in range(0, len(down)):
            if across[i] == down[j]:
                letters.append(across[i])
    if letters == []:
        print("Can't cross the words!")
    else:
        letter = letters[0]
        num = 0
        nums = []
        for i in range(0, len(across)):
            if letter == across[i]:
                nums.append(i)
        num = nums[0]
        numsb = []
        for i in range(0, len(down)):
            if letter == down[i]:
                numsb.append(i)
        numb = numsb[0]
        for i in range(0, numb):
            print(' ' * num + down[i])
        print(across)
        for i in range(numb + 1, len(down)):
            print(' ' * num + down[i])