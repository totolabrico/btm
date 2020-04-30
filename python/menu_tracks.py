from menu import*
from menu_editor import*

import copy

copy_track=[]

class Menu_tracks(Menu_editor):

	def __init__(self,Partition,Navigator,Name):
		Menu_editor.__init__(self,Partition,Navigator,Name)
		self.pointer_setting=0
		self.pointer_element=0

	def set_nb_pas(self):
		self.nb_pas=self.partition.nb_tracks
		self._element_per_line=8

	def set_copy_list(self)
		global copy_track
		self.copy_list=copy_track

	def _set_elements(self):
		self.elements=self.partition.tracks
		self.element=self.elements[self.pointer_element]

	def analyse(self,cmd):
		global copy_track
		Menu.analyse(self,cmd)
		length=len(self._list)
		if cmd=="back":
			self.navigator.menu="main"
		elif cmd=="edit":
			if self.pointer<length-1:
				self.navigator.track=self.pointer
				self.navigator.menu="track"
			elif self.pointer==length-1:
				self.partition.add_element()


		self._set_list()
