import logging
import threading
import time

from pynput import keyboard
from navigator import*

"""
DEBUGER MENU BROWSER : fleche haut et bas ne fonctionne plus
"""


class machine:

	def __init__(self):
		self.navigator=Navigator(self)

btm=machine()
print("btm")

while True:
	time.sleep(10);
