from menu import*

class MainMenu(Menu):

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		self.name="main"
		self.mom="main"
		self.list=["play","record","load","save","import","reset"]
		self.tools["grid"]=[2,3]

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

class PlayMenu(Menu):

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		self.name="play"
		self.mom="main"
		self.list=["sequencer","master","tracks"]
		self.tools["grid"]=[1,3]

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

class SequencerMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="sequencer"
		self.mom="play"
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,Partition.sequencer)
		self.nb_tick=self.set_nb_tick()

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)
	
	def set_nb_tick(self):
		tick=1
		for element in self.partition.tracks:
			begin=element[2][1][2][1]
			end=element[2][1][3][1]
			nbnote=element[2][1][0][1]*element[2][1][1][1]
			l=get_loop_length(begin,end,nbnote)
				
			if tick%l==0:
				pass
			elif l%tick==0:
				tick=l
			else:
				tick=tick*l
			
				
		print("nbtick",tick)
		osc_send("master","nb_tick",tick)
		self.nb_tick=tick
		return tick
		
	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("master",setting[0],setting[1])

class MasterMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="master"
		self.mom="play"
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,Partition.master)

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("master",setting[0],setting[1])

class TracksMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="tracks"
		self.mom="play"
		self.list=Partition.tracks
		self.tools["grid"]=[10,3]
		self.title=""
		list=[]
		for element in self.list:
			list.append(element[3][1][2])
		Editor.__init__(self,Machine,Partition,list)

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)
		if cmd=="enter":
			self.navigator.set_menu("track")
		else:
			self.set_parameters()
			
	def set_parameters(self):
		self.title=get_name(self.list[self.pointer][1][1][0][1])
		self.title=set_txt_size(self.title,10)
		
	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("track",setting[0],setting[1],self.pointer)
		
	def draw(self):
		draw_title("track "+str(self.pointer+1)+": "+self.title)
		draw_tracks(self.parameters,self.tools)

class TrackMenu(Menu,Editor,Mom):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		Mom.__init__(self)
		self.name="track"
		self.mom="tracks"
		self.list=[]
		self.title=""
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[])
			
	def set_parameters(self):
		id=self.navigator.menus["tracks"].pointer
		#print("track menu set parameters on track n°",id)
		self.parameters=self.partition.tracks[id]
		self.title=get_name(self.parameters[1][1][0][1])
		self.title=str(id+1)+": "+set_txt_size(self.title,15)
		Mom.set_list(self)
		
	def sort(self,cmd,arg):
		Mom.sort(self,cmd,arg)

	def set_sample(self,Path):
		self.parameters[1][1][0][1]=Path
		self.navigator.menus["child"].send_osc()
			
	def set_notes_length(self,Length):
		dif=Length-len(self.parameters[0][1])
		if dif<0:
			self.del_notes(abs(dif))
			self.set_begin_end(Length,"-")
		elif dif>0:
			self.add_notes(dif)
			self.set_begin_end(Length,"+")

	def del_notes(self,Dif):
		i=0
		while i<Dif:
			del self.parameters[0][1][-1]
			i+=1
			
	def add_notes(self,Dif):
		i=0
		while i<Dif:
			self.parameters[0][1].append(self.partition.init_note())
			i+=1

	def set_begin_end(self,Length,Cmd):
		if Cmd=="+":
			self.parameters[2][1][3]=edit(Length,self.parameters[2][1][3])#end
		if Cmd=="-":
			if self.parameters[2][1][2][1]>Length: #begin
				self.parameters[2][1][2]=edit(0,self.parameters[2][1][2])
			if self.parameters[2][1][3][1]>Length: #end
				self.parameters[2][1][3]=edit(Length,self.parameters[2][1][3])
		self.send_osc("begin",self.parameters[2][1][2][1])
		#self.send_osc("end",self.parameters[2][1][3][1]) on s'en fou du end dans pd!
		self.set_loop_length()
				
	def set_loop_length(self):
		begin=self.parameters[2][1][2][1]
		end=self.parameters[2][1][3][1]
		nbnote=self.parameters[2][1][0][1]*self.parameters[2][1][1][1]
		loop_length=get_loop_length(begin,end,nbnote)
		self.navigator.menus["sequencer"].set_nb_tick()
		self.send_osc("loop_length",loop_length)

	def send_osc(self,Setting,Value):
		osc_send("track",Setting,Value,self.navigator.menus["tracks"].pointer)
		
	def draw(self):
		draw_title(self.title)
		draw_list(self.list,self.tools)

class ChildMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name=""
		self.mom=""
		self.list=[]
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[])

	def set_parameters(self,Name,Mom,Parameters):
		self.name=Name
		self.mom=Mom
		self.parameters=Parameters
		self.reset_pointer()

	def sort(self,cmd,arg):
		Menu.sort(self,cmd,arg)
		Editor.sort(self,cmd,arg)

	def draw(self):
		Menu.draw(self)
		Editor.draw(self)

	def send_osc(self):
		setting=self.parameters[self.pointer]
		id_track=self.navigator.menus["tracks"].pointer

		if self.mom=="track":
			osc_send("track",setting[0],setting[1],id_track)
		if self.mom=="note":
			id_note=self.navigator.menus["notes"].pointer
			osc_send("note",setting[0],setting[1],id_track,id_note)

class SampleMenu(Menu,Browser):

	def __init__(self,Navigator):
		Menu.__init__(self,Navigator)
		Browser.__init__(self,"/home/pi/audiosamples")
		self.name="browser sample"
		self.mom="child"
		self.list=Browser.set_list(self)
		self.tools["grid"]=[1,3]

	def sort(self,cmd,arg):
		
		is_wav=check_wav(self.list[self.pointer])
		samplepath=self.path+"/"+self.list[self.pointer]
		if cmd=="back":
			self.navigator.set_menu("child")
		elif cmd=="enter" and is_wav:
			self.play_sound(samplepath)
		elif cmd=="edit" and arg=="+" and is_wav:
			self.set_sample(samplepath)
		else:
			Browser.sort(self,cmd,arg)
			
	def draw(self):
		Menu.draw(self)
		draw_list(self.list,self.tools)

	def play_sound(self,Path):
		print("play the sound now")
		os.system("omxplayer "+Path+" --adev local &")
		
	def set_sample(self,Path):
		self.navigator.menus["track"].set_sample(Path)
		self.navigator.set_menu(self.mom)
				
class NotesMenu(Menu,Editor):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		self.name="notes"
		self.mom="track"
		self.list=[]
		self.title=""
		Editor.__init__(self,Machine,Partition,[])


	def sort(self,cmd,arg):
		if cmd=="enter":
			self.navigator.set_menu("note")
		else:
			Menu.sort(self,cmd,arg)
			Editor.sort(self,cmd,arg)
			self.set_title()
			
	def set_parameters(self):
		track=self.partition.tracks[self.navigator.menus["tracks"].pointer]
		self.list=track[0][1]
		self.parameters=[]
		for element in self.list:
			self.parameters.append(element[0][1][0])
		temps=track[2][1][0][1]
		coef=4
		while temps*coef>16:
			coef-=1
		self.tools["grid"]=[temps*coef,3]
		self.tools["temps"]=temps
		self.set_title()
		self.reset_pointer()
		
	def set_title(self):
		self.title="note :"+str(self.pointer+1)+" | vol: "+str(self.parameters[self.pointer][1])
		
	def send_osc(self):
		setting=self.parameters[self.pointer]
		osc_send("note",setting[0],setting[1],self.navigator.menus["tracks"].pointer,self.pointer)
		
	def draw(self):
		draw_title(self.title)
		draw_notes(self.parameters,self.tools)
		
class NoteMenu(Menu,Editor,Mom):

	def __init__(self,Machine,Partition,Navigator):
		Menu.__init__(self,Navigator)
		Mom.__init__(self)
		self.name="note"
		self.mom="notes"
		self.list=[]
		self.title="note"
		self.tools["grid"]=[2,3]
		Editor.__init__(self,Machine,Partition,[])
		
	def set_parameters(self):
		idt=self.navigator.menus["tracks"].pointer
		idn=self.navigator.menus["notes"].pointer
		self.parameters=self.partition.tracks[idt][0][1][idn]
		print(self.parameters)
		self.title=get_name(self.navigator.menus["track"].parameters[1][1][0][1])
		self.title="note: "+str(idn+1)
		Mom.set_list(self)
		
	def sort(self,cmd,arg):
		Mom.sort(self,cmd,arg)

	def draw(self):
		draw_title(self.title)
		draw_list(self.list,self.tools)
