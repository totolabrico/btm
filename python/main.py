import copy
import threading
from clavier import*
from partition import*
from nav import*

class Machine:

	def __init__(self):
		self.partition=Partition(self)
		self.navigator=Navigator(self)
		self.clavier=Clavier(self)
		self.oled = threading.Thread(target=self.navigator.draw(), args=())
		self.oled.start()

btm=Machine()
print("btm")

while True:
	time.sleep(10)
