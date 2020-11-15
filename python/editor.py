from draw import*
from editor_interface import*
from osc import*

editor_tools={
"element":None,
"pos":[],
"grid":[0,0],
"origin":0,
"pointer":0,
"fork":[],
"selecter":[],
}

class Editor(): # separer les chose en deux !!!!

	def __init__(self,Machine,Navigator,Name,Settings):
		self.machine=Machine
		self.navigator=Navigator
		self.name=Name	
		self.settings=Settings
		self.switch_state=0 
		self.init_tools()
		self.interface=Editor_Interface(self.machine,self.navigator,self,self.machine.partition)


	def init_tools(self):	# initialisation des outils de l'editeur : deux liste : setting et children / contenu : copie de editor tools
		self.setting_tools=editor_tools.copy()
		if self.name!="master":
			self.children_tools=editor_tools.copy()
		self.set_tools();
			
	def set_tools(self):
		self.set_setting_tools()
		if self.name!="master":
			self.set_children_tools()

	def sort(self,cmd,arg): # tri des commandes : edit, move
		#print("editor sort: ",cmd,arg)
		if cmd=="edit":
			setting=self.setting_tools["element"]
			key=get_key(setting,self.setting_tools["pointer"])
			element=setting[key]
			if self.name=="track" and key=="sample" and arg=="+":
				self.machine.navigator.pointer="browser"
			else:
				self.edit_setting(arg,key,element)
		elif cmd=="move":
			self.move(arg)
				
	def move(self,cmd):
		if self.navigator.toggle_state==0:
			self.setting_tools=move(cmd[0],cmd[1],self.setting_tools) # edite la position du pointer et l'origine
		else:
			self.children_tools=move(cmd[0],cmd[1],self.children_tools)
			self.set_children_tools()
		self.set_setting_tools() # met a jour la liste de settings, sa grille d'affichage, ses positions d'affichages

	
	def edit_setting(self,cmd,key,el):
		track=self.navigator.track_editor.children_tools["pointer"]
		note=self.navigator.note_editor.children_tools["pointer"]
		self.machine.partition.edit(cmd,key,el,self.name,track,note)
		#osc_send(self.name,key,el[1],track,note)

	
	def get_sample(self,cmd):
		setting=self.setting_tools["element"]["sample"]
		self.edit_setting(cmd,"sample",setting)


	def set_setting_tools(self): # appel set_setting, set_grid_setting, et set pos
		self.setting_tools["element"]=self.set_setting()
		self.setting_tools["grid"]=self.set_grid_setting()
		self.setting_tools["pos"]=self.set_pos(self.setting_tools)	
		
	def set_children_tools(self): # appel set_chidlren, set_grid_children et set pos
		if self.name!="master":
			self.children_tools["element"]=self.set_children()
			self.children_tools["grid"]=self.set_grid_children()
			self.children_tools["pos"]=self.set_pos(self.children_tools)
			

	def set_setting(self):# defini la liste de setting 					
		if self.name=="master":
			return self.settings
		elif self.name=="track":
			return self.settings[self.children_tools["pointer"]]
		elif self.name=="note":
			return self.settings[self.navigator.track_editor.children_tools["pointer"]][self.children_tools["pointer"]]

	def set_children(self):# defini la liste de children				
		if self.name=="master":
			return None
		elif self.name=="track":
			return self.settings
		elif self.name=="note":
			return self.settings[self.navigator.track_editor.children_tools["pointer"]]


	def set_grid_setting(self): # defini la grille d'affichage des setting
		width= 2
		if self.name=="master":
			height= 4
		else:
			if self.navigator.toggle_state==0:
				height=3
			else:
				height=1
		return [width,height]


	def set_grid_children(self): # defini la grille d'affichage des children
		if self.name=="track":
			width= 10
		if self.name=="note":
			setting=self.machine.partition.master_setting
			for key,el in setting.items():
				if key=="temps":
					width= el[1]*4 # nombre de temps de la track*4
		if self.navigator.toggle_state==0:
			height= 1
		else:
			height= 3
		return [width,height]


	def set_pos(self,tools): # defini les positions d'affichage des elements (setting et children)
		pos=[]
		x=0
		y=0
		for element in tools["element"]:
			pos.append([x,y])
			x+=1
			if x==tools["grid"][0]:
				x=0
				y+=1
		return pos

	def reset_pointer(self):
		self.setting_tools["pointer"]=0
		self.children_tools["pointer"]=0
