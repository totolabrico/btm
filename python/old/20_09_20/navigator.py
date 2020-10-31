from draw import*
import time
from browser import*

class Navigator():

	def __init__(self,Machine):
		self.machine=Machine
		self.element=self.machine.partition
		self.mode=True
		self.menu="partition"
		self.browser=Browser(self)
		
	def receive(self,state,cmd,arg):
		if self.menu=="partition":
			self.sort(state,cmd,arg)
		elif self.menu=="browser":
			self.browser.sort(cmd,arg)
			
	def launch_browser(self,sample_element):
		self.sample_element=sample_element
		self.menu="browser"
		
	def close_browser(self,path):
		for setting in self.sample_element.setting:
			if setting[0]=="sample":
				setting[1]=path
		self.sample_element.save()
		self.menu="partition"
		

	def sort(self,state,cmd,arg):
		print("navigator_sort", state,cmd,arg)				

		if state=="element":
			if cmd=="move":
				if arg[0]=="y":	# deplacement parent/enfant
					if arg[1]=="-":
						self.moveto_parent_element()
					elif arg[1]=="+":
						self.moveto_child_element()
				elif arg[0]=="x" and self.element.mother!=None:#deplacement enfant/enfant
					self.move_between_element(arg[1])
		
		else:			
			if self.mode==True:# Edition de l'element
				self.edit_self_setting(cmd,arg)
			elif self.mode==False: # Edition des enfants
				if state=="default":
					self.edit_children(cmd,arg)	
				elif state =="setting":
					self.edit_children_setting(cmd,arg)	


	def edit_self_setting(self,cmd,arg):
		if cmd=="move":
			self.element.set_pointer("setting",arg[0],arg[1])		
		if cmd=="select":
			self.element.set_fork("setting",arg)
		if cmd=="edit":
			self.element.set_setting(arg)
			
	def edit_children(self,cmd,arg):
		if cmd=="move":
			self.element.set_pointer("children",arg[0],arg[1])
		if cmd=="select":
			self.element.set_fork("children",arg)
		if cmd=="create":
			self.element.set_children(arg)
		if cmd=="edit":
			self.edit_children_setting(cmd,arg) 

	def edit_children_setting(self,cmd,arg):
		ids=self.element.selecter_children
		children=[]
		if ids==[]:
			ids=[self.element.pointer_children]
			for id in ids:
				for child in self.element.children: # on creer une liste des enfant réels à partir de la fourchette
						children.append(child)
									
		for child in children:
			if cmd=="move":
				child.set_pointer("setting",arg[0],arg[1])
			if cmd=="select":
				child.set_fork("children",arg)
			elif cmd=="edit":
				child.set_setting(arg)			

	def moveto_parent_element(self):
		if self.mode==True:
			if self.element.mother!=None:
				self.element=self.element.mother
		self.mode = not self.mode
			
	def moveto_child_element(self):
		if self.mode==True:
			self.mode=False
		else:
			if self.element.child!=None:
				for child in self.element.children:
					if self.element.pointer_children+1==child.id:
						self.element=child
						self.mode=True

	
	def move_between_element(self,cmd):
		id=int(self.element.id)
		if cmd=="+":
			id+=1
		if cmd=="-":
			id-=1
		if id<1:
			id=len(self.element.mother.children)
		if id>len(self.element.mother.children):
			id=1
		for child in self.element.mother.children:
			if child.id==id:
				self.element=child
		
	
	def draw(self):
		while True:
			draw_begin()
			if self.menu=="partition":
				if self.mode==True:
					draw_title(self.element.name)
					self.element.draw_setting()
				else:
					draw_title(self.element.name+" / "+str(self.element.pointer_children+1))
					self.element.draw_children()
			elif self.menu=="browser":
				self.browser.draw()	
			draw_end()
			time.sleep(0.07)
