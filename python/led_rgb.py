from gpiozero import LED

led = [LED(23),LED(24),LED(25)]

class Led:
	def __init__(self,Menu):
		self.menu=Menu
		self.last_menu=""
		self.color={
		"main":[1,0,0],
		"tracks":[0,1,0],
		"track":[0,0,1],
		"notes":[1,0,1],
		"browser":[1,1,0],
		"save":[0,1,1],
		"load":[1,1,1]
		}
		
		
	def turn_on(self):
		self.turn_off()
		#print("turn on",self.color[self.menu.name])
		i=0
		self.leds_on=[]

		while i<len(led):
			if self.color[self.menu.name][i]==1:
				led[i].on()
				self.leds_on.append(i)
			i+=1
	
	def turn_off(self):
		for element in led :
			if element.is_active==True:
				#print (element)
				element.off()
	
"""
while True:
	for element in led:
		element.on()
		time.sleep(5)
		element.off()
"""
