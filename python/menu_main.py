from menu import*

class MainMenu(Menu):

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		self.name="main"
		self.mom="main"
		self.list=["play","record","load","save","import","reset"]
		self.tools["grid"]=[2,3]

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

class PlayMenu(Menu):

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		self.name="play"
		self.mom="main"
		self.list=["sequencer","master","tracks"]
		self.tools["grid"]=[1,3]

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

class SequencerMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="sequencer"
		self.mom="play"
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,Partition.sequencer)

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("master",setting[0],setting[1])

class MasterMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="master"
		self.mom="play"
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,Partition.master)

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("master",setting[0],setting[1])

class TracksMenu(Menu):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="tracks"
		self.mom="play"
		self.list=Partition.tracks
		self.tools["grid"]=[10,3]
		self.title=""

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		if cmd=="enter":
			self.navigator.set_menu("track")
		else:
			self.set_parameters()
			
	def set_parameters(self):
		self.title=get_name(self.list[self.pointer][1][1][0][1])
		self.title=set_txt_size(self.title,10)


	def draw(self):
		draw_title("track "+str(self.pointer+1)+": "+self.title)
		draw_tracks(self.list,self.tools)

class TrackMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="track"
		self.mom="tracks"
		self.list=[]
		self.title=""
		self.tools["grid"]=[2,3]
		self.partition=Partition
		self.navigator=Navigator
		Editor.__init__(self,Machine,Partition,[])

	def set_parameters(self):
		id=self.navigator.menus["tracks"].pointer
		#print("track menu set parameters on track n°",id)
		self.parameters=self.partition.tracks[id]
		self.title=str(id+1)+": "+get_name(self.parameters[1][1][0][1])
		self.title=set_txt_size(self.title,15)
		self.set_list()
		
	def set_list(self):
		self.list=[]
		for el in self.parameters:
			self.list.append(el[0])

	def sort(self,cmd,arg):
		if cmd=="enter":
			self.set_nextmenu_parameters()
		Menu.sort(self,cmd,arg)

	def set_nextmenu_parameters(self):
		self.navigator.set_menu("child")
		childname=self.list[self.pointer]
		self.navigator.menu.set_parameters(childname,self.name,self.parameters[self.pointer][1])
		
	def set_sample(self,Path):
		self.parameters[1][1][0][1]=Path
		self.navigator.menus["child"].send_osc()
		
	def draw(self):
		draw_title(self.title)
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

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		if self.mom=="track":
			id_track=self.navigator.menus["tracks"].pointer
			osc_send("track",setting[0],setting[1],id_track)

class SampleMenu(Menu,Browser):

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		Browser.__init__(self,"/home/pi/audiosamples")
		self.name="browser sample"
		self.mom="child"
		self.list=Browser.set_list(self)
		self.tools["grid"]=[1,3]

	def sort(self,cmd,arg):
		
		is_wav=check_wav(self.list[self.pointer])
		samplepath=self.path+"/"+self.list[self.pointer]
		if cmd=="back":
			self.navigator.set_menu("child")
		elif cmd=="enter" and is_wav:
			self.play_sound(samplepath)
		elif cmd=="edit" and arg=="+" and is_wav:
			self.set_sample(samplepath)
		else:
			Browser.sort(self,cmd,arg)
			
	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

	def play_sound(self,Path):
		print("play the sound now")
		os.system("omxplayer "+Path+" --adev local &")
		
	def set_sample(self,Path):
		self.navigator.menus["track"].set_sample(Path)
		self.navigator.set_menu(self.mom)
		
		
