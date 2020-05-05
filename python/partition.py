from save import*
from draw import*

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

		self.tools_setting={
			"pointer":0,
			"selecteur":[0,0],
			}
	
		self.tools_children={
			"pointer":[0,0], # 0: children / 1: children setting
			"selecteur":[[0,0],[0,0]],
			}
			
		self.grid_setting={
			"x":[1,2],# 1 tas de 10
			"y":4,
			"max":len(self.setting),
			"reste":len(self.setting)%2
			}
		
		self.set_grid_children()				


		save(self.save_name,self.setting)
		

	def sort(cmd,arg):
	
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
		if menu[0]==0:
			grid=self.grid_setting
			pointer=grid["pointer"]
		if menu[0]==1:
			grid=self.grid_children
			pointer=grid["pointer"][menu[1]]
		
		inc=1
		if cmd[0]=="y":
				inc=grid["x"][0]*grid["x"][1]
		if cmd[1]=="-":
			inc*=-1				
		pointer+=inc
		
		if pointer<0:
			pointer+=grid["max"]-grid["x"][0]*grid["x"][1]+grid["reste"]# algorythme a tester
		elif pointer>grid["max"]:
			pointer-=grid["max"]+grid["x"][0]*grid["x"][1]-grid["reste"]		

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
		
	def edit_children(cmd,arg):
		print("contiendra apend_children,del children etc.")

	def append_children(self,id):
		self.children.append(self.child(self,id))
	def del_children(self,ids):
		for id in ids:
			clean(self.children[id].name)
			del self.children[id]

	def edit_children_settings(self,cmd,arg,ids):
		for id in ids:
			self.children[id].edit_setting(cmd,arg)
			

	def draw(self):
		while True:
			if self.menu[0]==0:
				draw_settings(self)
			elif self.menu[0]==1:
				draw_children(self)
			time.sleep(0.07)


