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
		self.pointer_children=[0,0]
		self.pointer_setting=[0,0]
		self.selecter_children=[]
		self.selecter_setting=[]
		self.mode=True
		
		self.grid_setting={
			"x":[1,2],# 1 tas de 2
			"max":len(self.setting),
			"reste":len(self.setting)%2
			}
		
		self.set_grid_children()
		self.set_child()
		save(self.save_name,self.setting)
	
	def set_mode(self):
		self.mode=not self.mode

	def set_child(self):
		self.selected_child=None
		try:
			self.selected_child=self.children[self.pointer_children[0]]
		except:
			self.selected_child=None
	
	def edit_pointer_settings(self,cmd,arg):
		self.pointer_setting[0]=move(cmd,arg,self.pointer_setting[0],self.grid_setting)

	def edit_pointer_children(self,cmd,arg):
		self.pointer_children[0]=move(cmd,arg,self.pointer_children[0],self.grid_children)
		self.set_child()

	def edit_settings(self,cmd):
		pointer=self.pointer_setting[0]
		setting=self.setting[pointer]
		setting[1]=edit(cmd,setting)
		save(self.name,self.setting)
	
	def edit_children(self,cmd):
		if cmd=="+":
			self.children.append(self.child(self,len(self.children)+1))
		if cmd=="-":
			i=self.selecter_children[0]
			while i<self.selecter_children[1]:
				clean(self.children[i].name)
				del self.children[i]
				i+=1
			for element in self.children:
				save(element.save_name,element.setting)
		self.set_grid_children()

	def draw_settings(self):
		set_draw("setting",self.setting,self.pointer_setting,self.grid_setting,4)
	def draw_children(self):
		set_draw("children",self.children,self.pointer_children,self.grid_children,2)
		if self.selected_child!=None:
			child=self.selected_child
			set_draw("setting",child.setting,child.pointer_setting,child.grid_setting,2)

