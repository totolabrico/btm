from osc import*
from settings import*
from cmd import*
import copy
import dill as pickle
import time
class Partition():

	def __init__(self,Machine):
		self.machine=Machine
		self.nb_track=30
		self.nb_note=16
		self.master=self.init_master()
		self.tracks=self.init_tracks()
		self.init_osc()
		#self.load_set("/home/pi/btm/saves/last")	
		self.nb_tick=self.set_nb_tick()
		self.track_copy=[]
		self.note_copy=[]
		self.backup=None

	def init_master(self):
		setting=sequencer_setting.copy()
		audio=copy.deepcopy(audio_setting)
		del audio[3]
		for element in audio:
			setting.append(element)
		return setting

	def set_nb_tick(self):
		tick=1
		for element in self.tracks:
			begin=element[2][1][2][1]
			end=element[2][1][3][1]
			nbnote=element[2][1][0][1]*element[2][1][1][1]
			l=get_loop_length(begin-1,end,nbnote)
				
			if tick%l==0:
				pass
			elif l%tick==0:
				tick=l
			else:
				tick=tick*l
		#print("nbtick",tick)
		osc_send("master","nb_tick",tick)
		#self.nb_tick=tick
		return tick
				
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
				
	def copy_track(self,Ids):
		print("copy track")
		self.track_copy=[]
		for id in Ids:
			self.track_copy.append([id,self.tracks[id]])
		
	def paste_track(self,Pointer):
		print("paste track")
		if len(self.track_copy)>0:
			first=find_first(self.track_copy)
			for element in self.track_copy:
				#newId=element[0]-first+Pointer
				newId=get_paste_id(element[0],first,self.nb_track,Pointer)
				self.tracks[newId]=copy.deepcopy(element[1])
				self.osc_track(newId)
	
	def erase_track(self,Ids):
		for id in Ids:
			self.tracks[id]=self.init_track()
			self.osc_track(id)
	
	def copy_note(self,Idtrack,Ids):
		self.note_copy=[]
		for id in Ids:
			self.note_copy.append([id,copy.deepcopy(self.tracks[Idtrack][0][1][id])])
	def paste_note(self,Idtrack,Pointer):
		if len(self.note_copy)>0:
			first=find_first(self.note_copy)
			for element in self.note_copy:
				#newId=element[0]-first+Pointer
				newId=get_paste_id(element[0],first,len(self.tracks[Idtrack][0][1]),Pointer)
				self.tracks[Idtrack][0][1][newId]=copy.deepcopy(element[1])
			self.osc_note(self.tracks[Idtrack][0][1],Idtrack)
		
	def erase_note(self,Idtrack,Ids):
		for id in Ids:
			self.tracks[Idtrack][0][1][id]=self.init_note()
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
		osc_send("master","play",False)
		time.sleep(0.1)
		self.osc("master",self.master)
		#print(self.master)
		Id=0
		while Id<len(self.tracks):	
			self.osc_track(Id)
			time.sleep(0.1)
			Id+=1
		osc_send("master","play",True)

	def osc_track(self,Id):	
		for element in self.tracks[Id]:
			if element[0]!="notes":
				self.osc("track",element[1],Id)
		for element in self.tracks[Id]:
			if element[0]=="notes":
				self.osc_note(element[1],Id)
				self.set_loop_length(Id)
		
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
		#print("part send osc",Addr,List)
		for element in List:
			osc_send(Addr,element[0],element[1],Idtrack,Idnote)
						
	def set_sample(self,Id,Path):
		self.tracks[Id][1][1][0][1]=Path
		osc_send("track","sample",Path,Id)
			
	def set_notes_length(self,Id,Length):
		dif=Length-len(self.tracks[Id][0][1])
		if dif<0:
			self.del_notes(Id,abs(dif))
			self.set_begin_end(Id,Length,"-")
		elif dif>0:
			self.set_begin_end(Id,Length,"+")
			self.add_notes(Id,dif)

	def del_notes(self,Id,Dif):
		i=0
		while i<Dif:
			del self.tracks[Id][0][1][-1]
			i+=1
			
	def add_notes(self,Id,Dif):
		i=0
		while i<Dif:
			self.tracks[Id][0][1].append(self.init_note())
			i+=1
		self.osc_note(self.tracks[Id][0][1],Id)
		
	def set_begin_end(self,Id,Length,Cmd):
		p=self.tracks[Id][2][1]
		if Cmd=="+":
			p[3]=edit(Length,p[3])#end
		if Cmd=="-":
			if p[2][1]>Length: #begin
				p[2]=edit(0,p[2])
			if p[3][1]>Length: #end
				p[3]=edit(Length,p[3])
		#self.send_osc("begin",p[2][1])
		osc_send("track","begin",p[2][1],Id)

		self.tracks[Id][2][1]=p
		self.set_loop_length(Id)
				
	def set_loop_length(self,Id):
		p=self.tracks[Id][2][1]
		begin=p[2][1]
		end=p[3][1]
		nbnote=p[0][1]*p[1][1]
		if begin>nbnote:
			p[2][1]=nbnote
		if end>nbnote:
			p[3][1]=nbnote
		self.tracks[Id][2][1]=p
		
		loop_length=get_loop_length(begin-1,end,nbnote)
		#print(loop_length)
		self.set_nb_tick()
		osc_send("track","loop_length",loop_length,Id)

	def save_set(self,Path):
		print("save set")
		with open(Path,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump([self.master,self.tracks])

	def load_set(self,Path):
		with open(Path,'rb') as fichier:
			mon_depickler=pickle.Unpickler(fichier)
			save=mon_depickler.load()
			#print(save[0][0])
			self.master=save[0].copy()
			#self.master.Editor.set_list()
			self.tracks=save[1].copy()
		self.init_osc()
		print("loaded",Path)
		
	def save_backup(self):
		self.backup=copy.deepcopy(self.tracks)
	def load_backup(self):
		if self.backup!=None:
			self.tracks=copy.deepcopy(self.backup)
			self.init_osc()

