from menu import*
from menu_editor import*

import copy

copy_track=[]

class Menu_tracks(Menu_editor):

	def __init__(self,Partition,Navigator,Name):
		Menu_editor.__init__(self,Partition,Navigator,Name)
		self.pointer_pas=0


	def set_nb_pas(self):
		self.nb_pas=self.partition.nb_tracks
		self._element_per_line=8

	def set_copy_list(self)
		global copy_track
		self.copy_list=copy_track


	def _set_list_pas(self):
		self._list_pas=[]
		self._list_setting=[]

		if len(self.partition.tracks)!=0:
			i=0
			while i<len(self.partition.tracks):
				self._list.append([str(self.partition.tracks[i].id),self.partition.tracks[i].name])
				i+=1
		self._list_pas.append(["add","+"])
		#self._list.append(["remove","-"])



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
		elif cmd=="del":
			if self.pointer<length-1:
				self.partition.del_element(self.pointer)
		elif cmd=="copy":
			if self.pointer<length-1:
				copy_track=copy.deepcopy(self.partition.tracks[self.pointer])
				print (copy_track)
		elif cmd=="paste":
			if self.pointer<length-1 and copy_track!='':
				self.partition.paste_element(copy_track,self.pointer+1)

		self._set_list()
