# Imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import csv
import os

# Variables for Testing
pc_name = " "
player_name = " "
xp_total = str()
faction = "Mage"
subfaction = "Valdaerman"
energy_type = "Quintessence"
health = str()
willpower = str()
energy_pool = str()
awareness = 1
font = 0
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
    "Blot":1,
    "Fara":0,
    "Forlog":0,
    "Galdar":0,
    "Hjaldar":0
}

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

def borders(my_canvas,base_x,base_y):
    my_canvas.line(base_x, base_y-70, base_x+560, base_y-70)
    my_canvas.line(base_x, base_y-310, base_x+560, base_y-310)
    my_canvas.line(base_x+160, base_y-70, base_x+160, base_y-310)
    my_canvas.line(base_x+320, base_y-70, base_x+320, base_y-310)
    my_canvas.line(base_x+160, base_y-130, base_x+320, base_y-130)



def header_block(my_canvas,base_x,base_y):
    my_canvas.drawString(base_x+150, base_y, "Darkwood Nights Player Character Sheet")
    my_canvas.drawString(base_x, base_y-25, "PC Name:      "+pc_name)
    my_canvas.drawString(base_x+200, base_y-25, "Faction:          "+faction)    
    my_canvas.drawString(base_x+400, base_y-25, "Health:          "+str(health))    
    my_canvas.drawString(base_x, base_y-40, "Player Name: "+player_name)
    my_canvas.drawString(base_x+200, base_y-40, "Sub-Faction:   "+subfaction)
    my_canvas.drawString(base_x+400, base_y-40, "Willpower:     "+str(willpower))
    my_canvas.drawString(base_x, base_y-55, "XP Total:        "+str(xp_total))    
    my_canvas.drawString(base_x+200, base_y-55, "Energy Type:  "+energy_type)        
    my_canvas.drawString(base_x+400, base_y-55, "Energy Pool: "+str(energy_pool))       

def trade_specialization(name,x,y):
    if name == "Trade":
        my_canvas.drawString(x, y, str(name)+": "+pc_skills.get("trade_specialty"))
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
    
    foundations = ["Al-Ikhlas","Deity","Modus","Spontaneity","Sin","Blot","Sensitivity"]

    if faction == "Human":
        pass
    elif faction == "Vampire":
        pass
    elif faction == "Mage":
        trees_doc = open(os.path.join(os.path.dirname(__file__),'data','mage_trees.data'),"r")
        trees_dict = csv.DictReader(trees_doc)
        trees_list = []
        my_canvas.drawString(power_x+210, power_y+72, "Magic Skills")
        my_canvas.drawString(power_x+170, power_y+57, "Awareness: ")
        awareness_rank_assessment(power_x+250,power_y+60)
        my_canvas.drawString(power_x+170, power_y+42, "Font: ")
        font_rank_assessment(power_x+250,power_y+45)
        my_canvas.drawString(power_x+190, power_y+15, "Foundation & Pillars")
        for n in trees_dict:
            if n['Subfaction'] == subfaction:
                trees_list.append(n['TreeName'])
        print(trees_list)
        for n in trees_list:
            if n in foundations:
                my_canvas.drawString(power_x+170, power_y, n)
                powers_rank_assessment(n,power_x,power_y)
            else:
                my_canvas.drawString(power_x+170, power_y, n)
                powers_rank_assessment(n,power_x,power_y)
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


if __name__ == '__main__':
    my_canvas = canvas.Canvas("sample_sheet.pdf",pagesize=letter)
    borders(my_canvas,base_x,base_y)
    header_block(my_canvas,base_x,base_y)
    skills_block(my_canvas,base_x,base_y)
    power_block(my_canvas,base_x,base_y)
    if faction == "Mage":
        rotes_block(my_canvas,base_x,base_y)
    my_canvas.save()
