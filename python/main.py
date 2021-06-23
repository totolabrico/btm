
'''
0/ le load du master ne fonctionne pas
1/ faire des listes pours les notes dans les messages osc : on envoi la liste a chaque modif de note, tout les volumes par exemple
2/ Redimentionner les tableau puredata en fonction de la taille des partition
3/ Coder le end et virer le loop_lenght dans partition
'''

import copy
import threading
from clavier import*
from partition import*
from nav import*
import os


class Machine:
	reset=False
	def __init__(self):
		self.partition=Partition(self)
		self.navigator=Navigator(self)
		self.clavier=Clavier(self)
		self.oled = threading.Thread(target=self.navigator.draw(), args =(),daemon=True)
		self.oled.start()
		
	def close(self):
		self.clavier.listener.stop()
		self.reset=True
		
	def new_open(self):
		os.system("lxterminal -e sh /home/pi/bin/start.sh &")
btm=Machine()


