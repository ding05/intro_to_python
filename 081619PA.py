def print_squares_to_number(number):
    ''' Print a table of all integers and their squares '''
    if number < 1:
        print('ERROR: number must be at least 1')
    else:
        for num in range(1, number + 1):
            print(num, '*', num, '=', num * num)

def set_lowercase(strings):
    ''' modify that list by replacing each string with its lower-case '''
    for i in range(0, len(strings)):
        strings[i] = strings[i].lower()

def my_enumerate(items):
    ''' Return a list of tuples without the enumerate function '''
    for i in range(0, len(items)):
        items[i] = (i, items[i])
    return items

def get_column(game, col_num):
    ''' Return the colnum '''
    empty = []
    for i in range(0, len(game)):
        empty.append(game[i][col_num])
    return empty

def diagonals(game):
    ''' Return the diagnals '''
    diagonal_1 = []
    diagonal_2 = []
    for i in range(0, len(game)):
        diagonal_1.append(game[i][i])
        diagonal_2.append(game[i][2-i])
    return (diagonal_1, diagonal_2)

def row_sums(square):
    ''' Return the sum of each row without using sum() '''
    result = []
    for i in range(0, len(square)):
        temp = 0
        for j in range(0, len(square)):
            temp = temp + square[i][j]
        result.append(temp)
    return result
	
def column_sums(square):
    ''' Return the sum of each column without using sum() '''
    result = []
    for i in range(0, len(square)):
        temp = 0
        for j in range(0, len(square)):
            temp = temp + square[j][i]
        result.append(temp)
    return result

def print_daily_totals(rainfalls):
    ''' Return the sum of rainfalls on each day without using sum() '''
    for i in range(0, len(rainfalls)):
        temp = 0
        for j in range(0, len(rainfalls[i])):
            temp = temp + rainfalls[i][j]
        print('Day', i, 'total:', temp)

def months_to_reach_target(principal, interest_rate_per_annum, target):
    ''' Return the number of months to reach the given target amount '''
    interest_rate_per_month = interest_rate_per_annum / 12 / 100
    num_months = 0
    while principal < target:
        increase = principal * interest_rate_per_month
        principal = principal + increase
        num_months += 1
    return num_months

def print_names(names):
    ''' Print the names in the list of names, one per line '''
    i = 0
    while i < len(names): 
        print(names[i])
        i += 1

def print_names2(people):
    ''' Print a list of people's names, which each person's name
        is itself a list of names (first name, second name etc)
    '''
    i = 0
    word = ''
    while i < len(people):
        word = people[i]
        if len(word) == 2:
            print(word[0], word[1])
        else:
            print(word[0])
        i += 1

def guess_a_number(target_number, lower_bound, upper_bound):
    ''' Ask users to guess the target number between the bounds '''
    string_lower = str(lower_bound)
    string_upper = str(upper_bound)
    print("I'm thinking of a number between " + string_lower + ' and ' + string_upper + '.')
    given_number = target_number + 1
    while given_number != target_number:
        given_number = int(input('What do you think it is? '))
        if given_number == target_number:
            print('Congratulations! You guessed my number!')
        else:
            print("That's not my number. Try again.")

def num_rushes(slope_height, rush_height_gain, back_sliding):
    ''' Calculate how many rushes '''
    current_height = 0
    rushes = 0
    while current_height < slope_height:
        current_height += rush_height_gain
        if current_height < slope_height:
            current_height -= back_sliding
        rushes += 1
    return rushes

def num_rushes(slope_height, rush_height_gain, back_sliding):
    ''' Calculate how many rushes '''
    import math    
    current_height = 0
    rushes = 0
    i = 0
    while current_height < slope_height:
        current_height += rush_height_gain * (0.95 ** i)
        if current_height < slope_height:
            current_height -= back_sliding * (0.95 ** i)
        rushes += 1
        i += 1
    return rushes