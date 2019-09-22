''' Return the total cost '''

def fun_function(n_items, cost_per_item, discount_percent, discount_threshold):
    ''' Calculate the cost '''
    cost = n_items * cost_per_item                  # line 1
    if n_items > discount_threshold:                # line 2
        cost = cost * (1 - discount_percent / 100)
    return cost

def main():
    ''' Main program '''
    # First initialise all variables
    cost_per_item = 27      # Without discount
    discount_percent = 10
    discount_threshold = 20

    # Get the number of items in this delivery
    n_items = int(input("Count of items? "))

    # Now compute the total cost
    cost = fun_function(n_items, cost_per_item, discount_percent, discount_threshold)

    # Print the results
    print('{} items, costing ${:.2f}'.format(n_items, cost))

""" main() """

''' Print all the perfect squares from zero up to a given maximum.
    This version is refactored to make it more understandable
    and more maintainable '''

import math

"""
def read_bound():
    ''' Reads the upper bound from the standard input (keyboard).
        If the user enters something that is not a positive integer
        the function issues an error message and retries
        repeatedly - as per the original code '''
    upper_bound = None
    while upper_bound is None:
        line = input("Enter the upper bound: ")
        if line.isnumeric():
            upper_bound = int(line)
        else:
            print("You must enter a positive number.")
    return upper_bound
"""
def read_bound(strings=''):
    ''' Reads the upper bound from the standard input (keyboard).
        If the user enters something that is not a positive integer
        the function issues an error message and retries
        repeatedly - as per the original code '''
    if strings != '':
        lower_bound = None
        while lower_bound is None:
            line = input(strings)
            if line.isnumeric():
                lower_bound = int(line)
            else:
                print("You must enter a positive number.")
        return line
    else:
        lower_bound = None
        upper_bound = None
        while lower_bound is None:
            line = input("Enter the lower bound: ")
            if line.isnumeric():
                lower_bound = int(line)
            else:
                print("You must enter a positive number.")
        while upper_bound is None:
            line = input("Enter the upper bound: ")
            if line.isnumeric():
                upper_bound = int(line)
            else:
                print("You must enter a positive number.")
        return lower_bound, upper_bound

"""
def is_perfect_square(num):
    ''' Returns True if and only if num is a perfect square, 
        otherwise returns False '''
    for candidate in range(1, num):
        if candidate * candidate == num:
            return True
"""
def is_perfect_square(num):
    ''' Returns True if and only if num is a perfect square, 
        otherwise returns False '''
    sqrt = math.sqrt(num)
    if sqrt == math.ceil(sqrt):
        return True
    
"""
def print_squares(upper_bound, squares):
    ''' Print the given list of all the squares up to the given upper bound.
        The printout should be in the same format as the original code '''
    print("The perfect squares up to {} are: ".format(upper_bound))
    for square in squares:
        print(square, end=' ')
    print()
"""
def print_squares(lower_bound, upper_bound, squares):
    ''' Print the given list of all the squares up to the given upper bound.
        The printout should be in the same format as the original code '''
    print("The perfect squares from {} to {} are: ".format(lower_bound, upper_bound))
    for square in squares:
        print(square, end=' ')
    print()

"""
def main():
    ''' Every home should have one '''
    upper_bound = read_bound()
    squares = []
    for num in range(2, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)
    
    print_squares(upper_bound, squares)
"""
def main():
    ''' Every home should have one '''
    lower_bound, upper_bound = read_bound()
    squares = []
    for num in range(lower_bound, upper_bound + 1):
        if is_perfect_square(num):
            squares.append(num)
    
    print_squares(lower_bound, upper_bound, squares)

""" main() """

'''Read and process a file of student names and marks.
   Written for COSC121S2.
   Author: Angus McGurkinshaw
   Date: 29 July 2017.
'''

def get_filename():
    '''Return the name of the student data file to be processed.
       This is a so-called 'stub' implementation which always returns
       the same filename. A fuller implementation would prompt the user
       for the filename.
    '''
    return "data.csv"

