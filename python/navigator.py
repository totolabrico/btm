from clavier import*
from partition_main import*
#from menu import*
from menu_main import*
from menu_tracks import*
from menu_track import*
from menu_notes import*
from menu_browser import*
import pickle


class Navigator:

	def __init__(self,Machine):
		self.machine=Machine
		self.partition=Partition_main(self)
		self._menu=Menu_main(self,"main")
		self._track=0
		self._setting=0
		self.key=Clavier(self)
		
	def _get_track(self):
		return self._track
	def _set_track(self,cmd):
		self._track=cmd
		
	def _get_setting(self):
		return self._setting
	def _set_setting(self,cmd):
		self._setting=cmd
				
	def _get_menu(self):
		return self._menu
	def _set_menu(self,cmd):
		if cmd=="main":
			self._menu=Menu_main(self,cmd)
		if cmd=="tracks":
			self._menu=Menu_tracks(self,cmd)
		if cmd=="track":
			self._menu=Menu_track(self,cmd)
		if cmd=="notes":
			self._menu=Menu_notes(self,cmd)
		if cmd=="browser":
			self._menu=Menu_browser(self,cmd)
			
	def save_set(self):
		path="/home/pi/btm/saves/python/"+self.partition.name
		with open(name,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump(self.partition)

	def analyse_cmd(self,button):
		self._menu.analyse(button)
		self.save_set()

	menu=property(_get_menu,_set_menu)
	track=property(_get_track,_set_track)
	setting=property(_get_setting,_set_setting)
