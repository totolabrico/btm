from basic_function import*
import threading
from draw_menu import*
import time

class Menu:
	
	display = "wait for it"


	def __init__(self,Navigator,Name):
		self.navigator=Navigator
		self.name=Name
		self._pointer=0
		self._list=[]
		self._set_list()
		self.init_draw()
		
	def init_draw(self):
		self.draw_menu=Draw_menu(self)
		self.finish_draw=False
		display = threading.Thread(target=self.draw_led, args=())
		display.start()

	def _get_list(self):
		return self._list
	def _set_list(self):
		pass

	def _get_pointer(self):
		return self._pointer
	def _set_pointer(self,cmd):
		self._pointer=cmd

	def analyse(self,button):
		print("pointer:",self.pointer,button)

		if button=="up":
			self.pointer=loopValue("-",self.pointer,1,len(self.List)-1,0)
		elif button=="down":
			self.pointer=loopValue("+",self.pointer,1,len(self.List)-1,0)
		
		print("analyse",self.pointer)
		
	def set_draw(self):
		self.draw_menu.set_pointer()
		self.draw_menu.set_display_list()
		
	def draw_led(self):
		time.sleep(0.2)
		while self.finish_draw==False:	
			time.sleep(0.1)				
			self.draw_menu.draw_begin()
			self.draw_menu.draw_title()
			self.draw_menu.draw_list()
			self.draw_menu.draw_pointer()
			self.draw_menu.draw_end()

		return
	"""
	def kill_display(self):
		self.display.do_run = False
	"""
	
	pointer=property(_get_pointer,_set_pointer)
	List=property(_get_list,_set_list)
