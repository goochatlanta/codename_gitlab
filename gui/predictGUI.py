#Liz's computer runs Python 3.9.1 

#In order to use PySimpleGUI you need to make sure that your Python has 
#tkinter already install (this a default module.) Then you have to pip install PySimpleGUI.


import PySimpleGUI as sg
import re

#reading in the codenames 400 words as lowercase without the /n at the end of the lines.
codenames_list = []
with open("words400.txt", "r") as wordsfile:
    for line in wordsfile:
        codenames_list.append(line.strip().lower())

######################################################################
#list of words and its special popup window

#creating the autocomplete popup window
def autocomplete_popup_show(text_input, text_list):


    def predict_text(input, lista):

        #this selects the words in the codenames list the have the typed letter as their first letter
        pattern = re.compile(input + '.*')

        #this matches the first letter typed to the first letter of the words in codenames_list
        return [w for w in lista if re.match(pattern, w)]

    #using function - predict_text, we have the letter typed (text_input) and 
    prediction_list = predict_text(text_input, text_list)
    
    #this allows there to be alot of options for words to choose in the popup window.
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

################################################################
#main window

#these are the characteristics of the main popup window with the text boxes and submit buttom
text_window_layout = [[sg.Text('Playing Code Names? ')],
                               [sg.Text('What words are you considering?')],
                               [sg.Text('Insert two words from your cards.')],
                               [sg.Input(do_not_clear=True, key="text_input1", change_submits=True)],
                               [sg.Input(do_not_clear=True, key="text_input2", change_submits=True)],
                               [sg.Text('Insert the "Game Over" card.')],
                               [sg.Input(do_not_clear=True, key="text_input3", change_submits=True)],
                               [sg.Button('Get Clues!')]]

#this is the main popup window that draws on the layout above. Get a Clue! is the title of this main window.
input_window = sg.Window('Get a Clue!').Layout(text_window_layout)

district_plan_window_active = False
text_input = ""

#this creates the persisent main window that is waiting for texts to be inputted.
while True:

    window_events, window_values = input_window.Read()
    
    #the first word
    text_input = window_values['text_input1']
    input_window.Element('text_input1').Update(autocomplete_popup_show(text_input, codenames_list))
    
    #the second word
    text_input = window_values['text_input2']
    input_window.Element('text_input2').Update(autocomplete_popup_show(text_input, codenames_list))

    #the third word (bad word)
    text_input = window_values['text_input3']
    input_window.Element('text_input3').Update(autocomplete_popup_show(text_input, codenames_list))

    #this persistent window closes when one of two buttons is pushed.
    if window_events == sg.WIN_CLOSED or window_events == 'Get Clues!':
        break

input_window.Close()

##################################################################
#the results for sending to runCodeNames

#Data for the computations
goodWords = [ window_values['text_input1'],  window_values['text_input2']]

badWord = [ window_values['text_input3']]

#import file of Will's computations with these functions
#candidates will replace `text_input` in output box 
#outputList = candidates( goodWords, badWord ) #don't use tabulate which returns a pandas table

#temp output
outputList = 'answer1, answer2, answer3, answer4, answer5'
###################################################################
#answer window - very simple

sg.popup('Your clues! (Ordered by best fit.)', outputList)