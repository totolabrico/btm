import time
import dill as pickle
from browser import*
from draw import*
from osc import*
from menu_main import*

class Navigator():

	def __init__(self,Machine):
		self.machine=Machine
		
		self.menus={
			"main":MainMenu(self),
			"play":PlayMenu(self),
			"sequencer":SequencerMenu(self.machine,self.machine.partition,self),
			"master":MasterMenu(self.machine,self.machine.partition,self),
			"tracks":TracksMenu(self.machine,self.machine.partition,self),
			"track":TrackMenu(self.machine,self.machine.partition,self),
			"audio":AudioMenu(self.machine,self.machine.partition,self),
			}
			
		self.menu=self.menus["main"]
				
	def set_menu(self,Name):
		try:
			self.menu=self.menus[Name]
			print("menu",Name)
			try:
				self.menu.set_parameters()
			except:
				print("no parameters to set")
		except:
			print("no menu with that name")
		
	def sort(self,cmd,arg): # tri les commandes provenants du clavier vers set_current_editor ou un editeur ou le browser
		print("nav sort",cmd,arg)
		self.menu.sort(cmd,arg)
			
	def close_browser():
		self.pointer="editor"

	def draw(self): # appel le draw de l'editeur ou du browser
		while True:
			draw_begin()
			self.menu.draw()
			draw_end()
			time.sleep(0.1)
