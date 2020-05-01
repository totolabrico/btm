from menu import*
from draw_menu_editor import*
from partition_notes import*
import copy

class Menu_editor(Menu):

	def __init__(self,Partition,Navigator,Name):
		Menu.__init__(self,Partition,Navigator,Name)
		self.selection=[-1,-1]
		self.is_selecting=False
		self.copy_list=[]
		self._pointer_element=0# pointer de pas
		self._list_element=[]
		self._set_list_element()
		self.draw_menu_editor=Draw_menu_editor(self)
		
	def get_copy_list(self):
		return self.copy_list
	def set_copy_list(self):
		pass

	def _get_list_element(self):
		return self._list_element
	def _set_list_element(self):
		self.set_elements()
		self._list_element=self.child_elements
		self._list_setting=[]
		if len(self._list_element)!=0:
			
			print("menu-editor_set-list-element",self._list_element,self.pointer_element)
			#self._list_setting=self._list_element[self.pointer_element].setting
			
	def _get_pointer_element(self): 
		return self._pointer_element
	def _set_pointer_element(self,pas):
		self._pointer_element=pas

	def analyse(self,cmd):

		if cmd=="edit":
			if self.is_selecting==False:
				self.selection[0]=self.pointer_element
				self.is_selecting=True
		elif cmd=="edit_release":
			if self.selection[1]<self.selection[0]:
				transit=self.selection[1]
				self.selection[1]=self.selection[0]
				self.selection[0]=transit
			self.is_selecting=False

		elif cmd=="copy":
			self.copy_list=[]
			i=self.selection[0]
			while i<=self.selection[1]:
				self.copy_list.append(copy.deepcopy(self.list_element[i]))
				i+=1
			print("copy-notes",self.copy_list)

		elif cmd=="paste":
			paste_list = copy.deepcopy(self.copy_list)
			self.mother_element.paste_element(paste_list,self.pointer_element)

		elif cmd=="add":
			self.mother_element.add_element(self.pointer_element)
				
		elif cmd=="del":
			i=self.selection[0]
			while i<=self.selection[1]:
				if self.list_element[i]!=0:
					self.mother_element.del_element(self.pointer_element)
				i+=1

		elif cmd=="right":
			self.pointer_element=loopPas("+",self._pointer_element,1,self.nb_element-1,0)
		elif cmd=="left":
			self.pointer_element=loopPas("-",self._pointer_element,1,self.nb_element-1,0)
		elif cmd=="up":
			self.pointer_element=loopPas("-",self._pointer_element,self.element_per_line,self.nb_element-1,0)
		elif cmd=="down":
			self.pointer_element=loopPas("+",self._pointer_element,self.element_per_line,self.nb_element-1,0)


		if len(self.list_setting)>0:
			if cmd=="set-":
				self.pointer_setting=loopValue("+",self.pointer_setting,1,len(self.list_setting)-1,1)
			elif cmd=="set+":
				self.pointer_setting=loopValue("-",self.pointer_setting,1,len(self.list_setting)-1,1)


		if self.is_selecting:
			self.selection[1]=self.pointer_element

	pointer_element=property(_get_pointer_element,_set_pointer_element)
	list_element=property(_get_list_element,_set_list_element)
