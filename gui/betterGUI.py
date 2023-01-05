#Liz's computer runs Python 3.9.2

#In order to use PySimpleGUI you need to make sure that your Python has 
#tkinter already install (this a default module.) Then you have to pip install PySimpleGUI.

import PySimpleGUI as sg   
import FIFO

###########################################################################################
#trial inputValidation function and queue
def validateInput(value1):
    '''Returns tuple (success, extraction_type)'''
    lst = ['apple']
    
    for item in lst:
        if value1 == item:
            return True

    return False

q = FIFO.FIFO()
q.add('first')
q.add('second')

##########################################################################################
#start of GUI
sg.theme('BluePurple')

layout = [[sg.Text('Insert three words from your cards.')], 
          [sg.Input(key='-IN1-')],
          [sg.Input(key='-IN2-')],
          [sg.Input(key='-IN3-')],
          [sg.Text('Insert the "Game Over" card.')],
          [sg.Input(key='-IN4-', background_color = 'red', text_color= 'black' )],
        #   [sg.Button('Check')], 
        #   [sg.Text('Is your input A-okay?'), sg.Text(size=(15,1), key='-CHECKED-')],
          [sg.Button('Get Clue')],
          [sg.Text('Your clue ->:'), sg.Text(size=(27,3), key='-OUTPUT-')]]

window = sg.Window('CodeNames Clues - a cheater app', layout)

#best clue
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
  
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
            break
        else: 
            window['-OUTPUT-'].update('At least one of your inputs do not match the CodeNames 400 word dictionary.')
            break


#clue #2
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #3
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #4
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #5
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #6
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')


#clue #7
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #8
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #9
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')

#clue #10
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break 
    
    if event == 'Get Clue':  
        if validateInput(values['-IN1-']) and validateInput(values['-IN2-']) and validateInput(values['-IN3-']) and validateInput(values['-IN4-']):
            window['-OUTPUT-'].update(q.remove())
        else: 
            window['-OUTPUT-'].update('We repeat: something is wrong with your input.')


window.close()

