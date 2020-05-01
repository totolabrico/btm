from gpiozero import LED

led = [LED(23),LED(24),LED(25)]

class Led:
	def __init__(self):
		self.leds_on=[]
		self.color={
			"main":[1,0,0],
			"tracks":[0,1,0],
			"track":[0,0,1],
			"notes":[1,0,1],
			"browser":[1,1,0],
			"save":[0,1,1],
			"load":[1,1,1]
		}
	def turn_on(self,Menu):
		self.turn_off()
		i=0
		self.leds_on=[]
		while i<len(led):
			if self.color[Menu][i]==1:
				led[i].on()
				self.leds_on.append(i)
			i+=1
	
	def turn_off(self):
		global led
		for element in led :
			if element.is_active==True:
				#print (element)
				element.off()
