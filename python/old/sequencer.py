import time
from osc import*

class Sequencer:
	partition="waitforit"
	
	def __init__(self,Partition):
		self.partition=Partition

	def run(self):

		while True:
			tick=(60/self.partition.bpm)/8 #duree entre deux pas
			pas=self.partition.pas
			time.sleep(tick)
			if self.partition.playing:
				pas+=1
				if pas>=self.partition.loop_length:
					pas=0
				self.partition.pas=pas
				self.analysePas()
				
	def analysePas(self):
		pas=self.partition.pas

		if pas%8==0:
			#print ("tik")
			sendMessage("play",1,1)

		if (pas+4)%8==0:
			#print ("tik")
			sendMessage("play",2,1)
"""	
		if pas%16==0:
			#print ("tik")
			sendMessage("play",3,1)

"""
