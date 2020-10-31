import time
from browser import*
from editor import*
from draw import*

class Navigator():

	def __init__(self,Machine):
		self.pointer="editor"
		self.machine=Machine
		self.editor=Editor(self.machine) # peut etre creer trois menu editor plutot qu un , ca pourrai etre bien pratique ( et une variable pointer_editor_menu)
		self.browser=Browser(self)

	def receive(self,cmd,arg):
		if self.pointer=="editor":
			self.editor.sort(cmd,arg)
		elif self.pointer=="browser":
			self.browser.sort(cmd,arg)
			
			
	def draw(self):
		while True:
			draw_begin()
			if self.pointer=="editor":
				#print("editor interface draw")
				self.editor.editor_interface.draw()
			elif self.pointer=="browser":
				self.browser.draw()
			draw_end()
			time.sleep(0.1)
