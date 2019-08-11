''' Main program '''

def formatted_title(given_name, family_name, weight):
    ''' Return a string containing the family name, given name and weight in brackets '''
    cap_family_name = str(family_name.upper())
    first_given_name = str(given_name.capitalize())
    float_weight = '{:.1f}'.format(float(weight))
    title = cap_family_name + ', ' + first_given_name + ' (' + str(float_weight) + ' kg)'
    return title

def metres_from_steps(num_steps, step_length):
    ''' Return the total distance covered '''
    result = float(num_steps * step_length)
    return result

def activity_level_from_steps(steps):
    ''' Activity level indicated by the given number of steps '''
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

def health_risk(activity_level, is_smoker):
    ''' Level of health risk '''
    if activity_level == 'alive?' or activity_level == 'sedentary':
        if is_smoker == True:
            level = 'extreme'
        else:
            level = 'high'
    elif activity_level == 'very low' or activity_level == 'low':
        if is_smoker == True:
            level = 'high'
        else:
            level = 'medium'
    elif activity_level == 'active' or activity_level == 'very active':
        if is_smoker == True:
            level = 'medium'
        else:
            level = 'low'
    return level

def main():
    ''' Program containing all the functions above '''
    
    given_name = input('Given name: ')
    family_name = input('Family name: ')
    weight = input('Weight: ')
    step_length = input('Step length (in m): ')
    num_steps = input('Number of steps: ')
    is_smoker = input('Do you smoke (y or n): ')
    
    weight = float(weight)
    step_length = float(step_length)
    num_steps = int(num_steps)   
    
    print()
    print('-------------------------')
       
    title = formatted_title(given_name, family_name, weight)
    print(title)
    print('-------------------------')
    print('Steps Walked =', num_steps)
    
    result = metres_from_steps(num_steps, step_length)
    result = '{:.1f}'.format(result)
    print('Distance Walked =', result)
    
    steps = num_steps
    
    level = activity_level_from_steps(steps)
    print('Activity Level =', level)
    
    if is_smoker.lower() == 'y':
        is_smoker = 1 > 0
    elif is_smoker.lower() == 'n':
        is_smoker = 1 < 0
    activity_level = level
    
    level = health_risk(activity_level, is_smoker)
    print('Health Risk =', level)
    print('-------------------------')
    
main()