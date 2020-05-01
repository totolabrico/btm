from menu import*
import os, sys

class Menu_browser(Menu):


	def __init__(self,Partition,Navigator,Name):
		self._path="/home/pi/audiosamples/"
		Menu.__init__(self,Partition,Navigator,Name)
		self._set_path(self._path)


	def _get_path(self):
		return self._path
	def _set_path(self,Path):
		self._path=Path
		self._set_list_setting()

	def _set_list_setting(self):
		self._list_setting=[]
		for element in os.listdir(self._path):
			if element[:1]!=".":
				self._list_setting.append(element)

	def analyse(self,cmd):
		Menu.analyse(self,cmd)

		if cmd=="back":
			self.navigator.menu="track"
		elif cmd=="edit":
			if self._list_setting[self.pointer_setting][-4:].lower()==".wav":
				#print("browser_analyse",len(self.partition.tracks),self.navigator.track,self.pointer)
				self.partition.tracks[self.navigator.pointer_track].sample=self.path+self._list_setting[self.pointer_setting]
				self.navigator.menu="track"

		elif cmd=="left":
			to=self.path[:-1]
			letter=to[-1:]
			while letter!= "/":
				to=to[:-1]
				letter=to[-1:]
			print("road:",len(to))
			if len(to)>=9:# pour ne pas remonter plus haut que /home/pi/
				self.path=to
				#self._set_list()
				self.pointer_setting=0

		elif cmd=="right":
			to=self._path+self._list_setting[self.pointer_setting]
			print("right:",to)
			if os.path.isdir(to)==True:
				self.path=to+"/"
				#self._set_list()
				self.pointer_setting=0

		self._set_list_setting()

	path=property(_get_path,_set_path)
