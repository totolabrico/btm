from led_rgb import*
import threading
import time

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
line_height=[10,13]
X=[0,10,20,70]
Y=[7,20,35,45]


class Draw_oled:
    
    def __init__(self,Menu):
        self.menu=Menu
        
    def set_menu(self,Menu):
        self.menu=Menu
         
    def run_draw(self):
        
        while True:
            self.draw_begin()

                
            self.draw_title(self.menu.title)

            if self.menu.name=="notes":
                self.draw_setting()
                self.draw_sequence()
            elif self.menu.name=="save":
                self.draw_save()
            else:
                self.draw_list()
                self.draw_pointer()
        
            self.draw_end()
            time.sleep(0.1)


    def draw_begin(self):
        global draw,image,width,height
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)

    def draw_end(self):
        disp.image(image)
        disp.display()
        
    def draw_title(self,Title):
        y=Y[0]
        draw.rectangle((X[1],y,width,y+10), outline=0, fill=255)
        draw.text((X[2],Y[0]),Title,font=font, fill=0)

    def draw_list(self):
        y=Y[1]
        
        for element in self.menu.draw_menu.display_list:
            if type(element)==list:
                to= element[0]+":"+str(element[1])
            else:
                to=str(element)
            draw.text((X[1],y),to,font=font, fill=255)
            y+=line_height[0]
   
    def draw_pointer(self):
        y=self.menu.draw_menu.pointer_line*line_height[0]+Y[1]+3
        draw.rectangle((X[0],y,X[0]+3,y+3), outline=0, fill=255)


    def draw_setting(self):
        nb_pas=self.menu.track.mesure*self.menu.partition.temps
        draw.text((X[1],Y[3]),"pas:"+str(self.menu.pas+1)+"/"+str(nb_pas),font=font, fill=color[1])
        to=""
        for element in self.menu.track.notes:
            if element.setting[0][1]==self.menu.pas:
                to=element.setting[self.menu.id_setting]
                draw.text((X[3],Y[3]),to[0]+":"+str(to[1]),font=font, fill=255)


    def draw_sequence(self):

        color_pas=color[0]
        temps=self.menu.partition.temps
        rect_width=round((width-50)/self.menu.pas_per_line)
        #print("pas_per_line",self.menu.pas_per_line)
        rect_height=5
        x=X[1]
        y=Y[1]+5
        i=0

        while i<self.menu.nb_pas:
            color_pas=color[0]
            for element in self.menu.track.notes:
                if element.setting[0][1]==i:
                    color_pas=color[1]
            draw.rectangle((x,y,x+rect_width,y+rect_height), outline=color[1], fill=color_pas)
            if i==self.menu.pas:
                draw.rectangle((x,y-1,x+rect_width,y-2), outline=color[1], fill=color[1])
            x+=rect_width+2
            if (i+1)%temps==0 and i!=0:
                x+=2
            
            if (i+1) %(self.menu.pas_per_line)==0:
                y+=rect_height+5
                x=X[1]
            i+=1

        
    def draw_save(self):
        name=self.menu.save_name+self.menu.letter()
        draw.text((X[1],Y[2]),"name: "+name,font=font, fill=255)
