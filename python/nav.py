import time
from browser import*
from editor import*
from draw import*

menu_names=["master","track","note"] 

class Navigator():

	def __init__(self,Machine):
		self.pointer="editor"
		self.machine=Machine
		self.toggle_state=0 # 0:settings / 1:element
		self.master_editor=Editor(self.machine,self,"master",self.machine.partition.master_setting)
		self.track_editor=Editor(self.machine,self,"track",self.machine.partition.track_setting)
		self.note_editor=Editor(self.machine,self,"note",self.machine.partition.note_setting)
		self.editors=(self.master_editor,self.track_editor,self.note_editor)
		self.id_current_editor=0;
		self.pointer_editor=self.editors[self.id_current_editor] # prend la valeur de l"éditeur concerné , piloté depuis les editeurs 
		self.browser=Browser(self)

	def sort(self,cmd,arg): # tri les commandes provenants du clavier vers set_current_editor ou un editeur ou le browser
		if self.pointer=="editor":
			self.pointer_editor.sort(cmd,arg)
		elif self.pointer=="browser":
			self.browser.sort(cmd,arg)
						
		
	def edit_current_editor(self,cmd): # defini l'editeur actif
		last_id=int(self.id_current_editor)
		if cmd=="+":
			self.toggle_state=not self.toggle_state
			if self.id_current_editor<2:
				if self.toggle_state==True:
					self.id_current_editor+=1
		elif cmd=="-":
			if self.id_current_editor>0:
				self.toggle_state=not self.toggle_state
				if self.toggle_state==False:
					self.id_current_editor-=1
		
		if last_id!=self.id_current_editor:
			self.pointer_editor=self.editors[self.id_current_editor]
			if self.id_current_editor!=2:
				self.note_editor.reset_pointer();
		self.pointer_editor.set_tools() 
				
	def close_browser():
		self.pointer="editor"
		
	def draw(self): # appel le draw de l'editeur ou du browser
		while True:
			draw_begin()
			if self.pointer=="editor":
				#print("editor interface draw")
				self.pointer_editor.interface.draw()
			elif self.pointer=="browser":
				self.browser.draw()
			draw_end()
			time.sleep(0.1)
