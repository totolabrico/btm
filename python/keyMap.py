
''' MAPPING
0	1		2
5	6	7	8	3
9	10	11	12	4
13	14	15	16
'''

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
	
editor_keys={
	6:"up",
	14:"down",
	9:"left",
	11:"right",
	10:"edit",
	5:"back",
	13:"del",
	7:"+",
	15:"-",
	8:"set+",
	16:"set-",
	}

def getMap(key):
	global keys,editor_keys
	keyId=-1
	
	for cle, valeur in keys.items():
		#print("inKey:",inKey," Keys:",cle,valeur)
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
