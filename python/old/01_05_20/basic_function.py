import os, sys
from osc import*


def loopValue(cmd,value,inc,Max,Min):
	to=value
	if cmd=="-":
		to-=inc
	if cmd=="+":
		to+=inc
	if to>Max:
		to=Min
	if to<Min:
		to=Max
	#print("loopvalue",cmd,value,inc,Max,Min,to)
	return to


def loopPas(cmd,value,inc,Max,Min):	# trouver cett algorithme! definir une variable self.begin dans track
	to=value
	reste=Max%inc
	vide=inc-reste
	if vide==Max:
		vide=0

	if cmd=="-":
		to-=inc
	elif cmd=="+":
		to+=inc

	if to==Max+1:
		to=Min
	elif to == Min-1:
		to=Max

	elif to>Max and to >=Max+vide:
		to-=(Max+vide)

	elif to<Min and to <=Max+vide:
		to+=(Max+vide)

	#print("loopPas",cmd,value,inc,Max,Min,to)
	return to


def to_string(detail_list,valeur):
	to=""
	if type(valeur)==int or type(valeur)==float:
		to=str(valeur)
	if type(valeur)==str:
		to=valeur
	if type(valeur)==bool:
		to=str(int(valeur))
	if type(valeur)==list:
		if detail_list==True:
			i=0
			#print(len(valeur))
			while i<len(valeur):
				to+=str(valeur[i])
				if i<len(valeur)-1:
					to+=" "
				i+=1
		else:
			to=str(len(valeur))

	return to

def from_string(Mot,Type):

	if Type==str:
		return Mot
	elif Type==int:
		return int(Mot)
	elif Type==float:
		return float(Mot)
	elif Type==bool:
		return bool(Mot)
