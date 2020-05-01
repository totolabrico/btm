from basic_function import*

class Partition():

	def __init__(self,Machine):
		self.children=[]

	def sort_cmd(self,cmd,arg):
		value=self.setting[cmd][1]
		if type(value)==bool:
			if cmd=="-":
				value= False
			elif cmd=="+":
				value= True
		elif type(value)==int or type(value)==float:
			min=self.setting[cmd][2]
			max=self.setting[cmd][3]
			inc=self.setting[cmd][4]
			if cmd=="-":
				value-=inc
			if cmd=="+":
				value+=inc
			if value>max:
				value=max
			if value<min:
				value=min
		self.setting[cmd][1]=round(value,2)
		self.save()

	def add_element(self,*args):
		id=len(self.children)+1
		self.children.append(Partition_track(self.machine,id,*args))
		self.setting[6][1]+=1
		self.save()

	def del_element(self,id):
		for element in self.children:
			element.erase_files()

		del self.children[id]
		self.setting[6][1]-=1
		i=0
		while i<len(self.children):
			self.children[i].id=i+1
			self.children[i].save()
			i+=1
		self.save()

	def paste_element(self,list,id):
		i=0
		for element in list:
			self.children.insert(id+i,element)
			self.setting[6][1]+=1
			i+=1
			print("len",len(self.children))
		i=0
		while i<len(self.children):
			self.children[i].id=i+1
			self.children[i].save()
			i+=1
		self.save()