def read_data(filename):
    '''Read and return the contents of the given file.
       The file is assumed to exist, or an exception will occur.
       It is also assumed that each line of the file consists of a
       student name, a comma, and a floating-point mark.
       Returns: a list of (name, mark) tuples, where name is a string
       and mark is a floating-point number.
    '''
    infile = open(filename)
    lines = infile.readlines()
    data = []
    for line in lines:
        string = line.split(',')
        string[-1] = float(string[1].rstrip())
        string_tuple = (string[0], string[1])
        data.append(string_tuple)
    return data

def statistics(student_data):
    '''Given a list of (name, mark) pairs, returns a tuple containing
       statistics extracted from the list. The components of the returned tuple 
       are minimum_mark, maximum_mark, average_mark and top_students. The
       first three are just floating point values. The last one is an
       alphabetically ordered list of the names of all students whose
       marks are equal to the maximum_mark.
    '''
    nums = []
    for i in range(0, len(student_data)):
        num = student_data[i][1]
        nums.append(num)
    minimum_mark = min(nums)
    maximum_mark = max(nums)
    average_mark = sum(nums) / len(nums)
    top_students = []
    for i in range(0, len(student_data)):
        if student_data[i][1] == maximum_mark:
            top_students.append(student_data[i][0])
    top_students = sorted(top_students, key=str.lower)
    return minimum_mark, maximum_mark, average_mark, top_students

def print_results(stats):
    '''Print the statistics given. The parameters 'stats' is a
       tuple of the form returned by the 'statistics' function
       above. The required output is shown in the example output table.
    '''
    (minimum, maximum, average, top_students) = stats
    print("Minimum mark is: {:.1f}".format(minimum))
    print("Maximum mark is: {:.1f}".format(maximum))
    print("Average mark is: {:.1f}".format(average))
    if len(top_students) == 1:
        print("Top student: {}".format(top_students[0]))
    else:
        print("Top-equal students:\n  {}".format(", ".join(top_students)))

def main():
    ''' The main function (see module docstring) '''
    filename = get_filename()
    data = read_data(filename)
    stats = statistics(data)
    print_results(stats)

""" main() """

'''A program to read a CSV file of rainfalls and print the totals
   for each month.
'''

def get_filename():
    ''' Get the filename '''
    return "rainfalls2011.csv"

def get_columns(filename):
    ''' Get the data '''
    datafile = open(filename)
    data = datafile.readlines()
    columns = []
    for line in data:
        column = line.split(',')
        columns.append(column)
    return columns

def get_months(columns):
    ''' Get the months '''
    months = []  # A list of (month, rainfall) tuples
    for i in range(0, 12):
        months.append(int(columns[i][0]))
    return months

def get_rainfalls(columns):
    ''' Get the total rainfall '''
    rainfalls = []
    for i in range(0, 12):
        rainfall = 0
        for j in range(2, len(columns[i])):
            rainfall += float(columns[i][j]) 
        rainfalls.append(rainfall)
    return rainfalls

def join_two(months, rainfalls):
    ''' Join the two variables '''
    results = []
    for i in range(0, 12):
        result = (months[i], rainfalls[i])
        results.append(result)
    return results

def print_monthly_totals(filename):
    '''Process the given csv file of rainfall data and print the
       monthly rainfall totals. input_csv_filename is the name of
       the input file, which is assumed to have the month number in
       column 1, the number of days in the month in column 2 and the
       floating point rainfalls (in mm) for each month in the remaining
       columns of the row.
    '''
    columns = get_columns(filename)
    months = get_months(columns)
    rainfalls = get_rainfalls(columns)
    results = join_two(months, rainfalls)    
    print('Monthly total rainfalls')
    for (months, total_rainfalls) in results:
        print('Month {:2}: {:.1f}'.format(months, total_rainfalls))

def main():
    ''' The main function '''
    filename = get_filename()
    print_monthly_totals(filename)

main()