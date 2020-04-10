from pynput import keyboard
from keyMap import*

class Clavier:
    
    def __init__(self,Navigator):
	    self.navigator=Navigator
	    self.listener = keyboard.Listener(on_press=self.on_press)
	    self.listener.start()
    def on_press(self,key):
	    myKey=getMap(key)
	    self.navigator.analyse_cmd(myKey)







