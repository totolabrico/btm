import os, sys
from draw import*
import time

class Browser():

    def __init__(self,navigator):
        self.navigator=navigator
        self.pointer=0
        self.path="/home/pi/audiosamples"
        self.set_list()
    
    def set_list(self):
        self.list=[]
        for element in os.listdir(self.path):
            if element[:1]!=".":
                self.list.append(element)
    
    
    def sort(self,cmd,arg):
        if cmd=="move":
            if arg[0]=="y":
                self.set_pointer(arg[1])
            if arg[0]=="x":
                self.set_path(arg[1])
        
        if self.list[self.pointer][-4:].lower()==".wav":
            if cmd=="select" and arg=="+":
                print("play the sound now")
            if cmd=="edit" and arg=="+":
                self.navigator.close_browser(self.path+"/"+self.list[self.pointer])
                
        if cmd=="switch":
            self.navigator.menu="partition"
                    
    def set_pointer(self,cmd):
        if cmd=="+":
            self.pointer+=1
        if cmd=="-":
            self.pointer-=1
        if self.pointer<0:
            self.pointer=len(self.list)-1
        if self.pointer==len(self.list):
            self.pointer=0
    
    def set_path(self,cmd):
        cut=self.path.split("/")
        last_word=cut[len(cut)-1]
        
        if cmd=="+":
            new_path=self.path+"/"+self.list[self.pointer]
            if os.path.isdir(new_path)==True:
                self.pointer=0
                self.path=new_path
                self.set_list()
        # du petit debug a faire ci dessous     
        if cmd=="-" and len(cut)>3:
            self.path=self.path[:-(len(last_word)+1)]
            self.set_list()
            i=0
            for element in self.list:
                if element==last_word:
                    self.pointer=i
                i+=1
            

    def draw(self):
        path=self.path[9:]
        draw_title(path[-20:])

        min=self.pointer
        max=4
        size=len(self.list)
        if max>size:
            max=size
        y=Y_inc[1]
        i=min
        while i<min+max:
            id=i
            if id>=size:
                id-=size
            file=self.list[id]
            if os.path.isdir(self.path+"/"+file)==True:
                file="*"+file
            if i==min:
                file="> "+file
            draw.text((2,y),file,font=font, fill=255)
            y+=Y_inc[0]
            i+=1
  
