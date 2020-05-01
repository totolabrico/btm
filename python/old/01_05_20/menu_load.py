from menu import*

class Menu_load(Menu):

	def _set_list(self):
		path="/home/pi/btm/saves/"
		self._list=os.listdir(path)

	def analyse(self,cmd):

		Menu.analyse(self,cmd)
		if cmd=="back":
			self.navigator.menu="main"

		if cmd=="edit":
			self.navigator.load_set(self.list[self.pointer])

		self._set_list()
