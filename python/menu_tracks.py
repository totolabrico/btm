from menu import*

class Menu_tracks(Menu):

	def _set_list(self):
		self._list=[]
		i=0
		while i<len(self.navigator.partition.tracks):
			self._list.append([str(self.navigator.partition.tracks[i].Id),self.navigator.partition.tracks[i].sample])
			i+=1
		self._list.append(["add","+"])
		self._list.append(["remove","-"])

	def analyse(self,button):
		
		Menu.analyse(self,button)
		length=len(self._list)
		if button=="back":
			self.finish_draw=True
			self.navigator.menu="main"
		elif button=="edit":
			if self.pointer<length-2:
				self.navigator.track=self.pointer
				self.finish_draw=True
				self.navigator.menu="track"
			elif self.pointer==length-2:
				self.navigator.partition.add_track()
		
		self._set_list()
		self.set_draw()
