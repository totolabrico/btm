from draw import*
import time

class Navigator():

	def __init__(self,Machine):
		self.machine=Machine
		self.element=self.machine.partition
				
	def sort(self,cmd,arg):
		
		if cmd=="switch":

			if arg[0]=="element":
				if arg[1]=="-" and self.element.mother!=None:
					self.element=self.element.mother
				elif arg[1]=="+" and self.element.selected_child!=None:
					self.element=self.element.selected_child
			if arg[0]=="mode":
				self.element.set_mode()
					
		if self.element.mode==True:
			if cmd=="move":
				self.element.edit_pointer_settings(arg[0],arg[1])
			elif cmd=="edit":
				self.element.edit_settings(arg)
		
		elif self.element.mode==False:
			if cmd=="move":
				self.element.edit_pointer_children(arg[0],arg[1])
			elif cmd=="edit":
				self.element.edit_children(arg)
			
			"""	 ci dessous:obselete / a replacer
				self.element.selected_child.edit_pointer_settings(arg[0],arg[1])
			"""
	def draw(self):
		while True:
			draw_begin()
			if self.element.mode==True:
				draw_title(self.element.name)
				self.element.draw_settings()
			else:
				draw_title(self.element.name+":"+self.element.children_name)
				self.element.draw_children()
			draw_end()
			time.sleep(0.07)
