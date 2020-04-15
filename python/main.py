import logging
import threading
import time

from pynput import keyboard
from navigator import*


class machine:

	def __init__(self):
		self.navigator=Navigator(self)

btm=machine()
print("btm")

while True:
	time.sleep(10)
	
