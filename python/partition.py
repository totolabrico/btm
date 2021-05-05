from osc import*
from settings import*
from cmd import*
import copy

class Partition():

	def __init__(self,Machine):
		self.machine=Machine
		self.name="set"
		self.nb_track=30
		self.nb_note=16
		self.sequencer=self.init_sequencer()
		self.master=self.init_master()
		self.tracks=self.init_tracks()

	def init_sequencer(self):
		setting=sequencer_setting.copy()
		self.osc("master",setting)
		return setting
		
	def init_master(self):
		setting=copy.deepcopy(audio_setting)
		del setting[3]
		self.osc("master",setting)
		return setting
		
	def init_tracks(self):
		titles=["notes","file","loop","audio"]
		list=[self.init_notes(),copy.deepcopy(sample_setting),copy.deepcopy(time_setting),copy.deepcopy(audio_setting)]
		setting=[]
		i=0
		while i<self.nb_track:
			setting.append(self.init_element(titles,list))
			self.osc_track(setting[i],i)
			i+=1
		return setting
		
	def init_notes(self):
		titles=["audio","file"]
		list=[copy.deepcopy(audio_setting),copy.deepcopy(sample_setting)]
		del list[1][0]
		list[0][0][1]=0
		
		setting=[]
		i=0
		while i<self.nb_note:
			setting.append(self.init_element(titles,list))
			i+=1
		return setting

	def init_element(self,Titles,List):
		setting=[]
		i=0
		while i<len(List):
			setting.append([])
			setting[i].append(Titles[i])
			setting[i].append(copy.deepcopy(List[i]))
			i+=1
		return setting
	
	def osc_track(self,List,Id):
		for element in List:
			if element[0]=="notes":
				self.osc_note(element[1],Id)
			else:
				self.osc("track",element[1],Id)
				
	def osc_note(self,List,Idtrack):
		i=0
		for element in List:
			for parameter in element:
				self.osc("note",parameter[1],Idtrack,i)
			i+=1

	def osc(self,Addr,List,Idtrack=0,Idnote=0):
		#print("part send osc",Name,List)
		for element in List:
			osc_send(Addr,element[0],element[1],Idtrack,Idnote)
		
