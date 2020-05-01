import os
#from osc import*

#path="./set/"
path="/home/toto/btm/set/"
def clean(Name):
    global path
    if Name=="all":
        for element in os.listdir(path):
            os.remove(path+element)
    else:
        os.remove(path+Name)


def save(name,setting):
	global path
	myfile = open(path+name+".txt","w")
	i=0
	while i<len(setting):
		myfile.write(name+" "+setting[i][0]+" "+to_string(setting[i][1])+";\n")
		i+=1
	myfile.close()
	#sendMessage("load",self.name) A DECOMMENTER !


def to_string(valeur):
	to=""
	if type(valeur)==int or type(valeur)==float:
		to=str(valeur)
	elif type(valeur)==str:
		to=valeur
	elif type(valeur)==bool:
		to=str(int(valeur))
	elif type(valeur)==list:
		i=0
		while i<len(valeur):
			to+=str(valeur[i])
			if i<len(valeur)-1:
				to+=" "
			i+=1
	else:
		to=str(len(valeur))
	return to
