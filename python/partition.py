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
		self.sequencer=sequencer_setting.copy()
		self.master=self.init_master()
		self.tracks=self.init_tracks()

	def init_master(self):
		setting=copy.deepcopy(audio_setting)
		del setting[3]
		return setting
		
	def init_tracks(self):
		titles=["part","sample","loop","audio"]
		setting=[]
		i=0
		while i<self.nb_track:
			list=[[],copy.deepcopy(sample_setting),copy.deepcopy(time_setting),copy.deepcopy(audio_setting)]
			setting.append([])
			j=0
			while j<len(list):
				setting[i].append([])
				setting[i][j].append(titles[j])
				setting[i][j].append(list[j])
				j+=1
			i+=1
		return setting

	
	'''
		self.track_setting=[]
		self.note_setting=[]
		self.init_master()
		self.init_track()
		self.init_note()
		self.osc_init()
	

	
	def init_track(self): # initialisation de la partition tracks : liste 3d
		list_array=[track_setting,audio_setting,time_setting]
		i=0
		while (i<self.nb_track):
			self.track_setting.append({})
			self.init_list(self.track_setting[i],list_array)
			i+=1
	
	def init_note(self): # initialisation de la partition notes : liste 4d
		list_array=[audio_setting]
		i=0
		while (i<self.nb_track):
			j=0
			self.note_setting.append([])
			while (j<self.nb_note):
				self.note_setting[i].append({})
				self.init_list(self.note_setting[i][j],list_array)
				self.note_setting[i][j]["vol"][1]=0
				j+=1
			i+=1
					
	def init_list(self,List,List_array):
		id=0
		for array in List_array:
			for element in array:
				List[element[0]]=List[element[1]]
				i=1
				while i<len(element):
					Dict[element[0]].append(element[i])
					i+=1
				id+=1
				
	def osc_init(self):
		for key,element in self.master_setting.items():
			osc_send("master",key,element[1])
		
		track_id=0
		for track in self.track_setting:
			for key,element in track.items():
				osc_send("track",key,element[1],track_id)
			track_id+=1
			
		track_id=0
		for track in self.note_setting:
			note_id=0
			for note in track:
				for key,element in note.items():
					osc_send("note",key,element[1],track_id,note_id)
				note_id+=1
			track_id+=1
			
	#osc_send(editor_name,key,setting[1],track_id,note_id)

	'''			
