from partition import*
from partition_track import *

class Partition_main():

	def __init__(self,Machine):
		self.machine=Machine

		self.setting=[
		# 0:name / 1:value / 2:min / 3:max / 4:inc
		["name","default"],#0
		["playing",False],#1
		["bpm",120,0,300,0.5],#2
		["master",0.5,0,2,0.02],#3
		["temps",4,1,8,1],#4
		["mesure",8,1,64,1],#5
		["nb_tracks",0,0,30,1],#6
		]

		self.check_save_folder()
		self.save()

	def _get_name(self):
		return self.setting[0][1]
	def _set_name(self,cmd):
		self.setting[0][1]=cmd
		self.check_save_folder()
		self.save()
		self.save_tracks()

	def get_tracks_length(self):
		return len(self.tracks)

	def get_track(self,id):
		return str(self.tracks[id].id)+":"+self.tracks[id].sample


	def save(self):
		path="/home/pi/btm/saves/"+self.name+"/main.txt"
		myfile = open(path,"w")
		i=0
		while i<len(self.setting):
			myfile.write("main "+self.setting[i][0]+" "+to_string(True,self.setting[i][1])+";\n")
			i+=1
		myfile.close()
		sendMessage("load","main")

	def save_tracks(self):
		i=0
		while i<len(self.tracks):
			self.tracks[i].save()
			i+=1

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
