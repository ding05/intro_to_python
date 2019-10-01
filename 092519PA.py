''' Rewrite the codes from the previous intern '''
''' Author: D '''
''' Date: 09/25/2019 '''
import os
import matplotlib.pyplot as plt
from random import randint
MONTHS = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
         'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
MAX_BAR_SIZE = 50
BARCHAR = '='

def read_records_from_file():
    ''' Read lines from sample files '''
    filename = input('Input file name? ')
    while not os.path.isfile(filename):
        print('File does not exist.')
        filename = input('Input file name? ')
    lines = open(filename).readlines()
    return lines, filename

def is_int(value):
    ''' Judge if it is an integer '''
    try: 
        int(value)
        return True
    except ValueError:
        return False

def is_positive(value):
    ''' Judge if it is positive '''
    if int(value) >= 0:
        return True
    else:
        return False

def helper_total(readings):
    ''' A helper function used below '''
    total = 0
    for reading in readings:
        if is_int(reading) == True and is_positive(reading) == True:
            steps = int(reading)
        else:
            steps = 0
        total = total + steps
    return total

def helper_line(start, end, lines):
    ''' A helper function used below '''
    records = []
    for line_num in range(start + 1, end):
        line = lines[line_num]
        date, step_string = line.strip().split(':')
        readings = step_string.split(',')
        total = helper_total(readings)
        line_data = (date, total)
        records.append(line_data)
    return records

def daily_totals_from_lines(lines):
    ''' Return a list of records containing the date and the total steps '''
    start = lines.index('<begin step data>\n')
    end = lines.index('<end step data>\n', start + 1)
    records = helper_line(start, end, lines)
    return records

def helper_line_person(start, end, lines):
    ''' A helper function used below '''
    persons = []
    for line_num in range(start + 1, end):
        line = lines[line_num]
        labels, variables = line.strip().split(':')
        persons.append(variables)
    return persons

def person_data(lines):
    ''' Return a list of person data '''
    start = lines.index('<begin person data>\n')
    end = lines.index('<end person data>\n', start + 1)  
    persons = helper_line_person(start, end, lines)
    return persons

def helper_steps(records, month):
    ''' A helper function used below '''
    steps_for_month = []
    for date, steps in records:
        rec_month = int(date[5:7])
        if rec_month == month:
            steps_for_month.append(steps)
    return steps_for_month

def monthly_averages(records):
    ''' Return a list containing 12 monthly averages '''
    avers = []
    for month in range(1, 13):
        steps_for_month = helper_steps(records, month)
        if len(steps_for_month) > 0:
            ave = sum(steps_for_month) / len(steps_for_month)
            avers.append(ave)
        else:
            avers.append(-1)
    return avers

def print_person(persons):
    ''' Print the person information '''
    print('----------------------------------------')
    print(persons[0] + ', ' + '{:.2f}'.format(float(persons[1])) +
          ' kgs, ' + persons[2] + ' years')
    print('----------------------------------------')

def print_table(averages):
    ''' Print the average table '''
    for mon in range(12):
        month_name = MONTHS[mon]
        average = averages[mon]
        if average >= 0:
            print('{}: {:10.2f}'.format(month_name, average))
        else:
            print('{}: {:>6}'.format(month_name, 'n.a.'))

def print_graph(averages):
    ''' Print the average graph '''
    maxi = max(averages)
    for mon in range(12):
        month_name = MONTHS[mon]
        month_average = averages[mon]
        if month_average >= 0:
            proportion = month_average / maxi
            bar_str = int(proportion * MAX_BAR_SIZE) * BARCHAR
            print('{}: {}'.format(month_name, bar_str))
        else:
            print('{}: {}'.format(month_name, 'n.a.'))    

def graph(averages, filename):
    ''' Graphy with Matplotlib '''
    plt.bar(range(12), averages)
    plt.title('Average steps per day for each month (' + filename + ')')
    plt.xlabel("Month")
    plt.ylabel("Average daily steps")
    xtick_positions = []
    for i in range(12):
        xtick_positions.append(i)
    plt.xticks(xtick_positions, MONTHS)
    plt.show()    

def main():
    ''' Main program '''
    lines, filename = read_records_from_file()
    records = daily_totals_from_lines(lines)
    persons = person_data(lines)
    averages = monthly_averages(records)
    print_person(persons)
    print_table(averages)
    print()
    print_graph(averages)
    graph(averages, filename)
    
main()