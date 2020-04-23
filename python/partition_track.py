from partition_notes import*
from basic_function import*
from osc import*
import pickle


class Partition_track:


	def __init__(self,Machine,Id):

		self.machine=Machine
		self.setting=[
		["id",Id],#0
		["sample","empty"],#1
		["vol",0.5], # 2 volume
		["pan",0], # 3 panning
		["mute",False], # 4 mute
		["solo",False], # 5 solo
		["mesure",self.machine.partition.mesure], # 5 nombre de mesures
		["begin",0] # 6 mesure de départ
		]
		self.sample_name="empty"
		self.sample_length=0
		self._notes=[]
		self.save()

	def _get_id(self):
		return self.setting[0][1]
	def _set_id(self,Id):
		self.setting[0][1]=Id
		self.save()

	def _get_sample(self):
		return self.sample_name
	def _set_sample(self,name):
		self.setting[1][1]=name
		to=name.split("/")
		to=to[len(to)-1]
		to=to[:-4]
		self.sample_name=to
		self.save()


	def _get_sample_length(self):
		return 0 # un petit coup ici
	def _set_sample_length(self,cmd):
		print ("_set_sample_length:",cmd)


	def _get_mute(self):
		return self.setting[4][1]
	def _set_mute(self,cmd):
		setting=4
		self.edit_toggle(setting,cmd)

	def _get_solo(self):
		return self.setting[5][1]
	def _set_solo(self,cmd):
		setting=5
		self.edit_toggle(setting,cmd)

	def _get_mesure(self):
		return self.setting[6][1]
	def _set_mesure(self,cmd):
		setting=6
		inc,Max,Min=1,32,1
		self.edit_setting(setting,cmd,inc,Max,Min)

	def _get_vol(self):
		return self.setting[2][1]
	def _set_vol(self,cmd):
		setting=2
		inc,Max,Min=0.1,1,0
		self.edit_setting(setting,cmd,inc,Max,Min)

	def _get_pan(self):
		return self.setting[3][1]
	def _set_pan(self,cmd):
		setting=3
		inc,Max,Min=0.1,1,-1
		self.edit_setting(setting,cmd,inc,Max,Min)

	def _get_notes(self):
		return self._notes

	def _set_notes(self,*args):
		print ("partition_track / set_notes :cette fonction n'existe pas")
		return (0)
		
	def add_note(self,pas):
		Id=len(self._notes)
		self._notes.append(Partition_note(self,pas,Id))	
		self.save()
		
	def remove_note(self,removeId):
		del self._notes[removeId]
		i=0
		while i<len(self._notes):
			self._notes[i].Id=i
			i+=1
		self.save()
		
	def edit_setting(self,setting,cmd,inc,Max,Min):
		value=self.setting[setting][1]
		to=limitValue(cmd,value,inc,Max,Min)
		self.setting[setting][1]=to
		self.save()
	
	def edit_toggle(self,setting,cmd):
		value=self.setting[setting][1]
		to=boolValue(cmd)
		self.setting[setting][1]=to
		self.save()

	def save(self):
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/track_"+str(self.setting[0][1])+".txt"
		myfile = open(path,"w")
		for element in self.setting:
			myfile.write("track_"+str(self.setting[0][1])+" "+element[0]+" "+to_string(True,element[1])+";\n")
		myfile.close()			
		sendMessage("load","notes_"+str(self.setting[0][1]))		
		self.save_notes()
		
	def save_notes(self):
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/notes_"+str(self.setting[0][1])+".txt"
		myfile = open(path,"w")
		for element in self.notes:
			myfile.write("notes_"+str(self.setting[0][1])+" "+element.save()+";\n")
		myfile.close()
		sendMessage("load","track_"+str(self.setting[0][1]))

	def load_notes(self,Path):
		self._notes=[]
		path=Path+"/notes_"+str(self.setting[0][1])+".txt"
		myfile = open(path,"r")
		i=0
		for element in myfile:
			self._notes.append(Partition_note(self,0,i))
			self._notes[i].load(element)
			i+=1
		
	def erase(self):
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/track_"+str(self.setting[0][1])+".txt"
		os.remove(path)
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/notes_"+str(self.setting[0][1])+".txt"
		os.remove(path)

		
		"""
		path=Path+"/track_"+str(self.setting[0][1])+".txt"
		myfile = open(path,"r")
		for element in myfile:
			line=element.split(" ")
			setting=line[1]
			value=line[2][:-2]
			for element in self.setting:
				if element[0]==setting:
					element[1]=from_string(value,type(element[1]))
		self.load_notes(Path)
		"""
			
		
	sample=property(_get_sample,_set_sample)
	sample_length=property(_get_sample_length,_set_sample_length)
	Id=property(_get_id,_set_id)
	vol=property(_get_vol,_set_vol)
	pan=property(_get_pan,_set_pan)
	mute=property(_get_mute,_set_mute)
	solo=property(_get_solo,_set_solo)
	mesure=property(_get_mesure,_set_mesure)
	notes=property(_get_notes,_set_notes)
