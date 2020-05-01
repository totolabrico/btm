from partition import*

class Partition_note(Partition):

	def __init__(self,Name,Id):
		self.pas=pas
		self.name=Name+"_"+str(Id)
		self.child_name="no_child"
		self.child=None

		self.setting=[
		["solo",False]
		]

		Partition.__init__(self)
