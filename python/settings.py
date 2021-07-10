
menu_tools={
#"pos":[],
"grid":[0,0],
"origin":0,
"pointer":[0,0],
"fork":[],
"selecter":[],
}

sequencer_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["play",True],
	["bpm",120,0,300,0.1]
	]
	
time_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["mesure",4,1,64,1],
	["temps",4,1,8,1],
	["begin",1,1,8*64,1],
	["end",16,1,8*64,1],
	#["loop",True]
	]

sample_setting=[
    ["sample","empty"],
	["pitch",0,-100,100,0.05],
	["tone",0,-100,100,0.05],
	["s_begin",0,0,1,0.05],
	["s_end",1,0,1,0.05]
	]
	
audio_setting=[
	# 0:name / 1:value / 2:min / 3:max / 4:inc
	["vol",0.8,0,1,0.1],
	["pan",0,-1,1,0.1],
	["mute",False],
	["solo",False],
	["lpf",20000,0,20000,10],#low pass filter
	["hpf",0,0,20000,10],#high pass filter

	]


