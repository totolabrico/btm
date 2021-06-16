from osc import*
from settings import*
from cmd import*
import copy
import dill as pickle

class Partition():

	def __init__(self,Machine):
		self.machine=Machine
		self.nb_track=30
		self.nb_note=16
		#self.sequencer=self.init_sequencer()
		self.master=self.init_master()
		self.tracks=self.init_tracks()
		self.init_osc()
		#self.load_set(self.path+self.name)


	def init_sequencer(self):
		setting=sequencer_setting.copy()
		return setting
		
	def init_master(self):
		setting=sequencer_setting.copy()
		audio=copy.deepcopy(audio_setting)
		del audio[3]
		for element in audio:
			setting.append(element)
		return setting
		
	def init_tracks(self):
		titles=["notes","file","loop","audio"]
		list=[self.init_notes(),copy.deepcopy(sample_setting),copy.deepcopy(time_setting),copy.deepcopy(audio_setting)]
		setting=[]
		i=0
		while i<self.nb_track:
			setting.append(self.init_element(titles,list))
			i+=1
		return setting
		
		
	def init_notes(self):
		setting=[]
		i=0
		while i<self.nb_note:
			setting.append(self.init_note())
			i+=1
		return setting
		
	def init_note(self):
		titles=["audio","file"]
		list=[copy.deepcopy(audio_setting),copy.deepcopy(sample_setting)]
		del list[1][0]
		list[0][0][1]=0
		return self.init_element(titles,list)

	def init_element(self,Titles,List):
		setting=[]
		i=0
		while i<len(List):
			setting.append([])
			setting[i].append(Titles[i])
			setting[i].append(copy.deepcopy(List[i]))
			i+=1
		return setting
	
	def init_osc(self):
		#self.osc("master",self.sequencer)
		self.osc("master",self.master)
		self.osc_track()

	def osc_track(self):
		Id=0
		for track in self.tracks:
			for element in track:
				if element[0]=="notes":
					self.osc_note(element[1],Id)
				else:
					self.osc("track",element[1],Id)
			osc_send("track","loop_length",self.nb_note,Id) # envoi de la longueur initial d'une partition (bricolage)
			Id+=1
				
	def osc_note(self,List,Idtrack):
		i=0
		for element in List:
			for parameter in element:
				self.osc("note",parameter[1],Idtrack,i)
			i+=1

	def osc(self,Addr,List,Idtrack=0,Idnote=0):
		# print("part send osc",Name,List)
		for element in List:
			osc_send(Addr,element[0],element[1],Idtrack,Idnote)
			
	def save_set(self,Path):
		print("save set")
		with open(Path,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump([self.master,self.tracks])

	def load_set(self,Path):
		with open(Path,'rb') as fichier:
			mon_depickler=pickle.Unpickler(fichier)
			save=mon_depickler.load()
			#self.sequencer=save[0].copy()
			self.master=save[0]
			self.tracks=save[1]
		self.init_osc()
		print("loaded",Path)

