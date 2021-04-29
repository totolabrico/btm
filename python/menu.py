from cmd import*
from draw import*
from osc import*

menu_tools={
"pos":[],
"grid":[0,0],
"origin":0,
"pointer":[0,0],
"fork":[],
"selecter":[],
}


class Menu():
	
	def __init__(self,Navigator):
		self.navigator=Navigator
		self.tools=menu_tools.copy()
		self.pointer=0
		
	def set_pointer(self):
		self.pointer=self.tools["pointer"][0]+self.tools["pointer"][1]*self.tools["grid"][0]
		print("element",self.list[self.pointer])

	def sort(self,cmd,arg):
		if cmd=="move":
			self.tools=move(arg[0],arg[1],self.tools,len(self.list))
			self.set_pointer()
		elif cmd=="enter":
			self.navigator.set_menu(self.list[self.pointer])
		elif cmd=="back":
			self.navigator.set_menu(self.mom)
				
	def draw(self): 
		draw_title(self.name)


class Editor():
	def __init__(self,Machine,Partition,List):
		self.machine=Machine
		self.partition=Partition
		self.parameters=List

	def sort(self,cmd,arg):
		if cmd=="edit":
			self.parameters[self.pointer]=edit(arg,self.parameters[self.pointer])
			self.send_osc()
			#self.machine.save_set()
	
	def set_list(self):
		self.list=[]		
		for parameter in self.parameters:
			self.list.append(parameter[0]+":"+setting_to_string(parameter[1]))
		return self.list

	def draw(self):
		draw_list(self.set_list(),self.tools)
		#print(self.list)

class Rack():
	def __init__(self,List):
		self.parameters=List
	
