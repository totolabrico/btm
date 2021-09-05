import time
from draw import*
from osc import*
from menu_main import*

class Navigator():

	def __init__(self,Machine):
		self.machine=Machine
		self.backup_menu=None
		self.menus={
			"main":MainMenu(self,Machine),
			#"play":PlayMenu(self),
			"save":SaveMenu(self,self.machine.partition),
			"load":LoadMenu(self,self.machine.partition),
			#"sequencer":SequencerMenu(self.machine,self.machine.partition,self),
			"master":MasterMenu(self.machine,self.machine.partition,self),
			"tracks":TracksMenu(self.machine,self.machine.partition,self),
			"track":TrackMenu(self.machine,self.machine.partition,self),
			"child":ChildMenu(self.machine,self.machine.partition,self),
			"sample":SampleMenu(self,self.machine.partition),
			"notes":NotesMenu(self.machine,self.machine.partition,self),
			"note":NoteMenu(self.machine,self.machine.partition,self),
			}
			
		self.menu=self.menus["main"]
				
	def set_menu(self,Name):
		try:
			self.menu=self.menus[Name]
			print("menu",Name)
			try:
				self.menu.set_parameters()
			except:
				#print("no parameters to set for this menu")
				pass
		except:
			pass
		
	def sort(self,cmd,arg): # tri les commandes provenants du clavier vers set_current_editor ou un editeur ou le browser
		self.menu.sort(cmd,arg)
		#print("nav sort : ",cmd,arg)
			
	def close_browser():
		self.pointer="editor"

	def draw(self): # appel le draw de l'editeur ou du browser
		while self.machine.reset==False:
			draw_begin()
			self.menu.draw()
			draw_end()
			time.sleep(0.1)
