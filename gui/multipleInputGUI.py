#Liz's computer runs Python 3.9.1 

#In order to use PySimpleGUI you need to make sure that your Python has 
#tkinter already install (this a default module.) Then you have to pip install PySimpleGUI.


import pdb
import PySimpleGUI as sg      
   

sg.theme('DarkAmber')    # Keep things interesting for your users

#if we choose to do predictive inputs, have an event that corresponds to the letters typed. 

layout = [[sg.Text('Insert two words from your cards.')],      
          [sg.Input(key='-IN1-')],
          [sg.Input(key='-IN2-')],  
          [sg.Text('Insert the "Game Over" card.')], 
          [sg.Input(key='-IN3-', background_color = 'red', text_color= 'black' ) ],   
          [sg.Button('Get Clue')]]      

window = sg.Window('CodeNames Clue Generator', layout)      

while True:                             # The Event Loop
    event, values = window.read() 
    print(event, values)       
    if event == sg.WIN_CLOSED or event == 'Get Clue':
        break      


window.close()

text_input = values['-IN2-'] 

#Data for the computations
goodWords = [values['-IN1-'], values['-IN2-']]

badWord = [values['-IN3-']]

#import file of Will's computations with these functions
#candidates will replace `text_input` in output box 
#outputList = candidates( goodWords, badWord ) #don't use tabulate which returns a pandas table

sg.popup('Your clue!', text_input)


