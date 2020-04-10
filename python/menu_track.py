from menu import*

class Menu_track(Menu):

	def _get_list(self):
		return self._list
	def _set_list(self):
		track=self.navigator.partition.tracks[self.navigator.track]
		copy_list=[]
		copy_list.append(["sample",track.sample])
		for element in track.setting:
			if element[0]!="id" and element[0]!="sample":
				copy_list.append([element[0],element[1]])
		self._list=copy_list

	def analyse(self,cmd):
		Menu.analyse(self,cmd)
		track=self.navigator.partition.tracks[self.navigator.track]

		if cmd=="back":
			self.finish_draw=True
			self.navigator.menu="tracks"
		elif cmd=="edit":
			self.finish_draw=True
			self.navigator.menu="notes"
		elif cmd=="+" or cmd=="-":
			if self.pointer==0 and cmd=="+":
				self.finish_draw=True
				self.navigator.menu="browser"
			if self.pointer==1:
				track.vol=cmd
			if self.pointer==2:
				track.pan=cmd
			if self.pointer==3:
				track.mute=cmd
			if self.pointer==4:
				track.solo=cmd
			if self.pointer==5:
				track.mesure=cmd
		
		self._set_list()
		self.set_draw()

		"""
		elif self._menu=="track_info":
			if button=="info":
				self._set_menu("track")
		"""
