from menu import*

class Menu_main(Menu):

	def _set_list(self):
		copy_list=[]
		setting=self.navigator.partition.setting
		i=1
		while i<len(setting)-1:
			print(setting[i])
			if i==1:
				to=["machine","stoped"]
				if setting[i][1]==True:
					to= ["machine","playing"]
				copy_list.append(to)
			else:
				copy_list.append(setting[i])
			i+=1
		self._list=copy_list
		print("set_list",self._list)

	def analyse(self,cmd):
		length=len(self._list)
		partition=self.navigator.partition
		Menu.analyse(self,cmd)
		if cmd=="edit":
			self.finish_draw=True
			self.navigator.menu="tracks"
		elif cmd=="+" or cmd=="-":
			if self.pointer==0:
				partition.playing=cmd
			if self.pointer==1:
				partition.bpm=cmd
			if self.pointer==2:
				partition.master=cmd
			if self.pointer==3:
				partition.temps=cmd
			if self.pointer==4:
				partition.mesure=cmd
		self._set_list()
		self.set_draw()
