def silly(i, j):
    ''' Does something silly '''
    return j <= i and i > 3 and j < 12

def is_fashionable(socks_colour, tie_colour):
    ''' Test if you are fashionable '''
    if socks_colour == 'black' and tie_colour == 'pink':
        return 1 < 0
    else:
        return 1 > 0
    
def divisible_by_5(number):
    ''' Test if the number is divisible by 5 '''
    number_5 = number % 5
    if number_5 == 0:
        return 1 > 0
    else:
        return 1 < 0
    
def th_at_either_end(string):
    ''' Test if the string starts or ends with 'th' '''
    return string.startswith('th') or string.endswith('th')

def is_ok(volume):
    ''' Test if volume is at least 95.027 '''
    return volume >= 95.027

def risk_level(weight, age):
    ''' Use weights and ages to know the risk level '''
    if weight <= 61 and age < 70:
        return 1
    elif weight > 61 and age < 70:
        return 6
    elif weight <= 61 and age >= 70:
        return 4
    else:
        return 8