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
		self.list_element=[]
		self.nb_element=0
		self.set_nb_element()
		self._element_per_line=0
		self._set_element_per_line()

	def get_copy_list(self):
		return self.copy_list
	def set_copy_list(self)
		pass

	def _get_list_element(self):
		return self._list_element
	def _set_list_element(self):
	    pass
	def set_nb_element(self):
		pass

	def _get_element_per_line(self):
		return self._element_per_line
	def _set_element_per_line(self):
		pass

	def _get_pointer_element(self): # a remplacer par _get_setting
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
			if len(paste_list)>0:
				to=[]
				i=0
				while i<len(paste_list):
					if paste_list[i]!=0:
						paste_list[i].pas+=self.pointer_element-paste_list[i].pas+i
						to.append(paste_list[i])
					i+=1

				self.track.paste_element(to)

		elif cmd=="del":
			i=self.selection[0]
			while i<=self.selection[1]:
				if self.list_element[i]!=0:
					self.track.remove_element(self.list_element[i].Id)
				i+=1

		elif cmd=="right":
			self.pointer_element=loopPas("+",self._pointer_element,1,self.nb_element-1,0)
		elif cmd=="left":
			self.pointer_element=loopPas("-",self._pointer_element,1,self.nb_element-1,0)
		elif cmd=="up":
			self.pointer_element=loopPas("-",self._pointer_element,self.element_per_line,self.nb_element-1,0)
		elif cmd=="down":
			self.pointer_element=loopPas("+",self._pointer_element,self.element_per_line,self.nb_element-1,0)

		if self.is_selecting:
			self.selection[1]=self.pointer_element

	pointer_element=property(_get_pointer_element,_set_pointer_element)
	element_per_line=property(_get_element_per_line,_set_element_per_line)
	list_element=property(_get_list_element,_set_list_element)
