from menu import*

class Menu_track(Menu):
	
	def _get_list(self):
		return self._list
	def _set_list(self):
		copy_list=[]
		copy_list.append(["sample",self.track.sample])
		for element in self.track.setting:
			if element[0]!="id" and element[0]!="sample":
				copy_list.append([element[0],element[1]])
		self._list=copy_list

	def analyse(self,cmd):
		Menu.analyse(self,cmd)

		if cmd=="back":
			self.navigator.menu="tracks"
		elif cmd=="edit":
			self.navigator.menu="notes"
		elif cmd=="+" or cmd=="-":
			if self.pointer==0 and cmd=="+":
				self.navigator.menu="browser"
			if self.pointer==1:
				self.track.vol=cmd
			if self.pointer==2:
				self.track.pan=cmd
			if self.pointer==3:
				self.track.mute=cmd
			if self.pointer==4:
				self.track.solo=cmd
			if self.pointer==5:
				self.track.mesure=cmd
		
		elif type(cmd)==list:
			if cmd[0]=="track":
				self.switch_track(cmd[1])
		
		self._set_list()

		"""
		elif self._menu=="track_info":
			if button=="info":
				self._set_menu("track")
		"""
