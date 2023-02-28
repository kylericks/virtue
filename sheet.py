# Imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
import json
import csv
import os

# Variables for Testing
pc_name = " "
player_name = " "
xp_total = str()
faction = "Vampire"
subfaction = "Nosferatu"
energy_type = str()
health = str()
willpower = str()
energy_pool = int()
awareness = 1
font = 0
generation = 10
road = "Kings"
road_rank = 4
vps = 1
pc_skills = {
    "alch": 0,
    "arch": 0,
    "brwl": 0,
    "doge": 0,
    "esca": 0,
    "frtn": 0,
    "intm": 0,
    "litr": 0,
    "lock": 0,
    "medi": 0,
    "mele": 0,
    "smth": 0,
    "stel": 0,
    "trde": 0,
    "trade_specialty": " "
}

pc_trees = {
    "Animalism":1,
    "Auspex":0,
    "Celerity":1,
    "Chimerstry":0,
    "Daimoinion":0,
    "Dementation":0,
    "Dominate":0,
    "Fortitude":0,
    "Mortis: Grave's Decay":5,
    "Mortis: Corpse in the Monster":1,
    "Mortis: Cadaverous Animation":3,
    "Obfuscate":0,
    "Obtenebration":0,
    "Potence":0,
    "Presence":0,
    "Protean":0,
    "Quietus":0,
    "Serpentis":0,
    "Valeren (Healing)":1,
    "Valeren (Warrior)":0,
    "Vicissitude":0
}
'''
pc_trees = {
    "Blot":1,
    "Fara":0,
    "Forlog":0,
    "Galdar":0,
    "Hjaldar":0
}
'''

# Variables for stuff and things
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
base_x = 20
base_y = 750

with open(os.path.join(os.path.dirname(__file__),'data','subfaction_data.json'),"r") as factions_file:
    factions = json.load(factions_file)

def borders(my_canvas,base_x,base_y):
    my_canvas.line(base_x, base_y-70, base_x+570, base_y-70)
    my_canvas.line(base_x, base_y-310, base_x+320, base_y-310)
    my_canvas.line(base_x+160, base_y-70, base_x+160, base_y-310)
    my_canvas.line(base_x+320, base_y-70, base_x+320, base_y-310)

def vitae_pool():
    global energy_pool
    global vps
    if generation == 13:
        energy_pool = 10
    elif generation == 12:
        energy_pool = 11
    elif generation == 11:
        energy_pool = 12
    elif generation == 10:
        energy_pool = 13
    elif generation == 9:
        energy_pool = 14
        vps = 2
    elif generation == 8:
        energy_pool = 15
        vps = 3
    elif generation == 7:
        energy_pool = 20
        vps = 4
    elif generation == 6:
        energy_pool = 30
        vps = 6
    elif generation == 5:
        energy_pool = 40
        vps = 8
    elif generation == 4:
        energy_pool = 50
        vps = 10
    else:
        energy_pool = 0

def determine_energy():
    global energy_type
    global energy_pool
    if faction == "Human":
        if subfaction == "Ghoul":
            energy_type = "Vitae"
            energy_pool = "10"
        elif subfaction == "Gifted Kinfolk":
            pass
        else:
            pass
    elif faction == "Vampire":
        energy_type = "Vitae"
        vitae_pool()
    elif faction == "Mage":
        energy_type = "Quintessence"
        energy_pool = 10+(font*2)
    elif faction == "Fae":
        pass
    else:
        my_canvas.drawString(base_x+170, base_y-90, "Get it together "+player_name)

def header_block(my_canvas,base_x,base_y):
    my_canvas.drawString(base_x+150, base_y, "Darkwood Nights Player Character Sheet")
    my_canvas.drawString(base_x, base_y-25, "PC Name:      "+pc_name)
    my_canvas.drawString(base_x+200, base_y-25, "Faction:          "+faction)    
    my_canvas.drawString(base_x+400, base_y-25, "Health:          "+str(health))    
    my_canvas.drawString(base_x, base_y-40, "Player Name: "+player_name)
    my_canvas.drawString(base_x+200, base_y-40, "Sub-Faction:   "+subfaction)
    my_canvas.drawString(base_x+400, base_y-40, "Willpower:     "+str(willpower))
    my_canvas.drawString(base_x, base_y-55, "XP Total:        "+str(xp_total))    
    determine_energy()
    my_canvas.drawString(base_x+200, base_y-55, "Energy Type:  "+str(energy_type))        
    my_canvas.drawString(base_x+400, base_y-55, "Energy Pool: "+str(energy_pool))       

