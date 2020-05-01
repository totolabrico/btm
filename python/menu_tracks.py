from menu import*
from menu_editor import*

import copy

copy_track=[]

class Menu_tracks(Menu_editor):

	def __init__(self,Partition,Navigator,Name):
		Menu_editor.__init__(self,Partition,Navigator,Name)
		self.pointer_setting=2
		self.pointer_element=0

	def set_copy_list(self):
		global copy_track
		self.copy_list=copy_track

	def set_elements(self):
		self.nb_element=len(self.partition.tracks)
		self.element_per_line=5
		self.mother_element=self.partition
		self.child_elements=self.partition.tracks

	def analyse(self,cmd):
		Menu_editor.analyse(self,cmd)
		length=len(self._list_setting)
		if cmd=="back":
			self.navigator.menu="main"
		elif cmd=="edit":
			if len(self.child_elements)>0:
				self.navigator.menu="track"

		self.navigator.pointer_track=self.pointer_element
		self.set_elements()
		self._set_list_setting()
		self._set_list_element()
