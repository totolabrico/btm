from pythonosc import osc_message_builder
from pythonosc import udp_client
client = udp_client.UDPClient('127.0.0.1', 12000)

def osc_send(addr,setting_name,setting_value,idtrack=0,idnote=0):
	Addr="/"+str(addr)
	msg = osc_message_builder.OscMessageBuilder(address=Addr)
	if addr!="master":
		msg.add_arg(idtrack+1)
	
	msg.add_arg(setting_name)

	if addr=="notes":
		msg.add_arg(idnote)
	msg.add_arg(clean_value(setting_value))
	msg = msg.build()
	client.send(msg)

def clean_value(valeur):

	if type(valeur)==bool:
		valeur=int(valeur)
	return valeur
