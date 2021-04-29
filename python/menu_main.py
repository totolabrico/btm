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
