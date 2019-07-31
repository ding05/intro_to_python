def dinner_calculator(meal_cost, drinks_cost):
    ''' Calculate the cost of dinner during happy hour.
        Takes into consideration:
         - Pre-GST meal and drink costs
         - Happy Hour discounts
         - GST
    '''
    return (meal_cost + drinks_cost * 0.7) * 1.15

print(dinner_calculator(10, 0))
print(dinner_calculator(12, 4))

def bmi():
    ''' BMI = weight / height^2 '''
    weight = input('Enter your weight (kg): ')
    height = input('Enter your height (m): ')
    weight = float(weight)
    height = float(height)
    bmi_value = weight / height ** 2
    print("Your BMI is ", bmi_value)
    
full_name = input('Enter your full name: ')
pos_of_space = full_name.find(' ')
first_name = full_name[0:pos_of_space]
last_name = full_name[pos_of_space+1:]
corrected_first_name = first_name.capitalize()
corrected_last_name = last_name.capitalize()
print('Hi', corrected_first_name, corrected_last_name)

def say_little_hi():
    ''' Hello your name '''
    name = input('Please enter your name: ')
    name_s = name.lower()
    print('Hello there', name_s + '.')
    
def print_date(year, month, day):
    ''' Print out the date, formatted as year-month-day '''
    print(str(year)+'-'+str(month)+'-'+str(day))
    
def address(street_name, street_number):
    ''' Print names and numbers '''
    return str(street_number) + ';' + str(street_name)

def input_and_print_rectangle():
    ''' Recatangle's area calulation '''
    width = input('Rectangle width? ')
    height = input('Rectangle height? ')
    f_width = float(width)
    f_height = float(height)
    area = f_height * f_width
    print('Area:', "%.2f" % area)