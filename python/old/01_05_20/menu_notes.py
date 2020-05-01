from menu import*
from menu_editor import*

from partition_notes import*
import copy

copy_notes=[]

class Menu_notes(Menu_editor):

	def __init__(self,Partition,Navigator,Name):

		Menu_editor.__init__(self,Partition,Navigator,Name)
		self.pointer_setting=1
		self.pointer_element=0

	def set_copy_list(self):
		global copy_notes
		self.copy_list=copy_notes

	def set_elements(self):
		self.set_nb_element()
		self.mother_element=self.track
		self.child_elements=self.track.notes

	def set_nb_element(self):
		self.nb_element=self.partition.temps*self.track.mesure
		temps=self.partition.temps
		self.element_per_line=4*temps
		if temps>=5:
			self.element_per_line=2*temps
				
	def analyse(self,cmd):
		Menu_editor.analyse(self,cmd)
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


		elif type(cmd)==list:
			if cmd[0]=="track":
				self.switch_track(cmd[1])

		self.set_elements()
		self._set_list_setting()
		self._set_list_element()
