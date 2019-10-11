""" 
''' Display a windowing saying 'COSC121' '''
from tkinter import *
from tkinter.ttk import *

def main():
    ''' Construct the GUI and start it running '''
    window = Tk()
    cosc_label = Label(window, text = 'COSC121')
    cosc_label.grid(row = 0, column = 0)
    window.mainloop()

main()
"""

"""
''' Say hello or goodbye '''
from tkinter import *
from tkinter.ttk import *

def say_hello():
    ''' Event handler for clicks on the button '''
    global message_label
    message_label['text'] = 'Hello!'

def say_goodbye():
    ''' Event handler for clicks on the button '''
    global message_label
    message_label['text'] = 'Bye!'

def main():
    ''' Construct the GUI and run it '''
    global message_label
    window = Tk()
    message_label = Label(window, text = 'Click a button!')
    message_label.grid(row = 0, column = 0)
    hello_button = Button(window, text = 'Say hello', command = say_hello)
    hello_button.grid(row = 1, column = 0)
    goodbye_button = Button(window, text = 'Say goodbye', command = say_goodbye)
    goodbye_button.grid(row = 1, column = 1)
    window.mainloop()

main()
"""

"""
''' A sample counter '''
from tkinter import *
from tkinter.ttk import *

def add():
    ''' Event handler for clicks on the button '''
    global message_label, count
    count += 1
    message_label['text'] = count

def minus():
    ''' Event handler for clicks on the button '''
    global message_label, count
    count -= 1
    message_label['text'] = count

def main():
    ''' Construct the GUI and run it '''
    global message_label, count
    count = 0
    window = Tk()
    message_label = Label(window, text = 0)
    message_label.grid(row = 0, column = 0)
    add_button = Button(window, text = '+1', command = add)
    add_button.grid(row = 1, column = 0)
    minus_button = Button(window, text = '-1', command = minus)
    minus_button.grid(row = 1, column = 1)
    window.mainloop()

main()
"""

"""
''' Add 1 or 5 or Substract 1 or 5 '''
from tkinter import *
from tkinter.ttk import *

def change_message(number):
    ''' Set the global value label '''
    global value, value_label
    value += number
    value_label['text'] = value
    
def subtract_five():
    ''' Command handler '''
    change_message(-5)

def subtract_one():
    ''' Command handler '''
    change_message(-1)

def add_one():
    ''' Command handler '''
    change_message(+1)

def add_five():
    ''' Command handler '''
    change_message(+5)

def main():
    ''' Set up the GUI and run it '''
    global value, value_label
    window = Tk()
    value = 0
    value_label = Label(window, text = str(value))
    value_label.grid(row = 0, column = 0, columnspan = 4)
    subtract_five_button = Button(window, text = '-5', command = subtract_five)
    subtract_five_button.grid(row = 1, column = 0)
    subtract_one_button = Button(window, text= '-1', command = subtract_one)
    subtract_one_button.grid(row = 1, column = 1)
    add_one_button = Button(window, text = '+1', command = add_one)
    add_one_button.grid(row = 1, column = 2)
    add_five_button = Button(window, text = '+5', command = add_five)
    add_five_button.grid(row = 1, column = 3)
    window.mainloop()

main()
"""

"""
''' Display the name input '''
from tkinter import *
from tkinter.ttk import *

def process_name():
    ''' Do something with the name '''
    global name_entry, message_label
    message_label['text'] = 'Hi ' + name_entry.get()

def main():
    ''' Set up the GUI and run it '''
    global name_entry, message_label
    window = Tk()
    name_label = Label(window, text = 'Enter a name below')
    name_label.grid(row = 0, column = 0)
    message_label = Label(window)
    message_label.grid(row = 3, column = 0)    
    name_entry = Entry(window, text = '')
    name_entry.grid(row = 1, column = 0)
    button = Button(window, text = 'Say hello', command = process_name)
    button.grid(row = 2, column = 0, columnspan = 2)
    window.mainloop()

main()
"""

