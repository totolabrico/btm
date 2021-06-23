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
#text_calc = Image.new('1', (width, height))
font = ImageFont.load_default()
image = Image.open('/home/pi/btm/logo.jpg').convert('1')
draw = ImageDraw.Draw(image)

draw.text((20,38),"btm_4",font=font, fill=255)
disp.image(image)    
disp.display()
