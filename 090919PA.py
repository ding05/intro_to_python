def total_steps(step_records):
    ''' Return the total steps of all records '''
    temp = 0
    for i in range(0, len(step_records)):
        temp += step_records[i][1]
    return temp

def min_steps(step_records):
    ''' Return the minimum step of all records '''
    if step_records == []:
        return
    else:
        temp = step_records[0][1]
        for i in range(0, len(step_records)):
            if temp > step_records[i][1]:
                temp = step_records[i][1]
        return temp

def max_steps(step_records):
    ''' Return the maximum step of all records '''
    if step_records == []:
        return
    else:
        temp = step_records[0][1]
        for i in range(0, len(step_records)):
            if temp < step_records[i][1]:
                temp = step_records[i][1]
        return temp

def average_steps(step_records):
    ''' Return the average step of all records '''
    if step_records == []:
        return
    else:
        temp = total_steps(step_records)
        avg = temp / len(step_records)
        return '{0:.2f}'.format(avg)

def days_to_reach_target(step_records, target_steps):
    ''' Return how many days before the total reaches the target '''
    total = 0
    day = 0
    while total < target_steps and day < len(step_records):
        total += step_records[day][1]
        day += 1
    if total >= target_steps:
        return day

def date_reached_target_steps(step_records, target_steps):
    ''' Return the date when it reaches the target '''
    total = 0
    day = 0
    while total < target_steps and day < len(step_records):
        total += step_records[day][1]
        day += 1
        date = step_records[day - 1][0]
    if total >= target_steps:
        return date

def activity_level_from_steps(steps):
    ''' Return the activity level indicated by the given number of steps '''
    steps = int(steps)
    if steps == 0:
        level = 'alive?'
    elif steps > 0 and steps <= 4999:
        level = 'sedentary'
    elif steps > 4999 and steps <= 7499:
        level = 'very low'
    elif steps > 7499 and steps <= 9999:
        level = 'low'
    elif steps > 9999 and steps <= 12499:
        level = 'active'
    elif steps >= 12500:
        level = 'very active'
    return level

def n_days_at_activity_level(step_records, activity_level):
    ''' Return the number of days with the given activity level '''
    day = 0
    for i in range(0, len(step_records)):
        temp = activity_level_from_steps(step_records[i][1])
        if temp == activity_level:
            day += 1
    return day

def dates_at_activity_level(step_records, activity_level):
    ''' Return the dates with the given activity level '''
    date = []
    for i in range(0, len(step_records)):
        temp = activity_level_from_steps(step_records[i][1])
        if temp == activity_level:
            date.append(step_records[i][0])
    return date

def longest_run_at_level(step_records, activity_level):
    ''' Return the longest length of days in a row with the given level '''
    length = 0
    saved = 0
    for i in range(0, len(step_records)):
        temp = activity_level_from_steps(step_records[i][1])
        if temp == activity_level:
            length += 1
        if temp != activity_level:
            if saved < length:
                saved = length
            length = 0
    if saved < length:
        saved = length
    return saved

import os

def get_valid_filename():
    ''' Ask for a filename until one is given '''
    filename = input('Input file name? ')
    while os.path.isfile(filename) == False:
        print('File does not exist.')
        filename = input('Input file name? ')
    return filename

def read_records_from_file(filename):
    ''' Read step data from sample files '''
    records = []
    infile = open(filename)
    data = infile.readlines()
    for i in range(0, len(data)):
        if data[i].startswith('<begin step data>'):
            start = i
        if data[i].startswith('<end step data>'):
            end = i
    for n in range(start + 1, end):
        string = data[n]
        string = string.split(',')
        date_str = str(string[0])
        step_count = int(string[1])
        temp = (date_str, step_count)
        records.append(temp)
    return records

def main():
    ''' Program containing all the functions above '''
    filename = get_valid_filename()
    step_records = read_records_from_file(filename)
    print('Number of records =', len(step_records))
    print('Total steps =', total_steps(step_records))
    print('Average steps =', average_steps(step_records))
    print('Maximum steps =', max_steps(step_records))
    print('Days to reach 100000 steps =', days_to_reach_target(step_records, 100000))
    print('Date reached 100000 steps =', date_reached_target_steps(step_records, 100000))
    print('Number of active days =', n_days_at_activity_level(step_records, 'active'))
    print('Number of very active days =', n_days_at_activity_level(step_records, 'very active'))
    print('Longest run of active days =', longest_run_at_level(step_records, 'active'))

main()