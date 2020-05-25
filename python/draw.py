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
padding=2
setting_height=height/6

def draw_begin():
    global draw,image,width,height
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0,width,height), outline=0, fill=0)

def draw_end():
    disp.image(image)
    disp.display()

def draw_title(Title):
    draw.rectangle((0,0,width,setting_height), outline=255, fill=255)
    draw.text((2,0),Title,font=font, fill=0)

def set_draw(Type,List,Pointer,Selecter,Grid,Height):

    max_elements=Grid["x"][0]*Grid["x"][1]*Height
    min=int(Pointer/max_elements)*max_elements
    max=min+max_elements
    if max>Grid["max"]:
        max=Grid["max"]
    if Type=="setting":
        draw_setting(List,Pointer,Selecter,Grid,Height,min,max)
    elif Type=="children":
        draw_children(List,Pointer,Selecter,Grid,Height,min,max)

def draw_setting(List,Pointer,Selecter,Grid,Height,Min,Max):

    x=0+padding
    y=setting_height+6
    if Height==2:
        y=height/2+7

    while Min<Max:
        x_inc=0
        color=255

        for element in Selecter:
            if element==Min:
                draw.rectangle((x+x_inc-2,y,x+width/2-5,y+Y_inc[0]+2), outline=0, fill=color)
                color=0

        if Pointer==Min:
            draw.rectangle((x,y+3,x+5,y+3+5), outline=255-color, fill=color)
            x_inc=8

        draw.text((x+x_inc,y),List[Min][0]+":"+setting_to_string(List[Min][1]),font=font, fill=color)
        Min+=1
        x+=width/2
        if Min%(Grid["x"][0]*Grid["x"][1])==0:
            x=0+padding
            y+=setting_height

def draw_children(List,Pointer,Grid,Height,Min,Max):

    x=0
    y=setting_height+4

    while Min<Max:
        if Pointer==Min:
            draw.rectangle((x,y+1,x+6,y+3), outline=0, fill=255)
        color=0
        print("draw_children",List[Min])
        draw.rectangle((x,y+5,x+6,y+5+6), outline=0, fill=255)
        Min+=1
        x+=width/(Grid["x"][0]*Grid["x"][1])
        if Min%(Grid["x"][0]*Grid["x"][1])==0:
            x=0
            y+=setting_height

def setting_to_string(setting):
    if type(setting)==float or type(setting)==int:
        return str(setting)
    elif setting==True:
        return "on"
    elif setting==False:
        return "off"
    else:
        return setting
