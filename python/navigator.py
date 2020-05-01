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


	def analyse_cmd(self,cmd):

		print(self.element.setting,self.element.children)
		print("navigator",cmd)
