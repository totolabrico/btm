from gpiozero import LED
import time

led = [LED(23),LED(24),LED(25)]

while True:
	for element in led:
		element.on()
		time.sleep(2)
		element.off()
