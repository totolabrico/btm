from menu import*
from menu_editor import*

from partition_notes import*
import copy

copy_notes=[]

class Menu_notes(Menu_editor):

	def __init__(self,Partition,Navigator,Name):

		Menu_editor.__init__(self,Partition,Navigator,Name)
		self.pointer_setting=1

	def set_nb_element(self):
		self.nb_element=self.partition.temps*self.track.mesure
		temps=self.partition.temps
		self._element_per_line=4*temps
		if temps>=5:
			self._element_per_line=2*temps

	def set_copy_list(self)
		global copy_notes
		self.copy_list=copy_notes

	def _set_elements(self):
		self.elements=self.track.notes
		self.element=self.elements[self.pointer_element]

	def _set_list_element(self):
		self.list_element=[]
		self._list_setting=[]
		i=0
		while i<self.nb_element:
			self.list_element.append(0)
			if len(self.elements)>0:
				for element in self.elements:
					if i == element.element:
						self.list_element[i]=element
						if i==self.element:
							self.note=element
							self._list_setting=element.setting
			i+=1


	def analyse(self,cmd):

		if cmd=="back":
			self.navigator.menu="track"

		elif cmd=="+" or cmd=="-":
			if len(self.list_setting)>0:
				setting=self.list_setting[self.pointer_setting][0]
				if setting=="vol":
					self.note.vol=cmd
				elif setting=="pan":
					self.note.pan=cmd
				elif setting=="pitch":
					self.note.pitch=cmd
				elif setting=="tone":
					self.note.tone=cmd
				elif setting=="begin":
					self.note.begin=cmd
				elif setting=="length":
					self.note.length=cmd
			else:
				if cmd=="+":
					self.pointer_setting=1
					self.track.add_element(self.pointer_element)
					print("add note ",self.pointer_element)

		elif type(cmd)==list_setting:
			if cmd[0]=="track":
				self.switch_track(cmd[1])

		if len(self.list_setting)>0:
			if cmd=="set-":
				self.pointer_setting=loopValue("+",self.pointer_setting,1,len(self.list_setting)-1,1)
			elif cmd=="set+":
				self.pointer_setting=loopValue("-",self.pointer_setting,1,len(self.list_setting)-1,1)


		self._set_list()
