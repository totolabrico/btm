from save import*
from draw import*
from cmd import*

classic_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
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
	["lpf",0,0,20000,10],#low pass filter
	["hpf",20000,0,20000,10],#high pass filter
	["loop",True]
	]

class Partition():

	def __init__(self,Mother):
		global classic_setting

		for element in classic_setting:
			self.setting.append(element)

		self.mother=Mother
		self.children=[]
		self.pointer_children=0
		self.fork_children=[None,None]
		self.selecter_children=[]
		self.pointer_setting=0
		self.fork_setting=[None,None]
		self.selecter_setting=[]

		self.grid_setting={
			"x":[1,2],# 1 tas de 2
			"max":len(self.setting),
			"reste":len(self.setting)%2
			}

		self.set_grid_children()
		self.set_child()
		self.save()

	def set_id(self,id):
		self.id=id
		self.save_name=self.name+"_"+str(id)

	def set_child(self):
		self.selected_child=None
		try:
			self.selected_child=self.children[self.pointer_children[0]]
		except:
			self.selected_child=None

	def set_pointer(self,type,cmd,arg):
		if type=="setting":
			self.pointer_setting=move(cmd,arg,self.pointer_setting,self.grid_setting)	
		if type=="children":
			self.pointer_children=move(cmd,arg,self.pointer_children,self.grid_children)
			self.set_child()
		
	def set_fork(self,type,cmd):
		if type=="setting":
			pointer=self.pointer_setting
			fork=self.fork_setting
			selecter=self.selecter_setting
		elif type=="children":
			pointer=self.pointer_children
			fork=self.fork_children
			selecter=self.selecter_children		
			
		if cmd=="+" or cmd=="stop":
			fork=set_fork(pointer,fork,cmd)
		if cmd=="stop":
			selecter=set_selecter(fork,selecter)
			fork=[None,None]
		if cmd=="clear":
			del selecter[:]

	def set_setting(self,cmd):		
		if self.selecter_setting==[]:
			setting=self.setting[self.pointer_setting]
			self.edit_setting(cmd,setting)
		else:
			i=0
			while i<len(self.setting):
				for element in self.selecter_setting:
					if i==element:
						setting=self.setting[i]
						self.edit_setting(cmd,setting)
				i+=1
		self.save()
		
	def edit_setting(self,cmd,setting):
		if setting[0]=="sample":
			self.mother.machine.navigator.launch_browser(self)
		else:
			setting[1]=edit(cmd,setting)

	def set_children(self,cmd):
		if cmd=="+":
			self.children.insert(self.pointer_children,self.child(self,self.pointer_children+1))
		if cmd=="-" and self.selecter_children!=[]:
			for id in self.selecter_children:
				i=0
				while i<len(self.children):
					if self.children[i].id==id+1:
						if self.save_name=="main":
							clean(self.children[i].save_name)
						del self.children[i]
					i+=1
				
		self.sort_children()
		self.set_grid_children()

		
	def draw_setting(self):
		set_draw("setting",self.setting,self.pointer_setting,self.selecter_setting,self.fork_setting,self.grid_setting,4)
	def draw_children(self):
		# j'affiche uniquement les parametre de l'enfant pointer ! mais je modifi les parametre de touts les elements selectionnés
		set_draw("children",self.children,self.pointer_children,self.selecter_children,self.fork_children,self.grid_children,2)
		for element in self.children:
			if element.id==self.pointer_children+1:
				set_draw("setting",element.setting,element.pointer_setting,element.selecter_setting,element.fork_setting,element.grid_setting,2)
