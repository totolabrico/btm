from pynput import keyboard
import time

class Clavier:

    def __init__(self,Machine):
        self.machine=Machine
        self.switch_state=0
        self.select_state=False
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def on_press(self,Key):
        key=get_map(Key)
        cmd,arg=get_cmd_arg(key)
        if cmd=="switch":
            if self.switch_state!=arg:
                self.switch_state=arg
                self.machine.navigator.sort(cmd,arg)
        elif cmd== "select":
            if self.select_state==False:
                self.select_state=True
                self.machine.navigator.sort(cmd,1)
        else:
            self.machine.navigator.sort(cmd,arg)

    def on_release(self,Key):
        key=get_map(Key)
        cmd,arg=get_cmd_arg(key)
        if cmd=="switch":
            self.machine.navigator.sort(cmd,0)
            self.switch_state=0
        elif cmd=="select":
            self.select_state=False
            self.machine.navigator.sort(cmd,0)


def get_cmd_arg(Key):
    cmd=Key[0]
    if len(Key)>1:
        arg=Key[1]
    else:
        arg=None
    return cmd,arg
            

def get_map(key):
    global keys,editor_keys
    keyId=-1
    for cle, valeur in keys.items():
        if type(valeur)==list:
            for value in valeur:
                if str(key)==str(value) or str(key)=="'"+str(value)+"'":
                    keyId=cle
        else:
            if str(key)==str(valeur) or str(key)=="'"+str(valeur)+"'":
                keyId =cle
    to="none"
    for cle, valeur in editor_keys.items():
        if keyId==cle:
            to= valeur
    return to


keys={
    "A0":"Key.num_lock",
    "A1":["/"],
    "A2":"*",
    "A3":"-",

    "B0":["7","Key.home"],
    "B1":["8","Key.up"],
    "B2":["9","Key.page_up"],
    "B3":"+",

    "C0":["4","Key.left"],
    "C1":"<65437>",
    "C2":["6","Key.right"],

    "D0":["1","Key.end"],
    "D1":["2","Key.down"],
    "D2":["3","Key.page_down"],
    "D3":"Key.enter",

    "E2":[",","Key.delete"],
    "E0":["0","Key.insert"]
    }


''' MAPPING
    A0  A1  A2  A3
    B0  B1  B2  B3
    C0  C1  C2
    D0  D1  D2  D3
    E0      E2
'''

editor_keys={

    "A3":["edit","*"],
    "B3":["edit","+"],
    "D3":["edit","-"],
    
    "E0":["menu","+"],
    "E2":["menu","-"],

    "A0":["switch",0],
    "A2":["switch",1],
    "C2":["switch",2],
    "C0":["switch",3],

    "A1":["move",["x","-"]],
    "C1":["move",["x","+"]],
    "B0":["move",["y","+"]],
    "B2":["move",["y","-"]],
    
    "B1":["select"],
    
    "D2":["cmd",1],
    "D1":["cmd",2],
    "D0":["cmd",3],


    }
