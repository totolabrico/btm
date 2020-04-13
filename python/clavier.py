from pynput import keyboard
from keyMap import*
import time

class Clavier:
    
    def __init__(self,Navigator):
	    self.navigator=Navigator
	    self.timer=0
	    self.second=[0,0]
	    self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
	    self.listener.start()
    def on_press(self,key):
	    myKey=getMap(key)
	    #self.second[0] = Math.round(time.time()/1000)
		#if self.second!=
	    #self.timer+=1
	    print(self.second[0])
	    self.navigator.analyse_cmd(myKey)

    def on_release(self,key):
	    myKey=getMap(key)
	    #print("release")
	    #self.navigator.analyse_cmd(myKey)





