from menu import*
from partition_notes import*


class Menu_notes(Menu):

	
	def __init__(self,Partition,Navigator,Name):
		
		Menu.__init__(self,Partition,Navigator,Name)
		self._id_pas=0
		self.nb_pas=0
		self.set_nb_pas()
		self._setting=[]
		self.id_setting=1
		self.note=None
		self._pas_per_line=0
		self._set_pas_per_line()

	def _get_pas(self):
		return self._id_pas
	def _set_pas(self,pas):
		self._id_pas=pas
		self._set_setting()

	def _get_setting(self):
		return self._setting
	def _set_setting(self):
		self._setting=[]
		if len(self.track.notes)>0:
			for element in self.track.notes:
				if element.pas == self.pas:
					self._setting=element.setting	
					self.note=element
					break
				else:
					self.note=None
		else:
			self.note=None			


	def set_nb_pas(self):
		self.nb_pas=self.partition.temps*self.track.mesure
		
	def _get_pas_per_line(self):
		return self._pas_per_line
		
	def _set_pas_per_line(self):
		temps=self.partition.temps
		self._pas_per_line=4*temps
		if temps>=5:
			self._pas_per_line=2*temps

		
	def analyse(self,button):
		
		self._set_setting()
				
		if button=="back":
			self.finish_draw=True
			self.navigator.menu="track"
			
		elif button=="right":
			self.pas=loopPas("+",self._id_pas,1,self.nb_pas-1,0)
		elif button=="left":
			self.pas=loopPas("-",self._id_pas,1,self.nb_pas-1,0)

		elif button=="up":
			self.pas=loopPas("-",self._id_pas,-self.pas_per_line,self.nb_pas-1,0)
		elif button=="down":
			self.pas=loopPas("+",self._id_pas,self.pas_per_line,self.nb_pas-1,0)	
		#self._set_setting()	
 
		elif button=="+" or button=="-":
			if self.note!=None:					
				setting=self.setting[self.id_setting][0]
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
					self.id_setting=1
					self.track.add_note(self.pas)
					print("add note ",self.pas)
					
		elif type(button)==list:
			if button[0]=="track":
				self.switch_track(button[1])
			
		if self.note!=None:	
			if button=="set-":
				self.id_setting=loopValue("+",self.id_setting,1,len(self.setting)-1,1)
			elif button=="set+":
				self.id_setting=loopValue("-",self.id_setting,1,len(self.setting)-1,1)
			elif button=="del":
				self.track.remove_note(self.note.Id)
		
		#print("pas:",self.pas," setting:",self.setting)
	
	pas=property(_get_pas,_set_pas)
	pas_per_line=property(_get_pas_per_line,_set_pas_per_line)
	setting=property(_get_setting,_set_setting)
