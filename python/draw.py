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

def reverse_color():
    stock=int(color[0])
    color[0]=color[1]
    color[1]=stock

def draw_begin():
    global draw,image,width,height
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=color[0], fill=color[0])

def draw_end():
    disp.image(image)
    disp.display()

def draw_title(title):
    if (len(title)>20):
        title=title[-20:]
    draw.rectangle((0,0,width,setting_height), outline=color[1], fill=color[1])
    draw.text((X[1],0),title,font=font, fill=color[0])

def draw_footer(word):
   # draw.rectangle((0,height-setting_height,width,setting_height), outline=255, fill=255)
    draw.text((X[1],height-setting_height),word,font=font, fill=color[0])

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
            draw.text((xdraw,ydraw),txt,font=font, fill=color[1])
            draw_text_pointer(Tools,x,y,xdraw-X[1],ydraw)
            x+=1
            if x==w:
                x=0
                y+=1
        i+=1
    
def draw_text_pointer(Tools,X,Y,Xdraw,Ydraw):
    if Tools["pointer"][0]==X and Tools["pointer"][1]-Tools["origin"]==Y:
        draw.text((Xdraw,Ydraw),">",font=font, fill=color[1])

def draw_tracks(Tracks,Tools,Selection):
    w=Tools["grid"][0]
    h=Tools["grid"][1]
    o=Tools["origin"]
    x=0
    y=0
    
    i=o*w
    while i<len(Tracks):
        if y<h:
            xdraw=X[0]+x*(width/w)
            ydraw=Y[2]+y*(height*2/3)/h
            color=0
            if Tracks[i][1][1][0][1]!="empty":
                color=255
            #print(Tracks[i][3][1][2])
            if i in Selection:
                draw.rectangle((xdraw,ydraw-2,xdraw+rect_track_size,ydraw-1), outline=255, fill=0)
            draw.rectangle((xdraw,ydraw,xdraw+rect_track_size,ydraw+rect_track_size), outline=255, fill=color)
            if Tracks[i][3][1][3][1]==True:
                draw.text((xdraw+1,ydraw-3),"s",font=font, fill=0)
            elif Tracks[i][3][1][2][1]==True:
                draw.text((xdraw+1,ydraw-3),"m",font=font, fill=0)

            draw_grid_pointer(Tools,x,y,xdraw,ydraw,rect_track_size)

            x+=1
            if x==w:
                x=0
                y+=1
        i+=1

def draw_notes(List,Tools,Selection):
    w=Tools["grid"][0]
    h=Tools["grid"][1]
    t=Tools["temps"]
    o=Tools["origin"]
    be=Tools["beg_end"]
    x=0
    y=0
    
    i=o*w
    while i<len(List):
        if y<h:
            xdraw=X[1]/2+x*(rect_note_size+padding)+int((i%w)/t)*padding
            ydraw=Y[2]+y*(height*2/3)/h
            color=0
            if List[i][1]!=0:
                color=255
            draw_notes_begin_end(i,be[0],be[1],xdraw,ydraw)
            if i in Selection:
                draw.rectangle((xdraw,ydraw-2,xdraw+rect_note_size,ydraw-1), outline=255, fill=0)
            draw.rectangle((xdraw,ydraw,xdraw+rect_note_size,ydraw+rect_note_size), outline=255, fill=color)
            draw_grid_pointer(Tools,x,y,xdraw,ydraw,rect_note_size)
            x+=1
            if x==w:
                x=0
                y+=1
        i+=1

def draw_grid_pointer(Tools,X,Y,Xdraw,Ydraw,Size):
    if Tools["pointer"][0]==X and Tools["pointer"][1]-Tools["origin"]==Y:
        y=Ydraw+Size+2
        draw.rectangle((Xdraw,y,Xdraw+Size,y+2), outline=color[1], fill=color[0])

def draw_notes_begin_end(Id,Begin,End,X,Y):
    if Id==Begin-1:
        draw.rectangle((X,Y,X-2,Y-2), outline=color[1], fill=color[0])
    if Id==End-1:
        Xdraw=X+rect_note_size
        Ydraw=Y+rect_note_size
        draw.rectangle((Xdraw,Ydraw,Xdraw+2,Ydraw+2), outline=color[1], fill=color[0])
