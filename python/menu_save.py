from menu import*

class Menu_save(Menu):

	def _set_list(self):
		self._list=" abcdefghijklmnopqrstuvwxyz_0123456789"
		self.save_name=self.navigator.name
	def letter(self):
		return self._list[self.pointer]
	
	def analyse(self,cmd):
					
		if cmd=="+" or cmd=="-":		
			self.pointer=loopValue(cmd,self.pointer,1,len(self.List)-1,0)
		if cmd=="back":
			self.navigator.menu="main"
		if cmd=="del":
			self.save_name=self.save_name[:-1]
		if cmd=="right":
			self.save_name=self.save_name+self.letter()	
		if cmd=="edit":
			self.navigator.menu="main"
			self.navigator.name=self.partition.name=self.save_name
			self.navigator.save_set()


"""
def save_set(partition):
	print("toto")
	#my_part=DerivedPartition

	
		save = copy.copy(self.partition)
		path="/home/pi/btm/saves/"+self.name+"/master_main"
		with open(path,'wb') as fichier:
			mon_pickler=pickle.Pickler(fichier)
			mon_pickler.dump(save)
	"""

