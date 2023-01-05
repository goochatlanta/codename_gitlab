#Liz's computer runs Python 3.9.2

#In order to use PySimpleGUI you need to make sure that your Python has 
#tkinter already install (this a default module.) Then you have to pip install PySimpleGUI.

import PySimpleGUI as sg   
import CodeNames

# initialize dictionaries and queue
a = CodeNames.CodeNames()
a.read_codename_words()
a.create_dictionary()


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
          [sg.Text('Your clues ->:'), sg.Text(size=(27,5), key='-OUTPUT-')]]

window = sg.Window('CodeNames Clues - a cheater app', layout)

#best clue
while True:  # Event Loop
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        quit()
  
    if event == 'Get Clue': 
        
        if a.validateInput(values['-IN1-']) and a.validateInput(values['-IN2-']) and a.validateInput(values['-IN3-']) and a.validateInput(values['-IN4-']):
            clues = ''
            if a.queue.empty():
                a.candidates([values['-IN1-'], values['-IN2-'], values['-IN3-']], [values['-IN4-']])
            while a.queue.empty() is False:
                clues = clues + a.next_clue() + '\n'
            window['-OUTPUT-'].update(clues)

        else: 
            window['-OUTPUT-'].update('At least one of your inputs do not match the CodeNames 400 word dictionary.')



