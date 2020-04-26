from menu import*
from partition_notes import*


class Menu_notes(Menu):
	
	def __init__(self,Partition,Navigator,Name):
		
		Menu.__init__(self,Partition,Navigator,Name)		

	def _set_list(self):
		self.list_pas=[]
		self._list=[]
		i=0
		while i<self.nb_pas:
			self.list_pas.append(0)
			if len(self.track.notes)>0:
				for element in self.track.notes:
					if i == element.pas:
						self.list_pas[i]=element
						if i==self.pas:
							self.note=element
							self._list=element.setting
			i+=1

	def set_nb_pas(self):
		self.nb_pas=self.partition.temps*self.track.mesure
		
	def _get_pas_per_line(self):
		return self._pas_per_line		
	def _set_pas_per_line(self):
		temps=self.partition.temps
		self._pas_per_line=4*temps
		if temps>=5:
			self._pas_per_line=2*temps
		self._set_list()
		
	
	def _get_pas(self): # a remplacer par _get_setting
		return self._id_pas
	def _set_pas(self,pas):
		self._id_pas=pas
	
	def analyse(self,button):
				
		if button=="back":
			self.finish_draw=True
			self.navigator.menu="track"
			
		elif button=="right":
			self.pas=loopPas("+",self._id_pas,1,self.nb_pas-1,0)
		elif button=="left":
			self.pas=loopPas("-",self._id_pas,1,self.nb_pas-1,0)

		elif button=="up":
			self.pas=loopPas("-",self._id_pas,self.pas_per_line,self.nb_pas-1,0)
		elif button=="down":
			self.pas=loopPas("+",self._id_pas,self.pas_per_line,self.nb_pas-1,0)	
 
		elif button=="+" or button=="-":
			if len(self.List)>0:					
				setting=self.List[self.pointer][0]
				if setting=="vol":	
					self.note.vol=button
				elif setting=="pan":	
					self.note.pan=button
				elif setting=="pitch":	
					self.note.pitch=button
				elif setting=="tone":	
					self.note.tone=button
				elif setting=="begin":	
					self.note.begin=button
				elif setting=="length":	
					self.note.length=button
			else:
				if button=="+":
					self.pointer=1
					self.track.add_note(self.pas)
					print("add note ",self.pas)
					
		elif type(button)==list:
			if button[0]=="track":
				self.switch_track(button[1])
			
		if len(self.List)>0:	
			if button=="set-":
				self.pointer=loopValue("+",self.pointer,1,len(self.List)-1,1)
			elif button=="set+":
				self.pointer=loopValue("-",self.pointer,1,len(self.List)-1,1)
			elif button=="del":
				self.track.remove_note(self.note.Id)
		
		self._set_list()

	pas=property(_get_pas,_set_pas)
	pas_per_line=property(_get_pas_per_line,_set_pas_per_line)
