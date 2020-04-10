#!/usr/bin/python
from inventaire import*
import os, sys
def ls(chemin):
	dirs = os.listdir(chemin)
	return dirs
