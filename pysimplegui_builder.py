from cgitb import enable
import string
from weakref import finalize
import PySimpleGUI as sg
import json
import os
import textwrap


sg.theme('SandyBeach')     

## Datafile
with open(os.path.join(os.path.dirname(__file__),'data','subfaction_data.json'),"r") as factions_file:
    factions_data = json.load(factions_file)

## Variables

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




## Functions


## Layouts
faction_tab = [
    [
    sg.Text("Select your Faction",),
    sg.Push(),
    sg.Combo(factions,default_value=" ", **combo_style,key='faction_choice',enable_events=True,pad=(1, 1))
    ],
    [
    sg.Text("Subfactions",key='subfaction_text'),
    sg.Push(),
    sg.Combo(subfactions,default_value=" ",**combo_style,key='subfaction_choice',enable_events=True,pad=(1, 1)),
    ],
    [
    sg.Text("Energy Type:"), 
    sg.Push(),
    sg.Text("None", key="energy_type",pad=(1, 1))
    ],
    [
    sg.Text("Energy Pool:"), 
    sg.Push(),
    sg.Text("None", key="energy_pool",pad=(1, 1))
    ],    
    [
    sg.Text("Health Pool:"), 
    sg.Push(),
    sg.Text(10, key="health_pool",pad=(1, 1))
    ],
    [
    sg.Text("Willpower Pool:"), 
    sg.Push(),
    sg.Text(1, key="willpower_pool",pad=(1, 1))
    ],
    [
    sg.Text(" ", key="clan_weakness",pad=(1, 1))
    ],
]

skills_tab = [
    [
        sg.Text("Alchemy",key="alch"),
        sg.Push(),
        sg.Radio(0, "Alchemy", default=True),
        sg.Radio(1, "Alchemy"),
        sg.Radio(2, "Alchemy"),
        sg.Radio(3, "Alchemy"),
        sg.Radio(4, "Alchemy"),
    ],
    [
        sg.Text("Archery",key="arch"),
        sg.Push(),
        sg.Radio(0, "Archery", default=True),
        sg.Radio(1, "Archery"),
        sg.Radio(2, "Archery"),
        sg.Radio(3, "Archery"),
        sg.Radio(4, "Archery"),
    ],
    [
        sg.Text("Brawl",key="brwl"),
        sg.Push(),
        sg.Radio(0, "Brawl", default=True),
        sg.Radio(1, "Brawl"),
        sg.Radio(2, "Brawl"),
        sg.Radio(3, "Brawl"),
        sg.Radio(4, "Brawl"),
    ],
    [
        sg.Text("Dodge",key="doge"),
        sg.Push(),
        sg.Radio(0, "Dodge", default=True),
        sg.Radio(1, "Dodge"),
        sg.Radio(2, "Dodge"),
        sg.Radio(3, "Dodge"),
        sg.Radio(4, "Dodge"),
    ],
    [
        sg.Text("Escape Artist",key="esca"),
        sg.Push(),
        sg.Radio(0, "Escape_Artist", default=True),
        sg.Radio(1, "Escape_Artist"),
        sg.Radio(2, "Escape_Artist"),
        sg.Radio(3, "Escape_Artist"),
        sg.Radio(4, "Escape_Artist"),
    ],
    [
        sg.Text("Fortune Telling",key="frtn"),
        sg.Push(),
        sg.Radio(0, "Fortune_Telling", default=True),
        sg.Radio(1, "Fortune_Telling"),
        sg.Radio(2, "Fortune_Telling"),
        sg.Radio(3, "Fortune_Telling"),
        sg.Radio(4, "Fortune_Telling"),
    ],
    [
        sg.Text("Intimidation",key="intm"),
        sg.Push(),
        sg.Radio(0, "Intimidation", default=True),
        sg.Radio(1, "Intimidation"),
        sg.Radio(2, "Intimidation"),
        sg.Radio(3, "Intimidation"),
        sg.Radio(4, "Intimidation"),
    ],
    [
        sg.Text("Literacy",key="litr"),
        sg.Push(),
        sg.Radio(0, "Literacy", default=True),
        sg.Radio(1, "Literacy"),
        sg.Radio(2, "Literacy"),
        sg.Radio(3, "Literacy"),
        sg.Radio(4, "Literacy"),
    ],
    [
        sg.Text("Lockpicking",key="lock"),
        sg.Push(),
        sg.Radio(0, "Lockpicking", default=True),
        sg.Radio(1, "Lockpicking"),
        sg.Radio(2, "Lockpicking"),
        sg.Radio(3, "Lockpicking"),
        sg.Radio(4, "Lockpicking"),
    ],
    [
        sg.Text("Medicine",key="medi"),
        sg.Push(),
        sg.Radio(0, "Medicine", default=True),
        sg.Radio(1, "Medicine"),
        sg.Radio(2, "Medicine"),
        sg.Radio(3, "Medicine"),
        sg.Radio(4, "Medicine"),
    ],
    [
        sg.Text("Melee",key="mele"),
        sg.Push(),
        sg.Radio(0, "Melee", default=True),
        sg.Radio(1, "Melee"),
        sg.Radio(2, "Melee"),
        sg.Radio(3, "Melee"),
        sg.Radio(4, "Melee"),
    ],
    [
        sg.Text("Smithing",key="smth"),
        sg.Push(),
        sg.Radio(0, "Smithing", default=True),
        sg.Radio(1, "Smithing"),
        sg.Radio(2, "Smithing"),
        sg.Radio(3, "Smithing"),
        sg.Radio(4, "Smithing"),
    ],
    [
        sg.Text("Stealth",key="stel"),
        sg.Push(),
        sg.Radio(0, "Stealth", default=True),
        sg.Radio(1, "Stealth"),
        sg.Radio(2, "Stealth"),
        sg.Radio(3, "Stealth"),
        sg.Radio(4, "Stealth"),
    ],
    [
        sg.Text("Trade",key="trde"),
        sg.Push(),
        sg.Radio(0, "Trade", default=True),
        sg.Radio(1, "Trade"),
        sg.Radio(2, "Trade"),
        sg.Radio(3, "Trade"),
        sg.Radio(4, "Trade"),
    ]
    ]

