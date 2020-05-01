import logging
import threading
import time

#from pynput import keyboard
from navigator import*
from partition_main import*


class machine:

	def __init__(self):
		self.partition=Partition_main(self)
		self.navigator=Navigator(self)
btm=machine()
print("btm")

while True:
	time.sleep(10)
