from cgitb import enable
import string
from weakref import finalize
import PySimpleGUI as sg

sg.theme('SandyBeach')     

combo_style = {
    'size': (19, 1)
}
text_style = {
    'size': (16, 1)
}
box_style = {
    'size': (15, 1)
}
longbox_sytle = {
    'size': (53, 1)
}

factions = [" ","Human","Vampire","Mage","Fae"]
subfactions = []
human_subfactions = ["Commoner","Ghoul","Gifted Kinfolk","Kinfolk"]
vampire_subfactions = ["Assamite","Baali","Brujah","Cappadocian","Follower of Set","Gangrel","Malkavian","Nosferatu","Lasombra","Salubri (Healer)","Salubri (Warrior)","Toreador","Tzimisce","Ventrue"]
mage_subfactions = ["Ahl-i-Batin","Messianic Voice","Old Faith","Order of Hermes","Spirit Talker","Valdaerman","Veneficti"]
fae_subfactions = ["Changeling","Firstborn","Inanimae"]

skills_list = ["Alchemy", "Archery", "Brawl", "Dodge", "Escape Artist", "Fortune Telling", "Intimidation", "Literacy", "Lockpicking", "Medicine", "Melee", "Smithing", "Stealth", "Trade"]
skills_dict = {
    "Alchemy":"alch",
    "Archery":"arch",
    "Brawl":"brwl",
    "Dodge":"doge",
    "Escape Artist":"esca",
    "Fortune Telling":"frtn",
    "Intimidation":"intm",
    "Literacy":"litr",
    "Lockpicking":"lock",
    "Medicine":"medi",
    "Melee":"mele",
    "Smithing":"smth",
    "Stealth":"stel",
    "Trade":"trde"
}
skill_headings = ['Skill', '1','2','3','4']

faction_tab = [[
    sg.Text("Select your Faction", **text_style),
    sg.Combo(factions,default_value=" ", **combo_style,key='faction_choice',enable_events=True,pad=(1, 1)),
    sg.Text("Subfactions",key='subfaction_text', **text_style),
    sg.Combo(subfactions,default_value=" ",**combo_style,key='subfaction_choice',enable_events=True,pad=(1, 1)),        
    sg.Text("Energy Type: ", **text_style, key="energy_type",pad=(1, 1)),
    ]]
    
skills_tab = [[sg.T('Skillz yo')]]

powers_tab = [[sg.T('Powers yo')],[sg.Input(key='in')]]

button_frame = [[
    sg.Button("Generate Sheet")
]]

layout = [[
#    sg.Frame('Faction Choice',layout=faction_frame),
    sg.TabGroup([
        [sg.Tab('Factions', faction_tab),
        sg.Tab('Skills', skills_tab),
        sg.Tab('Powers', powers_tab)]])],
    [sg.Column(button_frame, pad=(0, None)),    
]]


# Create the window
window = sg.Window("Darkwood Nights Character Builder", layout, resizable=True, finalize=True)



# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the Generate Sheet button
    if event == "Generate Sheet" or event == sg.WIN_CLOSED:
        break
    if values['faction_choice'] == " ":
        selection = "No Faction Selected"
    elif values['faction_choice'] == "Human":
        window["subfaction_text"].update("Select your Subfaction")
        window['subfaction_choice'].update(values=human_subfactions)
        if values['subfaction_choice'] == "Ghoul":
            window["energy_type"].update("Energy Type: Vitae")
            event, values = window.read()
        elif values['subfaction_choice'] == "Gifted Kinfolk":
            window["energy_type"].update("Energy Type: Gnosis")
            event, values = window.read()
        else:
            window["energy_type"].update("Energy Type: None")
            event, values = window.read()
        event, values = window.read()
    elif values['faction_choice'] == "Vampire":
        window["subfaction_text"].update("Select your Clan")
        window["energy_type"].update("Energy Type: Vitae")
        window['subfaction_choice'].update(values=vampire_subfactions)
        event, values = window.read()
    elif values['faction_choice'] == "Mage":
        window["subfaction_text"].update("Select your Fellowship")
        window["energy_type"].update("Energy Type: Quintessence")
        window['subfaction_choice'].update(values=mage_subfactions)
        event, values = window.read()
    elif values['faction_choice'] == "Fae":
        window["subfaction_text"].update("Select your Origin")
        window["energy_type"].update("Energy Type: Mists / Weaving")
        window['subfaction_choice'].update(values=fae_subfactions)
        event, values = window.read()
    print(event, values)

window.close()