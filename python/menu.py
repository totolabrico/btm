from cmd import*
from draw import*
from osc import*
from settings import*
import os, sys


class Menu():

	def __init__(self,Navigator):
		self.navigator=Navigator
		self.tools=menu_tools.copy()
		self.pointer=0

	def set_pointer(self):
		self.pointer=int(self.tools["pointer"][0]+self.tools["pointer"][1]*self.tools["grid"][0])

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
		print("editot sort")
		if cmd=="edit":
			parameter=self.parameters[self.pointer]
			print(self.parameters,self.pointer)
			if parameter[0]=="sample":
				self.navigator.set_menu("sample")
			else:
				parameter=edit(arg,parameter)
				self.send_osc()
			#self.machine.save_set()

	def set_list(self):
		self.list=[]
		for parameter in self.parameters:
			self.list.append(parameter[0]+":"+setting_to_string(parameter[1]))
		return self.list

	def draw(self):
		draw_list(self.set_list(),self.tools)


class Browser(): # != Editor un browser est un menu qui permet de se deplacer dans l'oridnateur

	def __init__(self,Path):
		self.path=Path

	def set_list(self):
		self.list=[]
		for element in os.listdir(self.path):
			if element[:1]!=".":
				self.list.append(element)
		return self.list

	def sort(self,cmd,arg):
		if cmd=="move":
			if arg[0]=="y":
				self.tools=move(arg[0],arg[1],self.tools,len(self.list))
			if arg[0]=="x":
				self.set_path(arg[1])

	def set_path(self,cmd):
		cut=self.path.split("/")
		last_word=cut[len(cut)-1]

		if cmd=="+":
			new_path=self.path+"/"+self.list[self.pointer]
			if os.path.isdir(new_path)==True:
				self.pointer=0
				self.path=new_path
				self.set_list()
		if cmd=="-" and len(cut)>3:
			self.path=self.path[:-(len(last_word)+1)]
			self.set_list()
			i=0
			for element in self.list:
				if element==last_word:
					self.pointer=i
					i+=1
