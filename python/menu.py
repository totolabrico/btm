from cmd import*
from draw import*
from osc import*
from settings import*
from partition import Partition
import os, sys
import copy

class Menu():

	def __init__(self,Navigator):
		self.navigator=Navigator
		self.tools=menu_tools.copy()
		self.pointer=0

	def set_pointer(self):
		self.pointer=int(self.tools["pointer"][0]+self.tools["pointer"][1]*self.tools["grid"][0])
		
	def reset_pointer(self):
		self.tools["pointer"]=[0,0]
		self.tools["origin"]=0
		self.set_pointer()
		
	def sort(self,cmd,arg):
		if cmd=="move":
			self.tools=move(arg[0],arg[1],self.tools,len(self.list))
			self.set_pointer()
		elif cmd=="back":
			self.navigator.set_menu(self.mom)
		elif cmd=="enter":
			try:
				self.navigator.set_menu(self.list[self.pointer])
			except:
				pass
			
	def draw(self):
		draw_title(self.name)

class Mom():
	
	def __init__(self):
		pass
		
	def set_list(self):
		self.list=[]
		for el in self.parameters:
			self.list.append(el[0])

	def sort(self,cmd,arg):
		if cmd=="enter" and self.list[self.pointer]!="notes":
			self.navigator.set_menu("child")
			self.set_nextmenu_parameters()
			self.reset_pointer()
		else:
			Menu.sort(self,cmd,arg)

	def set_nextmenu_parameters(self):
		childname=self.list[self.pointer]
		self.navigator.menu.set_parameters(childname,self.name,self.parameters[self.pointer][1])
		
class Editor():
	def __init__(self,Machine,Partition,Parameters):
		self.machine=Machine
		self.partition=Partition
		self.parameters=Parameters
		
	def sort(self,cmd,arg):
		if cmd=="previous":
			self.partition.load_backup()
			try:
				self.set_parameters()
			except:
				pass
			return
		elif cmd=="erase" or cmd=="paste":
			self.partition.save_backup()
		if cmd=="edit":
			try:
				ids=self.selection
				if ids==[]:
					ids=[self.pointer]
			except:
				ids=[self.pointer]
			for id in ids:
				self.edit(id,arg)
			
	def edit(self,id,cmd):
		parameter=self.parameters[id]
		parameter=edit(cmd,parameter)
		try:
			self.send_osc(id)
		except:
			self.send_osc()
		print("selector edit",id,parameter)

	def set_list(self):
		self.list=[]
		for parameter in self.parameters:
			self.list.append(parameter[0][0:5]+":"+setting_to_string(parameter[1]))
		return self.list

	def draw(self):
		draw_list(self.set_list(),self.tools)

class Browser():

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
			self.set_pointer()
		if cmd=="erase":
			if self.path=="/home/pi/audiosamples/Records":
				try:
					os.system("rm "+self.path+"/"+self.list[self.pointer])
					self.set_list()
				except:
					pass

	def set_path(self,cmd):
		cut=self.path.split("/")
		last_word=cut[len(cut)-1]
		if cmd=="+":
			new_path=self.path+"/"+self.list[self.pointer]
			if os.path.isdir(new_path)==True:
				self.path=new_path
				self.set_list()
				self.set_y(0)

		if cmd=="-" and len(cut)>4:
			self.path=self.path[:-(len(last_word)+1)]
			self.set_list()
			i=0
			for element in self.list:
				if element==last_word:
					print(element,last_word)
					self.set_y(i)
				i+=1
	
	def set_y(self,Y):
		h=self.tools["grid"][1]
		if h>len(self.list):
			h=len(self.list)
		self.tools["pointer"][1]=Y
		self.tools["origin"]=Y

class KeyMenu():
	savename="default"
	def __init__(self):
		pass
	def sort(self,cmd,arg):
		if cmd=="edit":
			if arg[0]=="+":
				self.savename+=self.list[self.pointer]
			if arg[0]=="-":
				self.savename=self.savename[:-1]
	
	def draw(self):
		draw_footer(self.savename)

class Selector():
	
	def __init__(self):
		self.push_pointer=0
		self.is_push=False
		self.selection=[]
	def sort(self,cmd,arg):
		#print("selector sort",cmd,arg)
		if cmd=="select":
			if arg=="push":
				if self.is_push==False:
					self.push_pointer=self.pointer
					self.is_push=True
			if arg=="release":
				self.add_to_selection(self.push_pointer,self.pointer)
				self.is_push=False
			if arg=="erase":
				self.selection=[]
				print("selection is clear")
				
	def add_to_selection(self,posa,posb):
		if posa==posb:
			self.check_selection(posb)
		else:
			if posb<posa:
				prov=posa
				posa=posb
				posb=prov
			i=posa
			while i<=posb:
				self.check_selection(i)
				i+=1
		print("selection : ",self.selection)
	
	def check_selection(self,Pos):
		exist=False
		for element in self.selection:
			if element==Pos:
				self.selection.remove(Pos)
				exist=True
		if exist==False:
			self.selection.append(Pos)
	
