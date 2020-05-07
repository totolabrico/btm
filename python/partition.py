from save import*
from draw import*
import time

classic_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["loop",True],
	["solo",False],
	["mute",False],
	["vol",0.5,0,2,0.02],
	["pan",0,-1,1,0.02],
	["pitch",0,-3,3,0.02],
	["tone",0,-3,3,0.02],
	["begin",0,0,64,1],
	["end",8,1,64,1],
	["temps",4,1,8,1],
	["mesure",8,1,64,1],
	["lpf",4,1,8,1],#low pass filter
	["hpf",8,1,64,1],#high pass filter
	]

class Partition():

	def __init__(self):
		global classic_setting

		for element in classic_setting:
			self.setting.append(element)
			
		self.children=[]
		self.menu=[0,0]

		self.grid_children={
			"pointer":[0,0], # 0: children / 1: children setting
			"selecter":[[0,0],[0,0]],
			}
			
		self.grid_setting={
			"pointer":0,
			"selecter":[0,0],
			"x":[1,2],# 1 tas de 2
			"y":4,
			"max":len(self.setting),
			"reste":len(self.setting)%2
			}
		
		self.set_grid_children()				
		save(self.save_name,self.setting)
		

	def sort(self,cmd,arg):
	
		if cmd=="switch":
			if arg=="menu":
				self.menu[0]=abs(self.menu[0]-1)
			elif arg=="mode":
				self.menu[1]=abs(self.menu[1]-1)
		elif cmd=="move":
			self.move(arg)
		else:
			self.set_cmd(cmd,arg)
			
		
	def move(self,cmd):
		if self.menu[0]==0:
			grid=self.grid_setting
		if self.menu[0]==1:
			grid=self.grid_children
		inc=1
		if cmd[0]=="y":
				inc=grid["x"][0]*grid["x"][1]
		if cmd[1]=="-":
			inc*=-1		
		grid["pointer"]=self.set_pointer(grid,inc)
		
	def set_pointer(self,Grid,Inc)
		#ic : bien definir l'algorythme
		#vide=-Grid["reste"]
		#max=grid["max"]	
		print("set pointer!")
		return 0
		
	def set_cmd(cmd,arg):
		
		if menu[0]==0:
			self.mode[0]=menu[1]
			self.edit_settings(cmd,arg)

		elif menu[0]==1:
			if menu[1]==0:
				self.edit_children(cmd,arg)
			elif menu[1]==1:
				self.edit_children_settings(cmd,arg)
					
		
	def edit_settings(self,cmd,arg):

		value=self.setting[cmd+self.menu[1]][1]

		if type(value)==bool:
			if arg=="-":
				value= False
			elif arg=="+":
				value= True
			self.setting[cmd][1]=value

		elif type(value)==int or type(value)==float:
			min=self.setting[cmd][2]
			max=self.setting[cmd][3]
			inc=self.setting[cmd][4]
			if arg=="-":
				value-=inc
			elif arg=="+":
				value+=inc
			if value>max:
				value=max
			elif value<min:
				value=min
			self.setting[cmd][1]=round(value,2)
			print("edit_setting",cmd,value,inc)

		save(self.name,self.setting)
		
	def edit_children(self,cmd):
		
		if cmd=="append":
			self.children.append(self.child(self,self.grid_setting["pointer"]))
		if cmd=="del":
			i=self.grid_children["selecter"][0]
			while i<self.grid_children["selecter"][1]:
				clean(self.children[i].name)
				del self.children[i]
				i+=1

	def edit_children_settings(self,cmd,arg,ids):
		for id in ids:
			self.children[id].edit_setting(cmd,arg)
			

	def draw(self):
		while True:
			draw_begin()
			draw_title(self.name)
			if self.menu[0]==0:
				draw_settings(self.setting,self.grid_setting)
			elif self.menu[0]==1:
				draw_children(self)
			draw_end()
			time.sleep(0.07)
