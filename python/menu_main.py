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

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		if cmd=="enter":
			self.navigator.set_menu("track")

	def draw(self):
		draw_title("track n°"+str(self.pointer+1)+": ")#+self.list[self.pointer][0][1][0][1])
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
		self.id=0
		self.track=[]
		Editor.__init__(self,Machine,Partition,Partition.tracks[self.id]) 

	def set_parameters(self):
		self.id=self.navigator.menus["tracks"].pointer
		self.track=self.partition.tracks[self.id]
		self.title=str(self.id+1)+": "+self.track[1][1][0][1]
		self.list=[]
		for el in self.track:
			self.list.append(el[0])
			print(el[0])
		print(self.list)
		
	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		if cmd=="enter":
			print("id",self.id)
			print("element",self.list[self.pointer])
			print(self.parameters[self.pointer][1])
			nextmenu=self.navigator.menus[self.list[self.pointer]]
			nextmenu.set_parameters(self.name,self.parameters[self.pointer][1])
			
	def draw(self):
		draw_title(self.title)
		draw_list(self.list,self.tools)
		
class AudioMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator) 
		self.name="audio"
		self.mom=""
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[]) 
	
	def set_parameters(self,Mom,Parameters):
		Editor.set_parameters(self,Mom,Parameters)
		
	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)
		print(self.partition.tracks)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)
		
	def send_osc(self):
		setting=self.parameters[self.pointer]
		#osc_send("master",setting[0],setting[1])
