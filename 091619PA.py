def print_game_score(points, maximum_points=500):
    ''' Return a ratio and a percent '''
    percent = points / maximum_points * 100
    percent = '{:.1f}'.format(percent)
    points = '{:.1f}'.format(points)
    maximum_points = '{:.1f}'.format(maximum_points)
    print('Your points: ' + points + '/' + maximum_points + ' (' + percent + '%)')

def describe(name='Unknown name', species='unknown creature', age='unknown'):
    ''' Return a sentence '''
    age = str(age)
    print(name + ' is a ' + species + ', age: ' + age + '.')

def print_nth_item(data, n):
    ''' Use 'except' '''
    try:
        print(data[n])
    except:
        print('Invalid position provided.')

def print_nth_item_divided(data, n, divisor):
    ''' Use specific 'except' '''
    try:
        print(data[n] / divisor)
    except IndexError:
        print('Invalid position provided.')
    except TypeError:
        print('Parameters must be numbers.')
    except ZeroDivisionError:
        print('Cannot divide by zero.')