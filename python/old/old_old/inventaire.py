params={
    "isPlaying":False,
    "idInstru":1,
    "idRack":1,
    "idPas":0,
    "pas":0,
    "idMenu":0,
    "saveRoad":"/home/pi/Bureau/BTMachines_git/Machine_1/saves/",
    "currentRoad":"/home/pi/Bureau/BTMachines_git/Samples/",
    "saveName":"",
    "idInBrowser":0,
    "nbPlayers":12,
    "nbRack":8,
    "recIsOn":False
    }


partition={

    "bpm":120,
    "masterVol":0,
    
    "track_road":[],# chemins vers les samples
    "track_vol":[], # volumes des tracks
    "track_pan":[], # volumes des tracks
    "track_mute":[], # mute de chaque track
    "track_solo":[], # solo de chaque track
    "track_begin":[], # pas de début et fin de chaque track
    "track_end":[], # pas de début et fin de chaque track

    "step_velo":[], # velocités de chaque pas de chaque track
    "step_pan":[], # pannings de chaque pas de chaque track
    "step_speed":[], # vitesse de lecture de chaque pas de chaque track
    "step_begin":[], # instant de début de chaque pas de chaque track
    "step_end":[], # instantde fin fin de chaque pas de chaque track

    }

def getParamValue(param):
	global params
	return params[param]

def setParamValue(param,*args):
	global params
	print(params[param])
	if type(params[param])!=list: 
		params[param]=args[0]

def getPartitionValue(param):
	global partition
	return partition[param]
	
def setPartitionValue(param,*args):
	global partition
	print(partition[param])
	if type(partition[param])!=list: 
		partition[param]=args[0]

def addPartitionValue(param,*args):
	global partition
	"""print ("addValue: ",type(partition[param]))
	if type(partition[param])==list:
		partition[param].append([])
"""
