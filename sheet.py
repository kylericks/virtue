# Imports
from re import X
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import ParagraphStyle
import json
import csv
import os
import textwrap

# Variables for Testing
pc_name = " "
player_name = " "
xp_total = str()
faction = "Human"
subfaction = "Commoner"
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
mists = int()
weaving = int()
court = "Winter"
oath_pool = int()
max_oaths = int()
oath_power = str()
enigmas = 0
ken = 1
gram = 4
gramarye_specialty = "Oaths"
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
    "Dawn":1,
    "Day":0,
    "Dusk":2,
    "Night":3
}
'''
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
    global mists
    global weaving
    global ken
    global gram
    global enigmas

    if faction == "Human":
        if subfaction == "Ghoul":
            energy_type = "Vitae"
            energy_pool = "10"
        elif subfaction == "Gifted Kinfolk":
            pass
        else:
            energy_type = "None"
            energy_pool = "None"
    elif faction == "Vampire":
        energy_type = "Vitae"
        vitae_pool()
    elif faction == "Mage":
        energy_type = "Quintessence"
        energy_pool = 10+(font*2)
    elif faction == "Fae":
        mists = factions[faction]["Origin"][subfaction]["Mists"]
        weaving = factions[faction]["Origin"][subfaction]["Weaving"]
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
    if faction == "Fae":
        my_canvas.drawString(base_x, base_y-55, "XP Total:        "+str(xp_total))    
        determine_energy()
        my_canvas.drawString(base_x+200, base_y-55, "Mists:              "+str(mists))        
        my_canvas.drawString(base_x+400, base_y-55, "Weaving:   "+str(weaving))  
    else:
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

def faction_skill_assessment(skill,x,y):
    dots = 0
    skill_x = x
    skill_y = y
    skill_temp = skill

    while dots <= 3:
        if skill_temp >= 1:
            my_canvas.circle(skill_x, skill_y, 5, fill=1)
        else:
            my_canvas.circle(skill_x, skill_y, 5, fill=0)
        dots += 1
        skill_temp -= 1
        skill_x = skill_x+15

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

def vampire_conditionals(b_x,b_y):
    x = b_x
    y = b_y-160

    box_wrap = textwrap.TextWrapper(width = 50)
    clan_flaw = box_wrap.wrap(factions[faction]["Clans"][subfaction]["Clan Flaw"])
    road_aura = box_wrap.wrap(factions[faction]["Roads"][road])

    if subfaction == "Cappadocian":
        flaw_y = y+170
    else:
        flaw_y = y+210
    my_canvas.drawString(base_x+100, flaw_y, "Clan Weakness")
    flaw_y = flaw_y-20
    for line in clan_flaw:
        my_canvas.drawString(base_x, flaw_y, line)
        flaw_y = flaw_y-15
    flaw_y = flaw_y-20
    my_canvas.drawString(base_x+100, flaw_y, "Road Aura (7+):")
    flaw_y = flaw_y-20
    for line in road_aura:
        my_canvas.drawString(base_x, flaw_y, line)
        flaw_y = flaw_y-15
    my_canvas.line(base_x, flaw_y, base_x+320, flaw_y)

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

def devotions_block(my_canvas,x,y):
    devotions = 13
    if subfaction == "Cappadocian":
        x = x+85
        y = y-10
        my_canvas.line(base_x+320, base_y-340, base_x+570, base_y-340)
    else:
        x = x+85
        y = y-30
        my_canvas.line(base_x+320, base_y-395, base_x+570, base_y-395)
        y = y-10
    my_canvas.drawString(x, y, "Devotions")
    while devotions > 0:
        my_canvas.line(x-85, y-20, x+160, y-20)
        devotions = devotions-1
        y = y-20
    my_canvas.line(x-95, y+290, x-95, y-50)

def fae_oaths(x,y):
    global max_oaths

    stone_oaths = 0

    if gramarye_specialty == "Oaths":
        if gram <= 0:
            if court == "Solstice":
                max_oaths = 1
            else:
                max_oaths = 2
        elif gram == 1:
            if court == "Solstice":
                max_oaths = 2
            else:
                max_oaths = 4
        elif gram == 2:
            stone_oaths = 1
            if court == "Solstice":
                max_oaths = 3
            else:
                max_oaths = 6
        elif gram == 3:
            stone_oaths = 3
            if court == "Solstice":
                max_oaths = 4
            else:
                max_oaths = 8
        elif gram == 4:
            stone_oaths = 4
            if court == "Solstice":
                max_oaths = 5
            else:
                max_oaths = 9       
    else:
        if gram <= 0:
            if court == "Solstice":
                max_oaths = 1
            else:
                max_oaths = 2
        elif gram == 1:
            if court == "Solstice":
                max_oaths = 2
            else:
                max_oaths = 4
        elif gram == 2:
            if court == "Solstice":
                max_oaths = 3
            else:
                max_oaths = 6
        elif gram == 3:
            stone_oaths = 1
            if court == "Solstice":
                max_oaths = 4
            else:
                max_oaths = 8
        elif gram == 4:
            stone_oaths = 2
            if court == "Solstice":
                max_oaths = 5
            else:
                max_oaths = 9

    my_canvas.drawString(x+60, y, "Oath Pool")
    y -= 27
    my_canvas.drawString(x, y, "Oaths:")
    my_canvas.drawString(x+110, y, "Max Oaths: "+str(max_oaths))
    y -= 15
    if gramarye_specialty == "Oaths": 
        if gram == 4:
            my_canvas.drawString(x, y, "Stone Oaths:")
            my_canvas.drawString(x+110, y, "Stone Oaths Pool: "+str(stone_oaths))
            y -= 15
            my_canvas.drawString(x, y, "Can be an Oath Steward (Iron)")
            y -= 15
            my_canvas.drawString(x, y, "Can be an Oath Steward for 1 Stone")
            y -= 15
        elif gram >= 2:
            my_canvas.drawString(x, y, "Stone Oaths:")
            my_canvas.drawString(x, y, "Stone Oaths Pool: "+str(stone_oaths))
            y -= 15
            my_canvas.drawString(x, y, "Can be an Oath Steward (Iron)")
            y -= 15
        elif gram == 1:
            my_canvas.drawString(x, y, "Can be an Oath Steward (Iron)")
            y -= 15
        else:
            pass
    else:
        pass
    my_canvas.line(x-10, y, x+240, y)

    

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
            for p in paths:
                power_y = power_y-15
                my_canvas.drawString(power_x, power_y, p)
                powers_rank_assessment("Mortis: "+p,power_x-80,power_y)    
        my_canvas.line(base_x+320, base_y-310, base_x+320, base_y-395)
        vampire_conditionals(power_x,power_y)
        devotions_x = power_x
        devotions_y = power_y
        devotions_block(my_canvas,devotions_x,devotions_y)
    elif faction == "Mage":
        my_canvas.drawString(power_x+210, power_y+72, "Magic Skills")
        my_canvas.drawString(power_x+170, power_y+57, "Awareness: ")
        faction_skill_assessment(awareness,power_x+250,power_y+60)
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
        rotes_block(my_canvas,base_x,base_y)
    elif faction == "Fae":
        traits_x = power_x+200
        traits_y = power_y+72
        mtraits = 5
        echoes = 6
        
        #traits block
        my_canvas.drawString(traits_x, traits_y, "Major Traits")
        while mtraits > 0:
            traits_y -= 15
            my_canvas.line(traits_x-30, traits_y, traits_x+110, traits_y)
            mtraits -= 1
        traits_y -= 15
        my_canvas.line(traits_x-40, traits_y, traits_x+120, traits_y)
        traits_y -= 20
        my_canvas.drawString(traits_x+10, traits_y, "Echoes")
        while echoes > 0:
            traits_y -= 15
            my_canvas.line(traits_x-30, traits_y, traits_x+110, traits_y)
            echoes -= 1
        
        #fae skills block
        fae_skills_x = base_x
        fae_skills_y = base_y-325

        my_canvas.drawString(fae_skills_x+60, fae_skills_y, "Fae Skills")
        fae_skills_y -= 15
        my_canvas.drawString(fae_skills_x, fae_skills_y, "Kenning:")
        faction_skill_assessment(ken,fae_skills_x+100, fae_skills_y)
        fae_skills_y -= 15
        my_canvas.drawString(fae_skills_x, fae_skills_y, "Enigmas:")
        faction_skill_assessment(enigmas,fae_skills_x+100, fae_skills_y)
        fae_skills_y -= 15
        my_canvas.drawString(fae_skills_x, fae_skills_y, "Gramarye: "+gramarye_specialty)
        fae_skills_y -= 15
        faction_skill_assessment(gram,fae_skills_x+100, fae_skills_y)
        fae_skills_y -= 15
        my_canvas.line(fae_skills_x, fae_skills_y, fae_skills_x+160, fae_skills_y)
        my_canvas.line(fae_skills_x+160, fae_skills_y+90, fae_skills_x+160, fae_skills_y)

        #fae dominions block
        dominions_x = power_x+390
        dominions_y = power_y+72

        my_canvas.drawString(dominions_x, dominions_y, "Dominions")
        dominions_y -= 15
        if court == "Solstice":
            pass
        else:
            dominions_y -= 15
            my_canvas.drawString(dominions_x+2, dominions_y, "Favored")
            dominions_y -= 15
            my_canvas.drawString(dominions_x-60, dominions_y, factions[faction]["Court"][court]["Favored Dominion"])
            powers_rank_assessment(factions[faction]["Court"][court]["Favored Dominion"],dominions_x-180, dominions_y)
            # assess
            dominions_y -= 15
        my_canvas.drawString(dominions_x+7, dominions_y, "Other")
        dominions_y -= 15
        for d in factions[faction]["Dominions"]:
            if d == factions[faction]["Court"][court]["Favored Dominion"]:
                pass
            else:
                my_canvas.drawString(dominions_x-60, dominions_y, d)
                powers_rank_assessment(d,dominions_x-180, dominions_y)
                dominions_y -= 15
        my_canvas.line(dominions_x-70, dominions_y, dominions_x+180, dominions_y)
        dominions_y -= 15

        #fae oath block
        oath_x = dominions_x-60
        oath_y = dominions_y

        fae_oaths(oath_x,oath_y)
    else:
        my_canvas.drawString(base_x+170, base_y-90, "Invalid Faction.  Get it together "+player_name)

if __name__ == '__main__':
    my_canvas = canvas.Canvas("sample_sheet.pdf",pagesize=letter)
    borders(my_canvas,base_x,base_y)
    header_block(my_canvas,base_x,base_y)
    skills_block(my_canvas,base_x,base_y)
    power_block(my_canvas,base_x,base_y)
    my_canvas.save()
