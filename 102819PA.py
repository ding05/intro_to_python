def print_date(year, month, day):
    ''' Print out the date, formatted as year-month-day '''
    if year < 10:
        year = '0' + str(year)
    else:
        year = str(year)
    if month < 10:
        month = '0' + str(month)
    else:
        month = str(month)
    if day < 10:
        day = '0' + str(day)
    else:
        day = str(day)
    print(year + '-' + month + '-' + day)

def has_repeated_roots(a, b, c):
    ''' Return True iff the quadratic ax^2 + bx + c = 0 has repeated roots '''
    return b ** 2 == 4 * a * c

def is_satisfactory(name, age, weight):
    ''' Return True if and only if the given data satisfies some weird criteria '''
    return name[0].isalpha() and ((age < 18 and weight > 20) or (weight > 30))

def print_numbered_items(items):
    ''' Print a list of items one per line '''
    for i in range(0, len(items)):
        print(str(i) + ': ' + str(items[i]))

def print_numbered_items(items):
    ''' Must use enumerate() '''
    for count, item in enumerate(items):
        print(str(count) + ': ' + str(item))

def print_numbered_items(items):
    ''' Must not use len(), range() or enumerate() '''
    i = 0
    for item in items:
        print(str(i) + ': ' + str(items[i]))
        i += 1

def print_numbered_items(items):
    ''' Must use a while loop '''
    i = 0
    while i < len(items):
        print(str(i) + ': ' + str(items[i]))
        i += 1

def fillerup_printer(items, capacity):
    ''' Must not use a for loop, a break or more than one return '''
    current = 0
    i = 0
    while current <= capacity and i < len(items):
        if current + items[i][1] <= capacity:
            print('Loaded ' + str(items[i][0]))
            current += items[i][1]
            i = i + 1
        else:
            print('Item ' + str(items[i][0]) + ' is too much')
            i = i + 1

    unused = capacity - current
    print('Unused capacity = ' + str(unused))