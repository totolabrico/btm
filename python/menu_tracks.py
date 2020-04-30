from menu import*
import copy

copy_track=''

class Menu_tracks(Menu):

	def _set_list(self):
		self._list=[]
		if len(self.partition.tracks)!=0:
			i=0
			while i<len(self.partition.tracks):
				self._list.append([str(self.partition.tracks[i].Id),self.partition.tracks[i].name])
				i+=1
		self._list.append(["add","+"])
		#self._list.append(["remove","-"])

	def analyse(self,button):
		global copy_track
		Menu.analyse(self,button)
		length=len(self._list)
		if button=="back":
			self.navigator.menu="main"
		elif button=="edit":
			if self.pointer<length-1:
				self.navigator.track=self.pointer
				self.navigator.menu="track"
			elif self.pointer==length-1:
				self.partition.add_track()
		elif button=="del":
			if self.pointer<length-1:
				self.partition.del_track(self.pointer)
		elif button=="copy":
			if self.pointer<length-1:
				copy_track=copy.deepcopy(self.partition.tracks[self.pointer])
				print (copy_track)
		elif button=="paste":
			if self.pointer<length-1 and copy_track!='':
				self.partition.paste_track(copy_track,self.pointer+1)
				
		self._set_list()
