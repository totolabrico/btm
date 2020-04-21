import datetime
import copy
from clavier import*
from encoder import*
from partition_main import*
from menu_main import*
from menu_tracks import*
from menu_track import*
from menu_notes import*
from menu_browser import*
from menu_save import*
from menu_load import*

from draw_oled import*
from led_rgb import *


import dill as pickle


save="save"

class Navigator:

	def __init__(self,Machine):
		self.machine=Machine
		date = datetime.datetime.now()
		self.name=str(date.day)+"-"+str(date.month)+"_"+str(date.hour)+":"+str(date.minute)
		self._track=0
		self._setting=0
		self.key=Clavier(self)
		self.encoder=Encoder(self)
		self._menu=Menu_main(self.machine.partition,self,"main")
		self.draw_oled=Draw_oled(self.menu)
		self.led_rgb=Led()
		self.led_rgb.turn_on("main")
		self.display = threading.Thread(target=self.draw_oled.run_draw(), args=())
		self.display.start()
        
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
			self._menu=Menu_main(self.machine.partition,self,cmd)
		if cmd=="tracks":
			self._menu=Menu_tracks(self.machine.partition,self,cmd)
		if cmd=="track":
			self._menu=Menu_track(self.machine.partition,self,cmd)
		if cmd=="notes":
			self._menu=Menu_notes(self.machine.partition,self,cmd)
		if cmd=="browser":
			self._menu=Menu_browser(self.machine.partition,self,cmd)
		if cmd=="save":
			self._menu=Menu_save(self.machine.partition,self,cmd)
		if cmd=="load":
			self._menu=Menu_load(self.machine.partition,self,cmd)
			
		self.led_rgb.turn_on(cmd)
		
	def analyse_cmd(self,button):
		self.menu.analyse(button)
		self.menu.draw_menu.set_draw()
		self.draw_oled.set_menu(self.menu)

	def save_set(self):
		path="/home/pi/btm/saves/"+self.name+"/partition"
		with open(path,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump(self.machine.partition)

	def load_set(self,Name):
		path="/home/pi/btm/saves/"+Name+"/partition"
		with open(path,'rb') as fichier:
			mon_depickler=pickle.Unpickler(fichier)
			self.machine.partition=mon_depickler.load()
			self.machine.partition.check_save_folder()
			self.machine.partition.save()
			self.machine.partition.save_tracks()

	menu=property(_get_menu,_set_menu)
	track=property(_get_track,_set_track)
	setting=property(_get_setting,_set_setting)
	

