def my_abs(value):
    ''' Return aboslute value '''
    if value < 0:
        value = - value
    return value

def is_odd(number):
    ''' Test if it is odd '''
    if number % 2 == 1:
        return number % 2 == 1
    else:
        return number % 2 == 1

def silly(i, j):
    ''' Does something silly '''
    return  i > j and i != 3 and j != 2

def x_at_either_end(string):
    ''' True if starts or ends with x '''
    return string.startswith('x') or string.endswith('x')

def same_ends(string_1, string_2):
    ''' Two words start and end with the same character but are not the same '''
    if string_1 == string_2:
        return 1 < 0
    elif string_1[0] == string_2[0] and string_1[-1] == string_2[-1]:
        return 1 > 0
    else:
        return 1 < 0

def bmi_risk(bmi, age):
    ''' Test BMI and ages '''
    if age < 45 and age > 0:
        if bmi < 22 and bmi > 0:
            return 'Low'
        elif bmi >= 22:
            return 'Medium'
    elif age >= 45:
        if bmi < 22 and bmi > 0:
            return 'Medium'
        elif bmi >= 22:
            return 'High'

def thing(i, j):
    ''' Does something silly '''
    return i > 10 and j >= 5 and i < 20

''' Main program '''
def main():
    ''' Program to determine if a person is allowed to drive '''
    alcohol_level_string = input("Enter blood alcohol level (mg/100ml): ")
    alcohol_level = float(alcohol_level_string)
    age_string = input("Enter age in years: ")
    age = float(age_string)
    if (age < 20 and alcohol_level > 0):
        print("You're not allowed to drive")
    elif (age >= 20 and alcohol_level >= 50):
        print("You're not allowed to drive")
    elif (age >= 20 and alcohol_level >= 30 and alcohol_level < 50):
        print("You're legally allowed to drive, but please don't")
    else:
        print("You're allowed to drive")
main()