from menu import*

class Menu_main(Menu):

	def _set_list(self):
		copy_list=[]
		setting=self.partition.setting
		i=1
		while i<len(setting)-1:
			if i==1:
				to=["machine","stoped"]
				if setting[i][1]==True:
					to= ["machine","playing"]
				copy_list.append(to)
			else:
				copy_list.append(setting[i])
			i+=1
		copy_list.append("save")
		copy_list.append("load")
		self._list=copy_list

	def analyse(self,cmd):
		length=len(self._list)
		Menu.analyse(self,cmd)
		if cmd=="edit":
			self.finish_draw=True
			if self.pointer==5:
				self.navigator.menu="save"
			elif self.pointer==6:
				self.navigator.menu="load"
			else:
				self.navigator.menu="tracks"
		elif cmd=="+" or cmd=="-":
			if self.pointer==0:
				self.partition.playing=cmd
			if self.pointer==1:
				self.partition.bpm=cmd
			if self.pointer==2:
				self.partition.master=cmd
			if self.pointer==3:
				self.partition.temps=cmd
			if self.pointer==4:
				self.partition.mesure=cmd

		self._set_list()
