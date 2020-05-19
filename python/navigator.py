from draw import*
import time

class Navigator():

	def __init__(self,Machine):
		self.machine=Machine
		self.element=self.machine.partition

	def sort(self,state,cmd,arg):
		#print("navigator_sort", state,cmd,arg)				
		if cmd=="switch":
			self.element.set_mode()
					
		if self.element.mode==True:
			if cmd=="move":
				self.element.set_pointer_setting(arg[0],arg[1])		
			if cmd=="select":
				if arg=="+" or arg=="stop":
					self.element.set_fork_setting(arg)
				if arg=="clear":
					self.element.set_selecter_setting(arg)
			if cmd=="edit":
				self.element.set_setting(arg)

		
		elif self.element.mode==False:
			if state=="default":
				if cmd=="move":
					self.element.set_pointer_children(arg[0],arg[1])
				elif cmd=="edit":
					self.element.set_children(arg)		 
			
			elif state =="setting":
				if cmd=="move":
					self.element.selected_child.set_pointer_setting(arg[0],arg[1])
				elif cmd=="edit":
					self.element.selected_child.set_setting(arg)		
					
			elif state=="element":
				if cmd=="move":
					if arg[0]=="y":	
						if arg[1]=="-" and self.element.mother!=None:
							self.element=self.element.mother
						elif arg[1]=="+" and self.element.selected_child!=None:
							self.element=self.element.selected_child
			
			"""	 ci dessous:obselete / a replacer
				self.element.selected_child.edit_pointer_settings(arg[0],arg[1])
			"""
	def draw(self):
		while True:
			draw_begin()
			if self.element.mode==True:
				draw_title(self.element.name)
				self.element.draw_setting()
			else:
				draw_title(self.element.name+":"+self.element.children_name)
				self.element.draw_children()
			draw_end()
			time.sleep(0.07)
