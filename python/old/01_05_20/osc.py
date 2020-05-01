from pythonosc import osc_message_builder
from pythonosc import udp_client
import time

client = udp_client.UDPClient('localhost', 12000)

def sendMessage(cmd,*args):

	addr="/"+str(cmd)
	msg = osc_message_builder.OscMessageBuilder(address=addr)
	for element in args:
		msg.add_arg(element)
	msg = msg.build()
	client.send(msg)
	#print ("osc send/ cmd:",cmd,"/ arg:",args)

"""
while True:
	sendMessage("play",1,1)
	time.sleep(0.25)
	sendMessage("play",2,1)
	time.sleep(0.25)
"""
