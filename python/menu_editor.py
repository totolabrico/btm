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
		self._pointer_pas=0# pointer de pas
		self.list_pas=[]
		self.nb_pas=0
		self.set_nb_pas()
		self._pas_per_line=0
		self._set_pas_per_line()


	def get_copy_list(self):
		return self.copy_list
	def set_copy_list(self)
		pass

	def _get_list_pas(self):
		return self._list_pas
	def _set_list_pas(self):
	    pass
	def set_nb_pas(self):
		pass

	def _get_pas_per_line(self):
		return self._pas_per_line
	def _set_pas_per_line(self):
		pass

	def _get_pointer_pas(self): # a remplacer par _get_setting
		return self._pointer_pas
	def _set_pointer_pas(self,pas):
		self._pointer_pas=pas

	def analyse(self,cmd):

		if cmd=="edit":
			if self.is_selecting==False:
				self.selection[0]=self.pas
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
				self.copy_list.append(copy.deepcopy(self.list_pas[i]))
				i+=1
			print("copy-notes",self.copy_list)

		elif cmd=="paste":
			paste_list = copy.deepcopy(self.copy_list)
			if len(paste_list)>0:
				to=[]
				i=0
				while i<len(paste_list):
					if paste_list[i]!=0:
						paste_list[i].pas+=self.pas-paste_list[i].pas+i
						to.append(paste_list[i])
					i+=1

				self.track.paste_element(to)

		elif cmd=="del":
			i=self.selection[0]
			while i<=self.selection[1]:
				if self.list_pas[i]!=0:
					self.track.remove_element(self.list_pas[i].Id)
				i+=1

		elif cmd=="right":
			self.pas=loopPas("+",self._pointer_pas,1,self.nb_pas-1,0)
		elif cmd=="left":
			self.pas=loopPas("-",self._pointer_pas,1,self.nb_pas-1,0)
		elif cmd=="up":
			self.pas=loopPas("-",self._pointer_pas,self.pas_per_line,self.nb_pas-1,0)
		elif cmd=="down":
			self.pas=loopPas("+",self._pointer_pas,self.pas_per_line,self.nb_pas-1,0)

		if self.is_selecting:
			self.selection[1]=self.pas

	pointer_pas=property(_get_pointer_pas,_set_pointer_pas)
	pas_per_line=property(_get_pas_per_line,_set_pas_per_line)
	list_pas=property(_get_list_pas,_set_list_pas)
