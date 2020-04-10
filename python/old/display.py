import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import time
import threading

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
draw = ImageDraw.Draw(image)
###########################################

inc_line=10 #ecart entre les lignes
inc_line2=13 #ecart entre les lignes
x0,x1,x2=0,10,55
y0=7 # marge en y
yPointer=y0
height_pointer=3
begin_display_list=0

class Display:

    def __init__(self,Navigator):
        self.navigator=Navigator
        self.color=[0,255]
        self.nb_max_line=4
        self.pointer_line=0
        self.origin_line=0
        self.last_pointer=0
        self.last_menu=self.navigator.menu.name
        self.display = threading.Thread(target=self.choose_draw, args=())
        self.display.start()

    def reset_draw(self):
        self.pointer_line=0
        self.nb_line=4
        self.last_pointer=0
        self.origin_line=0
        if self.navigator.menu!="notes":
            self.set_display_max()
        
    def set_display_max(self):
        menu=self.navigator.menu
        self.nb_line=4
        if len(menu.List)<self.nb_line:
            self.nb_line=len(menu.List)
            
            
    def choose_draw(self):
        
        while True:
            draw = ImageDraw.Draw(image)
            draw.rectangle((0,0,width,height), outline=self.color[0], fill=self.color[0])

            menu=self.navigator.menu.name
            
            if menu!=self.last_menu:
                self.reset_draw()
            self.last_menu=menu
            
            if menu =="notes":
                self.draw_sequence()
            else:
                self.set_draw_list(self.navigator.menu.name)
                self.draw_list()

            disp.image(image)
            disp.display()
            time.sleep(0.1)


        

    def draw_list(self,name):# choix de la fonction d'affichage
              
        global y0,display_max,begin_display_list
        
        #menu=self.navigator.menu
        y=y0
        draw.text((x2,y),name,font=font, fill=self.color[1])
        yPointer=y+self.pointer_line*inc_line+inc_line2+3
        #yPointer=y+inc_line2+3
        draw.rectangle((x0,yPointer,5,yPointer+height_pointer), outline=self.color[0], fill=self.color[1])#dessine le pointer
        y+=inc_line2

        i=0
        while i<self.nb_max_line:

            value=self.origin_line+i
            if value>=len(menu.List):
                value-=len(menu.List)
            if type(menu.List[value])==list:
                to=str(menu.List[value][0])+":"+str(menu.List[value][1])
            else:
                to=menu.List[value]
            draw.text((x1,y),to,font=font, fill=self.color[1])
            y+=inc_line
            i+=1
        

    def set_draw_list(self):
        pointer=self.navigator.menu.pointer
        cmd=0

        if pointer!=self.last_pointer and pointer==0:
            cmd="origin"
        elif pointer>self.last_pointer:
            cmd="+"
        elif pointer<self.last_pointer:
            cmd="-"
        self.last_pointer=pointer
        
        if cmd =="+":
            if self.pointer_line<self.nb_max_line:
                self.pointer_line+=1
            elif self.pointer_line>=self.nb_max_line:
                self.origin_line+=1
            
        elif cmd =="-":
            if self.pointer_line>0:
                self.pointer_line-=1
            elif self.pointer_line==0:
                self.origin_line-=1
        
        elif cmd =="origin":
            self.pointer_line=0
            self.origin_line=0
        
        print("set_draw_list:",pointer,self.last_pointer,self.origin_line)


    def draw_sequence(self):
        y=y0
        menu=self.navigator.menu
        track=self.machine.partition.tracks[self.navigator.track]
        draw.text((x2,y),"note",font=font, fill=self.color[1])
        y+=inc_line
        draw.text((x1,y),"pas:"+str(menu.pas),font=font, fill=self.color[1])
        y+=inc_line
        to=0
        for element in track.notes:
            i=0
            while i<len(element.setting):
                if element.setting[i][0]==menu.setting:
                    to=element.setting[i][1]
                i+=1
                
        draw.text((x1,y),menu.setting+":"+str(to),font=font, fill=self.color[1])
        
        
    def draw_info(self):
        y=y0
        tracks=self.machine.partition.tracks
        pointer_track=self.navigator.pointer_track
        to=tracks[pointer_track].sample_length
        draw.text((x1,y),"duree:"+str(to),font=font, fill=self.color[1])
