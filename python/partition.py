from osc import*


sequencer_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["play",True],
	["bpm",120,0,300,0.5]
	]
	
time_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["temps",4,1,8,1],
	["mesure",8,1,64,1],
	["begin",0,0,64,1],
	["end",8*4,1,64,1],
	["loop",True]
	]

track_setting=[
    ["sample","empty"]
    ]

audio_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["vol",0.5,0,2,0.02],
	["mute",False],
	["solo",False],
	["pan",0,-1,1,0.02],
	["pitch",0,-10,10,0.02],
	["tone",0,-10,10,0.02],
	["s_begin",0,0,1,0.02],
	["s_end",1,0,1,0.02],
	["lpf",0,0,20000,10],#low pass filter
	["hpf",20000,0,20000,10],#high pass filter
	]


class Partition():

	def __init__(self,Machine):
		self.machine=Machine
		self.nb_track=30
		self.nb_note=16
		self.master_setting={}
		self.track_setting=[]
		self.note_setting=[]
		self.init_master()
		self.init_track()
		self.init_note()
		self.osc_init()

		
	def init_master(self): # initialisation de la partition master : liste 2d
		list_array=[sequencer_setting,audio_setting]
		self.init_dict(self.master_setting,list_array)
		
	def init_track(self): # initialisation de la partition tracks : liste 3d
		list_array=[track_setting,audio_setting,time_setting]
		i=0
		while (i<self.nb_track):
			self.track_setting.append({})
			self.init_dict(self.track_setting[i],list_array)
			i+=1
	
	def init_note(self): # initialisation de la partition notes : liste 4d
		list_array=[audio_setting]
		i=0
		while (i<self.nb_track):
			j=0
			self.note_setting.append([])
			while (j<self.nb_note):
				self.note_setting[i].append({})
				self.init_dict(self.note_setting[i][j],list_array)
				self.note_setting[i][j]["vol"][1]=0
				j+=1
			i+=1
					
	def init_dict(self,Dict,List_array):
		id=0
		for array in List_array:
			for element in array:
				Dict[element[0]]=[id]
				i=1
				while i<len(element):
					Dict[element[0]].append(element[i])
					i+=1
				id+=1
					
		
	def edit(self,cmd,key,setting,editor_name,track_id,note_id):
		print ("edit: ",cmd,setting)
		value=setting[1]
	
		if type(value)==bool:
			if cmd=="-":
				value=False
			elif cmd=="+":
				value=True
			elif cmd=="*":
				value= not value

		elif type(value)==int or type(value)==float:
			min=setting[2]
			max=setting[3]
			inc=setting[4]
			if cmd=="-":
				value-=inc
			elif cmd=="+":
				value+=inc
			if value>max:
				value=max
			elif value<min:
				value=min
			value=round(value,2)
			if key=="temps" or key=="mesure":
				 self.compute_length(key,setting)
			
		elif type(value)==str:
			value=cmd			
		
		setting[1]=value
		osc_send(editor_name,key,setting[1],track_id,note_id)

	def compute_length(self,Key,Setting):
		print("compute length =>",Key,Setting[1])

	
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
	
	
