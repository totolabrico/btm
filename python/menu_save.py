from menu import*
import datetime

class Menu_save(Menu):

	def _set_list(self):
		self._list=" abcdefghijklmnopqrstuvwxyz_0123456789"
		self._set_name()
		
	def _set_name(self):
		date=datetime.datetime.now()
		to=self.navigator.name
		if to=="default" or to=="new":
			to=str(date.day)+"-"+str(date.month)+"_"+str(date.hour)+":"+str(date.minute)
		self.save_name=to
		
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
			self.navigator.name=self.partition.name=self.save_name
			self.navigator.save_set()
			self.navigator.menu="main"


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

