# Imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Variables for Testing
pc_name = "Peety PC"
player_name = "Realworld Ralph"
xp_total = 15
faction = "Mage"
subfaction = "Veneficti"
energy_type = "Quintessence"
health = 10
willpower = 3
energy_pool = 10
alch = 1
arch = 0
brwl = 0
doge = 0
esca = 0
frtn = 0
intm = 0
litr = 1
lock = 0
medi = 0
mele = 1
smth = 0
stel = 0
trde = 1
trade_specialty = "Mining"

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

def header_block(my_canvas):
    my_canvas.drawString(20, 750, "PC Name:      "+pc_name)
    my_canvas.drawString(220, 750, "Faction:          "+faction)    
    my_canvas.drawString(420, 750, "Health:          "+str(health))    
    my_canvas.drawString(20, 735, "Player Name: "+player_name)
    my_canvas.drawString(220, 735, "Sub-Faction:   "+subfaction)
    my_canvas.drawString(420, 735, "Willpower:     "+str(willpower))
    my_canvas.drawString(20, 720, "XP Total:        "+str(xp_total))    
    my_canvas.drawString(220, 720, "Energy Type:  "+energy_type)        
    my_canvas.drawString(420, 720, "Energy Pool: "+str(energy_pool))       
    my_canvas.line(20, 705, 580, 705)

def rank_assessment(name,ability,x_coord,y_coord):
    if ability == 4:
        my_canvas.drawString(int(x_coord), int(y_coord), str(name)+":")
        my_canvas.circle(int(x_coord)+130, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+145, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+160, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+175, int(y_coord), 5, fill=1)     
    elif ability == 3:
        my_canvas.drawString(int(x_coord), int(y_coord), str(name)+":")
        my_canvas.circle(int(x_coord)+130, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+145, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+160, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+175, int(y_coord), 5, fill=0)  
    elif ability == 2:
        my_canvas.drawString(int(x_coord), int(y_coord), str(name)+":")
        my_canvas.circle(int(x_coord)+130, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+145, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+160, int(y_coord), 5, fill=0)
        my_canvas.circle(int(x_coord)+175, int(y_coord), 5, fill=0)  
    elif ability == 1:
        my_canvas.drawString(int(x_coord), int(y_coord), str(name)+":")
        my_canvas.circle(int(x_coord)+80, int(y_coord), 5, fill=1)
        my_canvas.circle(int(x_coord)+95, int(y_coord), 5, fill=0)
        my_canvas.circle(int(x_coord)+110, int(y_coord), 5, fill=0)
        my_canvas.circle(int(x_coord)+125, int(y_coord), 5, fill=0)  
    elif ability == 0:
        my_canvas.drawString(int(x_coord), int(y_coord), str(name)+":")
        my_canvas.circle(int(x_coord)+130, int(y_coord), 5, fill=0)
        my_canvas.circle(int(x_coord)+145, int(y_coord), 5, fill=0)
        my_canvas.circle(int(x_coord)+160, int(y_coord), 5, fill=0)
        my_canvas.circle(int(x_coord)+175, int(y_coord), 5, fill=0)  
    else:
        my_canvas.drawString(int(x_coord), int(y_coord), "Invalid Value for "+ability)

def power_block(my_canvas):
    my_canvas.drawString(20, 690, "Tree Name: ")
    my_canvas.circle(150, 690, 5) # Add fill=1 to make filled circle
    my_canvas.circle(165, 690, 5)
    my_canvas.circle(180, 690, 5)
    my_canvas.circle(195, 690, 5)

def skills_block(my_canvas):
    x = 20
    y = 690
    for name in skills_list:
        rank = skills_dict.get(name)
        print(rank)
        rank_assessment(name,rank,x,y)
        y = y-15


if __name__ == '__main__':
    my_canvas = canvas.Canvas("sample_sheet.pdf",pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    header_block(my_canvas)
    skills_block(my_canvas)
    #power_block(my_canvas)
    my_canvas.save()
