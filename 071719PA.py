def point_string(x, y):
    ''' Return a string referencing a point at (x, y) '''
    return "Point is at ("+str(x)+", "+str(y)+")"

    p1_string = point_string(10, 20)
    p2_string = point_string(5000, -90)
    print(p1_string)
    print(p2_string)
    print(point_string(0, 10))

def full_name(first_name, last_name):
    ''' Return a string consisting of the first name, a space and the last name '''
    return first_name + ' ' + last_name

def date_string(day_num, month_name, year_num):
    ''' Turn the date into a string of the form day month, year '''
    return str(day_num) + ' ' + month_name + ', ' + str(year_num)

def print_date(year, month, day):
    ''' Print out the date, formatted as year-month-day '''
    print(str(year)+'-'+str(month)+'-'+str(day))
    
def welcome_person():
    ''' Says hello to someone '''
    name = input("What is your name? ")
    print("Hello " + name)
    
def get_and_print_age():
    '''Prompt for a person's age, and print how old they'll be next year '''
    age_as_string = input("How old are you? ")
    age = int(age_as_string)
    print("Next year you'll be", age + 1)
    
def get_and_print_rectangle():
    ''' Input a rectangle's width and height then print its area '''
    str_width = input("Rectangle width? ")
    str_height = input("Rectangle height? ")
    width = float(str_width)
    height = float(str_height)
    print("The area of the rectangle is:", width * height)
    
def say_hi():
    ''' Ask one's name '''
    name = input("What is your name? ")
    name_1 = name.capitalize()
    print('Hi', name_1)
    
    total = 10
    count = 3
    average = total/count
    print('Average is {0} over {1} or {2:.2f}'.format(total, count, average))
    
def print_vector(x_coord, y_coord):
    ''' Print shortened coordinates '''
    x_coord_float = float(x_coord)
    y_coord_float = float(y_coord)
    print('(x, y) = ({0:.1f}, {1:.1f})'.format(x_coord_float, y_coord_float))