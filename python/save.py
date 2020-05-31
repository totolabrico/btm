import os
from pythonosc import osc_message_builder
from pythonosc import udp_client
client = udp_client.UDPClient('localhost', 12000)
path="/home/pi/btm/set/"

def clean(Name):
    global path
    if Name=="all":
        for element in os.listdir(path):
            os.remove(path+element)
    else:
        print("clean",Name)
        os.remove(path+Name+".txt")
        os.remove(path+Name+"_notes.txt")

def save_main(setting):
	global path
	myfile = open(path+"main.txt","w")
	for element in setting:
		myfile.write(element[0]+" "+to_string(element[1])+";\n")
	myfile.close()
	sendMessage("load","main")
	
def save_track(name,setting,children):
	global path
	#save track parameters
	myfile = open(path+name+".txt","w")
	for element in setting:
		myfile.write(name+" "+element[0]+" "+to_string(element[1])+";\n")
	myfile.close()
	#save notes parameters
	myfile = open(path+name+"_notes.txt","w")
	for element in children:
		for setting in element.setting:
			myfile.write(str(element.id)+" "+name+"_notes "+" "+setting[0]+" "+to_string(setting[1])+";\n")
	myfile.close()
	
	sendMessage("load",name)


def sendMessage(cmd,*args):

	addr="/"+str(cmd)
	msg = osc_message_builder.OscMessageBuilder(address=addr)
	for element in args:
		msg.add_arg(element)
	msg = msg.build()
	client.send(msg)

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
