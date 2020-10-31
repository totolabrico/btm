from osc import*

menu_names=["master","track","notes"] # pour osc

sequencer_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["play",False],
	["bpm",120,0,300,0.5],
	["temps",4,1,8,1]

	]

track_setting=[
    ["sample","empty"]
    ]

time_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["mesure",8,1,64,1],
	["begin",0,0,64,1],
	["end",8*4,1,64,1],
	["loop",True]
	]

audio_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["vol",0,0,2,0.02],
	["mute",False],
	["solo",False],
	["pan",0,-1,1,0.02],
	["pitch",0,-3,3,0.02],
	["tone",0,-3,3,0.02],
	["s_begin",0,0,1,0.02],
	["s_end",0,0,1,0.02],
	["lpf",0,0,20000,10],#low pass filter
	["hpf",20000,0,20000,10],#high pass filter
	]

class Partition():

	def __init__(self):
		global master_setting
		self.nb_track=30
		self.nb_note=32
		self.master_setting=[]
		self.track_setting=[]
		self.note_setting=[]
		self.init_master()
		self.init_track()
		self.init_note()
		self.osc_init()

		
	def init_master(self): # initialisation de la partition master : liste 2d
		for element in sequencer_setting:			
			self.master_setting.append(element.copy())
		for element in time_setting:			
			self.master_setting.append(element.copy())
		for element in audio_setting:			
			self.master_setting.append(element.copy())
					
	def init_track(self): # initialisation de la partition tracks : liste 3d
		i=0
		while (i<self.nb_track):
			self.track_setting.append([])
			for element in track_setting:			
				self.track_setting[i].append(element.copy())
			for element in audio_setting:			
				self.track_setting[i].append(element.copy())
			for element in time_setting:			
				self.track_setting[i].append(element.copy())
			i+=1
			
	def init_note(self): # initialisation de la partition notes : liste 4d
		i=0
		while (i<self.nb_track):
			j=0
			self.note_setting.append([])
			while (j<self.nb_note):
				self.note_setting[i].append([])
				for element in audio_setting:			
					self.note_setting[i][j].append(element.copy())
				j+=1
			i+=1
		
	def edit(self,cmd,setting,menu_id,track_id,note_id):
	
		print ("edit: ",setting[1])
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
			
		elif type(value)==str:
			value=cmd
		
		setting[1]=value
		
		osc_send(menu_names[menu_id],setting[0],setting[1],track_id,note_id)


	
	def osc_init(self):
		for element in self.master_setting:
			osc_send(menu_names[0],element[0],element[1])
		
		track_id=0
		for element in self.track_setting:
			for track in element:
				osc_send(menu_names[1],track[0],track[1],track_id)
			track_id+=1
			
		track_id=0
		for element in self.note_setting:
			note_id=0
			for track in element:
				for note in track:
					osc_send(menu_names[2],note[0],note[1],track_id,note_id)
				note_id+=1
			track_id+=1
	
