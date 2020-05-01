from pynput import keyboard
from clavier_map import*
import time

class Clavier:

    def __init__(self,Machine):
        self.machine=Machine
        self.switch_on=False
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def on_press(self,Key):
        key=getMap(Key)

        if key=="switch":
            self.switch_on=True

        if self.switch_on==True:
            if key=="up":
                key="+"
            if key=="down":
                key="-"
            if key=="left":
                key="set-"
            if key=="right":
                key="set+"
            if key=="edit":
                key="back"
            if key=="add":
                key="del"
            if key=="copy":
                key="paste"
        self.machine.navigator.analyse_cmd(key)


    def on_release(self,Key):
        key=getMap(Key)
        if key=="switch":
            self.switch_on=False
        if key=="edit":
            self.machine.navigator.analyse_cmd("edit_release")
