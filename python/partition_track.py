from partition_notes import*
from basic_function import*
from osc import*
import pickle
import copy


class Partition_track:


	def __init__(self,Machine,id,*args):

		self.machine=Machine
		self.setting=[
		["id",id],#0
		["sample","empty"],#1
		["vol",0.5], # 2 volume
		["pan",0], # 3 panning
		["mute",False], # 4 mute
		["solo",False], # 5 solo
		["mesure",self.machine.partition.mesure], # 6 nombre de mesures
		["name","empty"] # 7 mesure de départ
		#["length",0] # 7 durée de l'échantillon*
		]
		
		setting=args
		if type(setting)==list:
			for element_in in setting:
				for element in self.setting:
					if element_in[0]==element[0]:
						element[1]=element_in[1]
		
		
		self.sample_length=0
		self._notes=[]
		self.save()

	def _get_id(self):
		return self.setting[0][1]
	def _set_id(self,id):
		self.setting[0][1]=id
		self.save()

	def _get_sample(self):
		return self.setting[1][1]

	def _set_sample(self,Path):
		self.setting[1][1]=Path
		to=Path.split("/")
		to=to[len(to)-1]
		to=to[:-4]
		self.setting[7][1]=to
		self.save()

	def _get_name(self):
		return self.setting[7][1]
	def _set_name(self,cmd):
		if cmd=="-":
			self.setting[7][1]=self.setting[7][1][1:]
			self.save()

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
		inc,Max,Min=0.02,1,0
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

	def add_element(self,*args):
		self._notes.append(Partition_note(self,*args))
		self.save()

	def del_element(self,pas):
		print("remove_note",pas)
		for element in self.notes:
			if element.pas==pas:
				del element
		self.save()

	def paste_element(self,list,Pas):
					
		if len(list)>0:
			to=[]
			i=0
			while i<len(list):
				if list[i]!=0:
					list[i].pas+=Pas-list[i].pas+i
					to.append(list[i])
				i+=1
				
		for element in self.notes:
			for note in to:
				if element.pas==note.pas:
					print("pas_identique",element.pas)
					self.del_element(element.id)

		for note in to:
			self.add_note(note.setting)


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
		sendMessage("load","track_"+str(self.setting[0][1]))
		self.save_notes()

	def save_notes(self):
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/notes_"+str(self.setting[0][1])+".txt"
		myfile = open(path,"w")
		for element in self.notes:
			myfile.write("notes_"+str(self.setting[0][1])+" "+element.save()+";\n")
		myfile.close()
		sendMessage("load","notes_"+str(self.setting[0][1]))

	def erase_files(self):
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/track_"+str(self.setting[0][1])+".txt"
		os.remove(path)
		path="/home/pi/btm/saves/"+self.machine.partition.name+"/notes_"+str(self.setting[0][1])+".txt"
		os.remove(path)


	sample=property(_get_sample,_set_sample)
	name=property(_get_name,_set_name)
	#sample_length=property(_get_sample_length,_set_sample_length)
	id=property(_get_id,_set_id)
	vol=property(_get_vol,_set_vol)
	pan=property(_get_pan,_set_pan)
	mute=property(_get_mute,_set_mute)
	solo=property(_get_solo,_set_solo)
	mesure=property(_get_mesure,_set_mesure)
	notes=property(_get_notes,_set_notes)
