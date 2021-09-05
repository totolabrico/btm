from menu import*
import copy
import threading

class MainMenu(Menu):

	def __init__(self,Navigator,Machine):
		Menu.__init__(self,Navigator)
		self.name="main"
		self.mom="main"
		self.list=["master","record","load","save","reset"]#,"import"]
		self.tools["grid"]=[2,3]
		self.machine=Machine
		self.recording=False
		
	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		if cmd=="enter":
			el=self.list[self.pointer]
			if el=="reset":
				print("exit")
				self.machine.new_open()
				self.machine.close()
			if el=="record":
				if self.recording==False:
					start_record(self.navigator.menus["save"].savename)
					self.recording=True
				elif self.recording==True:
					stop_record()
					self.recording=False

	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)
		
class SaveMenu(Menu,KeyMenu):

	def __init__(self,Navigator,Partition):
		Menu.__init__(self,Navigator)
		KeyMenu.__init__(self)
		self.partition=Partition
		self.name="save"
		self.mom="main"
		self.list=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","_","0","1","2","3","4","5","6","7","8","9"]
		self.tools["grid"]=[8,3]
		self.path="/home/pi/btm/saves/"

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		KeyMenu.sort(self,cmd,arg)
		if cmd=="enter" and self.savename!="":
			self.partition.save_set(self.path+self.savename)
			self.navigator.set_menu(self.mom)

	def draw(self):
		draw_title(self.name+": "+self.savename)
		KeyMenu.draw(self)
		draw_list(self.list,self.tools)

class LoadMenu(Menu):

	def __init__(self,Navigator,Partition):
		Menu.__init__(self,Navigator)
		Browser.__init__(self,"/home/pi/btm/saves/")
		self.partition=Partition
		self.name="load"
		self.mom="main"
		self.list=Browser.set_list(self)
		self.tools["grid"]=[1,3]

	def set_parameters(self):
		self.list=Browser.set_list(self)

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		if cmd=="enter":
			try:
				self.partition.load_set(self.path+self.list[self.pointer])
				self.navigator.menus["save"].savename=self.list[self.pointer]
				self.navigator.set_menu(self.mom)
			except:
				pass
		if cmd=="erase":
			try:
				os.system("rm "+self.path+self.list[self.pointer])
				self.set_parameters()
			except:
				pass
			
	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)
		
class PlayMenu(Menu): # inutilisé

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		self.name="play"
		self.mom="main"
		self.list=["master","tracks"]
		self.tools["grid"]=[2,3]

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

class MasterMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="master"
		self.mom="main"
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,Partition.master)
		
	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)
		if cmd=="enter":
			self.navigator.set_menu("tracks")
					
	def set_parameters(self):
		self.list=self.partition.master
		self.parameters=self.list	
			
	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("master",setting[0],setting[1])

class TracksMenu(Menu,Editor,Selector):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="tracks"
		self.mom="master"
		self.list=Partition.tracks
		self.tools["grid"]=[10,3]
		self.title=""
		Editor.__init__(self,Machine,Partition,self.get_parameters(Partition.tracks))
		Selector.__init__(self)

	def sort(self,cmd,arg):

		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)
		Selector.sort(self,cmd,arg)
		if self.selection==[]:
			ids=[self.pointer]
		else:
			ids=self.selection
		if cmd=="erase":
			self.partition.erase_track(ids)
		if cmd=="copy":
			self.partition.copy_track(ids)
		if cmd=="paste":
			self.partition.paste_track(self.pointer)
		if cmd=="enter":
			self.navigator.set_menu("track")
		else:
			self.set_parameters()
	
	def get_parameters(self,Tracks):
		parameters=[]
		for element in Tracks:
			parameters.append(element[3][1][2])
		return parameters
					
	def set_parameters(self):
		self.list=self.partition.tracks
		self.parameters=self.get_parameters(self.list)
		self.title=get_name(self.list[self.pointer][1][1][0][1])
		self.title=set_txt_size(self.title,10)
		
	def send_osc(self,id):
		setting=self.parameters[id]
		osc_send("track",setting[0],setting[1],id)
		
	def draw(self):
		draw_title("track "+str(self.pointer+1)+": "+self.title)
		draw_tracks(self.list,self.tools,self.selection)

class TrackMenu(Menu,Editor,Mom):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		Mom.__init__(self)
		self.name="track"
		self.mom="tracks"
		self.list=[]
		self.id=0
		self.title=""
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[])
			
	def set_parameters(self):
		self.id=self.navigator.menus["tracks"].pointer
		self.parameters=self.partition.tracks[self.id]
		self.title=get_name(self.parameters[1][1][0][1])		
		Mom.set_list(self)
		if self.title=="empty":
			self.pointer=1
			self.sort("enter","")
		
	def sort(self,cmd,arg):
		Mom.sort(self,cmd,arg)
		if cmd=="back":
			self.reset_pointer()
			
	def draw(self):
		draw_title(str(self.id+1)+": "+set_txt_size(self.title,15))
		draw_list(self.list,self.tools)

class ChildMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name=""
		self.mom=""
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[])

	def set_parameters(self,Name,Mom,Parameters):
		self.name=Name
		self.mom=Mom
		self.parameters=Parameters
		self.reset_pointer()
		if self.parameters[0][1]=="empty":
			self.sort("enter","")

	def sort(self,cmd,arg):
		parameter=self.parameters[self.pointer]
		if cmd=="enter" and parameter[0]=="sample":
			self.navigator.set_menu("sample")
			
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)
		
		trackid=self.navigator.menus["tracks"].pointer
		if parameter[0]=="temps" or parameter[0]=="mesure":
			l=self.parameters[0][1]*self.parameters[1][1]
			self.partition.set_notes_length(trackid,l)
		elif parameter[0]=="begin" or parameter[0]=="end":
			self.partition.set_loop_length(trackid)
					

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		id_track=self.navigator.menus["tracks"].pointer

		if self.mom=="track":
			osc_send("track",setting[0],setting[1],id_track)
		if self.mom=="note":
			id_note=self.navigator.menus["notes"].pointer
			osc_send("note",setting[0],setting[1],id_track,id_note)

class SampleMenu(Menu,Browser):

	def __init__(self,Navigator,Partition):
		self.partition=Partition
		Menu.__init__(self,Navigator)
		Browser.__init__(self,"/home/pi/audiosamples")
		self.name="sample"
		self.mom="child"
		self.list=Browser.set_list(self)
		self.tools["grid"]=[1,3]

	def sort(self,cmd,arg):
		is_wav=False
		try:
			is_wav=check_wav(self.list[self.pointer])
			samplepath=self.path+"/"+self.list[self.pointer]
		except:
			pass
		if cmd=="back":
			self.navigator.set_menu("tracks")
		elif cmd=="enter" and is_wav:
			self.play_sound(samplepath)
		elif cmd=="edit" and arg=="+" and is_wav:
			self.partition.set_sample(self.navigator.menus["tracks"].pointer,samplepath)
			self.navigator.set_menu("notes")
		else:
			Browser.sort(self,cmd,arg)
			
	def draw(self):
		draw_title(self.path[14:])
		draw_list(self.list,self.tools)

	def play_sound(self,Path):
		print("play the sound now",Path)
		player = threading.Thread(target=play_sound, args =(Path,),daemon=True)
		player.start()
		
	def set_sample(self,Path):
		self.navigator.menus["track"].set_sample(Path)
				
class NotesMenu(Menu,Editor,Selector):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="notes"
		self.mom="track"
		self.list=[]
		self.title=""
		Editor.__init__(self,Machine,Partition,[])
		Selector.__init__(self)
		
	def sort(self,cmd,arg):
		Editor.sort(self,cmd,arg)
		if self.selection==[]:
			ids=[self.pointer]
		else:
			ids=self.selection
		if cmd=="erase":
			self.partition.erase_note(self.idtrack,ids)
			self.set_parameters()
		if cmd=="copy":
			self.partition.copy_note(self.idtrack,ids)
		if cmd=="paste":
			self.partition.paste_note(self.idtrack,self.pointer)
			self.set_parameters()

		if cmd=="enter":
			self.navigator.set_menu("note")
		
		elif cmd=="back":
			self.navigator.set_menu(self.mom)
			self.reset_pointer()
			self.selection=[]
		else:
			Menu.sort(self,cmd,arg)
			Selector.sort(self,cmd,arg)
			self.set_title()
			
	def set_parameters(self):
		self.idtrack=self.navigator.menus["tracks"].pointer
		track=self.partition.tracks[self.idtrack]
		self.list=track[0][1]
		self.parameters=[]
		for element in self.list:
			self.parameters.append(element[0][1][0])
		temps=track[2][1][1][1]
		coef=4
		while temps*coef>16:
			coef-=1
		self.tools["grid"]=[temps*coef,3]
		self.tools["temps"]=temps
		self.tools["beg_end"]=[track[2][1][2][1],track[2][1][3][1]]
		self.set_title()
		#self.reset_pointer()
		
	def set_title(self):
		self.title="note :"+str(self.pointer+1)+" | vol: "+str(self.parameters[self.pointer][1])
		
	def send_osc(self,id):
		setting=self.parameters[id]
		osc_send("note",setting[0],setting[1],self.idtrack,id)
		
	def draw(self):
		draw_title(self.title)
		draw_notes(self.parameters,self.tools,self.selection)
		
class NoteMenu(Menu,Editor,Mom):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		Mom.__init__(self)
		self.name="note"
		self.mom="notes"
		self.list=[]
		self.title="note"
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[])
		
	def set_parameters(self):
		idt=self.navigator.menus["tracks"].pointer
		idn=self.navigator.menus["notes"].pointer
		self.parameters=self.partition.tracks[idt][0][1][idn]
		print(self.parameters)
		self.title=get_name(self.navigator.menus["track"].parameters[1][1][0][1])
		self.title="note: "+str(idn+1)
		Mom.set_list(self)
		
	def sort(self,cmd,arg):
		Mom.sort(self,cmd,arg)

	def draw(self):
		draw_title(self.title)
		draw_list(self.list,self.tools)
