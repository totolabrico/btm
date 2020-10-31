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
Y=[0,12,17,35,45]
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
    draw.text((2,0),title,font=font, fill=0)