"""
''' Display the doubled '''
from tkinter import *
from tkinter.ttk import *

def process_double():
    ''' Do something with the number '''
    global number_entry, message_label
    number_entry = int(number_entry.get()) * 2
    message_label['text'] = number_entry

def main():
    ''' Set up the GUI and run it '''
    global number_entry, message_label
    window = Tk()
    message_label = Label(window)
    message_label.grid(row = 3, column = 0)    
    number_entry = Entry(window, text = '')
    number_entry.grid(row = 1, column = 0)
    button = Button(window, text = 'Double it!', command = process_double)
    button.grid(row = 2, column = 0, columnspan = 2)
    window.mainloop()

main()
"""

"""
''' A simple caclulator '''
from tkinter import *
from tkinter.ttk import *

def process_cal():
    ''' Do something with the number '''
    global left_entry, right_entry, message_label, numbers
    if numbers.get() == "+":
        message_label['text'] = '=' + str(int(left_entry.get()) + int(right_entry.get()))
    if numbers.get() == "-":
        message_label['text'] = '=' + str(int(left_entry.get()) - int(right_entry.get()))
    if numbers.get() == "*":
        message_label['text'] = '=' + str(int(left_entry.get()) * int(right_entry.get()))

def left_side():
    ''' Do something with the number '''
    global left_entry, right_entry, message_label, numbers
    left_entry.get()

def right_side():
    ''' Do something with the number '''
    global left_entry, right_entry, message_label, numbers
    right_entry.get()

def main():
    ''' Set up the GUI and run it '''
    global left_entry, right_entry, message_label, numbers
    window = Tk()
    left_entry = Entry(window)
    left_entry.grid(row = 0, column = 0)
    right_entry = Entry(window)
    right_entry.grid(row = 0, column = 2)
    message_label = Label(window)
    message_label.grid(row= 0 , column = 3)     
    operator = ['+', '-', '*']
    numbers = Combobox(window, values = operator)
    numbers.set('+')
    numbers.grid(row = 0, column = 1)
    calc_button = Button(window, text = 'Calculate', command = process_cal)
    calc_button.grid(row = 1, column = 1)
    window.mainloop()

main()
"""

"""
''' An exercise in improving layout '''
from tkinter import *
from tkinter.ttk import *

def calculate():
    ''' Calculate twice the number and set that answer into result'''
    global entry, result_label
    result_label['text'] = 2 * int(entry.get())

def main():
    ''' Every home should have one '''
    global entry, result_label
    window = Tk() 
    header = Label(window, text = 'Doubler', font = ("Arial", 18))
    header.grid(row = 0, column = 0, columnspan = 3, pady = 10)
    entry = Entry(window, width = 5)
    entry.grid(row = 1, column = 0, padx = (20, 0), pady = 10)
    times_2 = Label(window, text = ' * 2 = ')
    times_2.grid(row = 1, column = 1)
    result_label = Label(window, text = '0')
    result_label.grid(row = 1, column = 2, padx = (0, 20))
    button = Button(window, text = "Calculate", command = calculate)
    button.grid(row = 2, column = 0, columnspan = 3, pady = 10)
    window.mainloop()

main()
"""

''' Demonstrate event binding and variable tracing, this time with a clean
    OO design.
'''
from tkinter import *
from tkinter.ttk import *

class CounterGui:
    ''' The GUI class '''
    
    def __init__(self, window):
        ''' Setup the label and button on given window '''
        self.count = 0
        self.message_label = Label(window, text = 0)
        self.message_label.grid(row = 0, column = 0)
        self.add_button = Button(window, text = '+1', command = self.add)
        self.add_button.grid(row = 1, column = 0)
        self.minus_button = Button(window, text = '-1', command = self.minus)
        self.minus_button.grid(row = 1, column = 1)        

    def add(self):
        ''' Event handler for clicks on the button '''
        self.count += 1
        self.message_label['text'] = self.count
        
    def minus(self):
        ''' Event handler for clicks on the button '''
        self.count -= 1
        self.message_label['text'] = self.count
        
def main():
    ''' Set up the GUI and run it '''
    window = Tk()
    greeting_gui = CounterGui(window)
    window.mainloop()

main()