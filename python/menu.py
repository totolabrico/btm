from basic_function import*
import threading
from draw_menu import*

class Menu:
	
	display = "wait for it"

	def __init__(self,Partition,Navigator,Name):
		self.partition=Partition
		self.navigator=Navigator
		self.name=Name
		self._pointer=0
		self._list=[]
		self._set_list()
		self.draw_menu=Draw_menu(self)

	def _get_list(self):
		return self._list
	def _set_list(self):
		pass

	def _get_pointer(self):
		return self._pointer
	def _set_pointer(self,cmd):
		self._pointer=cmd

	def analyse(self,button):
		#print("pointer:",self.pointer,button)
		if button=="up":
			self.pointer=loopValue("-",self.pointer,1,len(self.List)-1,0)
		elif button=="down":
			self.pointer=loopValue("+",self.pointer,1,len(self.List)-1,0)	
		#print("analyse",self.pointer)
	
	pointer=property(_get_pointer,_set_pointer)
	List=property(_get_list,_set_list)
