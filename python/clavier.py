from pynput import keyboard
import time

class Clavier:

    def __init__(self,Machine):
        self.machine=Machine
        self.listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
        self.listener.start()

    def on_press(self,Key):
        key=getMap(Key)
        cmd=key[0]
        arg=key[1]
        self.machine.navigator.sort(cmd,arg)

    def on_release(self,Key):
        key=getMap(Key)
        cmd=key[0]
        arg=key[1]

keys={
	0:"-",
	1:"+",
	2:"Key.enter",
	3:[",","Key.delete"],
	4:["0","Key.insert"],
	5:"*",
	6:["9","Key.page_up"],
	7:["6","Key.right"],
	8:["3","Key.page_down"],
	9:["/"],
	10:["8","Key.up"],
	11:"<65437>",
	12:["2","Key.down"],
	13:"Key.num_lock",
	14:["7","Key.home"],
	15:["4","Key.left"],
	16:["1","Key.end"]
	}


''' MAPPING
	0	1		2
	5	6	7	8	3
	9	10	11	12	4
	13	14	15	16
'''

editor_keys={
	0:["switch",["mode",0]],
	#2:["switch",["mode",1]], # a remplacer par un switch actif ( a maintenir enfoncé )
    1:["switch",["element","-"]],
    2:["switch",["element","+"]],
	7:["move",["y","-"]],
	15:["move",["y","+"]],
	10:["move",["x","-"]],
	12:["move",["x","+"]],
	5:["edit","+"],
	9:["edit","-"],
    13:["edit","toggle"],

	}

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
