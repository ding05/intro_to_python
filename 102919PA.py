class Taganeran:
    ''' Define the Taganeran class.
    Data attributes: name of type str
                     height (metres) of type float
                     has_nose of type bool
                     jujubes of type int
    Methods: say_hello(), collect_jujubes(), eat(), feast()
    '''

    def __init__(self, name, height, has_nose=False):
        ''' Taganeran constructor '''
        self.name = name
        self.height = height
        self.has_nose = has_nose
        self.jujubes = 0
    
    def say_hello(self):
        ''' Print a message '''
        if self.has_nose == False:
            print('Hello. My name is ' + str(self.name) + '.')
        else:
            print('HELLO. MY NAME IS ' + str(self.name.upper()) + '.')
    
    def __str__(self):
        ''' Return a string '''
        if self.has_nose == False:
            temp = '{0} is a {1:.2f} m tall Taganeran!'.format(self.name, self.height)
            return temp
        else:
            temp = '{0} is a {1:.2f} m tall Taganeran with a nose!'.format(self.name, self.height)
            return temp
    
    def collect_jujubes(self, number=1):
        ''' Add the amount '''
        self.jujubes += number
    
    def eat(self):
        ''' Eat one '''
        if self.jujubes >= 1:
            self.jujubes -= 1
            self.height += 0.2
        else:
            print("I don't have any jujubes to eat!")
    
    def feast(self):
        ''' Eat five '''
        if self.jujubes >= 5:
            self.jujubes -= 5
            if self.has_nose == False:
                self.has_nose = True
            else:
                self.height = 1.5 * self.height
        else:
            print("I don't have enough jujubes to feast!")

class Geeble:
    ''' Define the Geeble class.
    Data attributes: level of type str
                     name of type str
                     health of type float
    Methods: inflict()
    '''
    
    def __init__(self, level, name, health):
        ''' Geeble! '''
        self.level = level
        self.name = name
        self.health = health
    
    def __str__(self):
        ''' Return a string '''
        if self.level in ['Sooglet', 'Throve', 'Plaguelet']:
            if self.health < 0:
                temp = '{0} ({1}), health = 0.0'.format(self.name, self.level)
            else:
                temp = '{0} ({1}), health = {2:.1f}'.format(self.name, self.level, self.health)                
            return temp
        else:
            temp = 'Invalid Geeble level'
            return temp
    
    def inflict(self, number):
        ''' Minus a number '''
        if self.health - number < 0:
            self.health = 0
        else:
            self.health -= number