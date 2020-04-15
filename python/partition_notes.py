from basic_function import* 

class Partition_note:

	def __init__(self,Track,Pas,Id):

		self.track=Track
		self.setting=[
		["pas",Pas], # 0
		["vol",0.5], # 1
		["pan",0], # 2
		["pitch",0], #3
		["tone",0], #4
		["begin",0],# 5
		["length",0], # 6
		]
		
		self._Id=Id
		print ("note id",Id)

	def _get_Id(self):
		return self._Id
	def _set_Id(self,Id):
		self._Id=Id

	def _get_pas(self):
		return self.setting[0][1]
	def _set_pas(self,pas):
		setting=0
		inc,Max,Min=1,self.track.temps*self.track.mesure,0
		self.edit_setting(setting,cmd,inc,Max,Min)

	def _get_vol(self):
		return self.setting[1][1]
	def _set_vol(self,cmd):
		setting=1
		inc,Max,Min=0.1,1,0
		value=self.setting[setting][1]
		to=limitValue(cmd,value,inc,Max,Min)
		if to==0:
			self.track.remove_note(self.Id)
		else:
			self.setting[setting][1]=to
		self.track.save()
		#self.edit_setting(setting,cmd,inc,Max,Min)
		
		
	def _get_pan(self):
		return self.setting[2][1]
	def _set_pan(self,cmd):
		setting=2
		inc,Max,Min=0.1,1,-1
		self.edit_setting(setting,cmd,inc,Max,Min)
		
	def _get_pitch(self):
		return self.setting[3][1]
	def _set_pitch(self,cmd):
		setting=3
		inc,Max,Min=1,100,-100
		self.edit_setting(setting,cmd,inc,Max,Min)

	def _get_tone(self):
		return self.setting[4][1]
	def _set_tone(self,cmd):
		setting=4
		inc,Max,Min=1,1000,-1000
		self.edit_setting(setting,cmd,inc,Max,Min)
	
	def _get_begin(self):
		return self.setting[5][1]
	def _set_begin(self,cmd):
		setting=5
		inc,Max,Min=1,100,0
		self.edit_setting(setting,cmd,inc,Max,Min)
		
	def _get_length(self):
		return self.setting[6][1]
	def _set_length(self,cmd):
		setting=6
		inc,Max,Min=1,100,0
		self.edit_setting(setting,cmd,inc,Max,Min)

	def edit_setting(self,setting,cmd,inc,Max,Min):
		value=self.setting[setting][1]
		to=limitValue(cmd,value,inc,Max,Min)
		self.setting[setting][1]=to
		self.track.save()

	def save(self):
		to=""
		for element in self.setting:
			to+= str(element[1])+" "
		to=to[:len(to)-1]
		return to

	Id=property(_get_Id,_set_Id)
	pas=property(_get_pas,_set_pas)
	vol=property(_get_vol,_set_vol)
	pan=property(_get_pan,_set_pan)
	pitch=property(_get_pitch,_set_pitch)
	tone=property(_get_tone,_set_tone)
	begin=property(_get_begin,_set_begin)
	length=property(_get_length,_set_length)
