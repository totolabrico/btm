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

def draw_settings(List,Grid):
    x=0
    y=setting_height+3
    min=0
    max=Grid["x"][0]*Grid["x"][1]*Grid["y"]
    if Grid["pointer"]>=max:
        min=max
        max=len(List)
    while min<max:
        if Grid["pointer"]==min:
            draw.rectangle((x,y+3,x+5,y+3+5), outline=0, fill=255)
        draw.text((x+8,y),List[min][0]+":"+setting_to_string(List[min][1]),font=font, fill=255)
        min+=1
        x+=width/2
        if min%Grid["x"][1]==0:
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
