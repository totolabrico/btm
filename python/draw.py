import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from cmd import*

############################################
#Oled Display Raspberry Pi pin configuration:
RST = None
DC = 17
SPI_PORT = 0
SPI_DEVICE = 0
disp = Adafruit_SSD1306.SSD1306_128_64(rst=RST)
disp.begin()
disp.clear()
disp.display()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
font = ImageFont.load_default()
draw = ImageDraw.Draw(image)
###########################################
color=[0,255]
X_inc=[width/2]
Y_inc=[10,11,13]
X=[0,10,20,70]
Y=[0,12,19,35,45]
rect_track_size=6
rect_note_size=5
padding=2
setting_height=height/6
symbol_size=4

def draw_begin():
    global draw,image,width,height
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

def draw_end():
    disp.image(image)
    disp.display()

def draw_title(title):
    draw.rectangle((0,0,width,setting_height), outline=255, fill=255)
    draw.text((X[1],0),title,font=font, fill=0)

def draw_list(List,Tools):

    w=Tools["grid"][0]
    h=Tools["grid"][1]
    o=Tools["origin"]
    x=0
    y=0
    
    i=o*w
    while i<len(List):
        if y<h:
            xdraw=X[1]+x*(width/w)
            ydraw=Y[2]+y*(height*2/3)/h
            txt=set_txt_size(List[i],18)
            draw.text((xdraw,ydraw),txt,font=font, fill=255)
            draw_text_pointer(Tools,x,y,xdraw-X[1],ydraw)
            x+=1
            if x==w:
                x=0
                y+=1
        i+=1

    
def draw_text_pointer(Tools,X,Y,Xdraw,Ydraw):
    if Tools["pointer"][0]==X and Tools["pointer"][1]-Tools["origin"]==Y:
        draw.text((Xdraw,Ydraw),">",font=font, fill=255)

        
def draw_tracks(List,Tools):

    w=Tools["grid"][0]
    h=Tools["grid"][1]
    o=Tools["origin"]
    x=0
    y=0
    
    i=o*w
    while i<len(List):
        if y<h:
            xdraw=X[0]+x*(width/w)
            ydraw=Y[2]+y*(height*2/3)/h
            #draw.text((xdraw,ydraw),"o",font=font, fill=255)
            draw.rectangle((xdraw,ydraw,xdraw+rect_track_size,ydraw+rect_track_size), outline=255, fill=0)
            draw_track_pointer(Tools,x,y,xdraw,ydraw)

            x+=1
            if x==w:
                x=0
                y+=1
        i+=1

def draw_track_pointer(Tools,X,Y,Xdraw,Ydraw):
    if Tools["pointer"][0]==X and Tools["pointer"][1]-Tools["origin"]==Y:
        y=Ydraw+rect_track_size+2
        draw.rectangle((Xdraw,y,Xdraw+rect_track_size,y+2), outline=255, fill=0)

