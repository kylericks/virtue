# Imports
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def header_block(my_canvas):
    my_canvas.drawString(20, 750, "PC Name: ")
    my_canvas.drawString(220, 750, "Faction: ")    
    my_canvas.drawString(420, 750, "Health: ")    
    my_canvas.drawString(20, 735, "Player Name: ")
    my_canvas.drawString(220, 735, "Sub-Faction: ")
    my_canvas.drawString(420, 735, "Willpower: ")
    my_canvas.drawString(20, 720, "XP Total: ")    
    my_canvas.drawString(220, 720, "Energy Type: ")        
    my_canvas.drawString(420, 720, "Energy Pool: ")       
    my_canvas.line(20, 705, 580, 705)

def power_block(my_canvas):
    my_canvas.drawString(20, 690, "Pillar: Modus")
    my_canvas.circle(150, 690, 5, fill=1)
    my_canvas.circle(165, 690, 5)
    my_canvas.circle(180, 690, 5)
    my_canvas.circle(195, 690, 5)

if __name__ == '__main__':
    my_canvas = canvas.Canvas("sample_sheet.pdf",pagesize=letter)
    my_canvas.setLineWidth(.3)
    my_canvas.setFont('Helvetica', 12)
    header_block(my_canvas)
    power_block(my_canvas)
    my_canvas.save()
