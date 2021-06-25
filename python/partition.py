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
		self.master=self.init_master()
		self.tracks=self.init_tracks()
		self.init_osc()
		#self.load_set("/home/pi/btm/saves/last")
	def init_master(self):
		setting=sequencer_setting.copy()
		audio=copy.deepcopy(audio_setting)
		del audio[3]
		for element in audio:
			setting.append(element)
		return setting
		
	def init_tracks(self):
		setting=[]
		i=0
		while i<self.nb_track:
			setting.append(self.init_track())
			i+=1
		return setting
		
	def init_track(self):
		titles=["notes","file","loop","audio"]
		list=[self.init_notes(),copy.deepcopy(sample_setting),copy.deepcopy(time_setting),copy.deepcopy(audio_setting)]
		return self.init_element(titles,list)
			
	def erase_track(self,Id):
		self.tracks[Id]=self.init_track()
		self.osc_track(Id)
		
	def erase_note(self,Idtrack,Id):
		print(self.tracks[Idtrack][0][1][Id])
		self.tracks[Idtrack][0][1][Id]=self.init_note()
		self.osc_note(self.tracks[Idtrack][0][1],Idtrack)
				
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
		self.osc("master",self.master)
		Id=0
		while Id<len(self.tracks):	
			self.osc_track(Id)
			Id+=1

	def osc_track(self,Id):	
		osc_send("track","loop_length",self.nb_note,Id) # envoi de la longueur initial d'une partition (bricolage)
		for element in self.tracks[Id]:
			if element[0]=="notes":
				self.osc_note(element[1],Id)
			else:
				self.osc("track",element[1],Id)
				
	def osc_note(self,List,Idtrack): #fonction appelée une fois par track
		n=0
		keys=[]
		values=[]
		for note in List:
			s=0
			for div in note: # div : file et audio
				for subdiv in div: # setting : div key et values
					if type(subdiv)!=str:
						for setting in subdiv: # chacun des settings, tout propre
							if n==0: # pour la premiere note
								keys.append(setting[0]) 
								values.append([])
							values[s].append(setting[1])
							s+=1
							#print(Idtrack,n,setting[0],setting[1])
			n+=1

		i=0
		#print(len(keys))
		while i<len(keys):
			osc_send("note",keys[i],values[i],Idtrack)
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
			#print(save[0])
			self.master=[save[0]]
			self.tracks=save[1].copy()
		self.init_osc()
		print("loaded",Path)

