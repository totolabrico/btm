from save import*
from draw import*
from move import*
from edit import*

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
		self.selecter_children=[]
		self.pointer_setting=0
		self.fork_setting=[None,None]
		self.selecter_setting=[]
		self.mode=True
		
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
	
	def set_mode(self):
		self.mode=not self.mode
		self.set_child()

	def set_child(self):
		self.selected_child=None
		try:
			self.selected_child=self.children[self.pointer_children[0]]
		except:
			self.selected_child=None
	
	def set_pointer_setting(self,cmd,arg):
		self.pointer_setting=move(cmd,arg,self.pointer_setting,self.grid_setting)
		
	def set_fork_setting(self,cmd):

		if cmd=="+":
			if self.fork_setting[0]==None:
				self.fork_setting[0]=int(self.pointer_setting)
		if cmd=="stop":
			self.fork_setting[1]=int(self.pointer_setting)
			if self.fork_setting[0]>self.fork_setting[1]:
				to=int(self.fork_setting[0])
				self.fork_setting[0]=int(self.fork_setting[1])
				self.fork_setting[1]=to
			self.set_selecter_setting("+")
			self.fork_setting=[None,None]
		
	def set_selecter_setting(self,cmd):

		if cmd=="+":
			print("fork_setting",self.fork_setting)

			i=self.fork_setting[0]
			while i<=self.fork_setting[1]:
				self.selecter_setting.append(i)
				i+=1
		if cmd=="clear":
			self.selecter_setting=[]
			
		print("selecter_setting",self.selecter_setting)


	def set_pointer_children(self,cmd,arg):
		self.pointer_children=move(cmd,arg,self.pointer_children,self.grid_children)
		self.set_child()

	def set_setting(self,cmd):
		i=0
		while i<len(self.setting):
			for element in self.selecter_setting:
				if i==element:
					setting=self.setting[i]
					setting[1]=edit(cmd,setting)
			i+=1
		self.save()
	
	def set_children(self,cmd):
		if cmd=="+":
			self.children.insert(self.pointer_children,self.child(self,self.pointer_children+1))
		if cmd=="-":
			del self.children[self.pointer_children]
			"""
			i=self.selecter_children[0]
			while i<self.selecter_children[1]:
				clean(self.children[i].name)
				del self.children[i]
				i+=1
			"""
		i=0
		for element in self.children:
			i+=1
			element.set_id(i)
			element.save()

		self.set_grid_children()

	def draw_setting(self):
		set_draw("setting",self.setting,self.pointer_setting,self.selecter_setting,self.grid_setting,4)
	def draw_children(self):
		set_draw("children",self.children,self.pointer_children,self.selecter_children,self.grid_children,2)
		if self.selected_child!=None:
			child=self.selected_child
			set_draw("setting",child.setting,child.pointer_setting,child.selecter_setting,child.grid_setting,2)

