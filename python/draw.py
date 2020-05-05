import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
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
Y_inc=[10,15]
X=[0,10,20,70]
Y=[0,20,35,45]


def draw_begin():
    global draw,image,width,height
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

def draw_end():
    disp.image(image)
    disp.display()
    

def draw_title(Title,x,y):
    draw.rectangle((x,y,width,y+Y_inc[0]), outline=255, fill=255)
    draw.text((x+2,y),Title,font=font, fill=0)


######################## a revoir !

def draw_settings(partition):
    global width,X,Y,Y_inc
    
    draw_begin()
    x=X[0]
    y=Y[0]    
    x_inc=(width-x)/Grid[0]
    draw_title(partition.name,x,y)
    y+=Y_inc[1]
    i=partition.menu[1]*grid_setting[0]*grid_setting[1]
    line=0
    while i<len(partition.setting):
        pointed=False
        if i==partition.pointer[0]:
            pointed=True
        if line<Grid[1]:
            draw_setting(partition.setting[i],x,y+line*Y_inc[0],pointed,x_inc)
            x+=x_inc
            if (i+1)%Grid[0]==0:
                x=X[0]
                line+=1
        i+=1

    draw_end()
    
def draw_setting(setting,x,y,pointed,width_setting):
    name=setting[0]
    value=str(float(setting[1]))
    if pointed==True:
        draw.rectangle((x,y,width_setting,y+Y_inc[0]), outline=255, fill=0)
    draw.text((x+2,y),name+":"+value,font=font, fill=255)

def draw_children(partition):
    global width,X,Y,Y_inc
    draw_begin()
    x=X[0]
    y=Y[0]    
    x_inc=(width-x)/Grid[0]
    draw_title(partition.child_name,x,y)
    y+=Y_inc[1]
    i=0
    line=0

    while i<Max:
        pointed=False
        if i==partition.pointer[1]:
            pointed=True
        exist=False
        for element in List_children:
            if element.id==i+1:
                exist=True
        if line<Grid[1]:
            draw_child(partition.children,x,y+line*Y_inc[0],exist,pointed,x_inc)
            x+=x_inc
            if (i+1)%Grid[0]==0:
                x=X[0]
                line+=1
        i+=1

    draw_end()
    
def draw_child(list_children,x,y,exist,pointed,width_setting):
    if pointed==True:
        draw.rectangle((x,y-1,x+width_setting-2,y-3), outline=255, fill=255)
    color=0
    if exist==True:
        color=255
    draw.rectangle((x,y,x+width_setting-2,y+Y_inc[0]), outline=255, fill=color)