def trade_specialization(name,x,y):
    if name == "Trade":
        my_canvas.drawString(x, y, str(name)+": "+str(pc_skills.get("trade_specialty")))
    else:
        my_canvas.drawString(x, y, str(name)+": ")

def skills_rank_assessment(name,ability,x,y):
    skill_rank = pc_skills.get(ability)
    dots = 0
    skills_x = x+100
    skills_y = y+3

    trade_specialization(name,x,y)
    while dots <= 3:
        if skill_rank >= 1:
            my_canvas.circle(skills_x, skills_y, 5, fill=1)
        else:
            my_canvas.circle(skills_x, skills_y, 5, fill=0)
        dots += 1
        skill_rank -= 1
        skills_x = skills_x+15

def skills_block(my_canvas,base_x,base_y):
    x = base_x
    y = base_y-105
    my_canvas.drawString(base_x+60, base_y-90, "Skills")
    for name in skills_list:
        skill_abbr = skills_dict.get(name)
        skills_rank_assessment(name,skill_abbr,base_x,y)
        y = y-15

def powers_rank_assessment(ability,x,y):
    power_rank = pc_trees.get(ability)
    dots = 0
    powers_x = x+250
    powers_y = y+3

    if faction == "Vampire":
        while dots <= 4:
            if power_rank >= 1:
                my_canvas.circle(powers_x, powers_y, 5, fill=1)
            else:
                my_canvas.circle(powers_x, powers_y, 5, fill=0)
            dots += 1
            power_rank -= 1
            powers_x = powers_x+15
    else:
        while dots <= 3:
            if power_rank >= 1:
                my_canvas.circle(powers_x, powers_y, 5, fill=1)
            else:
                my_canvas.circle(powers_x, powers_y, 5, fill=0)
            dots += 1
            power_rank -= 1
            powers_x = powers_x+15

def awareness_rank_assessment(x,y):
    dots = 0
    awareness_x = x
    awareness_y = y
    awareness_temp = awareness

    while dots <= 3:
        if awareness_temp >= 1:
            my_canvas.circle(awareness_x, awareness_y, 5, fill=1)
        else:
            my_canvas.circle(awareness_x, awareness_y, 5, fill=0)
        dots += 1
        awareness_temp -= 1
        awareness_x = awareness_x+15

def font_rank_assessment(x,y):
    dots = 0
    font_x = x
    font_y = y
    font_temp = font

    while dots <= 4:
        if font_temp >= 1:
            my_canvas.circle(font_x, font_y, 5, fill=1)
        else:
            my_canvas.circle(font_x, font_y, 5, fill=0)
        dots += 1
        font_temp -= 1
        font_x = font_x+15

