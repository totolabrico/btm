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

class Editor():

	def __init__(self,Machine):
		self.machine=Machine
		self.menu=0	
		self.edited_track=0
		self.edited_note=0
		
		self.toggle_state=0 # 0:settings / 1:element
		self.switch_state=0 
		
		self.init_tools()
		self.set_tools()
		self.editor_interface=Editor_Interface(self,self.machine.partition)


	def sort(self,cmd,arg): # tri des commandes
		print("editor sort: ",cmd,arg)
		if cmd=="menu":
			self.set_menu(arg)
		if cmd=="toggle":
			self.set_toggle()
		elif cmd=="edit":
			self.edit(arg)
		elif cmd=="move":
			self.move(arg)


	def set_toggle(self):
		if self.menu!=0:
			self.toggle_state=not self.toggle_state
			self.set_tools()
	
	
	def edit(self,cmd):
		setting=self.setting_tools["element"][self.setting_tools["pointer"]]
		if self.menu==1 and setting[0]=="sample" and cmd=="+":
			self.machine.navigator.pointer="browser"
		else:	
			self.machine.partition.edit(cmd,setting,self.menu,self.edited_track,self.edited_note)
			#osc_send(menu_names[self.menu],setting[0],setting[1],self.edited_track,self.edited_note)

	
	def get_sample(self,cmd):
		setting=self.setting_tools["element"][0]
		#self.machine.partition.edit(cmd,setting)
		self.machine.partition.edit(cmd,setting,menu_names[self.menu],self.edited_track,self.edited_note)
		#osc_send(menu_names[self.menu],setting[0],setting[1],self.edited_track,self.edited_note)


	def move(self,cmd):
		if self.toggle_state==0:
			self.setting_tools=move(cmd[0],cmd[1],self.setting_tools)
		if self.toggle_state==1:
			self.children_tools=move(cmd[0],cmd[1],self.children_tools)
			self.set_edited()
			self.set_tools()
			
			
	def set_menu(self,cmd):
		last_menu=int(self.menu)
		if cmd=="+" and self.menu<2:
			self.menu+=1
		elif cmd=="-" and self.menu>0:
			self.menu-=1
			
		if last_menu!=self.menu:
			self.set_toggle_default()
			self.init_tools()
			self.set_tools()	
	
	
	def set_toggle_default(self): # redefini l'etat du toggle en fonction du menu
		if self.menu==0:
			self.toggle_state=0
		else:
			self.toggle_state=1
	
	
	def reset_edited(self): # reset de l'element selectionné
		if self.menu==0:
			self.edited_track=0
		elif self.menu==1:
			self.edited_note=0
			
			
	def set_edited(self): # defini l'id de l'element selectionné
		if self.menu==1:
			self.edited_track=self.children_tools["pointer"]
			print("set edited track",self.edited_track)
		if self.menu==2:
			self.edited_note=self.children_tools["pointer"]
	
	
	def init_tools(self):	# initialisation des outils de l'editeur : deux liste : setting et children / contenu : copie de editor tools
		self.setting_tools=editor_tools.copy()
		if self.menu>0:
			self.children_tools=editor_tools.copy()
	
	
	def set_tools(self):
		self.setting_tools["element"]=self.set_element("setting")
		self.setting_tools["grid"]=self.set_grid("setting")
		self.setting_tools["pos"]=self.set_pos(self.setting_tools)			
	
		if self.menu>0:
			self.children_tools["element"]=self.set_element("children")
			self.children_tools["grid"]=self.set_grid("children")
			self.children_tools["pos"]=self.set_pos(self.children_tools)
			
		print(self.setting_tools["element"])
		if self.menu>1:
			print(self.children_tools["pointer"])


	def set_element(self,Type):# defini les elements selectionné par l'utilisateur					
		if Type=="setting": # setting selectionné
			if self.menu==0:
				return self.machine.partition.master_setting
			elif self.menu==1:
				return self.machine.partition.track_setting[self.edited_track]
			elif self.menu==2:
				return self.machine.partition.note_setting[self.edited_track][self.edited_note]

		elif Type=="children": # element enfant selectionné : tracks, notes : pour affichage
			if self.menu==0:
				return None
			elif self.menu==1:
				return self.machine.partition.track_setting
			elif self.menu==2:
				return self.machine.partition.note_setting[self.edited_track]


	def set_grid(self,Type): # defini la grille d'affichage
		############################### width
		if Type=="setting":
			width= 2
		elif Type=="children":
			if self.menu==1:
				width= 10
			if self.menu==2:
				setting=self.machine.partition.master_setting
				for el in setting:
					if el[0]=="temps":
						width= el[1]*4 # nombre de temps de la track*4

		############################### height
		if self.toggle_state==0:
			a=1
			b=3
		else:
			a=3
			b=1
				
		if self.menu==0:
			height= 4
		else:
			if Type=="children":
				height= a
			else:
				height= b
				
		return [width,height]


	def set_pos(self,tools): # defini les positions d'affichage des elements
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

