from pynput import keyboard
from keyMap import*
import time

tick=0.3
click_tick=0.13

class Clavier:

    def __init__(self,Navigator):
        self.navigator=Navigator
        self.timer=0
        self.second=[0,0]
        self.key=""
        self.first=True
        self.maintain=False
        self.double=False
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()
    def on_press(self,key):

        
        if self.first==True:
            self.key=getMap(key)
            self.second[0]=time.time()
            if self.second[0]-self.second[1]<click_tick:
                self.double=True
                
            if self.double==True:
                #print("on_press",myKey)
                if self.key=="left"or self.key=="right":
                    self.key+="++"  
            self.first=False
            
            
        self.second[1]=time.time()
        self.timer=self.second[1]-self.second[0]
        if self.timer>tick:
            self.maintain=True
            self.second[0]=time.time()
            print("on_press",self.key)
            self.navigator.analyse_cmd(self.key)
            # print("on_press",self.double)

    def on_release(self,key):
        self.Key=getMap(key)
        if self.maintain==False:
            self.on_the_go()
        else:    
            self.maintain=False
        self.first=True
        self.double=False
        self.second[1]=time.time()
        
    def on_the_go(self):
        local_timer=[time.time(),time.time()]
        while local_timer[1]-local_timer[0]>click_tick*2:
            local_timer[1]=time.time()
        if self.double==False:
            self.navigator.analyse_cmd(self.key)






