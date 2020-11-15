from draw import*
from cmd import*

class Editor_Interface():

	def __init__(self,Machine,Navigator,Editor,Partition):
		self.machine=Machine
		self.navigator=Navigator
		self.editor=Editor
		self.partition=Partition
		
	def draw(self):
		title=self.set_title()
		draw_title(title)
		self.Y_setting_margin=self.set_margin()
		self.draw_grid("settings",self.editor.setting_tools,self.Y_setting_margin)	
		if self.editor.name!="master":
			self.draw_grid("children",self.editor.children_tools,0)
	
	def set_title(self): # defini le titre
		#pointer=self.editor.children_tools["pointer"]+1
		if self.editor.name=="master":
			title="master"
		if self.editor.name!="master":
			title=str(self.navigator.track_editor.children_tools["pointer"]+1)+" / "+self.set_sample_name()
		if self.editor.name=="note":
			title+=" / "+str(self.editor.children_tools["pointer"]+1)
		return title
		
	
	def set_sample_name(self): # prepare le nom du sample
		track=self.partition.track_setting[self.navigator.track_editor.children_tools["pointer"]]
		name=track["sample"][1].split("/")
		name=name[len(name)-1]
		name=name.split(".")
		name=name[0][-10:]
		return name
		
				
	def set_margin(self): # defini l'increment en hauteur de l'affichage des settings
		if self.editor.name=="master":
			Y_margin=0
		else:
			if self.navigator.toggle_state==0:
				Y_margin=Y_inc[1]
			else:
				Y_margin=3*Y_inc[1]	
		return Y_margin
				
	def set_element_width(self,Type,tools): # defini la largeur d'un element
		el_size=(width/tools["grid"][0])
		if Type=="children":
			if self.editor.name=="track":
				el_size=rect_track_size
			elif self.editor.name=="note":
				el_size=rect_note_size
		return el_size
		
		
	def set_pos(self,Type,tools,id,min,margin,El_size): # defini les positions réelles des element sur l'ecran
		y_error=min/tools["grid"][0]*Y_inc[1]
		x_pos=tools["pos"][id][0]
		num_el_width=tools["grid"][0]
		x=0
		if Type=="settings":
			x=int(width/num_el_width)*x_pos
		elif Type=="children":
			x_exces=(width/num_el_width)-El_size
			if self.editor.name=="master":
				x=0
			elif self.editor.name=="track":
				x=int((width+x_exces)/num_el_width)*x_pos
			elif self.editor.name=="note":
				x_jump=3 # saut entre les mesures
				x=int((width+x_exces-4*x_jump)/num_el_width)*x_pos+int(x_pos/4)*x_jump
				#x=X[0]+x_pos*(El_size+2)+int(x_pos/4)*x_jump
			
		y=margin+Y[2]+tools["pos"][id][1]*Y_inc[1]-y_error
		return x,y
		
		
	def draw_grid(self,Type,tools,margin): # affichage d'une grille (appel draw_setting et draw_child)
		min=tools["origin"]
		num_el_per_width=tools["grid"][0]
		num_el_per_height=tools["grid"][1]
		if num_el_per_height==1:
			min=int(tools["pointer"]-tools["pointer"]%num_el_per_width)
		max=min+num_el_per_width*num_el_per_height
		if max>len(tools["pos"]):
			max=len(tools["pos"])
		
		id=min
		while id<max: 
			element_size=self.set_element_width(Type,tools)
			x,y=self.set_pos(Type,tools,id,min,margin,element_size)
			if Type=="settings":
				key=get_key(tools["element"],id)
				el= tools["element"][key]
				self.draw_setting(tools,id,key,el[1],x,y)
			elif Type=="children":
				self.draw_child(tools,id,x,y,element_size)
			id+=1
	
	
	def draw_setting(self,tools,id,Key,Element,x,y): #affiche un setting
		line_content=""
		if tools["pointer"]==id:
			line_content=">"
		line_content+=Key[:3]+":"+setting_to_string(Element)[:4]
		draw.text((x,y),line_content,font=font, fill=255)
	
	def draw_child(self,tools,id,x,y,rect_size): #affiche un enfants
		color=0
		if self.navigator.id_current_editor==2 and tools["element"][id]["vol"][1]>0:
			color=255
		draw.rectangle((x,y,x+rect_size,y+rect_size), outline=255, fill=color)
		if tools["pointer"]==id:
			draw.rectangle((x,y,x+rect_size,y-2), outline=255, fill=255)
			
		

