from basic_function import*
from partition_track import *
import threading
import pickle

class Partition_main:

	def __init__(self,Machine,Name):
		self.machine=Machine

		self.setting=[
		["name",Name],#0
		["playing",False],#1
		["bpm",120],#2
		["master",0.5],#3
		["temps",4],#4
		["mesure",4],#5
		["nb_tracks",0],#5
		]

		self.tracks=[]
		self.check_save_folder()
		self.save()

	def _get_name(self):
		return self.setting[0][1]
	def _set_name(self,cmd):
		#self.setting[0][1]=cmd
		self.save()

	def _get_playing(self):
		return self.setting[1][1]
	def _set_playing(self,cmd):
		if cmd=="-":
			self.setting[1][1]=False
		elif cmd=="+":
			self.setting[1][1]=True
		self.save()

	def _get_bpm(self):
		return self.setting[2][1]
	def _set_bpm(self,cmd):
		setting=2
		inc,Max,Min=1,300,40
		self.edit_setting(setting,cmd,inc,Max,Min)

	def _get_master(self):
		return self.setting[3][1]
	def _set_master(self,cmd):
		setting=3
		inc,Max,Min=0.1,2,0
		self.edit_setting(setting,cmd,inc,Max,Min)


	def _get_temps(self):
		return self.setting[4][1]
	def _set_temps(self,cmd):
		setting=4
		inc,Max,Min=1,10,1
		self.edit_setting(setting,cmd,inc,Max,Min)
		
	def _get_mesure(self):
		return self.setting[5][1]
	def _set_mesure(self,cmd):
		setting=5
		inc,Max,Min=1,32,1
		self.edit_setting(setting,cmd,inc,Max,Min)

	def get_tracks_length(self):
		return len(self.tracks)

	def get_track(self,Id):
		return str(self.tracks[Id].Id)+":"+self.tracks[Id].sample

	def add_track(self):
		id_track=len(self.tracks)+1
		self.tracks.append(Partition_track(self.machine,id_track))
		self.setting[6][1]+=1
		self.save()

	def edit_setting(self,setting,cmd,inc,Max,Min):
		value=self.setting[setting][1]
		if type(value)==bool:
			to=boolValue(cmd)
		else:
			to=limitValue(cmd,value,inc,Max,Min)
		self.setting[setting][1]=to
		self.save()

	def save(self):		
		path="/home/pi/btm/saves/"+self.setting[0][1]+"/main.txt"	
		myfile = open(path,"w")
		i=0
		while i<len(self.setting):
			myfile.write("main "+self.setting[i][0]+" "+to_string(True,self.setting[i][1])+";\n")
			i+=1
		myfile.close()
		sendMessage("load","main")
		
	def load(self,path):
		path="/home/pi/btm/saves/"+self.setting[0][1]+"/main.txt"	
		myfile = open(path,"r")
		i=0
		while i<len(self.setting):
			myfile.read()# icicicicici
			i+=1
		myfile.close()
		sendMessage("load","main")
		
	def check_save_folder(self):
		path="/home/pi/btm/saves/"+self.setting[0][1]
		if self.setting[0][1]=="default":	
			if os.path.exists(path)==True:
				erase_list=os.listdir(path)
				for element in erase_list:
					os.remove(path+"/"+element)
				os.rmdir(path)
			os.makedirs(path, exist_ok=True)
		elif os.path.exists(path)==False:
			os.makedirs(path, exist_ok=True)
		sendMessage("path",path)
		

	name = property(_get_name, _set_name)
	bpm = property(_get_bpm, _set_bpm)
	master = property(_get_master, _set_master)
	playing = property(_get_playing, _set_playing)
	temps = property(_get_temps, _set_temps)
	mesure = property(_get_mesure, _set_mesure)