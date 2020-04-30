from basic_function import*
import threading
from draw_menu import*

class Menu:

	display = "wait for it"

	def __init__(self,Partition,Navigator,Name):
		self.partition=Partition
		self.navigator=Navigator
		self.name=Name
		self.title=Name
		self.track=""
		self.init_more(Name)
		self._pointer_setting=0
		self._list_setting=[]
		self._set_list_setting()
		self.draw_menu=Draw_menu(self)

	def init_more(self,Name):
		if Name=="main":
			self.title="main: "+self.partition.name
		if Name=="notes" or Name=="track":
			self.track=self.partition.tracks[self.navigator.track]
			self.title=str(self.track.id)+":"+self.track.name


	def _get_list_setting(self):
		return self._list_setting
	def _set_list_setting(self):
		pass

	def _get_pointer_setting(self):
		return self._pointer_setting
	def _set_pointer_setting(self,cmd):
		self._pointer_setting=cmd

	def analyse(self,cmd):
		if cmd=="up":
			self.pointer_setting=loopValue("-",self.pointer_setting,1,len(self.list_setting)-1,0)
		elif cmd=="down":
			self.pointer_setting=loopValue("+",self.pointer_setting,1,len(self.list_setting)-1,0)

	def switch_track(self,cmd):
		if len(self.partition.tracks)>1:
			self.navigator.track=cmd
			self.navigator.menu=self.name


	pointer_setting=property(_get_pointer_setting,_set_pointer_setting)
	list_setting=property(_get_list_setting,_set_list_setting)
