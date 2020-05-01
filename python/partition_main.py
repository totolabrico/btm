from partition import*
from partition_track import*

class Partition_main(Partition):

	def __init__(self):
		self.name="main"
		self.child_name="track"
		self.child=Partition_track

		self.setting=[
		# 0:name / 1:value / 2:min / 3:max / 4:inc
		["playing",False],
		["bpm",120,0,300,0.5]
		]

		clean("all")
		Partition.__init__(self)
		self.append_children(1)
