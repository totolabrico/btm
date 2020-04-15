import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
#import subprocess
#import time
#import threading

############################################
#Oled Display Raspberry Pi pin configuration:
RST = None
DC = 23
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
#draw = ImageDraw.Draw(image)
###########################################

color=[0,255]
line_height=[10,13]
X=[0,10,55]
Y=[7,20,35]


class Draw_menu:
    
    def __init__(self,Menu):
        self.menu=Menu
        self.pointer=0
        self.pointer_line=0
        self.origin_line=0
        self.max_line=4
        self.display_list=[]
        self.set_display_list()


    def set_display_list(self):
        
        copy_list=self.menu.List
        self.set_max_line()
        self.display_list=[]
        i=self.origin_line 
        while i<self.origin_line+self.max_line:
            self.display_list.append(copy_list[i])
            i+=1
        
    def set_pointer(self):# set pointer & origin

        if self.menu.pointer==0: # if 'min'
            self.origin_line=0
            self.pointer_line=0
            
        elif self.menu.pointer==len(self.menu.List)-1: # if 'max'
            self.pointer_line=self.max_line-1
            self.origin_line=len(self.menu.List)-self.max_line
            
        elif self.menu.pointer>self.pointer:# if '+'
            if self.pointer_line<self.max_line-1:
                self.pointer_line+=1
            elif self.pointer_line==self.max_line-1:
                self.origin_line+=1
                
        elif self.menu.pointer<self.pointer:# if '-'
            if self.pointer_line>0:
                self.pointer_line-=1
            elif self.pointer_line==0:
                self.origin_line-=1
        
        self.pointer=self.menu.pointer
                
    def set_max_line(self):
        self.max_line=4
        if len(self.menu.List)<self.max_line:
            self.max_line=len(self.menu.List)

    def draw_begin(self):
        global draw,image,width,height
        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0,width,height), outline=0, fill=0)

    def draw_end(self):
        disp.image(image)
        disp.display()
        
    def draw_title(self):
        draw.text((X[2],Y[0]),self.menu.name,font=font, fill=255)

    def draw_list(self):
        y=Y[1]
        
        for element in self.display_list:
            if type(element)==list:
                to= element[0]+":"+str(element[1])
            else:
                to=str(element)
            draw.text((X[1],y),to,font=font, fill=255)
            y+=line_height[0]
   
    def draw_pointer(self):
        y=self.pointer_line*line_height[0]+Y[1]+3
        draw.rectangle((X[0],y,X[0]+3,y+3), outline=0, fill=255)


    def draw_setting(self):
        to=""
        for element in self.menu.track.notes:
            if element.setting[0][1]==self.menu.pas:
                to=element.setting[self.menu.id_setting]
                draw.text((X[2],Y[0]),to[0]+":"+str(to[1]),font=font, fill=255)


    def draw_sequence(self):

        draw.text((X[1],Y[0]),"pas:"+str(self.menu.pas),font=font, fill=color[1])

        color_pas=color[0]
        temps=self.menu.navigator.partition.temps
        rect_width=round((width-50)/self.menu.pas_per_line)
        print("pas_per_line",self.menu.pas_per_line)
        rect_height=5
        x=X[1]
        y=Y[2]
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
        
        """
        y+=inc_line
        to=0
        for element in track.notes:
            i=0
            while i<len(element.setting):
                if element.setting[i][0]==menu.setting:
                    to=element.setting[i][1]
                i+=1
        draw.text((x1,y),menu.setting+":"+str(to),font=font, fill=self.color[1])
        """
        
        
        
    '''    
    def draw_info(self):
        tracks=self.machine.partition.tracks
        pointer_track=self.navigator.pointer_track
        to=tracks[pointer_track].sample_length
    '''
