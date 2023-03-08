from cgitb import enable
from weakref import finalize
import PySimpleGUI as sg

sg.theme('SandyBeach')     

factions = [" ","Human","Vampire","Mage","Fae"]

layout = [
    [sg.Text("Darkwood Nights Character Builder")], 
    [sg.Text("Select your Faction",size = (20, 1),font = 'Lucida',justification = 'left')],
    [sg.Combo([" ","Human","Vampire","Mage","Fae"],default_value=" ",key='faction_choice',enable_events=True)],
    [sg.Text(" ",key='txt')],
    [sg.Button("Generate Sheet")]
]

# Create the window
window = sg.Window("Darkwood Nights Character Builder", layout, resizable=True).Finalize()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Generate Sheet button
    if event == "Generate Sheet" or event == sg.WIN_CLOSED:
        break
    print(event, values)
    if values['faction_choice'] == " ":
        selection = "No Faction Selected"
        window["txt"].update(selection)
        sg.Text("New Text Here")
    elif values['faction_choice'] == "Human":
        selection = "Human Build"
        window["txt"].update(selection)
    elif values['faction_choice'] == "Vampire":
        selection = "Vampire Build"
        window["txt"].update(selection)
    elif values['faction_choice'] == "Mage":
        selection = "Mage Build"
        window["txt"].update(selection)
    elif values['faction_choice'] == "Fae":
        selection = "Fae Build"
        window["txt"].update(selection)

window.close()