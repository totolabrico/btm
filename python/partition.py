from save import*

class Partition():

	def __init__(self):

		classic_setting=[
		# 0:name / 1:value / 2:min / 3:max / 4:inc
		["mute",False],
		["vol",0.5,0,2,0.02],
		["pan",0,-1,1,0.02],
		["pitch",0,-3,3,0.02],
		["tone",0,-3,3,0.02],
		["temps",4,1,8,1],
		["mesure",8,1,64,1],
		["begin",0,0,64,1],
		["end",8,1,64,1]
		]
		for element in classic_setting:
			self.setting.append(element)

		self.children=[]
		save(self.name,self.setting)

	def edit(self,cmd,arg):
		value=self.setting[cmd][1]
		if type(value)==bool:
			if cmd=="-":
				value= False
			elif cmd=="+":
				value= True
		elif type(value)==int or type(value)==float:
			min=self.setting[cmd][2]
			max=self.setting[cmd][3]
			inc=self.setting[cmd][4]
			if cmd=="-":
				value-=inc
			elif cmd=="+":
				value+=inc
			if value>max:
				value=max
			elif value<min:
				value=min
		self.setting[cmd][1]=round(value,2)
		save(self.name,self.setting)

	def append_children(self,id):
		self.children.append(self.child(self.child_name,id))

	def del_children(self,ids):
		for id in ids:
			clean(self.children[id].name)
			del self.children[id]

	def edit_children(self,cmd,arg,ids):
		for id in ids:
			self.children[id].edit(cmd,arg)
