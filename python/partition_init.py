from partition import*
	

class Partition_main(Partition):

	def __init__(self,mother):
		self.mother=mother
		self.name="main"
		self.save_name="main"
		self.child=Partition_track
		self.setting=[
		# 0:name / 1:value / 2:min / 3:max / 4:inc
		["play",False],
		["bpm",120,0,300,0.5]
		]

		clean("all")
		Partition.__init__(self)
		self.edit_children("+")
		
	def set_grid_children(self): # creer la grille d'element
		grid_children={
			"x":[1,10],# 1 tas de 10
			"y":2,
			"max":len(self.children),
			"reste":len(self.children)%10
			}
		for name,value in grid_children.items():
			self.grid_children[name]=value

class Partition_track(Partition):

	def __init__(self,mother,Id):
		self.id=Id
		self.name="track"
		self.save_name=self.name+"_"+str(self.id)
		self.child=Partition_note

		self.setting=[
        	["sample",["no_path","no_name"]]
			]

		Partition.__init__(self)

	def set_grid_children(self):
		temps=0
		mesure=0
		for element in self.setting:
			if element[0]=="mesure":
				mesure=element[1]
			elif element[0]=="temps":
				temps=element[1]
		x_max_mesure=int(16/temps)

		grid_children={
			"x":[x_max_mesure,temps],# x tas de temps
			"y":2,
			"max":mesure*temps,
			"reste":mesure%x_max_mesure
			}
		for name,value in grid_children.items():
			self.grid_children[name]=value
class Partition_note(Partition):

	def __init__(self,mother,Id):
		self.id=Id # ici il s'agit du pas
		self.name="notes"
		self.save_name=mother.save_name+self.name+"_"+str(self.id)
		self.child_name="no_child"
		self.child=None

		self.setting=[]

		Partition.__init__(self)

	def set_grid_children(self):
		self.grid_children=None
