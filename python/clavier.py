from pynput import keyboard
import time

class Clavier:

    def __init__(self,Machine):
        self.machine=Machine
        self.state="default"
        self.select=False
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def on_press(self,Key):
        key=getMap(Key)
        cmd=key[0]
        arg=key[1]
        if cmd=="button":
            self.state=arg

        elif cmd=="select" and arg=="+":
            if self.select==False:
                self.machine.navigator.sort(self.state,cmd,arg)
                self.select=True    
        else:
            self.machine.navigator.sort(self.state,cmd,arg)

    def on_release(self,Key):
        key=getMap(Key)
        cmd=key[0]
        arg=key[1]
        if cmd=="select":
             if arg=="+":
                self.machine.navigator.sort(self.state,cmd,"stop")
                self.select=False
        elif cmd=="button":
            if self.state==arg:
                self.state="default"

def getMap(key):
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
	A0	A1	A2	A3
    B0  B1  B2	B3
	C0	C1	C2
    D0  D1  D2	D3
    E0      E2
'''

editor_keys={
	"A0":["switch","mode"],
    "A1":["button","setting"],
    "A2":["button","element"],

	"B0":["edit","*"],
    "B1":["edit","copy"],
    "B2":["edit","previous"],

	"C0":["edit","-"],
	"C1":["move",["y","-"]],
	"C2":["edit","+"],

	"D0":["move",["x","-"]],
	"D1":["move",["y","+"]],
	"D2":["move",["x","+"]],

	"E0":["select","+"],
	"E2":["select","clear"],
	}