def power_block(my_canvas,x,y):
    power_x = x
    power_y = y-160
    
    if faction == "Human":
        pass
    elif faction == "Vampire":
        has_innate_mortis = 0
        has_mortis = 0
        paths = []
        innates = []

        my_canvas.drawString(power_x+200, power_y+72, "Vampire Traits")
        my_canvas.drawString(power_x+170, power_y+57, "Generation: "+str(generation))
        my_canvas.drawString(power_x+170, power_y+42, "Max Vitae per Second: "+str(vps))
        my_canvas.drawString(power_x+170, power_y+27, "Road of "+road+" : "+str(road_rank))
        #my_canvas.drawString(power_x+200, power_y+12, "Road Aura (7+):")
        #my_canvas.drawString(power_x+170, power_y-3, factions[faction]["Roads"][road])
        my_canvas.line(base_x+160, base_y-140, base_x+320, base_y-140)
        my_canvas.drawString(power_x+190, power_y+2, "Innate Disciplines")
        power_y = power_y-15
        for p in factions[faction]["Clans"][subfaction]["Innate Disciplines"]:
            if "Valeren" in p:
                my_canvas.drawString(power_x+170, power_y, p)
                power_y = power_y-15
                powers_rank_assessment(p,power_x,power_y)
                innates.append(p) 
            elif "Mortis" in p:
                has_innate_mortis = 1
                path = p.removeprefix("Mortis: ")
                paths.append(path)
            else:
                my_canvas.drawString(power_x+170, power_y, p)
                powers_rank_assessment(p,power_x,power_y)
                power_y = power_y-15
                innates.append(p) 
        if has_innate_mortis == 1:
            power_y = power_y-10
            my_canvas.drawString(power_x+220, power_y, "Mortis")
            print(paths)
            for p in paths:
                power_y = power_y-15
                my_canvas.drawString(power_x+170, power_y, p)
                power_y = power_y-15
                powers_rank_assessment("Mortis: "+p,power_x,power_y)
        
        power_x = x+330
        power_y = y-90
        my_canvas.drawString(power_x+85, power_y, "Disciplines")
        power_y = power_y-15
        for p in factions[faction]["Disciplines"]:
            if "Mortis" in p and has_innate_mortis == 1:
                pass
            elif "Mortis" in p:
                has_mortis = 1
                path = p.removeprefix("Mortis: ")
                paths.append(path)
            elif p in innates:
                pass
            else:
                my_canvas.drawString(power_x, power_y, p)
                powers_rank_assessment(p,power_x-80,power_y)
                power_y = power_y-15
        if has_mortis == 1:
            power_y = power_y-10
            my_canvas.drawString(power_x+90, power_y, "Mortis")
            print(paths)
            for p in paths:
                power_y = power_y-15
                my_canvas.drawString(power_x, power_y, p)
                powers_rank_assessment("Mortis: "+p,power_x-80,power_y)    
        my_canvas.line(base_x+320, base_y-395, base_x+570, base_y-395)
        my_canvas.line(base_x+320, base_y-310, base_x+320, base_y-395)


  
    elif faction == "Mage":
        my_canvas.drawString(power_x+210, power_y+72, "Magic Skills")
        my_canvas.drawString(power_x+170, power_y+57, "Awareness: ")
        awareness_rank_assessment(power_x+250,power_y+60)
        my_canvas.drawString(power_x+170, power_y+42, "Font: ")
        font_rank_assessment(power_x+250,power_y+45)
        my_canvas.line(base_x+160, base_y-130, base_x+320, base_y-130)
        my_canvas.drawString(power_x+190, power_y+15, "Foundation & Pillars")
        my_canvas.drawString(power_x+170, power_y, factions[faction][subfaction]["Foundation"])
        powers_rank_assessment(factions[faction][subfaction]["Foundation"],power_x,power_y)
        power_y = power_y-30
        for p in factions[faction][subfaction]["Pillars"]:
            my_canvas.drawString(power_x+170, power_y, p)
            powers_rank_assessment(p,power_x,power_y)
            my_canvas.drawString(power_x+190, power_y-15, "Foci :")
            my_canvas.line(power_x+190, power_y-17, power_x+315, power_y-17)
            power_y = power_y-30
    elif faction == "Fae":
        pass
    else:
        my_canvas.drawString(base_x+170, base_y-90, "Invalid Faction.  Get it together "+player_name)


def rotes_block(my_canvas,x,y):
    rotes_x = x+330
    rotes_y = y-90
    rotes = 10

    my_canvas.drawString(rotes_x+85, rotes_y, "Rotes")
    while rotes > 0:
        my_canvas.line(rotes_x, rotes_y-20, rotes_x+230, rotes_y-20)
        rotes = rotes-1
        rotes_y = rotes_y-20

    my_canvas.line(base_x+320, base_y-310, base_x+570, base_y-310)

if __name__ == '__main__':
    my_canvas = canvas.Canvas("sample_sheet.pdf",pagesize=letter)
    borders(my_canvas,base_x,base_y)
    header_block(my_canvas,base_x,base_y)
    skills_block(my_canvas,base_x,base_y)
    power_block(my_canvas,base_x,base_y)
    if faction == "Mage":
        rotes_block(my_canvas,base_x,base_y)
    my_canvas.save()
