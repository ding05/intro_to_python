def get_column(game, col_num):
    ''' Get the columns '''
    col = col_num
    result = []
    for i in range(0, 3):
        temp = game[i]
        result.append(temp[col])
    return result

def print_odd_cubes_to_number(number):
    ''' Print odds and their cubes '''
    if number < 1:
        print('ERROR: number must be at least 1')
    else:
        for i in range(1, number + 1):
            if i % 2 != 0:
                print(i, '*', i, '*', i, '=', i ** 3)

def print_hundred(nums):
    ''' Rewrite with while-loop '''
    total = 0
    i = 0
    while total <= 100 and i < len(nums):
        total = nums[i] + total
        print(nums[i])
        i = i + 1

def my_enumerate(items):
    ''' Like enumerate() '''
    temp = []
    for i in range(0, len(items)):
        temp_1 = (i, items[i])
        temp.append(temp_1)
    return temp

def num_rushes(slope_height, rush_height_gain, back_sliding):
    ''' Use the template '''
    current_height = 0
    rushes = 0
    while current_height < slope_height:
        current_height = current_height + rush_height_gain
        rushes = rushes + 1
        if current_height >= slope_height:
            break
        else:
            current_height = current_height - back_sliding
    return rushes

def rumbletron(strings):
    ''' Reserve and capitalize '''
    temp = []
    for i in range(0, len(strings)):
        string = strings[i]
        string = string[::-1]
        string = string.upper()
        temp.append(string)
    return temp