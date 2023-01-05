#Liz's computer runs Python 3.9.2

#In order to use PySimpleGUI you need to make sure that your Python has 
#tkinter already install (this a default module.) Then you have to pip install PySimpleGUI.

import PySimpleGUI as sg   
import CodeNames

# initialize dictionaries and queue
a = CodeNames.CodeNames()
a.read_codename_words()
a.create_dictionary()
a.fill_trie()
        

#creating the autocomplete popup window
def autocomplete_popup_show(text_input):
    
    prediction_list = a.perform_auto(text_input)
    
    # If an event string input by the user is not auto-completable, returns to loop
    if prediction_list == None:
        return
    
    if 0 < len(prediction_list) < 100:

        #this creates the popup of the list of possible words with the letter typed
        autocomplete_popup_layout = [[sg.Listbox(values=tuple(prediction_list),
                                                 size=(20, len(prediction_list) * 1),
                                                 enable_events=True, #param enable_events: Turns on the element specific events. Listbox generates events when an item is clicked
                                                 bind_return_key=True, #param bind_return_key: If True, then the return key will cause a the Listbox to generate an event
                                                 auto_size_text=True)]]
                                              
        #this creates the characteristics of the popup window with the list of matched codenames words
        autocomplete_popup = sg.Window("Borderless Window",
                                       default_element_size=(12, 1),
                                       text_justification='c',
                                       auto_size_text=False,
                                       auto_size_buttons=False,
                                       no_titlebar=False,
                                       grab_anywhere=True,
                                       default_button_element_size=(12, 1))

        autocomplete_popup.Layout(autocomplete_popup_layout)
        
        ev, val = autocomplete_popup.Read()
        autocomplete_popup.Close()

        #this returns the selected word from the list popup to the main popup window
        return val[0]



##########################################################################################
#start of GUI
sg.theme('BluePurple')

layout = [[sg.Text('Insert three words from your cards.')], 

          [sg.Input(do_not_clear=True, key='-IN1-', change_submits=True)],
          [sg.Input(do_not_clear=True, key='-IN2-', change_submits=True)],
          [sg.Input(do_not_clear=True, key='-IN3-', change_submits=True)],          
          [sg.Text('Insert the "Game Over" card.')],
          [sg.Input(do_not_clear=True, key='-IN4-', background_color = 'red', text_color= 'black', change_submits=True)],
          [sg.Button('Get Clue')],
          [sg.Text('Your clues ->:'), sg.Text(size=(27,5), key='-OUTPUT-')]]

window = sg.Window('CodeNames Clues - a cheater app', layout)

district_plan_window_active = False
text_input = ""

# Events
while True:  # Event Loop
    event, values = window.read()
    
    #the first word
    if event == '-IN1-':
        text_input1 = values['-IN1-']
        window.Element('-IN1-').Update(autocomplete_popup_show(text_input1))
        
    #the second word
    if event == '-IN2-':
        text_input2 = values['-IN2-']
        window.Element('-IN2-').Update(autocomplete_popup_show(text_input2))
        
    #the third word 
    if event == '-IN3-':
        text_input3= values['-IN3-']
        window.Element('-IN3-').Update(autocomplete_popup_show(text_input3))    
        
    #the fourth word (bad word)
    if event == '-IN4-':
        text_input4 = values['-IN4-']
        window.Element('-IN4-').Update(autocomplete_popup_show(text_input4))        

        
    if event == sg.WIN_CLOSED:
        quit()
  
    if event == 'Get Clue': 
        
        # Update window values after autocomplete filled them in
        values['-IN1-'] = values['-IN1-'][2:-3] 
        values['-IN2-'] = values['-IN2-'][2:-3] 
        values['-IN3-'] = values['-IN3-'][2:-3] 
        values['-IN4-'] = values['-IN4-'][2:-3] 
        
        # Validate the inputs are codename words
        if a.validateInput(values['-IN1-']) and a.validateInput(values['-IN2-']) and a.validateInput(values['-IN3-']) and a.validateInput(values['-IN4-']):
            clues = ''
            if a.queue.empty():
                a.candidates([values['-IN1-'], values['-IN2-'], values['-IN3-']], [values['-IN4-']])
            while a.queue.empty() is False:
                clues = clues + a.next_clue() + '\n'
            window['-OUTPUT-'].update(clues)

        else: 
            window['-OUTPUT-'].update('At least one of your inputs do not match the CodeNames 400 word dictionary.')



