""" le navigator effectue des actions sur les partitions:

			editer les parametres de la partition sur laquelle il se trouve
			ajouter, supprimer, copier, coller les enfants de la partition
			editer les parametres de plusieurs enfants de la partition (un parametre a la fois mais plusieurs enfants si souhaité)
			se deplacer dans une partition enfant ou dans la partition mère
"""


class Navigator:

	def __init__(self,Machine):
		self.machine=Machine
		self.element=self.machine.partition
		self.set_max()

	def set_max(self):
		self.max=0
		name=self.machine.partition.name[:4]
		if name =="main":
			self.max=len(self.machine.partition.children)
		if name=="trac":
			self.max=1
			for element in self.element.setting:
				if element[0]=="mesure" or element[0]=="temps":
					self.max*=element[1]

	def analyse_cmd(self,cmd):

		print(self.element.setting,self.element.children)
		print ("max",self.max)
		print("navigator",cmd)
