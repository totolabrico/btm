import copy
import dill as pickle

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

class Navigator:

	def __init__(self,Machine):
		self.machine=Machine
		date = datetime.datetime.now()
		self.name="default"
		self._pointer_track=0
		self._pointer_setting=0
		self.key=Clavier(self)
		self.encoder=Encoder(self)
		self.menu_browser=Menu_browser(self.machine.partition,self,"browser")
		self._menu=Menu_main(self.machine.partition,self,"main")
		self.draw_oled=Draw_oled(self.menu)
		self.led_rgb=Led()
		self.led_rgb.turn_on("main")
		self.welcolme=True
		self.display = threading.Thread(target=self.draw_oled.run_draw(), args=())
		self.display.start()

	def _get_pointer_track(self):
		return self._pointer_track
	def _set_pointer_track(self,cmd):
		if cmd == "+" or cmd =="-":
			self._pointer_track=loopValue(cmd,self._track,1,len(self.machine.partition.tracks)-1,0)
		else:
			self._pointer_track=cmd

	def _get_pointer_setting(self):
		return self._pointer_setting
	def _set_pointer_setting(self,cmd):
		self._pointer_setting=cmd

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
			self._menu=self.menu_browser
		if cmd=="save":
			self._menu=Menu_save(self.machine.partition,self,cmd)
		if cmd=="load":
			self._menu=Menu_load(self.machine.partition,self,cmd)

		self.led_rgb.turn_on(cmd)

	def analyse_cmd(self,cmd):
		if self.welcolme==True:
			self.welcolme=False
		else:
			self.menu.analyse(cmd)
			self.menu.draw_menu.set_draw()
			if self.menu.name=="tracks" or self.menu.name=="notes":
				self.menu.draw_menu_editor.set_draw()
			self.draw_oled.set_menu(self.menu)

	def save_set(self):

		path="/home/pi/btm/saves/"+self.name+"/partition"
		with open(path,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump(self.machine.partition)
		self.machine.partition.name=self.name

	def load_set(self,Name):
		path="/home/pi/btm/saves/"+Name+"/partition"
		with open(path,'rb') as fichier:
			mon_depickler=pickle.Unpickler(fichier)
			self.machine.partition=mon_depickler.load()
			self.machine.partition.check_save_folder()
			self.machine.partition.save()
			self.machine.partition.save_tracks()
		self.re_init()

	def re_init(self):
		self.name=self.machine.partition.name
		self.menu_browser=Menu_browser(self.machine.partition,self,"browser")
		self.menu="main"

	menu=property(_get_menu,_set_menu)
	pointer_track=property(_get_pointer_track,_set_pointer_track)
	pointer_setting=property(_get_pointer_setting,_set_pointer_setting)
