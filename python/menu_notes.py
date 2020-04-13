from menu import*
from partition_notes import*


class Menu_notes(Menu):

	
	def __init__(self,Navigator,Name):
		self.navigator=Navigator
		self.track=self.navigator.partition.tracks[self.navigator.track]
		self._id_pas=0
		self.nb_pas=0
		self.set_nb_pas()
		self._setting=[]
		self.id_setting=1
		self.note=None

		Menu.__init__(self,Navigator,Name)
		

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
		self.nb_pas=self.navigator.partition.temps*self.track.mesure
		
	def analyse(self,button):
		
		self._set_setting()
				
		if button=="back":
			self.finish_draw=True
			self.navigator.menu="track"
			
		elif button=="right":
			self.pas=loopValue("+",self._id_pas,1,self.nb_pas-1,0)
		elif button=="left":
			self.pas=loopValue("-",self._id_pas,1,self.nb_pas-1,0)			

		#self._set_setting()	
 
		if button=="+" or button=="-":
			if self.note!=None:					
				setting=self.setting[self.id_setting][0]
				if setting=="vol":	
					self.note.vol=button
				elif setting=="pan":	
					self.note.pan=button
				elif setting=="speed":	
					self.note.speed=button
				elif setting=="cut_begin":	
					self.note.cut_begin=button
				elif setting=="cut_end":	
					self.note.cut_end=button
			else:
				self.id_setting=1
				self.track.add_note(self.pas)
				print("add note ",self.pas)
		

			
		if self.note!=None:	
			if button=="set-":
				self.id_setting=loopValue("+",self.id_setting,1,len(self.setting)-1,1)
			elif button=="set+":
				self.id_setting=loopValue("-",self.id_setting,1,len(self.setting)-1,1)
		
		self.set_draw()

	def draw_led(self):
		time.sleep(0.2)
		while self.finish_draw==False:	
			time.sleep(0.1)				
			self.draw_menu.draw_begin()
			self.draw_menu.draw_setting()
			self.draw_menu.draw_sequence()
			self.draw_menu.draw_end()

		return

		#print("pas:",self.pas," setting:",self.setting)
	
	pas=property(_get_pas,_set_pas)
	setting=property(_get_setting,_set_setting)