powers_tab = [
    [
        sg.Text('Powers yo')
    ],
]

merits_tab = [
    [
        sg.Checkbox('Specialist', enable_events=True,key='specialist')
    ],
    [
        sg.Checkbox('Hobbyist', enable_events=True,key='hobbyist')
    ],
    [
        sg.Checkbox('Resilience', enable_events=True,key='relisience')
    ],
    [
        sg.Checkbox('Alchemic Prodigy', enable_events=True,key='alchemic_prodigy')
    ],
    [
        sg.Checkbox('Master of Shadows', enable_events=True,key='master_of_shadows')
    ],
    [
        sg.Checkbox('Master Crafter', enable_events=True,key='master_crafter')
    ],
    [
        sg.Checkbox('Wardancer', enable_events=True,key='wardancer')
    ],
    [
        sg.Checkbox('Master of Battle', enable_events=True,key='master_of_battle')
    ],
    [
        sg.Checkbox('Unkillable', enable_events=True,key='unkillable')
    ],
    [
        sg.Checkbox('Hedge Mage', enable_events=True,key='hedgemage')
    ],    
]

button_frame = [[
    sg.Button("Generate Sheet")
]]

layout = [[
#    sg.Frame('Faction Choice',layout=faction_frame),
    sg.TabGroup([
        [sg.Tab('Factions', faction_tab),
        sg.Tab('Skills', skills_tab),
        sg.Tab('Merits', merits_tab),
        sg.Tab('Powers', powers_tab)
        ]])],
    [sg.Column(button_frame, pad=(0, None)),    
]]


# Create the window
window = sg.Window("Darkwood Nights Character Builder", layout, resizable=True, finalize=True)

subfaction = ['subfaction_choice']


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
            window["energy_type"].update("Vitae")
            event, values = window.read()
        elif values['subfaction_choice'] == "Gifted Kinfolk":
            window["energy_type"].update("Gnosis")
            event, values = window.read()
        else:
            window["energy_type"].update("None")
            event, values = window.read()
        event, values = window.read()
    elif values['faction_choice'] == "Vampire":
        window["subfaction_text"].update("Select your Clan")
        window["energy_type"].update("Vitae")
        window['subfaction_choice'].update(values=vampire_subfactions)
        subfaction = ['subfaction_choice']
        event, values = window.read()
        window['clan_weakness'].update(values=factions_data["Vampire"]["Clans"][subfaction]["Clan Flaw"])
        event, values = window.read()
    elif values['faction_choice'] == "Mage":
        window["subfaction_text"].update("Select your Fellowship")
        window["energy_type"].update("Quintessence")
        window['subfaction_choice'].update(values=mage_subfactions)
        event, values = window.read()
    elif values['faction_choice'] == "Fae":
        window["subfaction_text"].update("Select your Origin")
        window["energy_type"].update("Mists / Weaving")
        window['subfaction_choice'].update(values=fae_subfactions)
        event, values = window.read()
# if Trade selected; if Hobbyist Merit
    print(event, values)

window.close()