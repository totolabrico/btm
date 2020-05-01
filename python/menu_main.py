from menu import*

class Menu_main(Menu):

	def _set_list_setting(self):
		self._list_setting=[]
		setting=self.partition.setting
		i=1
		while i<len(setting)-1:
			if i==1:
				to=["machine","stoped"]
				if setting[i][1]==True:
					to= ["machine","playing"]
				self._list_setting.append(to)
			else:
				self._list_setting.append(setting[i])
			i+=1
		self._list_setting.append("save")
		self._list_setting.append("load")

	def analyse(self,cmd):
		length=len(self._list_setting)
		Menu.analyse(self,cmd)
		if cmd=="edit":
			if self.pointer_setting==5:
				self.navigator.menu="save"
			elif self.pointer_setting==6:
				self.navigator.menu="load"
			else:
				self.navigator.menu="tracks"
				
		elif cmd=="+" or cmd=="-":
			if self.pointer_setting==0:
				self.partition.playing=cmd
			if self.pointer_setting==1:
				self.partition.bpm=cmd
			if self.pointer_setting==2:
				self.partition.master=cmd
			if self.pointer_setting==3:
				self.partition.temps=cmd
			if self.pointer_setting==4:
				self.partition.mesure=cmd

		self._set_list_setting()
