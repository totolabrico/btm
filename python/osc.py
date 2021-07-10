from pythonosc import osc_message_builder
from pythonosc import udp_client
client = udp_client.UDPClient('127.0.0.1', 12000)

def osc_send(addr,setting_name,setting_value,idtrack=0,idnote=0):
	Addr="/"+str(addr)
	msg = osc_message_builder.OscMessageBuilder(address=Addr)
	if addr=="track":
		msg.add_arg(idtrack+1)
	if addr=="note":
		msg.add_arg("notes_"+str(idtrack+1)+"_"+setting_name)
	else:
		msg.add_arg(setting_name)
	if addr=="note":
		msg.add_arg(idnote)
	
	if type(setting_value)==list:
		for value in setting_value:
			msg.add_arg(clean_value(value))
	else:
		msg.add_arg(clean_value(setting_value))
	#print (idtrack+1,setting_name,clean_value(setting_value))
	msg = msg.build()
	client.send(msg)

"""
def osc_send_path(Path):
	Addr="/recorder"
	msg = osc_message_builder.OscMessageBuilder(address=Addr)
	msg.add_arg(Path)
	msg = msg.build()
	client.send(msg)
"""

def clean_value(valeur):
	if type(valeur)==bool:
		valeur=int(valeur)
	return valeur
