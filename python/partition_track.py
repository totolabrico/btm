from partition import*
from partition_note import*

class Partition_track(Partition):

	def __init__(self,Name,Id):
		self.id=Id
		self.name=Name+"_"+str(Id)
		self.child_name=self.name+"_note"
		self.child=Partition_note

		self.setting=[
        	["sample","empty"],
	        ["name","empty"],
			["solo",False]
			]

		Partition.__init__(self)
