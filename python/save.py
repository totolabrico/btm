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
        os.remove(path+Name)

def save(name,setting):
	global path
	myfile = open(path+name+".txt","w")
	for element in setting:
		myfile.write(name+" "+element[0]+" "+to_string(element[1])+";\n")
	myfile.close()
	sendMessage("load",name)
	
def save_track(name,setting,children):
	global path
	myfile = open(path+name+".txt","w")
	for element in setting:
		myfile.write(name+" "+element[0]+" "+to_string(element[1])+";\n")
	for element in children:
		for setting in element.setting:
			myfile.write(name+" "+element.save_name+" "+setting[0]+" "+to_string(setting[1])+";\n")
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
