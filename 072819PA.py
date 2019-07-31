def say_little_hi():
    ''' Hello Name '''
    name = input('Please enter your name: ')
    name_s = name.lower()
    print('Hello there', name_s + '.')
    
def print_date(year, month, day):
    ''' Print out the date, formatted as year-month-day '''
    print(str(year)+'-'+str(month)+'-'+str(day))
    
def address(street_name, street_number):
    ''' Print Names and Numbers '''
    return str(street_number) + ';' + str(street_name)

def input_and_print_rectangle():
    ''' Calulation '''
    width = input('Rectangle width? ')
    height = input('Rectangle height? ')
    f_width = float(width)
    f_height = float(height)
    area = f_height * f_width
    print('Area:', "%.2f" % area)