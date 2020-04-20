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
		self._set_list()
		print("path:",self._path)
		
	def _set_list(self):
		self._list=[]
		for element in os.listdir(self._path):
			if element[:1]!=".":
				self._list.append(element)

	def analyse(self,button):
		Menu.analyse(self,button)
		
		if button=="back":
			self.finish_draw=True
			self.navigator.menu="track"
		elif button=="edit":
			if self._list[self.pointer][-4:].lower()==".wav":
				self.partition.tracks[self.navigator.track].sample=self.path+self._list[self.pointer]
				self.finish_draw=True
				self.navigator.menu="track"
			
		elif button=="left":
			to=self.path[:-1]
			letter=to[-1:]
			while letter!= "/":
				to=to[:-1]
				letter=to[-1:]
			print("road:",len(to))	
			if len(to)>=9:# pour ne pas remonter plus haut que /home/pi/
				self.path=to
				self._set_list()
				self.pointer=0
				
		elif button=="right":
			to=self._path+self._list[self.pointer]
			print("right:",to)
			if os.path.isdir(to)==True:
				self.path=to+"/"
				self._set_list()
				self.pointer=0
		
	path=property(_get_path,_set_path)
