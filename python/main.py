import copy
import dill as pickle
from clavier import*
from encoder import*
from partition_init import*
from navigator import*

class Machine:

	def __init__(self):
		self.partition=Partition_main(None)
		self.navigator=Navigator(self)
		self.clavier=Clavier(self)
		self.encoder=Encoder(self)
		self.oled = threading.Thread(target=self.navigator.draw(), args=())
		self.oled.start()		

	def save_set(self):
		path="home/pi/btm/saves/"+self.partition.name
		with open(path,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump(self.partition)

	def load_set(self,Path):
		with open(Path,'rb') as fichier:
			mon_depickler=pickle.Unpickler(fichier)
			self.partition=mon_depickler.load()


btm=Machine()
print("btm")

while True:
	time.sleep(10)
