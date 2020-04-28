from menu import*
from partition_notes import*
import copy

copy_notes=[]	

class Menu_notes(Menu):
	
	
	def __init__(self,Partition,Navigator,Name):
		
		Menu.__init__(self,Partition,Navigator,Name)
		self.selection=[-1,-1]
		self.is_selecting=False	
		self.pointer=1

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
		global copy_notes
		if button=="back":
			self.finish_draw=True
			self.navigator.menu="track"
			
		elif button=="edit":
			if self.is_selecting==False:
				self.selection[0]=self.pas
				self.is_selecting=True
		elif button=="edit_release":
			if self.selection[1]<self.selection[0]:
				transit=self.selection[1]
				self.selection[1]=self.selection[0]
				self.selection[0]=transit
			self.is_selecting=False	
			print("selection",self.selection)
			
		elif button=="copy":
			copy_notes=[]
			i=self.selection[0]
			while i<=self.selection[1]:
				if self.list_pas[i]!=0:
					copy_notes.append(copy.deepcopy(self.list_pas[i]))
				i+=1
			print("copy-notes",copy_notes)
		
		elif button=="paste":
			paste_notes = copy.deepcopy(copy_notes)
			if len(paste_notes)>0:					
				for element in paste_notes:
					element.pas+=self.pas
					if element.pas>=self.nb_pas:
						element.pas-=self.nb_pas
				self.track.paste_note(paste_notes)
				
		elif button=="del":
			i=self.selection[0]
			while i<=self.selection[1]:
				if self.list_pas[i]!=0:
					self.track.remove_note(self.list_pas[i].Id)
				i+=1
					
					
		elif button=="right":
			self.pas=loopPas("+",self._id_pas,1,self.nb_pas-1,0)
		elif button=="left":
			self.pas=loopPas("-",self._id_pas,1,self.nb_pas-1,0)
		elif button=="up":
			self.pas=loopPas("-",self._id_pas,self.pas_per_line,self.nb_pas-1,0)
		elif button=="down":
			self.pas=loopPas("+",self._id_pas,self.pas_per_line,self.nb_pas-1,0)	
			
		if self.is_selecting:
			self.selection[1]=self.pas
 
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

		
		self._set_list()

	pas=property(_get_pas,_set_pas)
	pas_per_line=property(_get_pas_per_line,_set_pas_per_line)
